# 复现指南

以下命令从仓库根目录运行。已发布的全部逐题分数可直接用标准库汇总。重新生成回答需要 Linux、支持 BF16 的 NVIDIA GPU、两个基础模型和对应方向的融合器。正式实验使用 RTX 3090；权重文件单独存放，可按下文步骤重新训练。

## 1. 固定上游代码与环境

```sh
git clone git@github.com:thu-nics/C2C.git third_party/C2C
git -C third_party/C2C checkout --detach bdb932aa63637959074a9a6fd59992a4d0d9ad22
```

训练和推理使用不同环境。训练用 Python 3.10、PyTorch 2.6.0/cu124、Transformers 4.52.4。推理和代码评分用 Python 3.11.17，推理用 PyTorch 2.8.0/cu128、Transformers 4.57.6。根据所做的步骤选用对应环境。

```sh
python3.10 -m venv .venv-train
. .venv-train/bin/activate
python -m pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cu124
python -m pip install -r requirements/train.txt
```

默认使用仓库根目录的 `models/`、`data/` 和 `runs/`。也可以在准备数据前分别设置环境变量 `C2C_MODELS`、`C2C_DATA`、`C2C_RUNS`，让训练与推理使用同一组路径。

## 2. 准备数据并训练

```sh
python scripts/prepare_assets.py models
python scripts/prepare_assets.py tests
python src/c2c/c2c_prepare_formal_data.py --root . --run-id prepare-openhermes
python scripts/c2c/c2c_clean_formal_split.py --root .
python scripts/c2c/c2c_train.py preflight --root . --config experiments/configs/M1.json --run-id verify-M1
python scripts/c2c/c2c_train.py formal --root . --config experiments/configs/M1.json --run-id M1
```

数据准备依次生成 OpenHermes 缓存、排除测试重合的训练索引和独立验证索引。清洗步骤在同一数据盘内硬链接已过滤的缓存。训练入口核对模型文件摘要、数据划分摘要和上游版本。训练 M2、M3 时替换配置和 run-id。各次调用使用独立的 run-id。

每次训练的 `result.json` 记录 `best_step` 和 `best_checkpoint`。本次发布的 M1 最佳点是 `checkpoint-1900`。使用自己训练的结果时，按该次验证损失选择保存点。若已有同格式训练产物，保留运行目录中的 `config.json` 以及保存点中的 `complete.json` 和 28 个 `projector_*.pt` 文件，可直接进入下一步。

## 3. 生成回答

```sh
python3.11 -m venv .venv-eval
. .venv-eval/bin/activate
python -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128
python -m pip install -r requirements/eval.txt
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2
python scripts/evaluate.py --direction M1 --protocol P1 --task humaneval --checkpoint runs/M1/checkpoint-1900 --output runs/M1-P1-code
```

示例一次生成 164 道 HumanEval 回答。若自定义了 `C2C_RUNS`，请把命令中两处显式路径换为实际路径。首次测试可在命令末尾加 `--limit 2` 并使用另一个输出目录。其他任务使用 `gsm8k`、`hotpotqa`。P1、P4 支持三项任务，P2、P3 只用于问答。

该入口复用原实验的模型前向、协议补传、三次合成预热和逐项计时，保留每题的回答、停止原因和 token 数。发布的耗时取自原始运行，其中包含后台计量快照的开销。此处的独立入口适用于重新测量，新环境所得耗时应单独记录。

## 4. 评分与比较

数学、问答在生成时评分。HumanEval 另用 Linux Bubblewrap（`bwrap`）与独立安装的 Python 3.11.17 运行。设置 `HE_PYTHON` 为该 Python 的安装前缀，其中应包含 `bin/python3.11` 和独立标准库 `lib/python3.11/`。评分脚本挂载此前缀，并先检查网络隔离、正确样例、错误样例和超时样例。

```sh
python scripts/c2c/score_code.py --batch runs/M1-P1-code --python-root "$HE_PYTHON" --upstream third_party/humaneval/execution.py
python scripts/summarize.py --batch runs/M1-P1-code
```

如只想查看已发布的实验，可以直接运行：

```sh
python scripts/summarize.py --task humaneval
python scripts/summarize.py --task hotpotqa --common
python -m unittest discover -s tests -v
```
