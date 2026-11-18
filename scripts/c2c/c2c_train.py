"""三方向线性退火训练入口：预检、完整训练及保持完整计划的有界验收。"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

import argparse
import copy
import hashlib
import json
import math
import platform
import subprocess
from contextlib import nullcontext

from project_paths import official_repo, asset_dir
from c2c.c2c_prepare_formal_data import digest
from c2c.c2c_alignment import CONTRACT, apply_paper_alignment
from c2c.c2c_config import frozen_training_contract

COMMIT = "bdb932aa63637959074a9a6fd59992a4d0d9ad22"


def model_names(config):
    """方向由配置明确指定；部署时仅替换模型根目录。"""
    sender = Path(config['model']['teacher_model']).name
    receiver = Path(config['model']['base_model']).name
    directions = {('Qwen3-0.6B', 'Qwen3-1.7B'): 'M1',
                  ('Qwen3-0.6B', 'Qwen3-4B'): 'M2',
                  ('Qwen3-4B', 'Qwen3-0.6B'): 'M3'}
    if (sender, receiver) not in directions:
        raise ValueError('模型方向不属于M1/M2/M3')
    return sender, receiver, directions[(sender, receiver)]


def assets(root, sources, wanted):
    """核对实际加载文件与固定 revision 的 LFS/普通 Git blob 摘要。"""
    result = {}
    for source in sources:
        name = source["repo_id"].split("/")[-1]
        if name not in wanted:
            continue
        files = {}
        for item in source["files"]:
            filename = item["rfilename"]
            if not filename.endswith((".json", ".txt", ".safetensors")):
                continue
            path = asset_dir(root, "models") / name / filename
            if path.stat().st_size != item["size"]:
                raise ValueError(f"模型文件长度不符：{name}/{filename}")
            if "lfs" in item:
                actual, expected = digest(path), item["lfs"]["sha256"]
            else:
                data = path.read_bytes()
                actual = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
                expected = item["blobId"]
            if actual != expected:
                raise ValueError(f"模型文件摘要不符：{name}/{filename}")
            files[filename] = actual
        result[name] = {"revision": source["revision"], "files": files}
    if set(result) != set(wanted):
        raise ValueError("缺少当前方向两端固定模型来源")
    if len({item['files']['tokenizer.json'] for item in result.values()}) != 1:
        raise ValueError("当前无对齐入口要求两端tokenizer一致")
    return result


def prepare(root, config):
    """仅 CPU 读取既有缓存和资产摘要，不构造基础模型、不初始化 CUDA。"""
    import torch
    import transformers
    from datasets import load_from_disk

    repo = official_repo(root)
    revision = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    dirty = subprocess.check_output(["git", "-C", str(repo), "status", "--porcelain"], text=True).strip()
    if revision != COMMIT or dirty:
        raise ValueError("官方代码必须处于固定且未修改的提交")
    if torch.__version__ != "2.6.0+cu124" or transformers.__version__ != "4.52.4" or sys.version_info[:2] != (3, 10):
        raise ValueError("入口要求已验收的 Python3.10/Torch2.6cu124/Transformers4.52.4")
    training = config["training"]
    if (training["num_epochs"], training["per_device_train_batch_size"], training["num_processes"],
        training["gradient_accumulation_steps"], training["max_length"], training["dtype"]) != (1, 1, 1, 256, 2048, "bfloat16"):
        raise ValueError("当前候选入口要求单进程BF16、micro1×accum256、长度2048完整一轮")
    sender, receiver, direction = model_names(config)
    frozen = frozen_training_contract(root, config, direction)
    source_path = root / "model_sources.json"
    if not source_path.exists():
        source_path = root / "experiments/sources/model_sources.json"
    sources = json.loads(source_path.read_text(encoding="utf-8-sig"))
    if 'Qwen3-4B' in (sender, receiver):
        sources = [s for s in sources if s['repo_id'] != 'Qwen/Qwen3-4B']
        sources.append(json.loads((root / 'experiments/sources/shared_4b_source.json').read_text()))
    verified_assets = assets(root, sources, {sender, receiver})
    if any(item["revision"] != frozen["models"][name]["revision"]
           for name, item in verified_assets.items()):
        raise ValueError("模型revision与训练冻结记录不一致")
    execution = config.get('execution', {})
    if execution.get('activation_offload', False) and direction != 'M2':
        raise ValueError('当前激活卸载候选仅验收M2方向')
    folder = asset_dir(root, "data") / config["data"]["folder"]
    manifest = json.loads((folder / "manifest.json").read_text())
    split = json.loads((folder / "split.json").read_text())
    if any(manifest[key] != frozen["data"][key]
           for key in ("source_revision", "source_sha256", "split_sha256", "source_rows_sha256")):
        raise ValueError("数据来源或划分与训练冻结记录不一致")
    for filename, key in [("split.json", "split_sha256"), ("source_rows.json", "source_rows_sha256")]:
        if digest(folder / filename) != manifest[key]:
            raise ValueError("冻结数据索引摘要不一致")
    data = load_from_disk(str(folder / "filtered"))
    train, validation = split["train_indices"], split["validation_indices"]
    if (len(train), len(validation)) != (493815, 4989) or set(train) & set(validation):
        raise ValueError("完整训练/验证数量或隔离不符")
    data_files = {p.relative_to(folder).as_posix(): digest(p)
                  for p in sorted(folder.rglob("*")) if p.is_file()}
    updates = math.ceil(len(train) / 256)
    if config["model"]["projector"]["params"]["anneal_steps"] != updates:
        raise ValueError("温度总步数必须等于完整 epoch 更新数")
    if config["model"]["mapping"] != "last_aligned" or config["model"]["is_do_alignment"]:
        raise ValueError("本入口要求last_aligned及相同tokenizer无需对齐")
    if config["model"].get("layer_alignment_contract") != CONTRACT:
        raise ValueError("须明确采用论文末层一一对齐合同")
    return data, train, validation, {"official_commit": revision, "models": verified_assets,
        "data_files": data_files, "torch": str(torch.__version__), "transformers": transformers.__version__,
        "python": platform.python_version(), "total_updates": updates,
        "warmup_steps": int(training["warmup_ratio"] * updates), "cuda_initialized": torch.cuda.is_initialized()}


def main(args):
    import torch
    from c2c.c2c_training import run_training, write_json
    from c2c.c2c_control import BoundaryStop, BoundaryCheckpoint
    root = args.root.resolve()
    config = json.loads(args.config.read_text(encoding="utf-8-sig"))
    output = asset_dir(root, "runs") / args.run_id
    output.mkdir(parents=True, exist_ok=False)
    data, train_ids, val_ids, provenance = prepare(root, config)
    write_json(output / "preflight.json", provenance)
    if args.mode == "preflight":
        print(json.dumps({"run_id": args.run_id, "assets_verified": True,
                          "train": len(train_ids), "validation": len(val_ids),
                          "cuda_initialized": torch.cuda.is_initialized()}), flush=True)
        return
    diagnostic = args.mode == "diagnostic"
    if not diagnostic and (args.stop_after or args.validation_limit or args.diagnostic_eval_every):
        raise ValueError("完整训练不接受缩减条件")
    if diagnostic and args.stop_after is None:
        raise ValueError("诊断必须显式给出停止点")
    if args.validation_limit is not None and not 0 < args.validation_limit <= len(val_ids):
        raise ValueError("诊断验证数量必须在完整验证集范围内")
    if args.diagnostic_eval_every:
        if args.diagnostic_eval_every < 1:
            raise ValueError("诊断验证间隔必须为正数")
        config["output"]["eval_steps"] = args.diagnostic_eval_every
    from c2c.c2c_smoke import load_official
    from c2c.c2c_checkpoint import make_optimizer
    from c2c.c2c_m1_gpu import preflight
    from transformers.optimization import get_scheduler
    official = load_official(root)
    from rosetta.train.dataset_adapters import ChatDataset, RosettaDataCollator
    official.enable_full_determinism()
    environment = preflight(root)
    torch.autograd.set_detect_anomaly(False)
    official.set_seed(config["training"]["seed"])
    # config 保留方法字段；仅将资产/输出位置绑定到当前部署。
    sender, receiver, direction = model_names(config)
    config["model"].update(base_model=str(asset_dir(root, "models") / receiver),
                            teacher_model=str(asset_dir(root, "models") / sender))
    model, tokenizer, _, _ = official.setup_models(config["model"], "rosetta", "cuda", torch.bfloat16)
    alignment = apply_paper_alignment(model, config["model"]["layer_alignment_contract"])
    write_json(output / "layer_alignment.json", alignment)
    for base in model.model_list:
        official.freeze_model(base)
    official.unfreeze_projectors(model)

    class Chats:
        def __init__(self, indices):
            self.indices = indices
        def __len__(self):
            return len(self.indices)
        def __getitem__(self, index):
            return data[self.indices[index]]["messages"]

    train = ChatDataset(Chats(train_ids), tokenizer, max_length=2048)
    used_val_ids = val_ids[:args.validation_limit] if args.validation_limit else val_ids
    validation = ChatDataset(Chats(used_val_ids), tokenizer, max_length=2048)
    collator = RosettaDataCollator(tokenizer, max_length=2048, do_alignment=False)
    training = config["training"]
    optimizer, names = make_optimizer(model, training["learning_rate"], training["weight_decay"],
                                      training["adam_betas"], training["adam_eps"])
    updates, warmup = provenance["total_updates"], provenance["warmup_steps"]
    scheduler = get_scheduler("linear", optimizer, num_warmup_steps=warmup, num_training_steps=updates)
    offload = None
    if config.get('execution', {}).get('activation_offload', False):
        from c2c.c2c_memory import ActivationOffload
        offload = ActivationOffload(model)
    code = [Path(__file__), root / "src/c2c/c2c_training.py", root / "src/c2c/c2c_checkpoint.py",
            root / "src/c2c/c2c_smoke.py", root / "src/c2c/c2c_m1_gpu.py",
            root / "src/c2c/c2c_alignment.py", root / "src/c2c/c2c_config.py",
            root / "src/c2c/c2c_control.py", root / 'src/c2c/c2c_runtime.py']
    if offload is not None:
        code.append(root / 'src/c2c/c2c_memory.py')
    config["output"]["output_dir"] = str(output)
    contract = {"recipe": copy.deepcopy(config), "provenance": provenance, "code": {p.name: digest(p) for p in code},
                "seed": training["seed"], "parameter_groups": names, "diagnostic": diagnostic,
                "validation_ids": used_val_ids, "temperature": "linear_after_optimizer_update",
                "loss": "mean_response_next_token_cross_entropy", "gpu": environment["gpu_name"]}
    # run_id/部署目录不属于训练条件；不同窗口仍沿同一计划和数据进度。
    contract["recipe"]["output"]["output_dir"] = "<run_directory>"
    write_json(output / "config.json", config)
    write_json(output / "environment.json", environment)
    write_json(output / "resume_contract.json", contract)
    checkpoint_control = BoundaryCheckpoint(output / 'SAVE_REQUEST', args.checkpoint_interval_seconds)
    write_json(output / 'runtime_protection.json', {
        'checkpoint_mode': 'in_process', 'interval_seconds': args.checkpoint_interval_seconds,
        'save_request': 'SAVE_REQUEST', 'pause_request': 'STOP_REQUEST'})
    with BoundaryStop(output / "STOP_REQUEST") as should_stop:
        result, _ = run_training(model, train, validation, collator,
            lambda batch: official.train_step(model, batch, tokenizer, 2048, "cuda", "rosetta"),
            optimizer, scheduler, output, contract, device="cuda", macro_batch=256,
            total_updates=updates, warmup_steps=warmup, eval_steps=config["output"]["eval_steps"],
            save_steps=config["output"]["save_steps"], max_grad_norm=training["max_grad_norm"],
            stop_after=args.stop_after, resume_from=args.resume_from,
            backward_context=offload.context if offload else nullcontext,
            stop_requested=should_stop, checkpoint_requested=checkpoint_control)
    result.update(diagnostic=diagnostic, formal_run=not diagnostic,
                  formal_result=not diagnostic and result["epoch_completed"],
                  full_validation=not args.validation_limit, full_recipe_validation_samples=len(val_ids),
                  cuda_peak_allocated_GiB=torch.cuda.max_memory_allocated()/2**30,
                  direction=direction)
    import resource
    result['process_peak_rss_GiB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20
    if offload is not None:
        result['activation_offload'] = offload.report()
    write_json(output / "result.json", result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["preflight", "diagnostic", "formal"])
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--stop-after", type=int)
    parser.add_argument("--validation-limit", type=int)
    parser.add_argument("--diagnostic-eval-every", type=int)
    parser.add_argument("--resume-from", type=Path)
    parser.add_argument('--checkpoint-interval-seconds', type=float, default=3600)
    args = parser.parse_args()
    main(args)
