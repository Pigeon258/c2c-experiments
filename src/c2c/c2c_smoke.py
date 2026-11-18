import importlib.util
import sys
from project_paths import official_repo


def load_official(root):
    """直接加载固定提交中的官方训练函数，避免另写模型实现。"""
    repo = official_repo(root)
    sys.path.insert(0, str(repo))
    spec = importlib.util.spec_from_file_location("official_sft", repo / "script/train/SFT_train.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
