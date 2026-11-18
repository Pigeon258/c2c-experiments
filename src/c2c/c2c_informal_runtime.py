"""P1推理：官方融合前向、完整源KV回环及实际分项计量。"""
import hashlib
import time


class CapacityError(RuntimeError):
    """输入已占满模型容量，作为资源失败保留在质量分母内。"""


class MeasuredP1:
    """保留官方两段P1前向；手写argmax只控制后续生成和计时。"""

    def __init__(self, model, tokenizer, progress):
        import torch
        from c2c.c2c_transport import LoopbackChannel
        self.torch, self.model, self.tokenizer = torch, model, tokenizer
        self.progress = progress
        self.channel = LoopbackChannel()
        self.originals = []
        self.state = {}
        self.checkpoint = None
        self.last_checkpoint = 0.0
        if model.include_response:
            raise ValueError('本入口只实现Sender预填充一次的P1，不支持include_response')
        self.capacity = min(m.config.max_position_embeddings for m in model.model_list)
        if self.capacity != 40960:
            raise ValueError('实际模型上下文容量与共同配置40960不同')
        eos = model.model_list[0].generation_config.eos_token_id
        self.eos = set(eos if isinstance(eos, list) else [eos])
        if self.eos != {151643, 151645}:
            raise ValueError('实际接收模型EOS集合与共同配置不同')
        for name, base in zip(('receiver', 'sender'), model.model_list):
            original = base.forward
            self.originals.append((base, original))

            def observed(*args, _name=name, _original=original, **kwargs):
                # 推理仅需要最后位置logits；不构造长输入×词表的无用张量。
                kwargs['logits_to_keep'] = 1
                if not self.state.get('active') or self.state.get('decode'):
                    return _original(*args, **kwargs)
                if _name == 'receiver':
                    stage = 'receiver_local_prefill' if self.state['receiver_calls'] == 0 else 'receiver_final_prompt_prefill'
                    self.state['receiver_calls'] += 1
                    if self.state.get('fusion_start') is not None:
                        self.finish_fusion()
                else:
                    stage = 'sender_prefill'
                result = self.measured(stage, lambda: _original(*args, **kwargs))
                if _name == 'sender':
                    if self.state['transport']:
                        result.past_key_values = self.exchange(result.past_key_values)
                    self.state['fusion_start'] = (self.event(), time.perf_counter())
                self.progress()
                return result
            base.forward = observed
        for projector in model.projector_list:
            original = projector.forward
            self.originals.append((projector, original))

            def projected(*args, _original=original, **kwargs):
                begin = self.event()
                result = _original(*args, **kwargs)
                end = self.event()
                self.state['projector_events'].append((begin, end))
                if self.state.get('check_fusion'):
                    self.state['deltas'].append(max(float((result[i].to(args[1][i].dtype)-args[1][i]).abs().max()) for i in (0, 1)))
                return result
            projector.forward = projected

    def event(self):
        event = self.torch.cuda.Event(enable_timing=True)
        event.record()
        return event

    def measured(self, name, fn):
        """同步墙钟与CUDA事件分别记账，嵌套总时长明确标为inclusive。"""
        self.torch.cuda.synchronize()
        start = time.perf_counter()
        begin = self.event()
        self.state.setdefault('running_stages', {})[name] = start
        complete = False
        try:
            result = fn()
            complete = True
        finally:
            # 可捕获异常也结算已发生的GPU/墙钟成本，失败的测量保持未知。
            measurement = {'synchronized_wall_s': time.perf_counter()-start}
            try:
                end = self.event()
                end.synchronize()
                measurement.update(cuda_event_s=begin.elapsed_time(end)/1000,
                                   synchronized_wall_s=time.perf_counter()-start)
            except Exception as error:
                self.state.setdefault('measurement_errors', {})[name] = type(error).__name__
            self.state['timings'][name] = measurement
            self.state.setdefault('stage_complete', {})[name] = complete
            self.state['running_stages'].pop(name, None)
            self.persist(force=True)
        self.progress()
        return result

    def snapshot(self):
        """只复制CPU可序列化事实；在途阶段墙钟是下界，不冒充完整CUDA时长。"""
        now = time.perf_counter()
        keys = ('metadata', 'input_tokens', 'sender_input_tokens', 'generated_token_ids',
                'timings', 'cpu_timings', 'communication', 'stage_complete', 'measurement_errors',
                'rendered_prompt_sha256', 'input_token_ids_sha256')
        keys += ('supplemental_transfers', 'endpoint_input_tokens')
        value = {k: self.state[k] for k in keys if k in self.state}
        value.update(snapshot_at_unix=time.time(),
                     observed_pipeline_wall_s=now-self.state.get('began', now),
                     running_stage_wall_lower_bounds={k: now-v for k,v in self.state.get('running_stages', {}).items()})
        value['output_tokens'] = len(self.state.get('generated_token_ids', []))
        return value

    def persist(self, force=False):
        if self.checkpoint and (force or time.perf_counter()-self.last_checkpoint >= 5):
            self.checkpoint(self.snapshot())
            self.last_checkpoint = time.perf_counter()

    def finish_fusion(self):
        begin, wall = self.state.pop('fusion_start')
        end = self.event()
        end.synchronize()
        self.state['timings']['receiver_conversion_fusion_inclusive'] = {
            'cuda_event_s': begin.elapsed_time(end)/1000,
            'synchronized_wall_s': time.perf_counter()-wall}

    def exchange(self, cache):
        """把收到并恢复的完整源KV交回官方融合器；不以估算代替实际传输。"""
        from transformers.cache_utils import DynamicCache
        from c2c.c2c_transport import serialize_kv, deserialize_kv
        torch = self.torch
        torch.cuda.synchronize()
        start = time.perf_counter()
        keys = [x.detach().cpu().contiguous().clone() for x in cache.key_cache]
        values = [x.detach().cpu().contiguous().clone() for x in cache.value_cache]
        timings = {'sender_device_to_host_s': time.perf_counter()-start}
        raw_bytes = sum(x.numel()*x.element_size() for x in keys+values)
        metadata = self.state['metadata']
        start = time.perf_counter()
        packet = serialize_kv(keys, values, metadata)
        timings['sender_pack_s'] = time.perf_counter()-start
        start = time.perf_counter()
        received, count = self.channel.transfer(packet)
        timings['transport_loopback_and_byte_verify_s'] = time.perf_counter()-start
        start = time.perf_counter()
        loaded = deserialize_kv(received)
        timings['receiver_unpack_s'] = time.perf_counter()-start
        if loaded['metadata'] != metadata:
            raise ValueError('KV元数据未正确还原')
        start = time.perf_counter()
        gpu_keys = [x.to('cuda') for x in loaded['keys']]
        gpu_values = [x.to('cuda') for x in loaded['values']]
        restored = DynamicCache.from_legacy_cache(tuple(zip(gpu_keys, gpu_values)))
        torch.cuda.synchronize()
        timings['receiver_restore_and_host_to_device_s'] = time.perf_counter()-start
        if self.state.get('check_fusion'):
            if not all(torch.equal(a, b) for a, b in zip(cache.key_cache+cache.value_cache, gpu_keys+gpu_values)):
                raise ValueError('恢复后KV张量不一致')
        self.state['communication'] = {
            'raw_kv_bytes': raw_bytes, 'serialized_payload_bytes': len(packet),
            'metadata_and_container_bytes': len(packet)-raw_bytes, 'framing_bytes': 8,
            'actual_sent_bytes': len(packet)+8, 'actual_received_bytes': count,
            'generated_text_bytes': 0, 'supplemental_text_bytes': 0,
            'payload_sha256': hashlib.sha256(packet).hexdigest(), 'bytes_equal': True,
            'keys': [{'shape': list(x.shape), 'dtype': str(x.dtype)} for x in keys],
            'values': [{'shape': list(x.shape), 'dtype': str(x.dtype)} for x in values],
            'scope': '全部源KV；应用层载荷+8字节长度帧，不含TCP/IP包头；同机回环'}
        self.state['cpu_timings'].update(timings)
        self.persist(force=True)
        return restored

    def generate(self, messages, metadata, *, diagnostic_tokens=None, max_new_tokens=None, transport=True, check_fusion=False):
        """正式短测按剩余容量；diagnostic_tokens仅供不含测试题的工程验收。"""
        torch = self.torch
        self.state = {'active': True, 'decode': False, 'receiver_calls': 0, 'timings': {},
                      'cpu_timings': {}, 'projector_events': [], 'deltas': [],
                      'transport': transport, 'check_fusion': check_fusion, 'metadata': metadata}
        began = time.perf_counter()
        self.state['began'] = began
        rendered = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
        ids = self.tokenizer.encode(rendered, add_special_tokens=False)
        self.state['cpu_timings']['input_assembly_tokenize_s'] = time.perf_counter()-began
        self.state['input_tokens'] = len(ids)
        self.state.update(sender_input_tokens=len(ids)-1,
            rendered_prompt_sha256=hashlib.sha256(rendered.encode()).hexdigest(),
            input_token_ids_sha256=hashlib.sha256(str(ids).encode()).hexdigest())
        self.persist(force=True)
        if len(ids) >= self.capacity:
            raise CapacityError(f'input={len(ids)},capacity={self.capacity}')
        if len(ids) < 2:
            raise ValueError('P1两段前向至少需要两个输入token')
        if max_new_tokens is not None:
            if type(max_new_tokens) is not int or max_new_tokens <= 0 or diagnostic_tokens is not None:
                raise ValueError('授权输出上限须为正整数，且不能与诊断长度模式混用')
        available = self.capacity-len(ids)
        budget = diagnostic_tokens if diagnostic_tokens is not None else min(max_new_tokens or available, available)
        torch.cuda.synchronize()
        baseline = torch.cuda.memory_allocated()
        torch.cuda.reset_peak_memory_stats()
        start = time.perf_counter()
        tensor = torch.tensor([ids], device='cuda')
        mask = torch.ones_like(tensor)
        sections = [torch.tensor([1, 0], device='cuda').repeat(len(ids)-1, 1).unsqueeze(0),
                    torch.tensor([[[-1, 0]]], device='cuda')]
        torch.cuda.synchronize()
        self.state['cpu_timings']['input_host_to_device_s'] = time.perf_counter()-start
        self.model.kv_cache_dict = {}
        generated = []
        self.state['generated_token_ids'] = generated
        with torch.inference_mode():
            out = self.measured('prefill_pipeline_inclusive', lambda: self.model(
                input_ids=tensor, attention_mask=mask, kv_cache_index=sections, use_cache=True))
            cache, logits = out.past_key_values, out.logits[:, -1, :]
            del out
            # Sender只参与一次预填充；释放官方wrapper留存的诊断缓存副本。
            self.model.kv_cache_dict = {}
            self.state['decode'] = True

            def decode():
                nonlocal cache, logits
                for i in range(budget):
                    token = torch.argmax(logits, dim=-1)
                    value = token.item()
                    generated.append(value)
                    self.persist()
                    self.progress()
                    if (diagnostic_tokens is None and value in self.eos) or i+1 == budget:
                        break
                    step = self.model.model_list[0](input_ids=token.reshape(1, 1),
                        past_key_values=cache, use_cache=True, logits_to_keep=1)
                    cache, logits = step.past_key_values, step.logits[:, -1, :]
                return generated
            self.measured('receiver_decode', decode)
        module_cuda = sum(a.elapsed_time(b)/1000 for a, b in self.state['projector_events'])
        self.state['timings']['receiver_conversion_fusion_modules_nested'] = {'cuda_event_s': module_cuda}
        start = time.perf_counter()
        output = self.tokenizer.decode(generated, skip_special_tokens=True)
        self.state['cpu_timings']['output_text_decode_s'] = time.perf_counter()-start
        result = {'output': output, 'input_tokens': len(ids), 'sender_input_tokens': len(ids)-1,
            'output_tokens': len(generated), 'generated_token_ids': generated,
            'rendered_prompt_sha256': hashlib.sha256(rendered.encode()).hexdigest(),
            'input_token_ids_sha256': hashlib.sha256(str(ids).encode()).hexdigest(),
            'termination': ('eos' if generated[-1] in self.eos else
                            'diagnostic_limit' if diagnostic_tokens is not None else
                            'token_limit' if budget < available else 'context_capacity'),
            'max_new_tokens': budget, 'context_capacity': self.capacity,
            'authorized_output_limit': max_new_tokens,
            'timings': self.state['timings'], 'cpu_timings': self.state['cpu_timings'],
            'communication': self.state.get('communication'), 'projector_calls': len(self.state['projector_events']),
            'memory': {'baseline_allocated_bytes': baseline, 'peak_allocated_bytes': torch.cuda.max_memory_allocated(),
                       'peak_reserved_bytes': torch.cuda.max_memory_reserved()},
            'hot_pipeline_wall_s': time.perf_counter()-began,
            'fusion_deltas': self.state['deltas']}
        if result['projector_calls'] != len(self.model.projector_list):
            raise ValueError('本题融合器调用数不完整')
        self.state['active'] = False
        return result

    def close(self):
        for obj, original in self.originals:
            obj.forward = original
        self.channel.close()
