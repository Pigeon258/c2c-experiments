"""使用已训练的融合器，在指定协议与任务上生成并记录逐题输出。"""
import argparse
import gc
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from project_paths import asset_dir, official_repo
from c2c.c2c_informal_eval import read_json, selected_samples, digest
from c2c.c2c_protocols import PROTOCOL_COUNTS, synthetic_row
from c2c.c2c_attempt_records import score_attempt
from c2c.c2c_protocol_runtime import MeasuredProtocols, CapacityError


def load_model(config, direction, checkpoint):
    """按训练方向核对两端模型，恢复门温度和全部逐层融合器。"""
    import torch
    from c2c.c2c_cache_compat import enable_inference_cache_compat
    from c2c.c2c_alignment import apply_paper_alignment
    from c2c.c2c_smoke import load_official
    revision = subprocess.check_output(['git', '-C', str(official_repo(ROOT)), 'rev-parse', 'HEAD'], text=True).strip()
    frozen = read_json(ROOT / 'experiments/configs/c2c_train_validation_frozen.json')
    dirty = subprocess.check_output(['git', '-C', str(official_repo(ROOT)), 'status', '--porcelain'], text=True)
    if dirty.strip() or revision != frozen['official_commit']:
        raise ValueError('C2C 上游版本不匹配')
    recipe = read_json(ROOT / frozen['configurations'][direction]['path'])['model']
    complete = read_json(checkpoint / 'complete.json')
    trained = read_json(checkpoint.parent / 'config.json')['model']
    for key in ('base_model', 'teacher_model'):
        if Path(trained[key]).name != Path(recipe[key]).name:
            raise ValueError('checkpoint 的模型方向与所选方向不一致')
        recipe[key] = str(asset_dir(ROOT, 'models') / Path(recipe[key]).name)
    official = load_official(ROOT)
    enable_inference_cache_compat()
    official.enable_full_determinism()
    official.set_seed(config['seed'])
    model, tokenizer, _, _ = official.setup_models(recipe, 'rosetta', 'cuda', torch.bfloat16)
    apply_paper_alignment(model, recipe['layer_alignment_contract'])
    if len(model.projector_list) != complete['projectors'] or complete['projectors'] != 28:
        raise ValueError('保存点的融合器数量不匹配')
    weights = {}
    for i, projector in enumerate(model.projector_list):
        path = checkpoint / f'projector_{i}.pt'
        state = torch.load(path, map_location='cpu', weights_only=True)
        projector.gate_temperature = projector.gate_temperature.float()
        projector.load_state_dict(state, strict=True)
        weights[path.name] = digest(path)
    return model.eval().requires_grad_(False), tokenizer, weights, complete['step']


def select_rows(config, task, protocol):
    if task not in PROTOCOL_COUNTS[protocol]:
        raise ValueError(f'{protocol} 没有 {task} 的正式条件')
    settings = dict(config, tasks={task: config['tasks'][task]})
    result = selected_samples(settings, asset_dir(ROOT, 'data') / 'test_sources')
    if protocol == 'P2':
        result = [row for row in result if row['common_7345']]
    if len(result) != PROTOCOL_COUNTS[protocol][task]:
        raise ValueError('题数与实验配置不一致')
    return result


def run(args):
    import torch
    torch.set_num_threads(2)
    config = read_json(ROOT / 'experiments/configs/evaluation.json')
    spec = read_json(ROOT / 'experiments/configs/prompts.json')
    rows = select_rows(config, args.task, args.protocol)
    if args.limit is not None:
        if not 1 <= args.limit <= len(rows):
            raise ValueError('limit 应在完整题数范围内')
        rows = rows[:args.limit]
    if args.output.exists():
        raise FileExistsError(args.output)
    model, tokenizer, weights, step = load_model(config, args.direction, args.checkpoint)
    batch = args.output
    subdir = batch / args.direction
    subdir.mkdir(parents=True, exist_ok=False)
    def line(f, row):
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
    with (batch / 'samples.jsonl').open('w', encoding='utf-8') as f:
        for row in rows:
            line(f, row)
    with (batch / 'config.json').open('w', encoding='utf-8') as f:
        line(f, {'directions':[args.direction], 'protocol':args.protocol, 'task':args.task,
                 'formal_result':False, 'checkpoint_step':step, 'weights':weights,
                 'expected_samples':len(rows), 'generation':config['generation']})
    runtime = MeasuredProtocols(model, tokenizer, lambda: None)
    try:
        for i in range(3):
            runtime.generate_protocol(synthetic_row(args.task), spec, args.protocol, 'c2c',
                                      {'purpose':'synthetic_warmup','task':args.task,'repeat':i},
                                      diagnostic_tokens=8)
        with (subdir / 'predictions.jsonl').open('x', encoding='utf-8') as f:
            for row in rows:
                meta = {'schema':'c2c_formal_protocols_v1', 'direction':args.direction,
                        'task':args.task, 'sample_id':row['task_id'], 'protocol':args.protocol, 'path':'c2c'}
                result = {'task':args.task, 'task_id':row['task_id'], 'direction':args.direction,
                          'protocol':args.protocol, 'common_7345':row.get('common_7345')}
                started = time.perf_counter()
                try:
                    measured = runtime.generate_protocol(row, spec, args.protocol, 'c2c', meta,
                                                         max_new_tokens=config['generation']['max_new_tokens'])
                    result.update(status='generated', **measured)
                except (torch.cuda.OutOfMemoryError, CapacityError) as error:
                    failure = 'capacity_failure' if isinstance(error, CapacityError) else 'oom_failure'
                    ids = list(runtime.state.get('generated_token_ids', []))
                    result.update(status=failure, termination=failure, output_tokens=len(ids),
                                  output=tokenizer.decode(ids, skip_special_tokens=True))
                model.kv_cache_dict = {}
                gc.collect()
                torch.cuda.empty_cache()
                result['elapsed_seconds'] = time.perf_counter() - started
                score_attempt(result, row)
                line(f, result)
                f.flush()
    finally:
        runtime.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--direction', choices=['M1','M2','M3'], required=True)
    parser.add_argument('--protocol', choices=list(PROTOCOL_COUNTS), required=True)
    parser.add_argument('--task', choices=['gsm8k','hotpotqa','humaneval'], required=True)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--limit', type=int, help='只跑原顺序前 N 题，供冒烟测试')
    os.environ.setdefault('WANDB_MODE', 'disabled')
    run(parser.parse_args())
