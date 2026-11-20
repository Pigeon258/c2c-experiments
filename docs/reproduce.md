# 复现指南

以下命令从仓库根目录运行。查看已发布成绩只需要 Python 标准库。使用发布的融合器生成回答，需要 Linux、支持 BF16 的 NVIDIA GPU 和该方向的两个 Qwen3 基础模型。正式实验使用 RTX 3090。

## 准备推理环境

```sh
git clone git@github.com:thu-nics/C2C.git third_party/C2C
git -C third_party/C2C checkout --detach bdb932aa63637959074a9a6fd59992a4d0d9ad22
python3.11 -m venv .venv-eval
. .venv-eval/bin/activate
python -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128
python -m pip install -r requirements/eval.txt
python scripts/prepare_assets.py models
python scripts/prepare_assets.py tests
```

推理环境使用 Python 3.11.17 和 Transformers 4.57.6。两个准备命令分别下载三个固定版本的 Qwen3 模型和三个测试集，各方向可共用。默认存放在 `models/` 和 `data/`。如需使用其他磁盘，在准备前设置 `C2C_MODELS` 和 `C2C_DATA`。

## 下载权重

按下表选择一个方向。下方命令以 M1 为例，改用其他方向时只需修改开头两行。

| 方向 | 发送端 → 接收端 | `direction` | `step` |
|---|---|---|---|
| M1 | Qwen3-0.6B → Qwen3-1.7B | M1 | 1900 |
| M2 | Qwen3-0.6B → Qwen3-4B | M2 | 1929 |
| M3 | Qwen3-4B → Qwen3-0.6B | M3 | 1900 |

```sh
direction=M1
step=1900
run_root="${C2C_RUNS:-runs}"
release="https://github.com/Pigeon258/c2c-experiments/releases/download/formal-projectors-v1"
asset="c2c-${direction}-step${step}.tar.gz"
mkdir -p "$run_root"
curl --fail --location --retry 3 --continue-at - --output "$run_root/$asset" "$release/$asset"
tar -xzf "$run_root/$asset" -C "$run_root"
checkpoint="$run_root/$direction/checkpoint-$step"
```

包内包含方向配置 `config.json`，保存点目录中有 `complete.json`、28 个逐层权重 `projector_*.pt` 和 28 个结构配置 `projector_*.json`。也可以从 [Release 页面](https://github.com/Pigeon258/c2c-experiments/releases/tag/formal-projectors-v1)手动下载。

## 生成回答

在同一终端运行。先用 P1 协议生成前两道 HumanEval 的回答，再按需运行完整 164 题。两次运行使用不同的输出目录。

```sh
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2
python scripts/evaluate.py --direction "$direction" --protocol P1 --task humaneval \
  --checkpoint "$checkpoint" --limit 2 --output "$run_root/$direction-P1-code-2"
python scripts/evaluate.py --direction "$direction" --protocol P1 --task humaneval \
  --checkpoint "$checkpoint" --output "$run_root/$direction-P1-code"
```

其他任务使用 `gsm8k` 或 `hotpotqa`。P1 / P4 支持三项任务，P2 / P3 只用于问答。该入口沿用原实验的模型前向、协议补传、三次合成预热和逐项计时，保留每题的回答、停止原因和 token 数。已发布的耗时取自原始运行，包含后台计量快照开销。新环境所得耗时应单独记录。

## 评分与比较

数学、问答在生成时评分。HumanEval 另用 Linux Bubblewrap（`bwrap`）与独立安装的 Python 3.11.17 运行。将 `HE_PYTHON` 设为该 Python 的安装前缀，其中应包含 `bin/python3.11` 和独立标准库 `lib/python3.11/`。评分脚本先检查网络隔离、正确样例、错误样例和超时样例。

```sh
python scripts/c2c/score_code.py --batch "$run_root/$direction-P1-code" --python-root "$HE_PYTHON" --upstream third_party/humaneval/execution.py
python scripts/summarize.py --batch "$run_root/$direction-P1-code"
```

如只想查看已发布的实验，可以直接运行：

```sh
python scripts/summarize.py --task humaneval
python scripts/summarize.py --task hotpotqa --common
python -m unittest discover -s tests -v
```

## 可选：自行训练融合器

训练使用同一上游提交，环境为 Python 3.10、PyTorch 2.6.0/cu124、Transformers 4.52.4。下面以 M1 为例，训练产物写入独立目录 `train-M1`。

```sh
python3.10 -m venv .venv-train
. .venv-train/bin/activate
python -m pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cu124
python -m pip install -r requirements/train.txt
python scripts/prepare_assets.py models
python scripts/prepare_assets.py tests
python src/c2c/c2c_prepare_formal_data.py --root . --run-id prepare-openhermes
python scripts/c2c/c2c_clean_formal_split.py --root .
python scripts/c2c/c2c_train.py preflight --root . --config experiments/configs/M1.json --run-id verify-M1
python scripts/c2c/c2c_train.py formal --root . --config experiments/configs/M1.json --run-id train-M1
```

数据准备依次生成 OpenHermes 缓存、排除测试重合的训练索引和独立验证索引。清洗步骤在同一数据盘内硬链接已过滤的缓存。训练入口核对模型文件、数据划分和上游版本。训练 M2 / M3 时替换配置文件和运行名称。每次使用新的运行名称。

训练完成后，在该次运行的 `result.json` 中查看 `best_step` 和 `best_checkpoint`。切回推理环境，把上文的 `direction` 和 `checkpoint` 设为训练方向和选中的保存点，再执行“生成回答”。
