# C2C 复现与评测

本仓库记录 Cache-to-Cache（C2C）在三个 Qwen3 模型组合上的训练和评测。发送端先读取输入，将 KV 缓存传给接收端。接收端用训练好的融合器转换并合并缓存，再生成回答。实验比较了数学、问答和代码生成的回答质量，以及双方初始信息不同时的通信量和推理耗时。模型实现基于 [THU-NICS/C2C](https://github.com/thu-nics/C2C/tree/bdb932aa63637959074a9a6fd59992a4d0d9ad22)，方法见 [Cache-to-Cache 原论文](https://arxiv.org/abs/2510.03215)。

## 主要结果

P1 条件下，两端都拿到完整输入。表中为完整测试集上的百分数。每个方向分别训练融合器，按 OpenHermes 验证损失选定一套权重，供三个任务共同使用。

| 发送端 → 接收端 | GSM8K 准确率 | HotpotQA EM / F1 | HumanEval pass@1 |
|---|---:|---:|---:|
| M1　0.6B → 1.7B | 26.91 | 10.82 / 24.07 | 43.29 |
| M2　0.6B → 4B | 69.98 | 9.16 / 27.60 | 58.54 |
| M3　4B → 0.6B | 7.51 | 0.49 / 13.37 | 25.61 |

全部评测覆盖三个模型方向、24 个适用条件，共 97,578 次生成与评分。在同一批 164 道代码题上，M1、M2、M3 分别通过 71、96、42 道。[结果与通信成本](reports/results.md) / [HumanEval 逐题比较与失败样例](reports/humaneval.md)

## 正式测试权重

每个下载包包含一个方向的 28 层融合器权重和对应配置。正式测试中，同一方向的各项任务和协议共用这套权重。

| 方向 | 发送端 → 接收端 | 保存点 | 下载 |
|---|---|---|---|
| M1 | Qwen3-0.6B → Qwen3-1.7B | `checkpoint-1900` | [M1 权重包](https://github.com/Pigeon258/c2c-experiments/releases/download/formal-projectors-v1/c2c-M1-step1900.tar.gz) |
| M2 | Qwen3-0.6B → Qwen3-4B | `checkpoint-1929` | [M2 权重包](https://github.com/Pigeon258/c2c-experiments/releases/download/formal-projectors-v1/c2c-M2-step1929.tar.gz) |
| M3 | Qwen3-4B → Qwen3-0.6B | `checkpoint-1900` | [M3 权重包](https://github.com/Pigeon258/c2c-experiments/releases/download/formal-projectors-v1/c2c-M3-step1900.tar.gz) |

选一个方向，解压到 `runs/`。准备好基础模型和测试集后即可直接评测。[下载与推理示例](docs/reproduce.md#下载权重)

## 快速查看

从仓库根目录运行以下命令。查看已发布的成绩只需要 Python 3.10 或以上版本，无需模型或 GPU。

```sh
python scripts/summarize.py --protocol P1
python scripts/summarize.py --task humaneval
python -m unittest discover -s tests
```

| 想了解什么 | 从这里开始 |
|---|---|
| 各协议的成绩、分母、置信区间和耗时 | [P1](reports/formal/P1.md) / [P2](reports/formal/P2.md) / [P3](reports/formal/P3.md) / [P4](reports/formal/P4.md) |
| 格式对评分有多大影响？换成作者权重会怎样？ | [格式与重复诊断](reports/format-diagnostics.md) / [M3 权重与提示词短测](reports/short-comparison.md) |
| 融合器如何训练和选权？P1–P4 有何区别？ | [实验设计](docs/method.md) / [训练记录](experiments/records/training.json) |
| 怎样重新训练、生成、评分？ | [环境、数据与运行命令](docs/reproduce.md) / [实际配置](experiments/configs/) |
| 怎样和另一种方法对齐到同一道题？ | [逐题数据字段](experiments/records/README.md) / [HumanEval 执行结果 CSV](experiments/records/humaneval.csv) |

源码按职责放在 `src/c2c/`，运行入口在 `scripts/`。基础模型和测试集由准备脚本下载。上游 C2C 的版本及许可证见 [第三方来源](third_party/README.md)。
