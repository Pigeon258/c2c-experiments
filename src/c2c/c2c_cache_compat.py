"""推理时适配Transformers4.57缓存容器，保持官方C2C张量和融合运算。"""


def enable_inference_cache_compat():
    """新增旧属性只读视图；缓存复制改走公开update接口，不改第三方文件。"""
    import transformers
    from transformers.cache_utils import DynamicCache
    if transformers.__version__ != '4.57.6':
        raise ValueError('该正式适配只验收Transformers4.57.6')
    import rosetta.model.wrapper as wrapper
    if not hasattr(DynamicCache, 'key_cache'):
        DynamicCache.key_cache = property(lambda self: [layer.keys for layer in self.layers])
        DynamicCache.value_cache = property(lambda self: [layer.values for layer in self.layers])

    def clone_kv_cache(cache):
        """克隆并detach每层K/V；新容器正确维护长度和mask元数据。"""
        result = DynamicCache()
        for index, (key, value) in enumerate(zip(cache.key_cache, cache.value_cache)):
            result.update(key.clone().detach(), value.clone().detach(), index)
        return result

    wrapper.clone_kv_cache = clone_kv_cache
    if not getattr(wrapper.RosettaModel.forward, '_c2c_full_decode_mask_compat', False):
        original_forward = wrapper.RosettaModel.forward

        def forward_with_full_decode_mask(self, *args, **kwargs):
            """旧wrapper单步把mask裁成1列；保留完整前缀可见范围再交接收模型。"""
            ids = kwargs.get('input_ids')
            cache = kwargs.get('past_key_values')
            sections = kwargs.get('kv_cache_index')
            receiver_only = (not args and not self.include_response and ids is not None and
                ids.ndim == 2 and ids.shape[1] == 1 and cache is not None and
                sections is not None and len(sections) == 1 and
                sections[0].shape == (1, 1, 2) and sections[0][0, 0].tolist() == [-1, 0])
            if receiver_only:
                mask = kwargs.get('attention_mask')
                if mask is not None and (mask.ndim != 2 or mask.shape[-1] != cache.get_seq_length()+1):
                    raise ValueError('接收端单步Decode的mask未覆盖完整历史和当前token')
                forwarded = {k: v for k, v in kwargs.items() if k != 'kv_cache_index'}
                return self.model_list[self.base_model_idx](**forwarded)
            return original_forward(self, *args, **kwargs)

        forward_with_full_decode_mask._c2c_full_decode_mask_compat = True
        wrapper.RosettaModel.forward = forward_with_full_decode_mask
    return {'transformers': transformers.__version__, 'cache_interface': 'DynamicCache.layers',
            'compatibility': 'legacy tensor views and public-update cloning',
            'receiver_only_decode': 'preserve full attention mask; old wrapper sliced it to one column',
            'official_files_modified': False, 'fusion_math_modified': False}
