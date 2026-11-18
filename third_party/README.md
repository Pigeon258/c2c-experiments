# 第三方来源

| 项目 | 使用内容 | 来源 |
|---|---|---|
| C2C | 模型封装、融合器、官方训练和数据处理函数。在本地检出固定版本后由实验入口加载。 | [THU-NICS/C2C，bdb932a](https://github.com/thu-nics/C2C/tree/bdb932aa63637959074a9a6fd59992a4d0d9ad22) / [上游仓库附带的许可证](C2C-LICENSE) |
| HumanEval | 代码评分沿用原题前缀、测试及隔离执行辅助函数。仓库附上实际使用的辅助函数。 | [OpenAI HumanEval](https://github.com/openai/human-eval) / [辅助函数](humaneval/execution.py) / [MIT 许可证](humaneval/LICENSE) |

基础模型和公开数据集按固定版本从各自来源获取。版本、测试文件地址和 SHA-256 见[训练配置索引](../experiments/configs/c2c_train_validation_frozen.json)和[评测配置](../experiments/configs/evaluation.json)。
