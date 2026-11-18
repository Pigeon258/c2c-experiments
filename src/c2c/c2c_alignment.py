"""论文§3.3.3/A.1.1的末层一一对齐，保留未配对接收层的原缓存。"""

CONTRACT = "paper_terminal_one_to_one_v1"


def terminal_pairs(target_layers, source_layers):
    """从双方末层向前配对，配对数取较小层数。"""
    if min(target_layers, source_layers) <= 0:
        raise ValueError("两端层数须为正数")
    count = min(target_layers, source_layers)
    return [(target_layers - count + i, source_layers - count + i)
            for i in range(count)]


def apply_paper_alignment(model, contract):
    """复用官方融合器，修正短发送端被clamp到第0层的映射并移除闲置模块。"""
    if contract != CONTRACT or model.base_model_idx != 0 or len(model.model_list) != 2:
        raise ValueError("当前论文对齐适配要求固定合同及双模型base=0")
    target_layers = model.model_list[0].config.num_hidden_layers
    source_layers = model.model_list[1].config.num_hidden_layers
    pairs = terminal_pairs(target_layers, source_layers)
    # 官方按接收层创建融合器；只保留有论文配对的模块，避免把闲置参数计入训练。
    if len(model.projector_list) != target_layers:
        raise ValueError("须在官方模型刚构造完成、加载权重前应用论文对齐")
    projectors = [model.projector_list[target] for target, _ in pairs]
    model.projector_list = type(model.projector_list)(projectors)
    model.projector_dict = {0: {1: {
        target: [(source, index)] for index, (target, source) in enumerate(pairs)
    }}}
    return {"contract": contract, "target_layers": target_layers,
            "source_layers": source_layers, "pairs": pairs,
            "projectors": len(projectors),
            "unfused_target_layers": list(range(target_layers - len(pairs)))}
