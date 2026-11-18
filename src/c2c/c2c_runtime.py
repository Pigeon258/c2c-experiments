def validate_resume_contract(stored, expected):
    """只接续同一版本、相同训练条件的保存点。"""
    if stored != expected:
        raise ValueError("保存点的配置、源码或数据与当前训练不一致")
