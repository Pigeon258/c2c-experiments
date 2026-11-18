"""将实际训练参数与已冻结的训练/验证方案绑定。"""

import hashlib
import json


def canonical_digest(config):
    """忽略JSON排版，对实际参数内容计算固定摘要。"""
    text = json.dumps(config, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()


def frozen_training_contract(root, config, direction):
    """诊断和正式入口均先核对方案；诊断缩短运行发生在核对之后。"""
    path = root / "experiments/configs/c2c_train_validation_frozen.json"
    frozen = json.loads(path.read_text(encoding="utf-8"))
    if canonical_digest(config) != frozen["configurations"][direction]["canonical_sha256"]:
        raise ValueError("实际配置与已冻结训练/验证方案不一致，须先修订方案及受影响验收")
    return frozen
