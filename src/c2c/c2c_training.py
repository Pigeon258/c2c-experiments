"""论文线性温度训练循环；实际模型、标签与前向继续调用固定官方实现。"""

import json
import math
import time
from contextlib import nullcontext
from pathlib import Path

import torch

from c2c.c2c_checkpoint import (StatefulSampler, capture_rng, load_checkpoint,
                                restore_rng, save_checkpoint)


def linear_temperature(completed, total, initial=1.0, final=0.001):
    """以完整计划的已完成更新数计进度，提前停止不压缩退火曲线。"""
    if total <= 0 or not 0 <= completed <= total:
        raise ValueError("温度进度必须属于完整训练计划")
    return initial + (final - initial) * completed / total


def set_temperature(projectors, completed, total):
    """按论文线性设置FP32调度标量，避免随模型BF16存储而抹掉小步变化。"""
    value = linear_temperature(completed, total)
    for projector in projectors:
        if projector.gate_temperature.dtype != torch.float32:
            projector.gate_temperature = projector.gate_temperature.float()
        projector.gate_temperature.fill_(value)
    return value


def response_tokens(batch):
    """官方 wrapper 只返回最后 response 段的 loss；因 causal shift 排除段首。"""
    length = batch["kv_cache_index"][-1].shape[1]
    labels = batch["labels"][:, -length:]
    count = int((labels[:, 1:] != -100).sum())
    if count == 0:
        raise ValueError("当前 response 没有有效 next-token 监督，不能计算均值 loss")
    return count


def weighted_backward(batches, loss_fn):
    """按整个宏批次的有效 response token 数归一化，末尾窗口使用实际分母。"""
    counts = [response_tokens(batch) for batch in batches]
    denominator = sum(counts)
    numerator = 0.0
    for batch, count in zip(batches, counts):
        loss = loss_fn(batch)
        if not torch.isfinite(loss):
            raise FloatingPointError("训练 loss 非有限")
        (loss * (count / denominator)).backward()
        numerator += float(loss.detach()) * count
    return {"loss": numerator / denominator, "supervised_tokens": denominator,
            "micro_supervised_tokens": counts}


def evaluate(model, dataset, collator, loss_fn, device):
    """遍历传入的整个验证集；评估不更新参数，也不改变续训的 RNG。"""
    rng = capture_rng(device)
    was_training = model.training
    model.eval()
    numerator, denominator = 0.0, 0
    started = time.perf_counter()
    try:
        with torch.no_grad():
            for index in range(len(dataset)):
                batch = collator([dataset[index]])
                count = response_tokens(batch)
                loss = loss_fn(batch)
                if not torch.isfinite(loss):
                    raise FloatingPointError("验证 loss 非有限")
                numerator += float(loss) * count
                denominator += count
        if not denominator:
            raise ValueError("验证集不能为空")
    finally:
        model.train(was_training)
        restore_rng(rng, device)
    return {"loss": numerator / denominator, "samples": len(dataset),
            "supervised_tokens": denominator, "seconds": time.perf_counter() - started}


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_training(model, train, validation, collator, loss_fn, optimizer, scheduler,
                 output, contract, *, device, macro_batch, total_updates,
                 warmup_steps, eval_steps, save_steps, max_grad_norm=1.0,
                 stop_after=None, resume_from=None, backward_context=nullcontext,
                 stop_requested=None, checkpoint_requested=None):
    """单进程一个完整 epoch；停止与恢复都发生在 optimizer 更新边界。"""
    if total_updates != math.ceil(len(train) / macro_batch):
        raise ValueError("总更新数必须覆盖整个训练集且不得跨 epoch 补样本")
    end = total_updates if stop_after is None else stop_after
    if not 0 < end <= total_updates or min(eval_steps, save_steps) <= 0:
        raise ValueError("停止点或 eval/save 间隔无效")
    output = Path(output)
    sampler = StatefulSampler(len(train), contract["seed"])
    state = {"best_loss": None, "best_step": None, "best_checkpoint": None,
             "validation_history": []}
    start = 0
    model.train()
    set_temperature(model.projector_list, 0, total_updates)
    if resume_from:
        loaded = load_checkpoint(resume_from, model.projector_list, optimizer, scheduler,
                                 sampler, contract)
        start = loaded["step"]
        state = loaded["trainer_state"]
        if state is None or sampler.cursor != min(start * macro_batch, len(train)):
            raise ValueError("恢复点缺少选择状态或样本进度不符")
        if scheduler.last_epoch != start:
            raise ValueError("恢复的学习率调度步数不符")
        expected = torch.as_tensor(linear_temperature(start, total_updates),
                                   dtype=model.projector_list[0].gate_temperature.dtype)
        if any(float(p.gate_temperature) != float(expected) for p in model.projector_list):
            raise ValueError("checkpoint 不是当前论文线性温度计划")
        restore_rng(loaded["rng"], device)
        if loaded.get('runtime_migration'):
            write_json(output / 'resume_migration.json', loaded['runtime_migration'])
        del loaded
    if not start < end:
        raise ValueError("停止点必须晚于恢复步数")
    records = []
    checkpoint_path = None
    paused = False
    for step in range(start + 1, end + 1):
        if device == "cuda":
            torch.cuda.synchronize()
        started = time.perf_counter()
        actual_batch = min(macro_batch, len(train) - sampler.cursor)
        indices = [sampler.next_index() for _ in range(actual_batch)]
        batches = [collator([train[index]]) for index in indices]
        optimizer.zero_grad(set_to_none=True)
        lr_used = [group["lr"] for group in optimizer.param_groups]
        temperature_used = float(model.projector_list[0].gate_temperature)
        # 卸载仅改变反传激活的保存位置，沿用同一token归一化和累积顺序。
        with backward_context():
            loss_record = weighted_backward(batches, loss_fn)
        del batches
        parameters = list(model.projector_list.parameters())
        if not any(p.grad is not None for p in parameters):
            raise RuntimeError("融合器没有梯度")
        if any(p.grad is not None for base in model.model_list for p in base.parameters()):
            raise RuntimeError("被冻结的基础模型产生了参数梯度")
        norm = torch.nn.utils.clip_grad_norm_(parameters, max_grad_norm, error_if_nonfinite=True)
        optimizer.step()
        scheduler.step()
        optimizer.zero_grad(set_to_none=True)
        requested = set_temperature(model.projector_list, step, total_updates)
        if device == "cuda":
            torch.cuda.synchronize()
        record = {"step": step, "indices": indices, "actual_batch": actual_batch,
                  **loss_record, "lr_used": lr_used, "next_lr": scheduler.get_last_lr(),
                  "temperature_used": temperature_used, "temperature_next_requested": requested,
                  "temperature_next_stored": float(model.projector_list[0].gate_temperature),
                  "grad_norm": float(norm), "sampler_cursor": sampler.cursor,
                  "train_seconds": time.perf_counter() - started}
        final_epoch = step == total_updates
        should_eval = step % eval_steps == 0 or final_epoch
        new_best = False
        if should_eval:
            checked = evaluate(model, validation, collator, loss_fn, device)
            new_best = state["best_loss"] is None or checked["loss"] < state["best_loss"]
            state["validation_history"].append({"step": step, **checked})
            record["validation"] = checked
            if new_best:
                state.update(best_loss=checked["loss"], best_step=step,
                             best_checkpoint=str(output / f"checkpoint-{step}"))
        # 先完成该更新原定的验证，再响应暂停；接续时保留同一验证日程。
        paused = not final_epoch and bool(stop_requested and stop_requested())
        runtime_save = bool(checkpoint_requested and checkpoint_requested())
        saved_this_step = step % save_steps == 0 or new_best or step == end or paused or runtime_save
        if saved_this_step:
            checkpoint_path = output / f"checkpoint-{step}"
            saved_at = time.perf_counter()
            save_checkpoint(checkpoint_path, model.projector_list, optimizer, scheduler,
                            sampler, step, contract, device, trainer_state=state)
            record["save_seconds"] = time.perf_counter() - saved_at
            record["checkpoint"] = str(checkpoint_path)
            if runtime_save:
                record['operational_checkpoint'] = list(checkpoint_requested.reasons)
        records.append(record)
        with (output / "steps.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
        if saved_this_step and checkpoint_requested:
            checkpoint_requested.committed(checkpoint_path, step)
        print(json.dumps({key: value for key, value in record.items()
                          if key not in ("indices", "micro_supervised_tokens")}), flush=True)
        if paused:
            break
    result = {"start_step": start, "end_step": step, "planned_total_updates": total_updates,
              "planned_train_samples": len(train), "planned_validation_samples": len(validation),
              "consumed_samples": sampler.cursor, "epoch_completed": step == total_updates,
              "paused": paused, "remaining_updates": total_updates - step,
              "warmup_steps": warmup_steps, "checkpoint": str(checkpoint_path), **state}
    write_json(output / "result.json", result)
    return result, records
