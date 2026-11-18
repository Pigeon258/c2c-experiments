"""在 Linux Bubblewrap 中执行 HumanEval 原样补全。"""
import argparse
import json
import os
import subprocess
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'src'))
import hashlib


def record_sha(record):
    return hashlib.sha256(json.dumps(record, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def strict_rows(path):
    """保留损坏尾行原样，拒绝把截断记录当成未开始题。"""
    p = Path(path)
    data = p.read_bytes() if p.exists() else b''
    if data and not data.endswith(b'\n'):
        raise ValueError('JSONL尾行未完整提交: '+str(p))
    return [json.loads(x) for x in data.splitlines()]


def command(python_root, code):
    """隔离网络和项目路径，仅挂载系统运行库及独立Python标准库。"""
    args = ['bwrap', '--unshare-all', '--die-with-parent', '--new-session', '--cap-drop', 'ALL',
            '--clearenv', '--ro-bind', '/usr', '/usr', '--ro-bind', '/lib', '/lib',
            '--ro-bind', str(python_root.resolve()), '/opt/python', '--tmpfs', '/tmp',
            '--tmpfs', '/run', '--tmpfs', '/work', '--proc', '/proc', '--dev', '/dev',
            '--chdir', '/work', '--setenv', 'PATH', '/opt/python/bin:/usr/bin',
            '--setenv', 'HOME', '/work', '--setenv', 'LD_LIBRARY_PATH', '/opt/python/lib']
    if Path('/lib64').exists():
        args += ['--ro-bind', '/lib64', '/lib64']
    return args + ['--', '/opt/python/bin/python3.11', '-I', '-S', '-c', code]


def evaluate(program, upstream, python_root):
    """模型执行错误计零，隔离基础设施错误保持None，不冒充失败答案。"""
    wrapper = '''import json,resource,sys
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
resource.setrlimit(resource.RLIMIT_CPU,(4,4))
resource.setrlimit(resource.RLIMIT_FSIZE,(16*1024**2,16*1024**2))
resource.setrlimit(resource.RLIMIT_NOFILE,(64,64))
p=json.load(sys.stdin)
u={}
exec(p['upstream'],u)
u['reliability_guard'](maximum_memory_bytes=2*1024**3)
try:
 with u['swallow_io']():
  with u['time_limit'](3.0):
   exec(p['program'],{})
 r={'pass@1':1.0,'execution_status':'passed'}
except u['TimeoutException']:
 r={'pass@1':0.0,'execution_status':'timeout'}
except BaseException as e:
 r={'pass@1':0.0,'execution_status':'failed','exception_type':type(e).__name__}
print(json.dumps(r))
'''
    try:
        result = subprocess.run(command(python_root, wrapper), input=json.dumps({'program': program, 'upstream': upstream}),
                                capture_output=True, text=True, timeout=8)
    except subprocess.TimeoutExpired:
        return {'pass@1': 0.0, 'execution_status': 'timeout', 'reason': 'sandbox_process_timeout'}
    if result.returncode:
        return {'pass@1': None, 'execution_status': 'infrastructure_failure', 'returncode': result.returncode,
                'stderr': result.stderr[-2000:]}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {'pass@1': None, 'execution_status': 'infrastructure_failure', 'reason': 'invalid_json'}


def main(args):
    upstream = args.upstream.read_text(encoding='utf-8')
    probe = subprocess.run(command(args.python_root, '''import os,socket,json,sys
assert not os.path.exists('/etc/passwd')
s=socket.socket();s.settimeout(0.2)
try: s.connect(('1.1.1.1',443))
except OSError: pass
else: raise RuntimeError('network accessible')
print(json.dumps({'python':sys.version,'network_isolated':True,'project_paths_hidden':True}))
'''), capture_output=True, text=True, timeout=10)
    if probe.returncode:
        raise RuntimeError('隔离预检失败: '+probe.stderr)
    checks = [evaluate(p, upstream, args.python_root) for p in ('assert 2+2==4', 'assert False', 'while True: pass')]
    if [r['execution_status'] for r in checks] != ['passed', 'failed', 'timeout']:
        raise RuntimeError('执行器边界验收未通过: '+str(checks))
    samples = {r['task_id']: r for r in map(json.loads, (args.batch/'samples.jsonl').read_text(encoding='utf-8').splitlines()) if r['task'] == 'humaneval'}
    config = json.loads((args.batch/'config.json').read_text(encoding='utf-8'))
    for direction in config['directions']:
        file = args.batch/direction/'predictions.jsonl'
        if not file.exists():
            continue
        out = args.batch/direction/'humaneval_execution'
        out.mkdir(exist_ok=True)
        previous = strict_rows(out/'samples.jsonl')
        existing = {r['task_id']: r for r in previous}
        if len(existing) != len(previous):
            raise ValueError('重复代码评分')
        if not json.loads(probe.stdout)['python'].startswith('3.11.17 '):
            raise ValueError('正式代码评分必须使用共同Python3.11.17')
        metadata = {'scope': 'HumanEval CPU 隔离评分',
            'runtime': json.loads(probe.stdout), 'checks': checks,
            'limits': {'wall_s': 3, 'cpu_s': 4, 'memory_bytes': 2*1024**3, 'outer_wall_s': 8},
            't2t_python_declared': '3.11.17', 'version_note': '以runtime实际版本为准；与T2T补丁版本差异显式记录'}
        (out/'environment.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
        with (out/'samples.jsonl').open('a', encoding='utf-8') as stream:
            for row in map(json.loads, file.read_text(encoding='utf-8').splitlines()):
                if row['task'] != 'humaneval':
                    continue
                if row['task_id'] in existing:
                    old = existing[row['task_id']]
                    if old.get('prediction_sha256') != record_sha(row):
                        raise ValueError('已有评分与预测摘要不符')
                    continue
                problem = samples[row['task_id']]
                if row['status'] != 'generated':
                    result = {'pass@1': 0.0, 'execution_status': 'generation_failure'}
                else:
                    program = problem['question']+row['output']+'\n'+problem['test']+'\ncheck('+problem['entry_point']+')'
                    result = evaluate(program, upstream, args.python_root)
                result['task_id'] = row['task_id']
                result['prediction_sha256'] = record_sha(row)
                if result['pass@1'] is None:
                    (out/'infrastructure_failure.json').write_text(json.dumps(result), encoding='utf-8')
                    raise RuntimeError(str(result))
                stream.write(json.dumps(result)+'\n')
                stream.flush()
                os.fsync(stream.fileno())
        print(direction, 'HumanEval评分完成', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch', type=Path, required=True)
    parser.add_argument('--python-root', type=Path, required=True)
    parser.add_argument('--upstream', type=Path, required=True)
    main(parser.parse_args())
