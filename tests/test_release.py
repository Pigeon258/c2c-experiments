"""核对发布成绩、HumanEval 题号与生成文本，以及分段证据补齐。"""
import csv
import json
import re
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'scripts'),str(ROOT/'src')]
from summarize import aggregate, released_rows
from c2c.c2c_protocols import endpoint_views, merge_received, missing_payload, synthetic_row


class ReleasedResults(unittest.TestCase):
    def test_all_reported_means(self):
        stats=aggregate(released_rows())
        conditions=set()
        referenced=set()
        expression=r'^\| (M[123])/(P[1234])/(\w+)/C2C \| (full|common_7345) \| (\d+) \| (\d+) \| (em|f1|accuracy|pass@1) \| ([\d.]+) \|'
        for p in sorted((ROOT/'reports/formal').glob('P?.md')):
            for m in re.finditer(expression,p.read_text(encoding='utf-8'),re.M):
                d,protocol,task,view,planned,scored,metric,val=m.groups()
                key=protocol,d,task,view,metric
                n,mean=stats[key]
                self.assertEqual(n,int(planned))
                self.assertEqual(n,int(scored))
                self.assertAlmostEqual(mean,float(val),delta=0.00000051)
                referenced.add(key)
                conditions.add((protocol,d,task))
        self.assertEqual(referenced,set(stats))
        self.assertEqual(len(conditions),24)
        self.assertEqual(sum(stats[(p,d,t,'full',{'gsm8k':'accuracy','hotpotqa':'em','humaneval':'pass@1'}[t])][0]
                             for p,d,t in conditions),97578)

    def test_humaneval_records(self):
        base=ROOT/'experiments/records'
        with (base/'humaneval-outputs.jsonl').open(encoding='utf-8') as f:
            outputs={(r['direction'],r['task_id']) for r in map(json.loads,f) if isinstance(r['output'], str)}
        formal={(r['protocol'],r['direction'],r['task_id']):float(r['pass@1'])
                for r in released_rows() if r['task']=='humaneval'}
        extra={d:0 for d in ['M1','M2','M3']}
        seen=set()
        with (base/'humaneval.csv').open(encoding='utf-8',newline='') as f:
            for r in csv.DictReader(f):
                key=r['protocol'],r['direction'],r['task_id']
                self.assertNotIn(key,seen)
                seen.add(key)
                self.assertEqual(int(r['passed']),formal[key])
                self.assertEqual(r['execution_status']=='passed',bool(int(r['passed'])))
                if key[0]=='P1':
                    extra[key[1]]+=int(r['passed_after_cleanup'])-int(r['passed'])
        self.assertEqual(len(seen),984)
        self.assertEqual(seen,set(formal))
        self.assertEqual(outputs, {k[1:] for k in seen})
        self.assertEqual(len(outputs),492)
        self.assertEqual(extra,{'M1':0,'M2':0,'M3':3})

    def test_reconstructed_prompt(self):
        row=synthetic_row('hotpotqa')
        expected,_=endpoint_views(row,'P1')
        for protocol in ('P2','P3','P4'):
            sender,receiver=endpoint_views(row,protocol)
            self.assertEqual(merge_received(sender,missing_payload(receiver,sender)),expected)
            self.assertEqual(merge_received(receiver,missing_payload(sender,receiver)),expected)
