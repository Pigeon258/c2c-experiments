"""代码依赖和本地大文件的位置。"""
import os
from pathlib import Path


def official_repo(root):
    return root / 'third_party' / 'C2C'


def asset_dir(root, kind):
    """通过 C2C_MODELS、C2C_DATA、C2C_RUNS 指定存储位置。"""
    return Path(os.environ.get('C2C_' + kind.upper(), root / kind)).expanduser().resolve()
