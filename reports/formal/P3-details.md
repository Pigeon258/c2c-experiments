# 完整指标与统计口径

- **批次**：`P3`。
- **对应正文**：[正式报告](<P3.md>)。
- **范围**：本协议、路径的完整分项与覆盖情况。

## A 配置与结果

| 组合 | 视图 | 计划N | 已评分n | 指标 | 均值 | 95% CI |
|---|---|---|---|---|---|---|
| M1/P3/hotpotqa/C2C | full | 7405 | 7405 | em | 0.108170 | [0.1012829169480081, 0.11532748143146522] |
| M1/P3/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.107828 | [0.10074880871341048, 0.11504424778761062] |
| M1/P3/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.240721 | [0.23335464308848075, 0.2482068002010702] |
| M1/P3/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.240365 | [0.23278845431436807, 0.2477856525871724] |
| M2/P3/hotpotqa/C2C | full | 7405 | 7405 | em | 0.091560 | [0.08507765023632681, 0.09804186360567184] |
| M2/P3/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.092035 | [0.085500340367597, 0.0987066031313819] |
| M2/P3/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.276049 | [0.26934856956447545, 0.28283269003987904] |
| M2/P3/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.276202 | [0.26924102875049, 0.2828945782066278] |
| M3/P3/hotpotqa/C2C | full | 7405 | 7405 | em | 0.004862 | [0.00337609723160027, 0.006482106684672519] |
| M3/P3/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.004901 | [0.0034036759700476512, 0.006535057862491491] |
| M3/P3/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.133725 | [0.1300072938726543, 0.1374455520450355] |
| M3/P3/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.133471 | [0.12973439221694455, 0.13720172646993634] |

| 组合 | 字段 | 已知n | N | 总tokens |
|---|---|---|---|---|
| M1/P3/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M1/P3/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M1/P3/hotpotqa/C2C | output_tokens | 7405 | 7405 | 156391 |
| M1/P3/hotpotqa/C2C | receiver_initial_prefill | 7405 | 7405 | 822006 |
| M1/P3/hotpotqa/C2C | receiver_visible | 7405 | 7405 | 822006 |
| M1/P3/hotpotqa/C2C | sender_visible | 7405 | 7405 | 11145864 |
| M2/P3/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M2/P3/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M2/P3/hotpotqa/C2C | output_tokens | 7405 | 7405 | 154491 |
| M2/P3/hotpotqa/C2C | receiver_initial_prefill | 7405 | 7405 | 822006 |
| M2/P3/hotpotqa/C2C | receiver_visible | 7405 | 7405 | 822006 |
| M2/P3/hotpotqa/C2C | sender_visible | 7405 | 7405 | 11145864 |
| M3/P3/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M3/P3/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M3/P3/hotpotqa/C2C | output_tokens | 7405 | 7405 | 274274 |
| M3/P3/hotpotqa/C2C | receiver_initial_prefill | 7405 | 7405 | 822006 |
| M3/P3/hotpotqa/C2C | receiver_visible | 7405 | 7405 | 822006 |
| M3/P3/hotpotqa/C2C | sender_visible | 7405 | 7405 | 11145864 |

## B 全部分项耗时

| 组合 | 阶段/计时口径 | 完整/部分 | n | N | 均值s | P50s | P95s |
|---|---|---|---|---|---|---|---|
| M1/P3/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.054542 | 0.055359 | 0.072593 |
| M1/P3/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.054514 | 0.055332 | 0.072568 |
| M1/P3/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.076047 | 0.074554 | 0.096147 |
| M1/P3/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.076056 | 0.074565 | 0.096154 |
| M1/P3/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.030203 | 0.029922 | 0.031404 |
| M1/P3/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.030184 | 0.029905 | 0.031386 |
| M1/P3/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.939378 | 0.920717 | 1.303762 |
| M1/P3/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.939354 | 0.920709 | 1.303747 |
| M1/P3/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 0.590877 | 0.488749 | 1.297917 |
| M1/P3/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 0.590852 | 0.488725 | 1.297884 |
| M1/P3/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.069910 | 0.068557 | 0.089585 |
| M1/P3/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.107614 | 0.108568 | 0.143393 |
| M1/P3/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.107588 | 0.108546 | 0.143363 |
| M1/P3/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.041892 | 0.037632 | 0.054577 |
| M1/P3/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.041847 | 0.037584 | 0.054528 |
| M1/P3/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.002763 | 0.002623 | 0.004054 |
| M1/P3/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000345 | 0.000327 | 0.000481 |
| M1/P3/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.061242 | 0.058572 | 0.097212 |
| M1/P3/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.141266 | 0.139918 | 0.192178 |
| M1/P3/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.273246 | 0.265933 | 0.381442 |
| M1/P3/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.067631 | 0.072448 | 0.116229 |
| M1/P3/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.022899 | 0.022225 | 0.030336 |
| M1/P3/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000068 | 0.000067 | 0.000086 |
| M1/P3/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7405 | 7405 | 0.000125 | 0.000121 | 0.000159 |
| M1/P3/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7405 | 7405 | 0.000207 | 0.000192 | 0.000361 |
| M1/P3/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7405 | 7405 | 0.000053 | 0.000052 | 0.000066 |
| M1/P3/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 1.598108 | 1.463112 | 2.454082 |
| M2/P3/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.054794 | 0.055949 | 0.073046 |
| M2/P3/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.054766 | 0.055921 | 0.073018 |
| M2/P3/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.076328 | 0.075654 | 0.097173 |
| M2/P3/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.076336 | 0.075661 | 0.097181 |
| M2/P3/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.038946 | 0.038709 | 0.040796 |
| M2/P3/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.038927 | 0.038691 | 0.040776 |
| M2/P3/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 1.111542 | 1.101073 | 1.535992 |
| M2/P3/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 1.111515 | 1.101050 | 1.535964 |
| M2/P3/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 0.756965 | 0.744971 | 1.540171 |
| M2/P3/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 0.756940 | 0.744949 | 1.540145 |
| M2/P3/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.069213 | 0.068524 | 0.089675 |
| M2/P3/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.245209 | 0.247410 | 0.334699 |
| M2/P3/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.245182 | 0.247384 | 0.334671 |
| M2/P3/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.046756 | 0.043289 | 0.062669 |
| M2/P3/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.046712 | 0.043246 | 0.062620 |
| M2/P3/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.002960 | 0.002830 | 0.004353 |
| M2/P3/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000329 | 0.000324 | 0.000400 |
| M2/P3/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.074709 | 0.070909 | 0.134945 |
| M2/P3/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.145258 | 0.143839 | 0.192975 |
| M2/P3/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.271926 | 0.266830 | 0.379645 |
| M2/P3/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.077188 | 0.075392 | 0.121033 |
| M2/P3/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.022571 | 0.022181 | 0.029997 |
| M2/P3/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000067 | 0.000067 | 0.000081 |
| M2/P3/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7405 | 7405 | 0.000130 | 0.000128 | 0.000164 |
| M2/P3/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7405 | 7405 | 0.000176 | 0.000137 | 0.000332 |
| M2/P3/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7405 | 7405 | 0.000053 | 0.000053 | 0.000065 |
| M2/P3/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 1.955030 | 1.928304 | 2.880163 |
| M3/P3/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.246637 | 0.246925 | 0.333784 |
| M3/P3/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.246605 | 0.246893 | 0.333736 |
| M3/P3/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.075937 | 0.074576 | 0.096028 |
| M3/P3/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.075945 | 0.074585 | 0.096036 |
| M3/P3/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.029500 | 0.029290 | 0.030714 |
| M3/P3/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.029482 | 0.029272 | 0.030695 |
| M3/P3/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 1.294554 | 1.282794 | 1.769103 |
| M3/P3/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 1.294525 | 1.282767 | 1.769072 |
| M3/P3/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 1.039517 | 0.700366 | 2.307390 |
| M3/P3/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 1.039489 | 0.700340 | 2.307363 |
| M3/P3/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.069293 | 0.068050 | 0.088886 |
| M3/P3/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.054868 | 0.055021 | 0.073865 |
| M3/P3/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.054845 | 0.054994 | 0.073839 |
| M3/P3/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.038262 | 0.033270 | 0.053806 |
| M3/P3/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.038220 | 0.033230 | 0.053757 |
| M3/P3/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.002756 | 0.002650 | 0.004053 |
| M3/P3/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000340 | 0.000328 | 0.000456 |
| M3/P3/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.095986 | 0.092716 | 0.169625 |
| M3/P3/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.181567 | 0.178869 | 0.238363 |
| M3/P3/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.346799 | 0.339932 | 0.482693 |
| M3/P3/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.104114 | 0.103282 | 0.150402 |
| M3/P3/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.027892 | 0.027412 | 0.037020 |
| M3/P3/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000078 | 0.000071 | 0.000104 |
| M3/P3/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7405 | 7405 | 0.000127 | 0.000125 | 0.000160 |
| M3/P3/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7405 | 7405 | 0.000214 | 0.000200 | 0.000365 |
| M3/P3/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7405 | 7405 | 0.000054 | 0.000053 | 0.000065 |
| M3/P3/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 2.410728 | 2.096591 | 3.728873 |

## C 异常及覆盖

| 组合 | 项目 | 数值 |
|---|---|---|
| M1/P3/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M1/P3/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M1/P3/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M1/P3/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M1/P3/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 1.9726826375492477, "p50": 1.830216045025736, "p95": 2.869627905124798} |
| M2/P3/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M2/P3/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M2/P3/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M2/P3/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M2/P3/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 2.404326985314599, "p50": 2.36565827508457, "p95": 3.3693909710738796} |
| M3/P3/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M3/P3/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M3/P3/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M3/P3/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M3/P3/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 2.810235506363319, "p50": 2.478709061862901, "p95": 4.173534883325914} |

## D 参数与环境

| 方向 | 模块 | 部署 | 参数量 |
|---|---|---|---|
| M1 | 联合转换融合层0 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层1 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层2 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层3 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层4 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层5 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层6 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层7 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层8 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层9 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层10 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层11 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层12 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层13 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层14 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层15 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层16 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层17 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层18 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层19 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层20 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层21 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层22 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层23 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层24 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层25 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层26 | receiver_gpu | 18901010 |
| M1 | 联合转换融合层27 | receiver_gpu | 18901010 |
| M1 | 通信模块去重总量 | Receiver GPU | 529228280 |
| M1 | receiver基础模型 | 同GPU | 1720574976 |
| M1 | sender基础模型 | 同GPU | 596049920 |
| M2 | 联合转换融合层0 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层1 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层2 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层3 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层4 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层5 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层6 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层7 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层8 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层9 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层10 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层11 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层12 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层13 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层14 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层15 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层16 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层17 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层18 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层19 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层20 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层21 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层22 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层23 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层24 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层25 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层26 | receiver_gpu | 18901010 |
| M2 | 联合转换融合层27 | receiver_gpu | 18901010 |
| M2 | 通信模块去重总量 | Receiver GPU | 529228280 |
| M2 | receiver基础模型 | 同GPU | 4022468096 |
| M2 | sender基础模型 | 同GPU | 596049920 |
| M3 | 联合转换融合层0 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层1 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层2 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层3 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层4 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层5 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层6 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层7 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层8 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层9 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层10 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层11 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层12 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层13 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层14 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层15 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层16 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层17 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层18 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层19 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层20 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层21 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层22 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层23 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层24 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层25 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层26 | receiver_gpu | 18901010 |
| M3 | 联合转换融合层27 | receiver_gpu | 18901010 |
| M3 | 通信模块去重总量 | Receiver GPU | 529228280 |
| M3 | receiver基础模型 | 同GPU | 596049920 |
| M3 | sender基础模型 | 同GPU | 4022468096 |

| 方向 | 项目 | 实际值 |
|---|---|---|
| M1 | gpu | NVIDIA GeForce RTX 3090 |
| M1 | torch | 2.8.0+cu128 |
| M1 | tokenizers | 0.22.2 |
| M1 | cuda_runtime | 12.8 |
| M1 | cpu | AMD Ryzen 9 5900X 12-Core Processor |
| M1 | platform | Linux-6.8.0-138-generic-x86_64-with-glibc2.35 |
| M1 | operation_devices | {"model_prefill_decode_conversion_fusion": "NVIDIA GeForce RTX 3090", "serialization_deserialization_tokenization": "CPU", "kv_transport": "CPU TCP loopback", "raw_text_transport": "CPU TCP loopback"} |
| M1 | transformers | 4.57.6 |
| M1 | python | 3.11.17 |
| M1 | dtype | bfloat16 |
| M1 | backend | sdpa |
| M1 | batch_size | 1 |
| M1 | cpu_threads | 2 |
| M1 | protocol | P3 |
| M1 | path | c2c |
| M1 | adaptation | P2双向补齐；P3/P4单向补齐；补齐后重建完整对齐输入 |
| M2 | gpu | NVIDIA GeForce RTX 3090 |
| M2 | torch | 2.8.0+cu128 |
| M2 | tokenizers | 0.22.2 |
| M2 | cuda_runtime | 12.8 |
| M2 | cpu | AMD Ryzen 9 5900X 12-Core Processor |
| M2 | platform | Linux-6.8.0-138-generic-x86_64-with-glibc2.35 |
| M2 | operation_devices | {"model_prefill_decode_conversion_fusion": "NVIDIA GeForce RTX 3090", "serialization_deserialization_tokenization": "CPU", "kv_transport": "CPU TCP loopback", "raw_text_transport": "CPU TCP loopback"} |
| M2 | transformers | 4.57.6 |
| M2 | python | 3.11.17 |
| M2 | dtype | bfloat16 |
| M2 | backend | sdpa |
| M2 | batch_size | 1 |
| M2 | cpu_threads | 2 |
| M2 | protocol | P3 |
| M2 | path | c2c |
| M2 | adaptation | P2双向补齐；P3/P4单向补齐；补齐后重建完整对齐输入 |
| M3 | gpu | NVIDIA GeForce RTX 3090 |
| M3 | torch | 2.8.0+cu128 |
| M3 | tokenizers | 0.22.2 |
| M3 | cuda_runtime | 12.8 |
| M3 | cpu | AMD Ryzen 9 5900X 12-Core Processor |
| M3 | platform | Linux-6.8.0-138-generic-x86_64-with-glibc2.35 |
| M3 | operation_devices | {"model_prefill_decode_conversion_fusion": "NVIDIA GeForce RTX 3090", "serialization_deserialization_tokenization": "CPU", "kv_transport": "CPU TCP loopback", "raw_text_transport": "CPU TCP loopback"} |
| M3 | transformers | 4.57.6 |
| M3 | python | 3.11.17 |
| M3 | dtype | bfloat16 |
| M3 | backend | sdpa |
| M3 | batch_size | 1 |
| M3 | cpu_threads | 2 |
| M3 | protocol | P3 |
| M3 | path | c2c |
| M3 | adaptation | P2双向补齐；P3/P4单向补齐；补齐后重建完整对齐输入 |

## E 通信

| 组合 | 字段 | n | N | 总字节 | 均值字节 | P50 | P95 |
|---|---|---|---|---|---|---|---|
| M1/P3/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1277447585792 | 172511490.316273 | 168935424.000000 | 242198118.400000 |
| M1/P3/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1277615922591 | 172534223.172316 | 168958296.000000 | 242223770.000000 |
| M1/P3/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 126219492 | 17045.171101 | 17042.000000 | 17130.000000 |
| M1/P3/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 118480 | 16.000000 | 16.000000 | 16.000000 |
| M1/P3/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1277616041071 | 172534239.172316 | 168958312.000000 | 242223786.000000 |
| M1/P3/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1277616041071 | 172534239.172316 | 168958312.000000 | 242223786.000000 |
| M1/P3/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P3/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 42117307 | 5687.684943 | 5574.000000 | 8326.400000 |
| M2/P3/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1277447585792 | 172511490.316273 | 168935424.000000 | 242198118.400000 |
| M2/P3/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1277615922591 | 172534223.172316 | 168958296.000000 | 242223770.000000 |
| M2/P3/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 126219492 | 17045.171101 | 17042.000000 | 17130.000000 |
| M2/P3/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 118480 | 16.000000 | 16.000000 | 16.000000 |
| M2/P3/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1277616041071 | 172534239.172316 | 168958312.000000 | 242223786.000000 |
| M2/P3/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1277616041071 | 172534239.172316 | 168958312.000000 | 242223786.000000 |
| M2/P3/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P3/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 42117307 | 5687.684943 | 5574.000000 | 8326.400000 |
| M3/P3/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1642432610304 | 221800487.549494 | 217202688.000000 | 311397580.800000 |
| M3/P3/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1642634239983 | 221827716.405537 | 217230056.000000 | 311427728.400000 |
| M3/P3/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 159512372 | 21541.171101 | 21538.000000 | 21626.000000 |
| M3/P3/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 118480 | 16.000000 | 16.000000 | 16.000000 |
| M3/P3/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1642634358463 | 221827732.405537 | 217230072.000000 | 311427744.400000 |
| M3/P3/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1642634358463 | 221827732.405537 | 217230072.000000 | 311427744.400000 |
| M3/P3/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P3/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 42117307 | 5687.684943 | 5574.000000 | 8326.400000 |

| 组合 | K/V | n | 层数 | dtype | 序列长度[min,max] | 其余维度(batch,heads,head_dim) |
|---|---|---|---|---|---|---|
| M1/P3/hotpotqa/C2C | keys | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M1/P3/hotpotqa/C2C | values | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M2/P3/hotpotqa/C2C | keys | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M2/P3/hotpotqa/C2C | values | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M3/P3/hotpotqa/C2C | keys | 7405 | [36] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M3/P3/hotpotqa/C2C | values | 7405 | [36] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |

## F GPU竞争观察分项

原始总体耗时保持；以下分列观测到竞争、未观测到竞争及未覆盖监测的样本。采样间隔5秒，未观测到竞争不等于连续独占证明。

| 组合 | 监测分类 | 阶段 | n | 均值s | P50s | P95s |
|---|---|---|---|---|---|---|
| M1/hotpotqa | no_contention_observed | sender_prefill.synchronized_wall_s | 7395 | 0.054526 | 0.055355 | 0.072570 |
| M1/hotpotqa | no_contention_observed | sender_prefill.cuda_event_s | 7395 | 0.054498 | 0.055329 | 0.072536 |
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7395 | 0.076023 | 0.074552 | 0.096129 |
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7395 | 0.076031 | 0.074562 | 0.096136 |
| M1/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7395 | 0.030198 | 0.029922 | 0.031385 |
| M1/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7395 | 0.030179 | 0.029904 | 0.031365 |
| M1/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7395 | 0.939235 | 0.920689 | 1.303550 |
| M1/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7395 | 0.939210 | 0.920667 | 1.303525 |
| M1/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7395 | 0.590801 | 0.488749 | 1.296180 |
| M1/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7395 | 0.590777 | 0.488725 | 1.296154 |
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7395 | 0.069892 | 0.068556 | 0.089580 |
| M1/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7395 | 0.107588 | 0.108568 | 0.143313 |
| M1/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7395 | 0.107562 | 0.108544 | 0.143284 |
| M1/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7395 | 0.041887 | 0.037627 | 0.054576 |
| M1/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7395 | 0.041842 | 0.037580 | 0.054527 |
| M1/hotpotqa | contended | sender_prefill.synchronized_wall_s | 10 | 0.066203 | 0.068972 | 0.083973 |
| M1/hotpotqa | contended | sender_prefill.cuda_event_s | 10 | 0.066098 | 0.068851 | 0.083857 |
| M1/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 10 | 0.093989 | 0.096034 | 0.118515 |
| M1/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 10 | 0.094193 | 0.096120 | 0.118601 |
| M1/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 10 | 0.033480 | 0.030625 | 0.046842 |
| M1/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 10 | 0.033376 | 0.030319 | 0.046807 |
| M1/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 10 | 1.045451 | 1.040346 | 1.325646 |
| M1/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 10 | 1.045414 | 1.040314 | 1.325608 |
| M1/hotpotqa | contended | receiver_decode.synchronized_wall_s | 10 | 0.646685 | 0.513127 | 1.632936 |
| M1/hotpotqa | contended | receiver_decode.cuda_event_s | 10 | 0.646572 | 0.513096 | 1.632803 |
| M1/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 10 | 0.082721 | 0.083526 | 0.105787 |
| M1/hotpotqa | contended | receiver_additional_prefill.synchronized_wall_s | 10 | 0.126759 | 0.129868 | 0.165134 |
| M1/hotpotqa | contended | receiver_additional_prefill.cuda_event_s | 10 | 0.126712 | 0.129828 | 0.165097 |
| M1/hotpotqa | contended | receiver_initial_prefill.synchronized_wall_s | 10 | 0.045730 | 0.046374 | 0.059276 |
| M1/hotpotqa | contended | receiver_initial_prefill.cuda_event_s | 10 | 0.045648 | 0.046154 | 0.059214 |
| M2/hotpotqa | no_contention_observed | sender_prefill.synchronized_wall_s | 7405 | 0.054794 | 0.055949 | 0.073046 |
| M2/hotpotqa | no_contention_observed | sender_prefill.cuda_event_s | 7405 | 0.054766 | 0.055921 | 0.073018 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7405 | 0.076328 | 0.075654 | 0.097173 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7405 | 0.076336 | 0.075661 | 0.097181 |
| M2/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7405 | 0.038946 | 0.038709 | 0.040796 |
| M2/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7405 | 0.038927 | 0.038691 | 0.040776 |
| M2/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7405 | 1.111542 | 1.101073 | 1.535992 |
| M2/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7405 | 1.111515 | 1.101050 | 1.535964 |
| M2/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7405 | 0.756965 | 0.744971 | 1.540171 |
| M2/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7405 | 0.756940 | 0.744949 | 1.540145 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7405 | 0.069213 | 0.068524 | 0.089675 |
| M2/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7405 | 0.245209 | 0.247410 | 0.334699 |
| M2/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7405 | 0.245182 | 0.247384 | 0.334671 |
| M2/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7405 | 0.046756 | 0.043289 | 0.062669 |
| M2/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7405 | 0.046712 | 0.043246 | 0.062620 |
| M3/hotpotqa | no_contention_observed | sender_prefill.synchronized_wall_s | 7393 | 0.246477 | 0.246873 | 0.333496 |
| M3/hotpotqa | no_contention_observed | sender_prefill.cuda_event_s | 7393 | 0.246446 | 0.246847 | 0.333466 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7393 | 0.075858 | 0.074570 | 0.095966 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7393 | 0.075866 | 0.074581 | 0.095972 |
| M3/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7393 | 0.029473 | 0.029290 | 0.030665 |
| M3/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7393 | 0.029455 | 0.029271 | 0.030647 |
| M3/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7393 | 1.293746 | 1.282425 | 1.766169 |
| M3/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7393 | 1.293717 | 1.282387 | 1.766183 |
| M3/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7393 | 1.039271 | 0.698903 | 2.303157 |
| M3/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7393 | 1.039243 | 0.698879 | 2.303128 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7393 | 0.069230 | 0.068044 | 0.088842 |
| M3/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7393 | 0.054832 | 0.055011 | 0.073787 |
| M3/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7393 | 0.054809 | 0.054988 | 0.073758 |
| M3/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7393 | 0.038239 | 0.033264 | 0.053786 |
| M3/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7393 | 0.038197 | 0.033220 | 0.053737 |
| M3/hotpotqa | contended | sender_prefill.synchronized_wall_s | 12 | 0.344909 | 0.334166 | 0.458402 |
| M3/hotpotqa | contended | sender_prefill.cuda_event_s | 12 | 0.344797 | 0.334116 | 0.458282 |
| M3/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 12 | 0.124716 | 0.126457 | 0.153259 |
| M3/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 12 | 0.124885 | 0.126545 | 0.153695 |
| M3/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 12 | 0.046251 | 0.053308 | 0.055447 |
| M3/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 12 | 0.046163 | 0.053272 | 0.055405 |
| M3/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 12 | 1.792619 | 1.756789 | 2.319315 |
| M3/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 12 | 1.792476 | 1.756647 | 2.318929 |
| M3/hotpotqa | contended | receiver_decode.synchronized_wall_s | 12 | 1.191219 | 0.959238 | 2.345462 |
| M3/hotpotqa | contended | receiver_decode.cuda_event_s | 12 | 1.191138 | 0.959191 | 2.345312 |
| M3/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 12 | 0.108343 | 0.108592 | 0.132240 |
| M3/hotpotqa | contended | receiver_additional_prefill.synchronized_wall_s | 12 | 0.076972 | 0.073133 | 0.104000 |
| M3/hotpotqa | contended | receiver_additional_prefill.cuda_event_s | 12 | 0.076892 | 0.073093 | 0.103735 |
| M3/hotpotqa | contended | receiver_initial_prefill.synchronized_wall_s | 12 | 0.052454 | 0.058551 | 0.059703 |
| M3/hotpotqa | contended | receiver_initial_prefill.cuda_event_s | 12 | 0.052360 | 0.058491 | 0.059633 |

## 附录：口径与证据

- 本报告统计P3的C2C路径；协议与路径分别汇总。
- 本轮Receiver输出上限为1024；T2T沿其既定预算，成本比较同时列出实际输出token数。
- 数学首个####正则、问答整段EM/F1、代码原样补全；OOM/输入容量失败计0，触顶按实际前缀正常评分，固定分母不删除失败题。
- 质量与配对差值均为10000次seed42 percentile bootstrap；配对按同方向/协议/任务/ID及明确的基线路径，完整覆盖规定视图。
- 未测项保持未知；异常部分成本单列；inclusive/nested计时不能相加，参数联合模块去重计一次。
- 通信分列原始KV、补传原文、序列化payload、metadata及每包8字节帧；P2 C2C合计两个方向的补传。逐包方向记录在 supplemental_transfers 中。计时拓扑为同机TCP回环。
- P2–P4先记录Receiver初始Prefill，再记录补齐后的完整输入重建；P2 C2C另记录Sender初始与重建Prefill。完整重建保留所有原始任务信息。没有文本生成消息、筛选、池化或广播。
- GPU用CUDA Event与同步墙钟，CPU操作用墙钟。每任务3条合成预热、每条8tokens；每正式题单次生成。快照观测开销保留，不扣估计常数。
- 正文只列关键阶段，附件列实际已采集全部分项。逐题成绩见共享的评测记录。
