"""训练激活的选择性CPU卸载；权重保留GPU，诊断先验收数值等价性。"""

from collections import Counter
from contextlib import contextmanager
from pathlib import Path


def resident_bytes():
    """读取当前进程实际驻留内存，不把文件缓存当作激活占用。"""
    for line in Path('/proc/self/status').read_text().splitlines():
        if line.startswith('VmRSS:'):
            return int(line.split()[1]) * 1024
    return 0


class ActivationOffload:
    """保存反传所需激活到CPU；参数及其视图沿用原GPU存储。"""

    def __init__(self, model, minimum_bytes=65536, host_limit_bytes=24 * 2**30):
        self.parameter_storage = {
            (p.device, p.untyped_storage().data_ptr()) for p in model.parameters()
        }
        self.minimum_bytes = minimum_bytes
        self.host_limit_bytes = host_limit_bytes
        self.saved_bytes = 0
        self.offloaded_bytes = 0
        self.parameter_alias_bytes = 0
        self.shapes = Counter()

    def pack(self, tensor):
        """每个保存点独立复制，保留原dtype及当时值，不复用可变缓存快照。"""
        size = tensor.numel() * tensor.element_size()
        self.saved_bytes += size
        self.shapes[(str(tensor.dtype), tuple(tensor.shape))] += size
        is_parameter = (tensor.device, tensor.untyped_storage().data_ptr()) in self.parameter_storage
        if is_parameter:
            self.parameter_alias_bytes += size
        if tensor.device.type != 'cuda' or is_parameter or size < self.minimum_bytes:
            return tensor.detach()
        original_shape, original_stride = tuple(tensor.shape), tuple(tensor.stride())
        reduced = tensor.detach()
        # 广播视图只复制一份值，恢复时再展开；避免对重叠存储执行copy_。
        for axis, (length, stride) in enumerate(zip(original_shape, original_stride)):
            if length > 1 and stride == 0:
                reduced = reduced.narrow(axis, 0, 1)
        copied_bytes = reduced.numel() * reduced.element_size()
        if resident_bytes() + copied_bytes > self.host_limit_bytes:
            raise MemoryError('激活卸载达到本轮24GiB进程驻留内存预算')
        self.offloaded_bytes += copied_bytes
        return tensor.device, reduced.to('cpu'), original_shape, original_stride

    @staticmethod
    def unpack(packed):
        """按原dtype、stride及广播布局恢复到原设备。"""
        if isinstance(packed, tuple):
            import torch
            device, tensor, shape, stride = packed
            # to(device)可能把带行间padding的mask变成紧凑布局，破坏SDPA反向的对齐条件。
            restored = torch.empty_strided(tensor.shape, stride, dtype=tensor.dtype, device=device)
            restored.copy_(tensor)
            return restored.expand(shape)
        return packed

    @contextmanager
    def context(self):
        import torch
        with torch.autograd.graph.saved_tensors_hooks(self.pack, self.unpack):
            yield self

    def report(self):
        """累计保存字节含重复保存，不能把它解读为同时驻留的峰值。"""
        return {
            'saved_bytes_cumulative': self.saved_bytes,
            'offloaded_bytes_cumulative': self.offloaded_bytes,
            'parameter_alias_bytes_retained': self.parameter_alias_bytes,
            'largest_saved_shapes': [
                {'dtype': dtype, 'shape': list(shape), 'cumulative_bytes': size}
                for (dtype, shape), size in self.shapes.most_common(12)
            ],
        }
