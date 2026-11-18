def score_attempt(record, sample):
    """触顶文本照常评分；超时/OOM/容量失败保留诊断分数且主指标计零。"""
    from c2c.c2c_informal_eval import gsm_score
    from c2c.c2c_p1_metrics import hotpot_score
    task=sample['task']
    if task=='gsm8k': score=gsm_score(record['output'],sample['reference'])
    elif task=='hotpotqa': score=hotpot_score(record['output'],sample['reference'])
    else: score={'pass@1':0.0 if record['status']!='generated' else None}
    if record['status'] in ('timeout_failure','oom_failure','capacity_failure'):
        record['partial_output_score']=score
        score=({'accuracy':0.0} if task=='gsm8k' else {'em':0.0,'f1':0.0}
               if task=='hotpotqa' else {'pass@1':0.0})
    record['score']=score
