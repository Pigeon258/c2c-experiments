def task_view(question, evidence=''):
    """保留题目、函数前缀及证据的原始空白，不自动修剪或重排。"""
    if not isinstance(question, str) or not isinstance(evidence, str):
        raise TypeError('题目与证据须为字符串')
    text='<TASK>\n'+question+'\n</TASK>'
    return text+('\n<EVIDENCE>\n'+evidence+'\n</EVIDENCE>' if evidence else '')


def c2c_p1_candidate_messages(spec, task, question, evidence=''):
    """两端共享接收端任务提示词及同一输入。"""
    if task not in spec['per_task']:
        raise ValueError('未知任务')
    if task!='hotpotqa' and evidence:
        raise ValueError('数学及代码没有额外证据')
    template=spec['per_task'][task]
    return [{'role':'system','content':template['receiver_system']},
            {'role':'user','content':task_view(question,evidence)+'\n\n'+template['receiver_task']}]
