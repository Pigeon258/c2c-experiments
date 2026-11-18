# 完整指标与统计口径

- **批次**：`P2`。
- **对应正文**：[正式报告](<P2.md>)。
- **范围**：本协议、路径的完整分项与覆盖情况。

## A 配置与结果

| 组合 | 视图 | 计划N | 已评分n | 指标 | 均值 | 95% CI |
|---|---|---|---|---|---|---|
| M1/P2/hotpotqa/C2C | full | 7345 | 7345 | em | 0.107828 | [0.10074880871341048, 0.11504424778761062] |
| M1/P2/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.107828 | [0.10074880871341048, 0.11504424778761062] |
| M1/P2/hotpotqa/C2C | full | 7345 | 7345 | f1 | 0.240365 | [0.23278845431436807, 0.2477856525871724] |
| M1/P2/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.240365 | [0.23278845431436807, 0.2477856525871724] |
| M2/P2/hotpotqa/C2C | full | 7345 | 7345 | em | 0.092035 | [0.085500340367597, 0.0987066031313819] |
| M2/P2/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.092035 | [0.085500340367597, 0.0987066031313819] |
| M2/P2/hotpotqa/C2C | full | 7345 | 7345 | f1 | 0.276202 | [0.26924102875049, 0.2828945782066278] |
| M2/P2/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.276202 | [0.26924102875049, 0.2828945782066278] |
| M3/P2/hotpotqa/C2C | full | 7345 | 7345 | em | 0.004901 | [0.0034036759700476512, 0.006535057862491491] |
| M3/P2/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.004901 | [0.0034036759700476512, 0.006535057862491491] |
| M3/P2/hotpotqa/C2C | full | 7345 | 7345 | f1 | 0.133471 | [0.12973439221694455, 0.13720172646993634] |
| M3/P2/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.133471 | [0.12973439221694455, 0.13720172646993634] |

| 组合 | 字段 | 已知n | N | 总tokens |
|---|---|---|---|---|
| M1/P2/hotpotqa/C2C | sender_input_tokens | 7345 | 7345 | 11105204 |
| M1/P2/hotpotqa/C2C | input_tokens | 7345 | 7345 | 11112549 |
| M1/P2/hotpotqa/C2C | output_tokens | 7345 | 7345 | 155455 |
| M1/P2/hotpotqa/C2C | receiver_initial_prefill | 7345 | 7345 | 5995829 |
| M1/P2/hotpotqa/C2C | receiver_visible | 7345 | 7345 | 5995829 |
| M1/P2/hotpotqa/C2C | sender_initial_prefill | 7345 | 7345 | 5998584 |
| M1/P2/hotpotqa/C2C | sender_visible | 7345 | 7345 | 5998584 |
| M2/P2/hotpotqa/C2C | sender_input_tokens | 7345 | 7345 | 11105204 |
| M2/P2/hotpotqa/C2C | input_tokens | 7345 | 7345 | 11112549 |
| M2/P2/hotpotqa/C2C | output_tokens | 7345 | 7345 | 153482 |
| M2/P2/hotpotqa/C2C | receiver_initial_prefill | 7345 | 7345 | 5995829 |
| M2/P2/hotpotqa/C2C | receiver_visible | 7345 | 7345 | 5995829 |
| M2/P2/hotpotqa/C2C | sender_initial_prefill | 7345 | 7345 | 5998584 |
| M2/P2/hotpotqa/C2C | sender_visible | 7345 | 7345 | 5998584 |
| M3/P2/hotpotqa/C2C | sender_input_tokens | 7345 | 7345 | 11105204 |
| M3/P2/hotpotqa/C2C | input_tokens | 7345 | 7345 | 11112549 |
| M3/P2/hotpotqa/C2C | output_tokens | 7345 | 7345 | 271124 |
| M3/P2/hotpotqa/C2C | receiver_initial_prefill | 7345 | 7345 | 5995829 |
| M3/P2/hotpotqa/C2C | receiver_visible | 7345 | 7345 | 5995829 |
| M3/P2/hotpotqa/C2C | sender_initial_prefill | 7345 | 7345 | 5998584 |
| M3/P2/hotpotqa/C2C | sender_visible | 7345 | 7345 | 5998584 |

## B 全部分项耗时

| 组合 | 阶段/计时口径 | 完整/部分 | n | N | 均值s | P50s | P95s |
|---|---|---|---|---|---|---|---|
| M1/P2/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7345 | 7345 | 0.076368 | 0.075181 | 0.096836 |
| M1/P2/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7345 | 7345 | 0.076376 | 0.075191 | 0.096845 |
| M1/P2/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.030453 | 0.030120 | 0.031941 |
| M1/P2/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.030432 | 0.030100 | 0.031917 |
| M1/P2/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7345 | 7345 | 0.975070 | 0.955957 | 1.342597 |
| M1/P2/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7345 | 7345 | 0.975039 | 0.955916 | 1.342567 |
| M1/P2/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7345 | 7345 | 0.597253 | 0.488027 | 1.314856 |
| M1/P2/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7345 | 7345 | 0.597225 | 0.488000 | 1.314865 |
| M1/P2/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7345 | 7345 | 0.070031 | 0.068962 | 0.090076 |
| M1/P2/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.108158 | 0.109270 | 0.142456 |
| M1/P2/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.108125 | 0.109250 | 0.142440 |
| M1/P2/hotpotqa/C2C | sender_reconstruction_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.054973 | 0.055720 | 0.072806 |
| M1/P2/hotpotqa/C2C | sender_reconstruction_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.054937 | 0.055688 | 0.072774 |
| M1/P2/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.064759 | 0.068844 | 0.081421 |
| M1/P2/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.064708 | 0.068798 | 0.081367 |
| M1/P2/hotpotqa/C2C | sender_initial_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.033077 | 0.031515 | 0.040514 |
| M1/P2/hotpotqa/C2C | sender_initial_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.033046 | 0.031476 | 0.040474 |
| M1/P2/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7345 | 7345 | 0.003238 | 0.002992 | 0.005360 |
| M1/P2/hotpotqa/C2C | input_host_to_device_s | 完整 | 7345 | 7345 | 0.000361 | 0.000343 | 0.000511 |
| M1/P2/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7345 | 7345 | 0.069437 | 0.066660 | 0.111143 |
| M1/P2/hotpotqa/C2C | sender_pack_s | 完整 | 7345 | 7345 | 0.143905 | 0.141127 | 0.199754 |
| M1/P2/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7345 | 7345 | 0.281103 | 0.273377 | 0.394685 |
| M1/P2/hotpotqa/C2C | receiver_unpack_s | 完整 | 7345 | 7345 | 0.080230 | 0.083074 | 0.121506 |
| M1/P2/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7345 | 7345 | 0.024330 | 0.023586 | 0.033603 |
| M1/P2/hotpotqa/C2C | output_text_decode_s | 完整 | 7345 | 7345 | 0.000074 | 0.000071 | 0.000099 |
| M1/P2/hotpotqa/C2C | receiver_to_sender_text_pack_s | 完整 | 7345 | 7345 | 0.000095 | 0.000086 | 0.000152 |
| M1/P2/hotpotqa/C2C | receiver_to_sender_text_transport_s | 完整 | 7345 | 7345 | 0.000148 | 0.000131 | 0.000283 |
| M1/P2/hotpotqa/C2C | receiver_to_sender_text_unpack_reconstruct_s | 完整 | 7345 | 7345 | 0.000063 | 0.000061 | 0.000079 |
| M1/P2/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7345 | 7345 | 0.000055 | 0.000054 | 0.000072 |
| M1/P2/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7345 | 7345 | 0.000082 | 0.000079 | 0.000097 |
| M1/P2/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7345 | 7345 | 0.000048 | 0.000047 | 0.000059 |
| M1/P2/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7345 | 7345 | 1.701824 | 1.566428 | 2.554789 |
| M2/P2/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7345 | 7345 | 0.078475 | 0.076925 | 0.097926 |
| M2/P2/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7345 | 7345 | 0.078483 | 0.076931 | 0.097933 |
| M2/P2/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.039679 | 0.039637 | 0.041016 |
| M2/P2/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.039660 | 0.039619 | 0.040997 |
| M2/P2/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7345 | 7345 | 1.144542 | 1.126202 | 1.603030 |
| M2/P2/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7345 | 7345 | 1.144510 | 1.126156 | 1.602990 |
| M2/P2/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7345 | 7345 | 0.772568 | 0.752897 | 1.571446 |
| M2/P2/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7345 | 7345 | 0.772539 | 0.752886 | 1.571405 |
| M2/P2/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7345 | 7345 | 0.071208 | 0.069692 | 0.090348 |
| M2/P2/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.249304 | 0.250144 | 0.339288 |
| M2/P2/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.249276 | 0.250114 | 0.339260 |
| M2/P2/hotpotqa/C2C | sender_reconstruction_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.055751 | 0.056547 | 0.074316 |
| M2/P2/hotpotqa/C2C | sender_reconstruction_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.055723 | 0.056516 | 0.074283 |
| M2/P2/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.140084 | 0.140761 | 0.198017 |
| M2/P2/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.140037 | 0.140722 | 0.197969 |
| M2/P2/hotpotqa/C2C | sender_initial_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.033166 | 0.031543 | 0.040029 |
| M2/P2/hotpotqa/C2C | sender_initial_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.033138 | 0.031516 | 0.040003 |
| M2/P2/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7345 | 7345 | 0.002869 | 0.002716 | 0.004226 |
| M2/P2/hotpotqa/C2C | input_host_to_device_s | 完整 | 7345 | 7345 | 0.000329 | 0.000323 | 0.000400 |
| M2/P2/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7345 | 7345 | 0.071359 | 0.066949 | 0.138156 |
| M2/P2/hotpotqa/C2C | sender_pack_s | 完整 | 7345 | 7345 | 0.144553 | 0.139235 | 0.201955 |
| M2/P2/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7345 | 7345 | 0.285122 | 0.277459 | 0.400556 |
| M2/P2/hotpotqa/C2C | receiver_unpack_s | 完整 | 7345 | 7345 | 0.088277 | 0.087724 | 0.127408 |
| M2/P2/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7345 | 7345 | 0.023064 | 0.022563 | 0.030857 |
| M2/P2/hotpotqa/C2C | output_text_decode_s | 完整 | 7345 | 7345 | 0.000068 | 0.000068 | 0.000083 |
| M2/P2/hotpotqa/C2C | receiver_to_sender_text_pack_s | 完整 | 7345 | 7345 | 0.000085 | 0.000083 | 0.000111 |
| M2/P2/hotpotqa/C2C | receiver_to_sender_text_transport_s | 完整 | 7345 | 7345 | 0.000146 | 0.000123 | 0.000355 |
| M2/P2/hotpotqa/C2C | receiver_to_sender_text_unpack_reconstruct_s | 完整 | 7345 | 7345 | 0.000058 | 0.000058 | 0.000068 |
| M2/P2/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7345 | 7345 | 0.000054 | 0.000053 | 0.000068 |
| M2/P2/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7345 | 7345 | 0.000082 | 0.000078 | 0.000099 |
| M2/P2/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7345 | 7345 | 0.000046 | 0.000046 | 0.000054 |
| M2/P2/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7345 | 7345 | 2.130477 | 2.095546 | 3.117375 |
| M3/P2/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7345 | 7345 | 0.075101 | 0.074388 | 0.095771 |
| M3/P2/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7345 | 7345 | 0.075110 | 0.074396 | 0.095778 |
| M3/P2/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.029194 | 0.029030 | 0.030211 |
| M3/P2/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.029176 | 0.029012 | 0.030190 |
| M3/P2/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7345 | 7345 | 1.303687 | 1.291124 | 1.756387 |
| M3/P2/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7345 | 7345 | 1.303651 | 1.291089 | 1.756292 |
| M3/P2/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7345 | 7345 | 1.020008 | 0.689878 | 2.275623 |
| M3/P2/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7345 | 7345 | 1.019975 | 0.689834 | 2.275575 |
| M3/P2/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7345 | 7345 | 0.068508 | 0.067932 | 0.088756 |
| M3/P2/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.054547 | 0.055395 | 0.071927 |
| M3/P2/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.054525 | 0.055371 | 0.071903 |
| M3/P2/hotpotqa/C2C | sender_reconstruction_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.245624 | 0.246709 | 0.333307 |
| M3/P2/hotpotqa/C2C | sender_reconstruction_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.245592 | 0.246682 | 0.333251 |
| M3/P2/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.042448 | 0.041475 | 0.054389 |
| M3/P2/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.042405 | 0.041435 | 0.054336 |
| M3/P2/hotpotqa/C2C | sender_initial_prefill.synchronized_wall_s | 完整 | 7345 | 7345 | 0.141065 | 0.140749 | 0.199963 |
| M3/P2/hotpotqa/C2C | sender_initial_prefill.cuda_event_s | 完整 | 7345 | 7345 | 0.141035 | 0.140722 | 0.199923 |
| M3/P2/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7345 | 7345 | 0.002870 | 0.002691 | 0.004415 |
| M3/P2/hotpotqa/C2C | input_host_to_device_s | 完整 | 7345 | 7345 | 0.000344 | 0.000332 | 0.000449 |
| M3/P2/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7345 | 7345 | 0.079666 | 0.075930 | 0.123934 |
| M3/P2/hotpotqa/C2C | sender_pack_s | 完整 | 7345 | 7345 | 0.182643 | 0.177572 | 0.249321 |
| M3/P2/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7345 | 7345 | 0.358328 | 0.350477 | 0.500397 |
| M3/P2/hotpotqa/C2C | receiver_unpack_s | 完整 | 7345 | 7345 | 0.105989 | 0.106671 | 0.160388 |
| M3/P2/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7345 | 7345 | 0.028259 | 0.027723 | 0.037581 |
| M3/P2/hotpotqa/C2C | output_text_decode_s | 完整 | 7345 | 7345 | 0.000075 | 0.000070 | 0.000102 |
| M3/P2/hotpotqa/C2C | receiver_to_sender_text_pack_s | 完整 | 7345 | 7345 | 0.000086 | 0.000081 | 0.000125 |
| M3/P2/hotpotqa/C2C | receiver_to_sender_text_transport_s | 完整 | 7345 | 7345 | 0.000154 | 0.000127 | 0.000299 |
| M3/P2/hotpotqa/C2C | receiver_to_sender_text_unpack_reconstruct_s | 完整 | 7345 | 7345 | 0.000061 | 0.000060 | 0.000073 |
| M3/P2/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7345 | 7345 | 0.000054 | 0.000053 | 0.000069 |
| M3/P2/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7345 | 7345 | 0.000104 | 0.000079 | 0.000256 |
| M3/P2/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7345 | 7345 | 0.000048 | 0.000047 | 0.000057 |
| M3/P2/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7345 | 7345 | 2.536726 | 2.229328 | 3.835221 |

## C 异常及覆盖

| 组合 | 项目 | 数值 |
|---|---|---|
| M1/P2/hotpotqa/C2C | input_tokens | {"known": 7345, "missing": 0} |
| M1/P2/hotpotqa/C2C | output_tokens | {"known": 7345, "missing": 0} |
| M1/P2/hotpotqa/C2C | communication | {"known": 7345, "missing": 0} |
| M1/P2/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7345, "missing": 0} |
| M1/P2/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7345, "mean": 2.095661095117832, "p50": 1.9581300790887326, "p95": 2.976543132634832} |
| M2/P2/hotpotqa/C2C | input_tokens | {"known": 7345, "missing": 0} |
| M2/P2/hotpotqa/C2C | output_tokens | {"known": 7345, "missing": 0} |
| M2/P2/hotpotqa/C2C | communication | {"known": 7345, "missing": 0} |
| M2/P2/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7345, "missing": 0} |
| M2/P2/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7345, "mean": 2.52513034527708, "p50": 2.4847537151072174, "p95": 3.5271204328164454} |
| M3/P2/hotpotqa/C2C | input_tokens | {"known": 7345, "missing": 0} |
| M3/P2/hotpotqa/C2C | output_tokens | {"known": 7345, "missing": 0} |
| M3/P2/hotpotqa/C2C | communication | {"known": 7345, "missing": 0} |
| M3/P2/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7345, "missing": 0} |
| M3/P2/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7345, "mean": 2.9602678302124237, "p50": 2.6528526071924716, "p95": 4.326833933964369} |

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
| M1 | protocol | P2 |
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
| M2 | protocol | P2 |
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
| M3 | protocol | P2 |
| M3 | path | c2c |
| M3 | adaptation | P2双向补齐；P3/P4单向补齐；补齐后重建完整对齐输入 |

## E 通信

| 组合 | 字段 | n | N | 总字节 | 均值字节 | P50 | P95 |
|---|---|---|---|---|---|---|---|
| M1/P2/hotpotqa/C2C | raw_kv_bytes | 7345 | 7345 | 1273633636352 | 173401448.107828 | 169279488.000000 | 242450432.000000 |
| M1/P2/hotpotqa/C2C | serialized_payload_bytes | 7345 | 7345 | 1273802669624 | 173424461.487270 | 169302248.000000 | 242475880.400000 |
| M1/P2/hotpotqa/C2C | metadata_and_container_bytes | 7345 | 7345 | 127020863 | 17293.514364 | 17287.000000 | 17376.000000 |
| M1/P2/hotpotqa/C2C | framing_bytes | 7345 | 7345 | 176280 | 24.000000 | 24.000000 | 24.000000 |
| M1/P2/hotpotqa/C2C | actual_sent_bytes | 7345 | 7345 | 1273802845904 | 173424485.487270 | 169302272.000000 | 242475904.400000 |
| M1/P2/hotpotqa/C2C | actual_received_bytes | 7345 | 7345 | 1273802845904 | 173424485.487270 | 169302272.000000 | 242475904.400000 |
| M1/P2/hotpotqa/C2C | generated_text_bytes | 7345 | 7345 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P2/hotpotqa/C2C | supplemental_text_bytes | 7345 | 7345 | 42012409 | 5719.865078 | 5587.000000 | 8330.800000 |
| M2/P2/hotpotqa/C2C | raw_kv_bytes | 7345 | 7345 | 1273633636352 | 173401448.107828 | 169279488.000000 | 242450432.000000 |
| M2/P2/hotpotqa/C2C | serialized_payload_bytes | 7345 | 7345 | 1273802669624 | 173424461.487270 | 169302248.000000 | 242475880.400000 |
| M2/P2/hotpotqa/C2C | metadata_and_container_bytes | 7345 | 7345 | 127020863 | 17293.514364 | 17287.000000 | 17376.000000 |
| M2/P2/hotpotqa/C2C | framing_bytes | 7345 | 7345 | 176280 | 24.000000 | 24.000000 | 24.000000 |
| M2/P2/hotpotqa/C2C | actual_sent_bytes | 7345 | 7345 | 1273802845904 | 173424485.487270 | 169302272.000000 | 242475904.400000 |
| M2/P2/hotpotqa/C2C | actual_received_bytes | 7345 | 7345 | 1273802845904 | 173424485.487270 | 169302272.000000 | 242475904.400000 |
| M2/P2/hotpotqa/C2C | generated_text_bytes | 7345 | 7345 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P2/hotpotqa/C2C | supplemental_text_bytes | 7345 | 7345 | 42012409 | 5719.865078 | 5587.000000 | 8330.800000 |
| M3/P2/hotpotqa/C2C | raw_kv_bytes | 7345 | 7345 | 1637528961024 | 222944718.995779 | 217645056.000000 | 311721984.000000 |
| M3/P2/hotpotqa/C2C | serialized_payload_bytes | 7345 | 7345 | 1637731017416 | 222972228.375221 | 217672312.000000 | 311751928.400000 |
| M3/P2/hotpotqa/C2C | metadata_and_container_bytes | 7345 | 7345 | 160043983 | 21789.514364 | 21783.000000 | 21872.000000 |
| M3/P2/hotpotqa/C2C | framing_bytes | 7345 | 7345 | 176280 | 24.000000 | 24.000000 | 24.000000 |
| M3/P2/hotpotqa/C2C | actual_sent_bytes | 7345 | 7345 | 1637731193696 | 222972252.375221 | 217672336.000000 | 311751952.400000 |
| M3/P2/hotpotqa/C2C | actual_received_bytes | 7345 | 7345 | 1637731193696 | 222972252.375221 | 217672336.000000 | 311751952.400000 |
| M3/P2/hotpotqa/C2C | generated_text_bytes | 7345 | 7345 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P2/hotpotqa/C2C | supplemental_text_bytes | 7345 | 7345 | 42012409 | 5719.865078 | 5587.000000 | 8330.800000 |

| 组合 | K/V | n | 层数 | dtype | 序列长度[min,max] | 其余维度(batch,heads,head_dim) |
|---|---|---|---|---|---|---|
| M1/P2/hotpotqa/C2C | keys | 7345 | [28] | ["torch.bfloat16"] | [524, 3666] | [[1, 8, 128]] |
| M1/P2/hotpotqa/C2C | values | 7345 | [28] | ["torch.bfloat16"] | [524, 3666] | [[1, 8, 128]] |
| M2/P2/hotpotqa/C2C | keys | 7345 | [28] | ["torch.bfloat16"] | [524, 3666] | [[1, 8, 128]] |
| M2/P2/hotpotqa/C2C | values | 7345 | [28] | ["torch.bfloat16"] | [524, 3666] | [[1, 8, 128]] |
| M3/P2/hotpotqa/C2C | keys | 7345 | [36] | ["torch.bfloat16"] | [524, 3666] | [[1, 8, 128]] |
| M3/P2/hotpotqa/C2C | values | 7345 | [36] | ["torch.bfloat16"] | [524, 3666] | [[1, 8, 128]] |

## F GPU竞争观察分项

原始总体耗时保持；以下分列观测到竞争、未观测到竞争及未覆盖监测的样本。采样间隔5秒，未观测到竞争不等于连续独占证明。

| 组合 | 监测分类 | 阶段 | n | 均值s | P50s | P95s |
|---|---|---|---|---|---|---|
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7335 | 0.076317 | 0.075170 | 0.096766 |
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7335 | 0.076325 | 0.075180 | 0.096771 |
| M1/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7335 | 0.030433 | 0.030118 | 0.031923 |
| M1/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7335 | 0.030413 | 0.030100 | 0.031900 |
| M1/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7335 | 0.974711 | 0.955598 | 1.341788 |
| M1/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7335 | 0.974680 | 0.955615 | 1.341768 |
| M1/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7335 | 0.596750 | 0.487875 | 1.314095 |
| M1/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7335 | 0.596722 | 0.487862 | 1.314099 |
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7335 | 0.069986 | 0.068957 | 0.090052 |
| M1/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7335 | 0.108140 | 0.109270 | 0.142413 |
| M1/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7335 | 0.108107 | 0.109247 | 0.142378 |
| M1/hotpotqa | no_contention_observed | sender_reconstruction_prefill.synchronized_wall_s | 7335 | 0.054954 | 0.055715 | 0.072780 |
| M1/hotpotqa | no_contention_observed | sender_reconstruction_prefill.cuda_event_s | 7335 | 0.054918 | 0.055686 | 0.072739 |
| M1/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7335 | 0.064750 | 0.068844 | 0.081411 |
| M1/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7335 | 0.064699 | 0.068798 | 0.081337 |
| M1/hotpotqa | no_contention_observed | sender_initial_prefill.synchronized_wall_s | 7335 | 0.033052 | 0.031513 | 0.040342 |
| M1/hotpotqa | no_contention_observed | sender_initial_prefill.cuda_event_s | 7335 | 0.033020 | 0.031473 | 0.040310 |
| M1/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 10 | 0.113558 | 0.112104 | 0.127657 |
| M1/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 10 | 0.113637 | 0.112190 | 0.127746 |
| M1/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 10 | 0.044605 | 0.047691 | 0.056580 |
| M1/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 10 | 0.044571 | 0.047656 | 0.056541 |
| M1/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 10 | 1.238474 | 1.214992 | 1.434301 |
| M1/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 10 | 1.238404 | 1.214940 | 1.434203 |
| M1/hotpotqa | contended | receiver_decode.synchronized_wall_s | 10 | 0.966358 | 1.020893 | 1.488509 |
| M1/hotpotqa | contended | receiver_decode.cuda_event_s | 10 | 0.966255 | 1.020837 | 1.488468 |
| M1/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 10 | 0.102684 | 0.101926 | 0.115755 |
| M1/hotpotqa | contended | receiver_additional_prefill.synchronized_wall_s | 10 | 0.121502 | 0.122888 | 0.158687 |
| M1/hotpotqa | contended | receiver_additional_prefill.cuda_event_s | 10 | 0.121385 | 0.122643 | 0.158637 |
| M1/hotpotqa | contended | sender_reconstruction_prefill.synchronized_wall_s | 10 | 0.068934 | 0.063163 | 0.093742 |
| M1/hotpotqa | contended | sender_reconstruction_prefill.cuda_event_s | 10 | 0.068832 | 0.063006 | 0.093683 |
| M1/hotpotqa | contended | receiver_initial_prefill.synchronized_wall_s | 10 | 0.071798 | 0.074374 | 0.084893 |
| M1/hotpotqa | contended | receiver_initial_prefill.cuda_event_s | 10 | 0.071711 | 0.074290 | 0.084812 |
| M1/hotpotqa | contended | sender_initial_prefill.synchronized_wall_s | 10 | 0.051882 | 0.052128 | 0.057108 |
| M1/hotpotqa | contended | sender_initial_prefill.cuda_event_s | 10 | 0.051793 | 0.052067 | 0.057046 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7343 | 0.078470 | 0.076924 | 0.097921 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7343 | 0.078478 | 0.076929 | 0.097929 |
| M2/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7343 | 0.039674 | 0.039636 | 0.041008 |
| M2/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7343 | 0.039655 | 0.039619 | 0.040989 |
| M2/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7343 | 1.144522 | 1.126202 | 1.603037 |
| M2/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7343 | 1.144490 | 1.126156 | 1.602997 |
| M2/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7343 | 0.772437 | 0.752897 | 1.571343 |
| M2/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7343 | 0.772408 | 0.752886 | 1.571299 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7343 | 0.071203 | 0.069692 | 0.090341 |
| M2/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7343 | 0.249304 | 0.250144 | 0.339295 |
| M2/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7343 | 0.249276 | 0.250114 | 0.339267 |
| M2/hotpotqa | no_contention_observed | sender_reconstruction_prefill.synchronized_wall_s | 7343 | 0.055752 | 0.056547 | 0.074323 |
| M2/hotpotqa | no_contention_observed | sender_reconstruction_prefill.cuda_event_s | 7343 | 0.055724 | 0.056516 | 0.074291 |
| M2/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7343 | 0.140084 | 0.140761 | 0.198018 |
| M2/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7343 | 0.140037 | 0.140722 | 0.197969 |
| M2/hotpotqa | no_contention_observed | sender_initial_prefill.synchronized_wall_s | 7343 | 0.033162 | 0.031542 | 0.040019 |
| M2/hotpotqa | no_contention_observed | sender_initial_prefill.cuda_event_s | 7343 | 0.033135 | 0.031516 | 0.039995 |
| M2/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 2 | 0.099544 | 0.099544 | 0.118463 |
| M2/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 2 | 0.099662 | 0.099662 | 0.118606 |
| M2/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 2 | 0.056347 | 0.056347 | 0.068684 |
| M2/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 2 | 0.056315 | 0.056315 | 0.068648 |
| M2/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 2 | 1.216493 | 1.216493 | 1.377720 |
| M2/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 2 | 1.216441 | 1.216441 | 1.377663 |
| M2/hotpotqa | contended | receiver_decode.synchronized_wall_s | 2 | 1.252834 | 1.252834 | 1.797291 |
| M2/hotpotqa | contended | receiver_decode.cuda_event_s | 2 | 1.252791 | 1.252791 | 1.797234 |
| M2/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 2 | 0.087970 | 0.087970 | 0.104583 |
| M2/hotpotqa | contended | receiver_additional_prefill.synchronized_wall_s | 2 | 0.246166 | 0.246166 | 0.261437 |
| M2/hotpotqa | contended | receiver_additional_prefill.cuda_event_s | 2 | 0.246095 | 0.246095 | 0.261354 |
| M2/hotpotqa | contended | sender_reconstruction_prefill.synchronized_wall_s | 2 | 0.054492 | 0.054492 | 0.061310 |
| M2/hotpotqa | contended | sender_reconstruction_prefill.cuda_event_s | 2 | 0.054342 | 0.054342 | 0.061167 |
| M2/hotpotqa | contended | receiver_initial_prefill.synchronized_wall_s | 2 | 0.140709 | 0.140709 | 0.142136 |
| M2/hotpotqa | contended | receiver_initial_prefill.cuda_event_s | 2 | 0.140620 | 0.140620 | 0.142059 |
| M2/hotpotqa | contended | sender_initial_prefill.synchronized_wall_s | 2 | 0.045377 | 0.045377 | 0.055369 |
| M2/hotpotqa | contended | sender_initial_prefill.cuda_event_s | 2 | 0.045322 | 0.045322 | 0.055300 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7337 | 0.075089 | 0.074386 | 0.095769 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7337 | 0.075097 | 0.074394 | 0.095777 |
| M3/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7337 | 0.029193 | 0.029029 | 0.030211 |
| M3/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7337 | 0.029175 | 0.029011 | 0.030191 |
| M3/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7337 | 1.303543 | 1.291111 | 1.755986 |
| M3/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7337 | 1.303507 | 1.291088 | 1.755938 |
| M3/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7337 | 1.016002 | 0.689561 | 2.255452 |
| M3/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7337 | 1.015969 | 0.689536 | 2.255409 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7337 | 0.068498 | 0.067930 | 0.088754 |
| M3/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7337 | 0.054541 | 0.055395 | 0.071911 |
| M3/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7337 | 0.054518 | 0.055370 | 0.071884 |
| M3/hotpotqa | no_contention_observed | sender_reconstruction_prefill.synchronized_wall_s | 7337 | 0.245583 | 0.246704 | 0.333292 |
| M3/hotpotqa | no_contention_observed | sender_reconstruction_prefill.cuda_event_s | 7337 | 0.245550 | 0.246675 | 0.333247 |
| M3/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7337 | 0.042456 | 0.041526 | 0.054391 |
| M3/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7337 | 0.042412 | 0.041482 | 0.054337 |
| M3/hotpotqa | no_contention_observed | sender_initial_prefill.synchronized_wall_s | 7337 | 0.141030 | 0.140738 | 0.199944 |
| M3/hotpotqa | no_contention_observed | sender_initial_prefill.cuda_event_s | 7337 | 0.141001 | 0.140711 | 0.199909 |
| M3/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 8 | 0.086481 | 0.087732 | 0.102123 |
| M3/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 8 | 0.086557 | 0.087817 | 0.102209 |
| M3/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 8 | 0.029546 | 0.029542 | 0.029739 |
| M3/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 8 | 0.029525 | 0.029523 | 0.029718 |
| M3/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 8 | 1.435655 | 1.420015 | 2.022653 |
| M3/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 8 | 1.435598 | 1.419947 | 2.022580 |
| M3/hotpotqa | contended | receiver_decode.synchronized_wall_s | 8 | 4.694457 | 0.868560 | 20.174622 |
| M3/hotpotqa | contended | receiver_decode.cuda_event_s | 8 | 4.694319 | 0.868515 | 20.174168 |
| M3/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 8 | 0.077882 | 0.079458 | 0.090132 |
| M3/hotpotqa | contended | receiver_additional_prefill.synchronized_wall_s | 8 | 0.060564 | 0.064131 | 0.078182 |
| M3/hotpotqa | contended | receiver_additional_prefill.cuda_event_s | 8 | 0.060532 | 0.064099 | 0.078141 |
| M3/hotpotqa | contended | sender_reconstruction_prefill.synchronized_wall_s | 8 | 0.283989 | 0.296013 | 0.370636 |
| M3/hotpotqa | contended | sender_reconstruction_prefill.cuda_event_s | 8 | 0.283917 | 0.295900 | 0.370559 |
| M3/hotpotqa | contended | receiver_initial_prefill.synchronized_wall_s | 8 | 0.035472 | 0.036220 | 0.039094 |
| M3/hotpotqa | contended | receiver_initial_prefill.cuda_event_s | 8 | 0.035429 | 0.036177 | 0.039050 |
| M3/hotpotqa | contended | sender_initial_prefill.synchronized_wall_s | 8 | 0.172826 | 0.166459 | 0.240550 |
| M3/hotpotqa | contended | sender_initial_prefill.cuda_event_s | 8 | 0.172734 | 0.166416 | 0.240495 |

## 附录：口径与证据

- 本报告统计P2的C2C路径；协议与路径分别汇总。
- 本轮Receiver输出上限为1024；T2T沿其既定预算，成本比较同时列出实际输出token数。
- 数学首个####正则、问答整段EM/F1、代码原样补全；OOM/输入容量失败计0，触顶按实际前缀正常评分，固定分母不删除失败题。
- 质量与配对差值均为10000次seed42 percentile bootstrap；配对按同方向/协议/任务/ID及明确的基线路径，完整覆盖规定视图。
- 未测项保持未知；异常部分成本单列；inclusive/nested计时不能相加，参数联合模块去重计一次。
- 通信分列原始KV、补传原文、序列化payload、metadata及每包8字节帧；P2 C2C合计两个方向的补传。逐包方向记录在 supplemental_transfers 中。计时拓扑为同机TCP回环。
- P2–P4先记录Receiver初始Prefill，再记录补齐后的完整输入重建；P2 C2C另记录Sender初始与重建Prefill。完整重建保留所有原始任务信息。没有文本生成消息、筛选、池化或广播。
- GPU用CUDA Event与同步墙钟，CPU操作用墙钟。每任务3条合成预热、每条8tokens；每正式题单次生成。快照观测开销保留，不扣估计常数。
- 正文只列关键阶段，附件列实际已采集全部分项。逐题成绩见共享的评测记录。
