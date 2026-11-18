import shutil
import subprocess
import sys
import time
from project_paths import official_repo

OFFICIAL_COMMIT = "bdb932aa63637959074a9a6fd59992a4d0d9ad22"


def cuda_memory():
    """记录 PyTorch 张量峰值及设备空闲量，二者的含义不同。"""
    import torch
    free, total = torch.cuda.mem_get_info()
    return {"peak_allocated_GiB": torch.cuda.max_memory_allocated() / 2**30,
            "peak_reserved_GiB": torch.cuda.max_memory_reserved() / 2**30,
            "device_free_GiB": free / 2**30, "device_total_GiB": total / 2**30}


def preflight(root):
    """在加载大模型前核对版本、实际 CUDA 运算、BF16 和工作盘。"""
    import torch
    import transformers
    commit = subprocess.check_output(["git", "-C", str(official_repo(root)), "rev-parse", "HEAD"], text=True).strip()
    status = subprocess.check_output(["git", "-C", str(official_repo(root)), "status", "--porcelain"], text=True)
    if commit != OFFICIAL_COMMIT or status.strip():
        raise RuntimeError("官方代码提交不匹配或有未提交改动，先核对差异")
    if torch.__version__.split("+")[0] != "2.6.0" or transformers.__version__ != "4.52.4":
        raise RuntimeError(f"依赖版本不匹配: torch={torch.__version__}, transformers={transformers.__version__}")
    if sys.version_info[:2] != (3, 10) or torch.version.cuda != "12.4":
        raise RuntimeError(f"本轮环境要求 Python 3.10 / torch cu124，实际为 {sys.version_info[:2]} / {torch.version.cuda}")
    if not torch.cuda.is_available():
        raise RuntimeError("当前 Python 入口的 CUDA 不可用，尚未加载模型")
    if not torch.cuda.is_bf16_supported():
        raise RuntimeError("当前设备不支持本轮要求的 BF16；不自动更换精度")
    started = time.perf_counter()
    probe = torch.arange(16, device="cuda", dtype=torch.bfloat16).reshape(4, 4)
    assert torch.isfinite(probe @ probe).all(), "BF16 矩阵运算非有限"
    torch.cuda.synchronize()
    del probe
    disk = shutil.disk_usage(root)
    return {"checked_unix": time.time(), "python": sys.version,
            "torch": torch.__version__, "transformers": transformers.__version__,
            "torch_cuda_runtime": torch.version.cuda, "official_commit": commit,
            "gpu_name": torch.cuda.get_device_name(0), "bf16_matmul": "passed",
            "probe_seconds": time.perf_counter() - started,
            "disk_free_GiB": disk.free / 2**30, "cuda": cuda_memory()}
