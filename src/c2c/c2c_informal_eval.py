import gzip
import hashlib
import json
import random
import re
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write_json(path, value):
    """以临时文件原子发布小型结果，保留中文。"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)


def digest(path, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line]


def gsm_score(prediction, reference):
    """与T2T/原作者一致：首个正则匹配去逗号，按字符串判等。"""
    pattern = r'#### (\-?[0-9\.\,]+)'
    matches = re.search(pattern, prediction)
    gold = re.search(pattern, reference)
    if not gold:
        raise ValueError('GSM8K参考答案格式错误')
    extracted = matches.group(1).strip().replace(',', '') if matches else None
    return {'accuracy': float(extracted == gold.group(1).strip().replace(',', '')),
            'parse_failed': extracted is None, 'extracted': extracted}


def format_evidence(pairs):
    """按发布模板§1.3保留顺序，以[标题]、正文、段间空行组装证据。"""
    return '\n\n'.join('[' + title + ']\n' + ''.join(sentences) for title, sentences in pairs)


def evidence_order(sample_id, count):
    """复现T2T的按题目ID派生随机源，不消耗抽样随机流。"""
    seed = int(hashlib.sha256(f'42:{sample_id}:full_order'.encode()).hexdigest(), 16)
    order = list(range(count))
    random.Random(seed).shuffle(order)
    return order


def selected_samples(config, data):
    """只按源索引随机抽样；答案保留用于评分，输入组装不读取答案。"""
    import pyarrow.parquet as pq
    selected = []
    for task, settings in config['tasks'].items():
        path = data / settings['filename']
        if digest(path) != settings['sha256']:
            raise ValueError('测试来源摘要不符: ' + task)
        if task == 'hotpotqa':
            source = pq.read_table(path).to_pylist()
        elif task == 'humaneval':
            with gzip.open(path, 'rt', encoding='utf-8') as stream:
                source = [json.loads(line) for line in stream]
        else:
            source = jsonl(path)
        if config.get('selection_mode') == 'full_source_order':
            if settings['samples'] != len(source):
                raise ValueError('正式全量分母与源文件不一致: '+task)
            indices = range(len(source))
        else:
            indices = random.Random(config['seed']).sample(range(len(source)), settings['samples'])
        for index in indices:
            item = source[index]
            row = {'task': task, 'source_index': index, 'evidence': ''}
            if task == 'gsm8k':
                row.update(task_id=f'gsm8k/main/test/{index:04d}', question=item['question'], reference=item['answer'])
            elif task == 'hotpotqa':
                context = item['context']
                pairs = list(zip(context['title'], context['sentences'])) if isinstance(context, dict) else context
                sid = item.get('_id', item.get('id'))
                if not sid:
                    raise ValueError('Hotpot缺少原题目ID')
                order = evidence_order(sid, len(pairs))
                facts = item['supporting_facts']
                supports = set(facts['title'] if isinstance(facts, dict) else [f[0] for f in facts])
                common = len(pairs) == 10 and len({p[0] for p in pairs}) == 10 and len(supports) == 2 and sum(p[0] in supports for p in pairs) == 2
                from c2c.c2c_protocols import split_indices
                _, sender, receiver = split_indices(sid, pairs, supports)
                row.update(sender_indices=sender, receiver_indices=receiver)
                row.update(task_id=sid, question=item['question'], reference=item['answer'],
                           evidence=format_evidence([pairs[i] for i in order]), evidence_order=order,
                           common_7345=common, context=pairs)
            else:
                row.update(task_id=item['task_id'], question=item['prompt'],
                           reference=None, entry_point=item['entry_point'], test=item['test'])
            selected.append(row)
    return selected


def encode(tokenizer, messages):
    """两端共享前缀，末token走官方本地Decode段，与已有诊断入口一致。"""
    import torch
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
    inputs = tokenizer(text, return_tensors='pt', add_special_tokens=False).to('cuda')
    length = inputs['input_ids'].shape[1]
    sections = [torch.tensor([1, 0], device='cuda').repeat(length - 1, 1).unsqueeze(0),
                torch.tensor([[[-1, 0]]], device='cuda')]
    return inputs, sections, text
