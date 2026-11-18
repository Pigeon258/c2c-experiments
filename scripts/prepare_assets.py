"""下载固定版本的模型快照和正式评测使用的三个测试文件。"""
import argparse
import sys
from pathlib import Path
from urllib.request import urlopen
from shutil import copyfileobj

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from project_paths import asset_dir
from c2c.c2c_informal_eval import digest, read_json


def fetch_tests():
    target = asset_dir(ROOT, 'data') / 'test_sources'
    target.mkdir(parents=True, exist_ok=True)
    for item in read_json(ROOT / 'experiments/configs/evaluation.json')['tasks'].values():
        dest = target / item['filename']
        if not dest.exists():
            temp = dest.with_suffix(dest.suffix + '.part')
            with urlopen(item['url'], timeout=120) as response, temp.open('wb') as f:
                copyfileobj(response, f)
            if digest(temp) != item['sha256']:
                raise ValueError(f'下载文件摘要不符：{dest.name}')
            temp.replace(dest)
        if digest(dest) != item['sha256']:
            raise ValueError(f'已有文件摘要不符：{dest.name}')
        print(dest.name, 'OK')


def fetch_models():
    from huggingface_hub import snapshot_download
    lock = read_json(ROOT / 'experiments/configs/c2c_train_validation_frozen.json')
    for name, source in lock['models'].items():
        snapshot_download(source['repo_id'], revision=source['revision'],
                          local_dir=asset_dir(ROOT, 'models') / name,
                          allow_patterns=['*.json', '*.safetensors', '*.txt'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('asset', choices=['models', 'tests'])
    args = parser.parse_args()
    (fetch_models if args.asset == 'models' else fetch_tests)()
