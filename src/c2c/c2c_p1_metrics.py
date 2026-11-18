import re
import string
from collections import Counter


def hotpot_normalize(text):
    """复用官方 HotpotQA 的小写、标点、冠词与空白处理顺序。"""
    text=''.join(c for c in text.lower() if c not in string.punctuation)
    return ' '.join(re.sub(r'\b(a|an|the)\b',' ',text).split())


def hotpot_score(prediction,reference):
    """Answer EM/F1；yes/no/noanswer 不匹配时 F1 为零。"""
    p,g=hotpot_normalize(prediction),hotpot_normalize(reference)
    if (p in ['yes','no','noanswer'] or g in ['yes','no','noanswer']) and p!=g:
        f1=0.
    else:
        same=sum((Counter(p.split())&Counter(g.split())).values())
        f1=2*same/(len(p.split())+len(g.split())) if same else 0.
    return {'em':float(p==g),'f1':f1}
