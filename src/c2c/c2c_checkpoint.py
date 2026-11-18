"""C2C 单进程诊断的完整 checkpoint；只在 optimizer 更新边界保存。"""

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / 'src'))


import json
import random
from pathlib import Path

import numpy as np
import torch


class StatefulSampler:
    """保存随机排列、游标及独立生成器，恢复时接续同一条样本流。"""

    def __init__(self, size, seed):
        self.size = size
        self.generator = torch.Generator(device="cpu").manual_seed(seed)
        self.order = torch.randperm(size, generator=self.generator).tolist()
        self.cursor = 0
        self.epoch = 0

    def next_index(self):
        if self.cursor == self.size:
            self.order = torch.randperm(self.size, generator=self.generator).tolist()
            self.cursor = 0
            self.epoch += 1
        index = self.order[self.cursor]
        self.cursor += 1
        return index

    def state_dict(self):
        return {"size": self.size, "order": list(self.order), "cursor": self.cursor,
                "epoch": self.epoch, "generator_state": self.generator.get_state()}

    def load_state_dict(self, state):
        if state["size"] != self.size:
            raise ValueError("恢复时训练样本数量发生变化")
        self.order = list(state["order"])
        self.cursor, self.epoch = state["cursor"], state["epoch"]
        self.generator.set_state(state["generator_state"])


def capture_rng(device):
    """NumPy 数组转为普通列表，使训练状态可用 weights_only=True 加载。"""
    name, keys, position, has_gauss, cached_gauss = np.random.get_state()
    return {"python": random.getstate(),
            "numpy": [name, keys.tolist(), position, has_gauss, cached_gauss],
            "torch_cpu": torch.get_rng_state(),
            "torch_cuda": torch.cuda.get_rng_state_all() if device == "cuda" else []}


def restore_rng(state, device):
    """在模型、优化器、采样器等初始化和加载全部结束后调用。"""
    random.setstate(state["python"])
    name, keys, position, has_gauss, cached_gauss = state["numpy"]
    np.random.set_state((name, np.asarray(keys, dtype=np.uint32), position, has_gauss, cached_gauss))
    torch.set_rng_state(state["torch_cpu"])
    if device == "cuda":
        torch.cuda.set_rng_state_all(state["torch_cuda"])


def make_optimizer(module, learning_rate=1e-4, weight_decay=0.01,
                   betas=(0.9, 0.999), eps=1e-8):
    """保持既有三组顺序，并记录参数名以核对 optimizer 状态的对应关系。"""
    groups, names = [[], [], []], [[], [], []]
    for name, parameter in module.named_parameters():
        if not parameter.requires_grad:
            continue
        index = 0 if "gate" in name else 1 if "key_weight" in name or "value_weight" in name else 2
        groups[index].append(parameter)
        names[index].append(name)
    optimizer = torch.optim.AdamW([{"params": group, "lr": learning_rate} for group in groups],
                                  weight_decay=weight_decay, betas=tuple(betas), eps=eps)
    return optimizer, names


def save_checkpoint(folder, projectors, optimizer, scheduler, sampler, step, contract, device,
                    trainer_state=None):
    """保存参数、温度 buffer、优化状态与随机状态；最后写入完成标记。"""
    from rosetta.model.projector import save_projector

    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=False)
    # torch.__version__ 是 str 的子类 TorchVersion；规范元数据以保留严格加载方式。
    state = {"schema_version": 1, "contract": json.loads(json.dumps(contract)), "step": step,
             "optimizer": optimizer.state_dict(), "scheduler": scheduler.state_dict(),
             "sampler": sampler.state_dict(), "rng": capture_rng(device),
             "trainer_state": trainer_state}
    for index, projector in enumerate(projectors):
        torch.save(projector.state_dict(), folder / f"projector_{index}.pt")
        save_projector(projector, str(folder / f"projector_{index}.json"))
    torch.save(state, folder / "training_state.pt")
    (folder / "complete.json").write_text(json.dumps({"schema_version": 1, "step": step,
                                                     "projectors": len(projectors)}, indent=2), encoding="utf-8")


def load_checkpoint(folder, projectors, optimizer, scheduler, sampler, contract):
    """加载到既有融合器，保留 optimizer 参数引用；随机状态交给调用方最后恢复。"""
    folder = Path(folder)
    complete = json.loads((folder / "complete.json").read_text())
    state = torch.load(folder / "training_state.pt", map_location="cpu", weights_only=True, mmap=True)
    if state["schema_version"] != 1:
        raise ValueError("checkpoint 与当前训练计划/数据/环境/参数顺序不一致")
    from c2c.c2c_runtime import validate_resume_contract
    migration = validate_resume_contract(state['contract'], contract)
    if complete["projectors"] != len(projectors) or complete["step"] != state["step"]:
        raise ValueError("checkpoint 完成标记与内容不一致")
    for index, projector in enumerate(projectors):
        projector.load_state_dict(torch.load(folder / f"projector_{index}.pt", map_location="cpu",
                                             weights_only=True, mmap=True), strict=True)
    # scheduler 必须先构造并加载；之后加载 optimizer，避免其 LR 被初始化覆盖。
    scheduler.load_state_dict(state["scheduler"])
    optimizer.load_state_dict(state["optimizer"])
    sampler.load_state_dict(state["sampler"])
    if migration:
        state['runtime_migration'] = migration
    return state


def compare_values(left, right):
    """逐项精确比较完整状态；大张量只在不同时分块计算差异，控制临时内存。"""
    report = {"tensor_count": 0, "tensor_elements": 0, "max_abs_difference": 0.0,
              "difference_count": 0, "first_differences": []}

    def different(path):
        report["difference_count"] += 1
        if len(report["first_differences"]) < 10:
            report["first_differences"].append(path)

    def visit(a, b, path):
        if isinstance(a, torch.Tensor) and isinstance(b, torch.Tensor):
            report["tensor_count"] += 1
            report["tensor_elements"] += a.numel()
            if a.shape != b.shape or a.dtype != b.dtype:
                different(path)
            elif not torch.equal(a, b):
                different(path)
                for start in range(0, a.numel(), 1_000_000):
                    delta = (a.reshape(-1)[start:start + 1_000_000].double()
                             - b.reshape(-1)[start:start + 1_000_000].double()).abs().max().item()
                    report["max_abs_difference"] = max(report["max_abs_difference"], delta)
        elif isinstance(a, dict) and isinstance(b, dict):
            if a.keys() != b.keys():
                different(path + ".keys")
            for key in a.keys() & b.keys():
                visit(a[key], b[key], f"{path}.{key}")
        elif isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
            if type(a) is not type(b) or len(a) != len(b):
                different(path + ".sequence")
            for index, (x, y) in enumerate(zip(a, b)):
                visit(x, y, f"{path}[{index}]")
        elif type(a) is not type(b) or a != b:
            different(path)

    visit(left, right, "state")
    report["equal"] = report["difference_count"] == 0
    return report
