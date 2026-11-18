"""从逐题成绩计算各协议各方向的指标，也支持汇总一次新运行。"""
import argparse
import csv
import gzip
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRICS = {'gsm8k':('accuracy',), 'hotpotqa':('em','f1'), 'humaneval':('pass@1',)}


def released_rows():
    with gzip.open(ROOT / 'experiments/records/scores.csv.gz','rt',encoding='utf-8',newline='') as f:
        yield from csv.DictReader(f)


def batch_rows(batch):
    """执行成绩与本次预测按规范化摘要匹配，避免复用其他生成的分数。"""
    import hashlib
    config = json.loads((batch/'config.json').read_text(encoding='utf-8'))
    for d in config['directions']:
        sub = batch/d
        scores = {}
        execution = sub/'humaneval_execution/samples.jsonl'
        if execution.exists():
            scores = {r['task_id']:r for r in map(json.loads,execution.read_text(encoding='utf-8').splitlines())}
        count = 0
        with (sub/'predictions.jsonl').open(encoding='utf-8') as f:
            for r in map(json.loads,f):
                values = r['score'].copy()
                if r['task']=='humaneval':
                    if r['task_id'] not in scores:
                        raise ValueError('请先对本次输出运行 score_code.py')
                    s = scores.pop(r['task_id'])
                    sha = hashlib.sha256(json.dumps(r,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
                    if s['prediction_sha256'] != sha:
                        raise ValueError('HumanEval 执行记录来自其他预测')
                    values['pass@1'] = s['pass@1']
                yield {**r, **values}
                count += 1
        if count != config['expected_samples'] or scores:
            raise ValueError('样本覆盖与本次计划不符')


def aggregate(rows):
    """full 表示当前协议的全部题，common_7345 表示 HotpotQA 的共同子集。"""
    groups = defaultdict(list)
    keys = set()
    for r in rows:
        k = r['protocol'],r['direction'],r['task'],r['task_id']
        if k in keys:
            raise ValueError(f'重复题号 {k}')
        keys.add(k)
        views = ['full']
        if r['task']=='hotpotqa' and r['common_7345'] in (True,'True'):
            views.append('common_7345')
        for view in views:
            for metric in METRICS[r['task']]:
                groups[k[:3]+(view,metric)].append(float(r[metric]))
    return {k:(len(v),sum(v)/len(v)) for k,v in groups.items()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--protocol', choices=['P1','P2','P3','P4'])
    parser.add_argument('--task', choices=METRICS)
    parser.add_argument('--batch', type=Path, help='汇总 evaluate.py 输出的运行目录')
    parser.add_argument('--common', action='store_true', help='只看 HotpotQA 共同子集')
    args = parser.parse_args()
    rows = batch_rows(args.batch) if args.batch else released_rows()
    stats = aggregate(rows)
    print('protocol direction task view metric n percent')
    for (p,d,t,v,m),(n,a) in sorted(stats.items()):
        if (args.protocol and args.protocol!=p) or (args.task and args.task!=t):
            continue
        if v != ('common_7345' if args.common else 'full'):
            continue
        print(p,d,t,v,m,n,f'{100*a:.2f}')
