"""固定 OpenHermes 文件并复用官方消息/过滤函数，产出可复查的训练缓存。"""

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / 'src'))
from project_paths import official_repo, asset_dir

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REVISION = "b82037821055c377bed0d495e72e46de3bc72e84"
SOURCE_SHA = "abe573d17eade4161aac321028027dd5ba614a6d9516d51bde9299d5353e1609"
SOURCE_SIZE = 1936276651


def digest(path):
    """流式计算文件摘要，避免把大文件复制到内存。"""
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def preprocess(batch, indices, model_path, repo):
    """过滤采用官方默认 thinking；训练文本采用官方 enable_thinking=False。"""
    from transformers import AutoTokenizer
    sys.path.insert(0, repo)
    from rosetta.train.dataset_adapters import extract_openhermes_messages
    global TOKENIZER
    if "TOKENIZER" not in globals():
        TOKENIZER = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    tok = TOKENIZER
    messages = [extract_openhermes_messages({k: v[i] for k, v in batch.items()}) for i in range(len(indices))]
    filter_texts = [tok.apply_chat_template(m, tokenize=False, add_generation_prompt=False) for m in messages]
    filter_ids = tok(filter_texts, add_special_tokens=False)["input_ids"]
    full = [tok.apply_chat_template(m, tokenize=False, add_generation_prompt=False, enable_thinking=False) for m in messages]
    prompt = [tok.apply_chat_template(m[:-1], tokenize=False, add_generation_prompt=True, enable_thinking=False) for m in messages]
    ids = tok(full, add_special_tokens=False)["input_ids"]
    prompts = tok(prompt, add_special_tokens=False)["input_ids"]
    return {"source_row": indices, "messages": messages, "filter_length": [len(x) for x in filter_ids],
            "input_ids": ids, "instruction_length": [len(x) for x in prompts],
            "supervised_tokens": [max(0, len(x)-len(p)) for x, p in zip(ids, prompts)]}


def main(args):
    """先取原文件前 500K，再过滤，再用独立 seed42 固定划分。"""
    import numpy as np
    import torch
    from datasets import load_dataset, load_from_disk
    root = Path(args.root).resolve()
    out = asset_dir(root, "runs") / args.run_id
    out.mkdir(parents=True, exist_ok=False)
    target = asset_dir(root, "data") / ("openhermes_formal_" + REVISION[:12])
    target.mkdir(parents=True, exist_ok=True)
    source = target / "openhermes2_5.json"
    url = f"https://huggingface.co/datasets/teknium/OpenHermes-2.5/resolve/{REVISION}/openhermes2_5.json"
    write(out / "source.json", {"repository": "teknium/OpenHermes-2.5", "revision": REVISION,
                                "url": url, "expected_size": SOURCE_SIZE, "expected_sha256": SOURCE_SHA})
    if not source.exists():
        part = source.with_suffix(".json.part")
        subprocess.run(["curl", "-fL", "--retry", "5", "--retry-delay", "10", "--connect-timeout", "20",
                        "--max-time", "10800", "-C", "-", "-o", str(part), url], check=True)
        if part.stat().st_size != SOURCE_SIZE or digest(part) != SOURCE_SHA:
            raise ValueError("下载文件与固定仓库 LFS 摘要不一致")
        part.rename(source)
    assert source.stat().st_size == SOURCE_SIZE and digest(source) == SOURCE_SHA
    print("SOURCE_VERIFIED", flush=True)
    cached = target / "preprocessed"
    if cached.exists():
        ds = load_from_disk(str(cached))
    else:
        raw = load_dataset("json", data_files=str(source), split="train", cache_dir=str(target / "hf_cache"))
        write(out / "raw_count.json", {"raw_rows": len(raw), "selected_rows": min(500000, len(raw))})
        raw = raw.select(range(min(500000, len(raw))))
        ds = raw.map(preprocess, batched=True, batch_size=128, with_indices=True, num_proc=4,
                     fn_kwargs={"model_path": str(asset_dir(root, "models") / "Qwen3-0.6B"), "repo": str(official_repo(root))},
                     remove_columns=raw.column_names, desc="固定模板预处理")
        ds.save_to_disk(str(cached))
    lengths = np.asarray(ds["filter_length"])
    accepted = np.flatnonzero(lengths <= 2048).tolist()
    filtered = ds.select(accepted)
    assert all(n > 0 for n in filtered["supervised_tokens"]), "存在无监督 token 的样本，需记录差异后再冻结"
    generator = torch.Generator().manual_seed(42)
    order = torch.randperm(len(filtered), generator=generator).tolist()
    train_count = int(len(filtered) * .99)
    train_ids, val_ids = order[:train_count], order[train_count:]
    rows = filtered["source_row"]
    write(target / "split.json", {"seed": 42, "method": "torch.randperm with independent Generator",
                                  "train_indices": train_ids, "validation_indices": val_ids})
    filtered.save_to_disk(str(target / "filtered"))
    train_rows, val_rows = [rows[i] for i in train_ids], [rows[i] for i in val_ids]
    write(target / "source_rows.json", {"train": train_rows, "validation": val_rows})
    # 固定哈希集合用于后续测试重合核查，不使用测试分数选择训练配置。
    with (target / "conversation_hashes.jsonl").open("w") as stream:
        for i, item in enumerate(filtered):
            text = json.dumps(item["messages"], sort_keys=True, ensure_ascii=False)
            stream.write(json.dumps({"source_row": item["source_row"], "sha256": hashlib.sha256(text.encode()).hexdigest()}) + "\n")
    manifest = {"source_revision": REVISION, "source_sha256": SOURCE_SHA, "source_size": SOURCE_SIZE,
                "selected_rows": len(ds), "retained_rows": len(filtered), "filtered_out": len(ds)-len(filtered),
                "train_rows": len(train_ids), "validation_rows": len(val_ids), "seed": 42,
                "split_method": "独立 torch.Generator(seed=42)，固定索引；避免模型初始化耗 RNG 改变划分",
                "split_sha256": digest(target / "split.json"), "source_rows_sha256": digest(target / "source_rows.json"),
                "cache": str(target / "filtered"), "max_length": 2048,
                "filter_semantics": "官方默认 thinking 模板计数 <=2048；先前500K再过滤",
                "training_semantics": "官方 ChatDataset 的 enable_thinking=False；监督最后一条回答",
                "length_percentiles": {str(p): float(np.percentile(filtered["filter_length"], p)) for p in [0,50,90,95,99,100]},
                "optimizer_updates": (len(train_ids)+255)//256, "effective_batch": 256,
                "test_overlap": "待执行固定测试题文本规范化匹配；正式数据验收尚未完成",
                "code_sha256": digest(__file__), "finished_unix": time.time()}
    write(target / "manifest.json", manifest)
    write(out / "result.json", manifest)
    print(json.dumps(manifest, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--run-id", required=True)
    a = parser.parse_args()
    try:
        main(a)
    except Exception as e:
        p = Path(a.root) / "runs" / a.run_id
        p.mkdir(parents=True, exist_ok=True)
        write(p / "failure.json", {"error": str(e), "type": type(e).__name__, "time": time.time()})
        raise
