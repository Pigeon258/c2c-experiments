"""C2C协议原文补齐路径及直接原文转发路径的真实收发、重建和计量。"""
import hashlib
import json
import time

from c2c.c2c_informal_runtime import MeasuredP1, CapacityError
from c2c.c2c_protocols import canonical, endpoint_views, messages, missing_payload, merge_received, raw_text_bytes


class ReceiverOnly:
    """直接转发路径的接收端前向，不调用融合器或Sender模型。"""
    def __init__(self, model):
        self.model_list = model.model_list
        self.projector_list = []
        self.kv_cache_dict = {}

    def __call__(self, input_ids, attention_mask, kv_cache_index, use_cache):
        return self.model_list[0](input_ids=input_ids, attention_mask=attention_mask, use_cache=use_cache,
                                  logits_to_keep=1)


class MeasuredProtocols(MeasuredP1):
    def __init__(self, model, tokenizer, progress):
        super().__init__(model, tokenizer, progress)
        from c2c.c2c_transport import LoopbackChannel
        self.reverse_channel = LoopbackChannel()
        self.prelude = None

    def snapshot(self):
        value = super().snapshot()
        if self.prelude is not None and self.prelude is not self.state:
            value['protocol_preparation'] = {k: self.prelude.get(k) for k in
                ('timings', 'cpu_timings', 'communication', 'transfers', 'endpoint_input_tokens')}
        return value

    def initial_prefill(self, role, prompt):
        """按该端初始可见信息形成缓存；补齐后重新构建，并计入两次计算。"""
        torch = self.torch
        ids = self.tokenizer.apply_chat_template(prompt, tokenize=True, add_generation_prompt=True, enable_thinking=False)
        if len(ids) >= self.capacity:
            raise CapacityError('initial input exceeds capacity')
        index = 0 if role == 'receiver' else 1
        tensor = torch.tensor([ids], device='cuda')
        with torch.inference_mode():
            out = self.measured(role+'_initial_prefill', lambda:self.model.model_list[index](
                input_ids=tensor, attention_mask=torch.ones_like(tensor), use_cache=True, logits_to_keep=1))
        cache_tokens = out.past_key_values.get_seq_length()
        assert cache_tokens == len(ids)
        del out, tensor
        self.state['endpoint_input_tokens'][role+'_initial_prefill'] = len(ids)

    def transfer_text(self, source, destination, route, metadata):
        """两条方向独立TCP通道，保留每份补传字节及实际接收摘要。"""
        began = time.perf_counter()
        payload = missing_payload(source, destination)
        obj = {'metadata': {**metadata, 'route': route, 'kind': 'raw_missing_input_v1'}, 'input': payload}
        wire = canonical(obj).encode('utf-8')
        self.state['cpu_timings'][route+'_text_pack_s'] = time.perf_counter()-began
        channel = self.channel if route == 'sender_to_receiver' else self.reverse_channel
        began = time.perf_counter()
        received, count = channel.transfer(wire)
        self.state['cpu_timings'][route+'_text_transport_s'] = time.perf_counter()-began
        began = time.perf_counter()
        decoded = json.loads(received)
        if decoded['metadata'] != obj['metadata']:
            raise ValueError('补传元数据不一致')
        merged = merge_received(destination, decoded['input'])
        self.state['cpu_timings'][route+'_text_unpack_reconstruct_s'] = time.perf_counter()-began
        raw = raw_text_bytes(payload)
        record = {'route': route, 'supplemental_text_bytes': raw, 'serialized_payload_bytes':len(wire),
            'metadata_and_container_bytes':len(wire)-raw, 'framing_bytes':8,
            'actual_sent_bytes':len(wire)+8, 'actual_received_bytes':count,
            'payload_sha256':hashlib.sha256(wire).hexdigest(),
            'receive_sha256':hashlib.sha256(received).hexdigest(), 'bytes_equal':True,
            'question_transmitted':payload['q'] is not None,
            'paragraph_positions':[p['position'] for p in payload['paragraphs']]}
        self.state['transfers'].append(record)
        for field in ('supplemental_text_bytes','serialized_payload_bytes','metadata_and_container_bytes',
                      'framing_bytes','actual_sent_bytes','actual_received_bytes'):
            self.state['communication'][field] += record[field]
        self.persist(force=True)
        self.progress()
        return merged

    def generate_protocol(self, row, spec, protocol, path, metadata, *, max_new_tokens=1024,
                          diagnostic_tokens=None, check_fusion=False):
        """保持初始信息边界，按实收原文构造对齐输入，随后复用P1融合与生成。"""
        if path not in ('c2c', 'raw_forward') or (protocol == 'P1' and path != 'c2c'):
            raise ValueError('不适用的通信路径')
        if protocol == 'P1':
            s, r = endpoint_views(row, protocol)
            return super().generate(messages(spec,row['task'],r), metadata,
                max_new_tokens=None if diagnostic_tokens is not None else max_new_tokens,
                diagnostic_tokens=diagnostic_tokens, check_fusion=check_fusion)
        began = time.perf_counter()
        self.state = {'active':False, 'began':began, 'metadata':metadata, 'timings':{}, 'cpu_timings':{},
            'projector_events':[], 'generated_token_ids':[], 'transfers':[], 'endpoint_input_tokens':{},
            'communication': {**{k:0 for k in ('raw_kv_bytes','serialized_payload_bytes','metadata_and_container_bytes',
                'framing_bytes','actual_sent_bytes','actual_received_bytes','generated_text_bytes','supplemental_text_bytes')},
                'keys':[], 'values':[], 'bytes_equal':True}}
        self.prelude = self.state
        torch = self.torch
        torch.cuda.reset_peak_memory_stats()
        model = self.model
        result = None
        try:
            sender, receiver = endpoint_views(row, protocol)
            self.state['endpoint_input_tokens'] = {role+'_visible':len(self.tokenizer.apply_chat_template(
                messages(spec,row['task'],view),tokenize=True,add_generation_prompt=True,enable_thinking=False))
                for role,view in [('sender',sender),('receiver',receiver)]}
            self.initial_prefill('receiver', messages(spec,row['task'],receiver))
            if protocol == 'P2' and path == 'c2c':
                self.initial_prefill('sender', messages(spec,row['task'],sender))
            # P2先补齐Sender缺失的Receiver段落，随后Receiver只接收其缺失的Sender段落。
            full_sender = (self.transfer_text(receiver,sender,'receiver_to_sender',metadata)
                           if protocol == 'P2' and path == 'c2c' else sender)
            full_receiver = self.transfer_text(sender,receiver,'sender_to_receiver',metadata)
            if path == 'c2c' and full_sender != full_receiver:
                raise ValueError('实际补齐后两端输入不一致')
            final_messages = messages(spec,row['task'],full_receiver)
            self.prelude['peak_allocated_bytes'] = torch.cuda.max_memory_allocated()
            if path == 'raw_forward':
                self.model = ReceiverOnly(model)
            result = super().generate(final_messages,metadata,
                max_new_tokens=None if diagnostic_tokens is not None else max_new_tokens,
                diagnostic_tokens=diagnostic_tokens, check_fusion=check_fusion and path=='c2c')
            return result
        finally:
            self.model = model
            pre = self.prelude
            if self.state is not pre:
                # 保留部分异常记录；已完成补传成本不能因后续OOM而丢失。
                for old,new in [('receiver_local_prefill','receiver_additional_prefill'),
                                ('sender_prefill','sender_reconstruction_prefill' if protocol=='P2' else 'sender_prefill')]:
                    if old in self.state['timings'] and old != new:
                        self.state['timings'][new] = self.state['timings'].pop(old)
                self.state['timings'].update(pre['timings'])
                self.state['cpu_timings'].update(pre['cpu_timings'])
                comm = self.state.get('communication')
                if comm is not None:
                    for field,value in pre['communication'].items():
                        if isinstance(value,int) and not isinstance(value,bool): comm[field] += value
                else:
                    # raw路径没有KV交换，或者在KV交换之前异常。
                    comm = dict(pre['communication'])
                    self.state['communication'] = comm
                self.state['began'] = began
                self.state['supplemental_transfers'] = pre['transfers']
                self.state['endpoint_input_tokens'] = pre['endpoint_input_tokens']
                if result is not None:
                    result.update(communication=comm, supplemental_transfers=pre['transfers'],
                        endpoint_input_tokens=pre['endpoint_input_tokens'],
                        hot_pipeline_wall_s=time.perf_counter()-began,
                        adaptation='raw_supplement_and_aligned_reconstruction' if path=='c2c' else 'raw_forward_and_receiver_reconstruction')
                    if path == 'raw_forward':
                        result['sender_input_tokens'] = 0
                    result['memory']['peak_allocated_bytes'] = max(result['memory']['peak_allocated_bytes'],pre['peak_allocated_bytes'])
                    result['timings'] = self.state['timings']
                    result['cpu_timings'] = self.state['cpu_timings']
            self.prelude = None
            self.persist(force=True)

    def close(self):
        self.reverse_channel.close()
        super().close()
