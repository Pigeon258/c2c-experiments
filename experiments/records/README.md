# 实验记录

| 文件 | 每行或每项表示什么 |
|---|---|
| [scores.csv.gz](scores.csv.gz) | 每次正式生成一行，97,578 行。联合键为 protocol、direction、task、task_id。包含状态、停止原因、输入输出 token 数、实际任务分数、该题记录的 elapsed_seconds。未用于该任务的指标为空。 |
| [humaneval.csv](humaneval.csv) | 每次代码执行一行，共 984 行。passed 为原始通过标记，exception_type 为实际异常类型，passed_after_cleanup 为 P1 补充诊断（空值表示未做）。 |
| [humaneval-outputs.jsonl](humaneval-outputs.jsonl) | 每方向、每道代码题一个原始输出，共 492 行。P1 和 P4 共享相同文本，两个协议的评分各自保留。 |
| [short-comparison.csv](short-comparison.csv) | M3 受控短测的 240 次新生成和 20 份既有回答，含固定题号、条件、评分和复用标记。 |
| [training.json](training.json) | 各方向训练步数、训练样本数、验证轮数以及最佳点和最终点的损失。 |

`common_7345` 标记问答题是否属于 P2 可用的共同子集。GSM8K 使用 accuracy，HotpotQA 使用 em 和 f1，HumanEval 使用 pass@1，均以 0–1 记录。仓库首页以百分数展示。耗时的阶段划分、样本范围和聚合口径见[正式报告示例](../../reports/formal/P1-details.md)。
