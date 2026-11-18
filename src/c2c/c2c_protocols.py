"""P1—P4的初始可见信息与原文补齐；模型输入不读取答案。"""
import copy
import hashlib
import json
import random

from c2c.c2c_informal_eval import format_evidence
from c2c.c2c_prompt_assembly import c2c_p1_candidate_messages

PROTOCOL_COUNTS = {
    'P1': {'gsm8k': 1319, 'hotpotqa': 7405, 'humaneval': 164},
    'P2': {'hotpotqa': 7345}, 'P3': {'hotpotqa': 7405},
    'P4': {'gsm8k': 1319, 'hotpotqa': 7405, 'humaneval': 164}}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def split_indices(sample_id, context, support_titles):
    """只在准备阶段使用支持标签，逐字复现共同P2分配随机源。"""
    order = list(range(len(context)))
    def shuffle(items, phase):
        seed = int(hashlib.sha256(f'42:{sample_id}:{phase}'.encode()).hexdigest(), 16)
        random.Random(seed).shuffle(items)
    shuffle(order, 'full_order')
    supports = [i for i, pair in enumerate(context) if pair[0] in set(support_titles)]
    valid = (len(context) == 10 and len({p[0] for p in context}) == 10
             and len(set(support_titles)) == len(supports) == 2)
    if not valid:
        return order, [], []
    noise = [i for i in range(10) if i not in supports]
    shuffle(supports, 'support')
    shuffle(noise, 'distractors')
    s, r = [supports[0]]+noise[:4], [supports[1]]+noise[4:]
    return order, [i for i in order if i in s], [i for i in order if i in r]


def endpoint_views(row, protocol):
    """返回各端实际拥有的题目和段落；P4接收端不含当前题目信息。"""
    if row['task'] not in PROTOCOL_COUNTS[protocol]:
        raise ValueError('该任务与协议不适用')
    order = row.get('evidence_order', [])
    context = row.get('context', [])
    if protocol == 'P2':
        if not row.get('common_7345'):
            raise ValueError('P2题目不符合共同结构')
        si, ri = row['sender_indices'], row['receiver_indices']
        if len(si) != 5 or len(ri) != 5 or set(si) & set(ri) or set(si+ri) != set(order):
            raise ValueError('P2分配不完整或有重合')
    else:
        si, ri = order, order if protocol == 'P1' else []
    rank = {index: j for j, index in enumerate(order)}
    def part(indices, question):
        return {'q': question, 'paragraphs': [
            {'position': rank[i], 'title': context[i][0], 'sentences': list(context[i][1])}
            for i in indices]}
    return part(si, row['question']), part(ri, None if protocol == 'P4' else row['question'])


def messages(spec, task, view):
    if view['q'] is None:
        p = spec['per_task'][task]
        return [{'role': 'system', 'content': p['receiver_system']}, {'role': 'user', 'content': p['p0']}]
    evidence = format_evidence([(p['title'], p['sentences']) for p in sorted(view['paragraphs'], key=lambda p:p['position'])])
    return c2c_p1_candidate_messages(spec, task, view['q'], evidence)


def missing_payload(source, destination):
    """发送缺失原文及排序元数据，不重复发送接收端已有内容。"""
    positions = {p['position'] for p in destination['paragraphs']}
    return {'q': source['q'] if destination['q'] is None else None,
            'paragraphs': [copy.deepcopy(p) for p in source['paragraphs'] if p['position'] not in positions]}


def merge_received(local, payload):
    """接收端仅使用本地视图和实际收到的载荷重建输入。"""
    if set(payload) != {'q', 'paragraphs'}:
        raise ValueError('补传包含未知字段')
    value = copy.deepcopy(local)
    if payload['q'] is not None:
        if value['q'] is not None and value['q'] != payload['q']:
            raise ValueError('补传题面冲突')
        value['q'] = payload['q']
    entries = {p['position']: p for p in value['paragraphs']}
    for p in payload['paragraphs']:
        if set(p) != {'position', 'title', 'sentences'} or p['position'] in entries:
            raise ValueError('补传段落字段非法或重复')
        entries[p['position']] = p
    value['paragraphs'] = [entries[i] for i in sorted(entries)]
    return value


def raw_text_bytes(payload):
    """原文按UTF-8计数，JSON结构、转义和位置字段归元数据。"""
    texts = ([payload['q']] if payload['q'] is not None else [])
    texts += [text for p in payload['paragraphs'] for text in [p['title'], *p['sentences']]]
    return sum(len(text.encode('utf-8')) for text in texts)


def synthetic_row(task, words=1):
    """工程预热使用自造题；Hotpot十段结构覆盖P2分配。"""
    row = {'task':task,'task_id':'synthetic/'+task,'evidence':'','context':[], 'evidence_order':[],
           'question':{'gsm8k':'A basket has 4 apples. Add 3. How many apples?',
             'hotpotqa':'Which city is named in paragraph A?',
             'humaneval':'def add_two(a, b):\n    """Return the sum of a and b."""\n'}[task]}
    if task=='hotpotqa':
        context = [(chr(65+i),['Paris.' if i==0 else 'Synthetic note.'+(' apple'*words)]) for i in range(10)]
        order,s,r = split_indices(row['task_id'],context,['A','B'])
        row.update(context=context,evidence_order=order,sender_indices=s,receiver_indices=r,common_7345=True,
                   evidence=format_evidence([context[i] for i in order]))
    return row
