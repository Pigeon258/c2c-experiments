# 完整指标与统计口径

- **批次**：`P1`。
- **对应正文**：[正式报告](<P1.md>)。
- **范围**：本协议、路径的完整分项与覆盖情况。

## A 配置与结果

| 组合 | 视图 | 计划N | 已评分n | 指标 | 均值 | 95% CI |
|---|---|---|---|---|---|---|
| M1/P1/gsm8k/C2C | full | 1319 | 1319 | accuracy | 0.269143 | [0.244882486732373, 0.2934040940106141] |
| M1/P1/hotpotqa/C2C | full | 7405 | 7405 | em | 0.108170 | [0.1012829169480081, 0.11532748143146522] |
| M1/P1/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.107828 | [0.10074880871341048, 0.11504424778761062] |
| M1/P1/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.240721 | [0.23335464308848075, 0.2482068002010702] |
| M1/P1/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.240365 | [0.23278845431436807, 0.2477856525871724] |
| M1/P1/humaneval/C2C | full | 164 | 164 | pass@1 | 0.432927 | [0.3597560975609756, 0.5121951219512195] |
| M2/P1/gsm8k/C2C | full | 1319 | 1319 | accuracy | 0.699773 | [0.6747536012130402, 0.7240523123578466] |
| M2/P1/hotpotqa/C2C | full | 7405 | 7405 | em | 0.091560 | [0.08507765023632681, 0.09804186360567184] |
| M2/P1/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.092035 | [0.085500340367597, 0.0987066031313819] |
| M2/P1/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.276049 | [0.26934856956447545, 0.28283269003987904] |
| M2/P1/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.276202 | [0.26924102875049, 0.2828945782066278] |
| M2/P1/humaneval/C2C | full | 164 | 164 | pass@1 | 0.585366 | [0.5121951219512195, 0.6585365853658537] |
| M3/P1/gsm8k/C2C | full | 1319 | 1319 | accuracy | 0.075057 | [0.06141015921152388, 0.0887035633055345] |
| M3/P1/hotpotqa/C2C | full | 7405 | 7405 | em | 0.004862 | [0.00337609723160027, 0.006482106684672519] |
| M3/P1/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.004901 | [0.0034036759700476512, 0.006535057862491491] |
| M3/P1/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.133725 | [0.1300072938726543, 0.1374455520450355] |
| M3/P1/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.133471 | [0.12973439221694455, 0.13720172646993634] |
| M3/P1/humaneval/C2C | full | 164 | 164 | pass@1 | 0.256098 | [0.18902439024390244, 0.3231707317073171] |

| 组合 | 字段 | 已知n | N | 总tokens |
|---|---|---|---|---|
| M1/P1/gsm8k/C2C | sender_input_tokens | 1319 | 1319 | 178471 |
| M1/P1/gsm8k/C2C | input_tokens | 1319 | 1319 | 179790 |
| M1/P1/gsm8k/C2C | output_tokens | 1319 | 1319 | 494436 |
| M1/P1/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M1/P1/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M1/P1/hotpotqa/C2C | output_tokens | 7405 | 7405 | 156391 |
| M1/P1/humaneval/C2C | sender_input_tokens | 164 | 164 | 39725 |
| M1/P1/humaneval/C2C | input_tokens | 164 | 164 | 39889 |
| M1/P1/humaneval/C2C | output_tokens | 164 | 164 | 22511 |
| M2/P1/gsm8k/C2C | sender_input_tokens | 1319 | 1319 | 178471 |
| M2/P1/gsm8k/C2C | input_tokens | 1319 | 1319 | 179790 |
| M2/P1/gsm8k/C2C | output_tokens | 1319 | 1319 | 158966 |
| M2/P1/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M2/P1/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M2/P1/hotpotqa/C2C | output_tokens | 7405 | 7405 | 154491 |
| M2/P1/humaneval/C2C | sender_input_tokens | 164 | 164 | 39725 |
| M2/P1/humaneval/C2C | input_tokens | 164 | 164 | 39889 |
| M2/P1/humaneval/C2C | output_tokens | 164 | 164 | 26647 |
| M3/P1/gsm8k/C2C | sender_input_tokens | 1319 | 1319 | 178471 |
| M3/P1/gsm8k/C2C | input_tokens | 1319 | 1319 | 179790 |
| M3/P1/gsm8k/C2C | output_tokens | 1319 | 1319 | 207075 |
| M3/P1/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M3/P1/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M3/P1/hotpotqa/C2C | output_tokens | 7405 | 7405 | 274274 |
| M3/P1/humaneval/C2C | sender_input_tokens | 164 | 164 | 39725 |
| M3/P1/humaneval/C2C | input_tokens | 164 | 164 | 39889 |
| M3/P1/humaneval/C2C | output_tokens | 164 | 164 | 48319 |

## B 全部分项耗时

| 组合 | 阶段/计时口径 | 完整/部分 | n | N | 均值s | P50s | P95s |
|---|---|---|---|---|---|---|---|
| M1/P1/gsm8k/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.049856 | 0.052977 | 0.058829 |
| M1/P1/gsm8k/C2C | receiver_local_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.049826 | 0.052948 | 0.058794 |
| M1/P1/gsm8k/C2C | sender_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.032424 | 0.031564 | 0.036031 |
| M1/P1/gsm8k/C2C | sender_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.032398 | 0.031539 | 0.035999 |
| M1/P1/gsm8k/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.062916 | 0.063010 | 0.064431 |
| M1/P1/gsm8k/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.062923 | 0.063017 | 0.064440 |
| M1/P1/gsm8k/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.029828 | 0.029767 | 0.030554 |
| M1/P1/gsm8k/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.029808 | 0.029746 | 0.030537 |
| M1/P1/gsm8k/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.215022 | 0.215584 | 0.231079 |
| M1/P1/gsm8k/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.214983 | 0.215544 | 0.231040 |
| M1/P1/gsm8k/C2C | receiver_decode.synchronized_wall_s | 完整 | 1319 | 1319 | 10.899367 | 3.628268 | 30.062252 |
| M1/P1/gsm8k/C2C | receiver_decode.cuda_event_s | 完整 | 1319 | 1319 | 10.899242 | 3.628211 | 30.061933 |
| M1/P1/gsm8k/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 1319 | 1319 | 0.057523 | 0.057675 | 0.058936 |
| M1/P1/gsm8k/C2C | input_assembly_tokenize_s | 完整 | 1319 | 1319 | 0.000784 | 0.000768 | 0.000975 |
| M1/P1/gsm8k/C2C | input_host_to_device_s | 完整 | 1319 | 1319 | 0.000443 | 0.000445 | 0.000552 |
| M1/P1/gsm8k/C2C | sender_device_to_host_s | 完整 | 1319 | 1319 | 0.004772 | 0.004672 | 0.006013 |
| M1/P1/gsm8k/C2C | sender_pack_s | 完整 | 1319 | 1319 | 0.006103 | 0.005959 | 0.007446 |
| M1/P1/gsm8k/C2C | transport_loopback_and_byte_verify_s | 完整 | 1319 | 1319 | 0.006374 | 0.006128 | 0.008635 |
| M1/P1/gsm8k/C2C | receiver_unpack_s | 完整 | 1319 | 1319 | 0.005324 | 0.005272 | 0.005878 |
| M1/P1/gsm8k/C2C | receiver_restore_and_host_to_device_s | 完整 | 1319 | 1319 | 0.005806 | 0.005550 | 0.007149 |
| M1/P1/gsm8k/C2C | output_text_decode_s | 完整 | 1319 | 1319 | 0.000150 | 0.000108 | 0.000290 |
| M1/P1/gsm8k/C2C | hot_pipeline_wall_s | 完整 | 1319 | 1319 | 11.117036 | 3.856921 | 30.274910 |
| M1/P1/hotpotqa/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.109520 | 0.110163 | 0.147574 |
| M1/P1/hotpotqa/C2C | receiver_local_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.109491 | 0.110122 | 0.147539 |
| M1/P1/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.055238 | 0.055891 | 0.074183 |
| M1/P1/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.055208 | 0.055862 | 0.074155 |
| M1/P1/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.076071 | 0.074699 | 0.096760 |
| M1/P1/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.076089 | 0.074714 | 0.096770 |
| M1/P1/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.030001 | 0.029833 | 0.030870 |
| M1/P1/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.029981 | 0.029814 | 0.030847 |
| M1/P1/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.959168 | 0.952904 | 1.307703 |
| M1/P1/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.959124 | 0.952835 | 1.307663 |
| M1/P1/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 0.587930 | 0.488257 | 1.284263 |
| M1/P1/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 0.587900 | 0.488211 | 1.284190 |
| M1/P1/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.069869 | 0.068732 | 0.090204 |
| M1/P1/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.026765 | 0.028803 | 0.051305 |
| M1/P1/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000585 | 0.000557 | 0.000797 |
| M1/P1/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.073359 | 0.070907 | 0.132047 |
| M1/P1/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.146370 | 0.149538 | 0.188495 |
| M1/P1/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.268341 | 0.263255 | 0.371897 |
| M1/P1/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.074866 | 0.074881 | 0.111447 |
| M1/P1/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.022864 | 0.022463 | 0.030765 |
| M1/P1/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000067 | 0.000066 | 0.000084 |
| M1/P1/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 1.576166 | 1.446918 | 2.384528 |
| M1/P1/humaneval/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.040217 | 0.039556 | 0.047429 |
| M1/P1/humaneval/C2C | receiver_local_prefill.cuda_event_s | 完整 | 164 | 164 | 0.040179 | 0.039526 | 0.047399 |
| M1/P1/humaneval/C2C | sender_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.033652 | 0.033293 | 0.035637 |
| M1/P1/humaneval/C2C | sender_prefill.cuda_event_s | 完整 | 164 | 164 | 0.033607 | 0.033227 | 0.035606 |
| M1/P1/humaneval/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.065277 | 0.064973 | 0.067395 |
| M1/P1/humaneval/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.065374 | 0.065066 | 0.067491 |
| M1/P1/humaneval/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.030943 | 0.030857 | 0.031629 |
| M1/P1/humaneval/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 164 | 164 | 0.030917 | 0.030833 | 0.031604 |
| M1/P1/humaneval/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.241225 | 0.230618 | 0.316305 |
| M1/P1/humaneval/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.241165 | 0.230569 | 0.316255 |
| M1/P1/humaneval/C2C | receiver_decode.synchronized_wall_s | 完整 | 164 | 164 | 4.101148 | 1.812352 | 30.418295 |
| M1/P1/humaneval/C2C | receiver_decode.cuda_event_s | 完整 | 164 | 164 | 4.100868 | 1.812247 | 30.417159 |
| M1/P1/humaneval/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 164 | 164 | 0.059241 | 0.058975 | 0.060728 |
| M1/P1/humaneval/C2C | input_assembly_tokenize_s | 完整 | 164 | 164 | 0.001132 | 0.001096 | 0.001455 |
| M1/P1/humaneval/C2C | input_host_to_device_s | 完整 | 164 | 164 | 0.000472 | 0.000442 | 0.000806 |
| M1/P1/humaneval/C2C | sender_device_to_host_s | 完整 | 164 | 164 | 0.008014 | 0.007413 | 0.011964 |
| M1/P1/humaneval/C2C | sender_pack_s | 完整 | 164 | 164 | 0.011968 | 0.009754 | 0.037284 |
| M1/P1/humaneval/C2C | transport_loopback_and_byte_verify_s | 完整 | 164 | 164 | 0.015321 | 0.011073 | 0.040884 |
| M1/P1/humaneval/C2C | receiver_unpack_s | 完整 | 164 | 164 | 0.006978 | 0.006733 | 0.009181 |
| M1/P1/humaneval/C2C | receiver_restore_and_host_to_device_s | 完整 | 164 | 164 | 0.009962 | 0.008757 | 0.014917 |
| M1/P1/humaneval/C2C | output_text_decode_s | 完整 | 164 | 164 | 0.000113 | 0.000089 | 0.000348 |
| M1/P1/humaneval/C2C | hot_pipeline_wall_s | 完整 | 164 | 164 | 4.346201 | 2.053696 | 30.655417 |
| M2/P1/gsm8k/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.053145 | 0.048122 | 0.070632 |
| M2/P1/gsm8k/C2C | receiver_local_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.053115 | 0.048090 | 0.070599 |
| M2/P1/gsm8k/C2C | sender_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.032160 | 0.031804 | 0.034218 |
| M2/P1/gsm8k/C2C | sender_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.032132 | 0.031780 | 0.034193 |
| M2/P1/gsm8k/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.065223 | 0.064813 | 0.068437 |
| M2/P1/gsm8k/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.065239 | 0.064820 | 0.068516 |
| M2/P1/gsm8k/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.039442 | 0.039244 | 0.041148 |
| M2/P1/gsm8k/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.039421 | 0.039219 | 0.041129 |
| M2/P1/gsm8k/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.231609 | 0.228550 | 0.252336 |
| M2/P1/gsm8k/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.231569 | 0.228512 | 0.252294 |
| M2/P1/gsm8k/C2C | receiver_decode.synchronized_wall_s | 完整 | 1319 | 1319 | 4.649295 | 4.240618 | 8.449577 |
| M2/P1/gsm8k/C2C | receiver_decode.cuda_event_s | 完整 | 1319 | 1319 | 4.649224 | 4.240560 | 8.449469 |
| M2/P1/gsm8k/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 1319 | 1319 | 0.058855 | 0.058583 | 0.061492 |
| M2/P1/gsm8k/C2C | input_assembly_tokenize_s | 完整 | 1319 | 1319 | 0.000776 | 0.000755 | 0.000974 |
| M2/P1/gsm8k/C2C | input_host_to_device_s | 完整 | 1319 | 1319 | 0.000431 | 0.000408 | 0.000556 |
| M2/P1/gsm8k/C2C | sender_device_to_host_s | 完整 | 1319 | 1319 | 0.004859 | 0.004749 | 0.006187 |
| M2/P1/gsm8k/C2C | sender_pack_s | 完整 | 1319 | 1319 | 0.006333 | 0.006198 | 0.007700 |
| M2/P1/gsm8k/C2C | transport_loopback_and_byte_verify_s | 完整 | 1319 | 1319 | 0.006606 | 0.006300 | 0.008989 |
| M2/P1/gsm8k/C2C | receiver_unpack_s | 完整 | 1319 | 1319 | 0.005733 | 0.005649 | 0.006374 |
| M2/P1/gsm8k/C2C | receiver_restore_and_host_to_device_s | 完整 | 1319 | 1319 | 0.005853 | 0.005530 | 0.007539 |
| M2/P1/gsm8k/C2C | output_text_decode_s | 完整 | 1319 | 1319 | 0.000106 | 0.000102 | 0.000143 |
| M2/P1/gsm8k/C2C | hot_pipeline_wall_s | 完整 | 1319 | 1319 | 4.883496 | 4.467441 | 8.679197 |
| M2/P1/hotpotqa/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.251352 | 0.252016 | 0.340826 |
| M2/P1/hotpotqa/C2C | receiver_local_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.251320 | 0.251981 | 0.340804 |
| M2/P1/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.056564 | 0.057148 | 0.077275 |
| M2/P1/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.056532 | 0.057122 | 0.077230 |
| M2/P1/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.078416 | 0.076662 | 0.098614 |
| M2/P1/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.078433 | 0.076678 | 0.098627 |
| M2/P1/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.039295 | 0.039134 | 0.040682 |
| M2/P1/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.039275 | 0.039115 | 0.040633 |
| M2/P1/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 1.120888 | 1.104974 | 1.545281 |
| M2/P1/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 1.120844 | 1.104922 | 1.545236 |
| M2/P1/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 0.767779 | 0.750654 | 1.553511 |
| M2/P1/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 0.767747 | 0.750622 | 1.553437 |
| M2/P1/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.070963 | 0.069374 | 0.090894 |
| M2/P1/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.024068 | 0.026057 | 0.050912 |
| M2/P1/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000568 | 0.000548 | 0.000756 |
| M2/P1/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.068856 | 0.064933 | 0.132937 |
| M2/P1/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.150191 | 0.149165 | 0.205356 |
| M2/P1/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.272409 | 0.266725 | 0.380101 |
| M2/P1/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.075632 | 0.072406 | 0.118575 |
| M2/P1/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.023031 | 0.022606 | 0.030935 |
| M2/P1/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000070 | 0.000067 | 0.000082 |
| M2/P1/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 1.915146 | 1.882128 | 2.847264 |
| M2/P1/humaneval/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.053692 | 0.047334 | 0.073915 |
| M2/P1/humaneval/C2C | receiver_local_prefill.cuda_event_s | 完整 | 164 | 164 | 0.053663 | 0.047308 | 0.073883 |
| M2/P1/humaneval/C2C | sender_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.032683 | 0.032484 | 0.034001 |
| M2/P1/humaneval/C2C | sender_prefill.cuda_event_s | 完整 | 164 | 164 | 0.032658 | 0.032459 | 0.033954 |
| M2/P1/humaneval/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.065027 | 0.064829 | 0.067451 |
| M2/P1/humaneval/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.065037 | 0.064838 | 0.067460 |
| M2/P1/humaneval/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.039438 | 0.039389 | 0.040179 |
| M2/P1/humaneval/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 164 | 164 | 0.039415 | 0.039369 | 0.040159 |
| M2/P1/humaneval/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.260973 | 0.244889 | 0.352698 |
| M2/P1/humaneval/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.260927 | 0.244850 | 0.352656 |
| M2/P1/humaneval/C2C | receiver_decode.synchronized_wall_s | 完整 | 164 | 164 | 6.276222 | 5.131725 | 12.506896 |
| M2/P1/humaneval/C2C | receiver_decode.cuda_event_s | 完整 | 164 | 164 | 6.275903 | 5.131461 | 12.506292 |
| M2/P1/humaneval/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 164 | 164 | 0.058340 | 0.058243 | 0.059740 |
| M2/P1/humaneval/C2C | input_assembly_tokenize_s | 完整 | 164 | 164 | 0.001093 | 0.001062 | 0.001434 |
| M2/P1/humaneval/C2C | input_host_to_device_s | 完整 | 164 | 164 | 0.000400 | 0.000394 | 0.000468 |
| M2/P1/humaneval/C2C | sender_device_to_host_s | 完整 | 164 | 164 | 0.007736 | 0.007231 | 0.011824 |
| M2/P1/humaneval/C2C | sender_pack_s | 完整 | 164 | 164 | 0.011776 | 0.009716 | 0.036405 |
| M2/P1/humaneval/C2C | transport_loopback_and_byte_verify_s | 完整 | 164 | 164 | 0.015310 | 0.010702 | 0.041898 |
| M2/P1/humaneval/C2C | receiver_unpack_s | 完整 | 164 | 164 | 0.006972 | 0.006704 | 0.008920 |
| M2/P1/humaneval/C2C | receiver_restore_and_host_to_device_s | 完整 | 164 | 164 | 0.008893 | 0.008134 | 0.013388 |
| M2/P1/humaneval/C2C | output_text_decode_s | 完整 | 164 | 164 | 0.000124 | 0.000115 | 0.000188 |
| M2/P1/humaneval/C2C | hot_pipeline_wall_s | 完整 | 164 | 164 | 6.540563 | 5.379305 | 12.853634 |
| M3/P1/gsm8k/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.046375 | 0.045456 | 0.060167 |
| M3/P1/gsm8k/C2C | receiver_local_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.046345 | 0.045417 | 0.060131 |
| M3/P1/gsm8k/C2C | sender_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.041906 | 0.040815 | 0.046380 |
| M3/P1/gsm8k/C2C | sender_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.041880 | 0.040790 | 0.046331 |
| M3/P1/gsm8k/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.063112 | 0.063156 | 0.064691 |
| M3/P1/gsm8k/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.063119 | 0.063164 | 0.064702 |
| M3/P1/gsm8k/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.029165 | 0.029107 | 0.029938 |
| M3/P1/gsm8k/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.029145 | 0.029084 | 0.029921 |
| M3/P1/gsm8k/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.235567 | 0.234012 | 0.259473 |
| M3/P1/gsm8k/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.235527 | 0.233978 | 0.259432 |
| M3/P1/gsm8k/C2C | receiver_decode.synchronized_wall_s | 完整 | 1319 | 1319 | 4.444569 | 3.032788 | 19.496282 |
| M3/P1/gsm8k/C2C | receiver_decode.cuda_event_s | 完整 | 1319 | 1319 | 4.444541 | 3.032846 | 19.495870 |
| M3/P1/gsm8k/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 1319 | 1319 | 0.057274 | 0.057369 | 0.058830 |
| M3/P1/gsm8k/C2C | input_assembly_tokenize_s | 完整 | 1319 | 1319 | 0.000807 | 0.000789 | 0.001039 |
| M3/P1/gsm8k/C2C | input_host_to_device_s | 完整 | 1319 | 1319 | 0.000447 | 0.000428 | 0.000571 |
| M3/P1/gsm8k/C2C | sender_device_to_host_s | 完整 | 1319 | 1319 | 0.006169 | 0.006045 | 0.007760 |
| M3/P1/gsm8k/C2C | sender_pack_s | 完整 | 1319 | 1319 | 0.007649 | 0.007430 | 0.009363 |
| M3/P1/gsm8k/C2C | transport_loopback_and_byte_verify_s | 完整 | 1319 | 1319 | 0.013088 | 0.012585 | 0.017177 |
| M3/P1/gsm8k/C2C | receiver_unpack_s | 完整 | 1319 | 1319 | 0.007058 | 0.007013 | 0.007771 |
| M3/P1/gsm8k/C2C | receiver_restore_and_host_to_device_s | 完整 | 1319 | 1319 | 0.007218 | 0.006995 | 0.008945 |
| M3/P1/gsm8k/C2C | output_text_decode_s | 完整 | 1319 | 1319 | 0.000109 | 0.000099 | 0.000218 |
| M3/P1/gsm8k/C2C | hot_pipeline_wall_s | 完整 | 1319 | 1319 | 4.682832 | 3.264854 | 19.720624 |
| M3/P1/hotpotqa/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.057134 | 0.057361 | 0.074721 |
| M3/P1/hotpotqa/C2C | receiver_local_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.057104 | 0.057332 | 0.074695 |
| M3/P1/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.246531 | 0.246778 | 0.333972 |
| M3/P1/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.246500 | 0.246747 | 0.333923 |
| M3/P1/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.075391 | 0.074414 | 0.095851 |
| M3/P1/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.075399 | 0.074423 | 0.095861 |
| M3/P1/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.028927 | 0.028846 | 0.029518 |
| M3/P1/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.028908 | 0.028828 | 0.029497 |
| M3/P1/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 1.283274 | 1.271733 | 1.750397 |
| M3/P1/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 1.283225 | 1.271687 | 1.750310 |
| M3/P1/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 1.016030 | 0.679482 | 2.258451 |
| M3/P1/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 1.015999 | 0.679448 | 2.258426 |
| M3/P1/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.068808 | 0.067934 | 0.088770 |
| M3/P1/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.037127 | 0.043315 | 0.067751 |
| M3/P1/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000632 | 0.000592 | 0.000867 |
| M3/P1/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.091894 | 0.088311 | 0.167529 |
| M3/P1/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.182398 | 0.184427 | 0.232430 |
| M3/P1/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.342547 | 0.335878 | 0.476177 |
| M3/P1/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.102131 | 0.099768 | 0.150295 |
| M3/P1/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.028001 | 0.027632 | 0.037249 |
| M3/P1/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000074 | 0.000070 | 0.000099 |
| M3/P1/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 2.338981 | 2.033030 | 3.639630 |
| M3/P1/humaneval/C2C | receiver_local_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.050969 | 0.055802 | 0.060663 |
| M3/P1/humaneval/C2C | receiver_local_prefill.cuda_event_s | 完整 | 164 | 164 | 0.050934 | 0.055763 | 0.060622 |
| M3/P1/humaneval/C2C | sender_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.051608 | 0.045045 | 0.074941 |
| M3/P1/humaneval/C2C | sender_prefill.cuda_event_s | 完整 | 164 | 164 | 0.051579 | 0.045012 | 0.074914 |
| M3/P1/humaneval/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.062783 | 0.062689 | 0.064063 |
| M3/P1/humaneval/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.062791 | 0.062697 | 0.064072 |
| M3/P1/humaneval/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.029012 | 0.028935 | 0.029665 |
| M3/P1/humaneval/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 164 | 164 | 0.028993 | 0.028916 | 0.029646 |
| M3/P1/humaneval/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.297143 | 0.277476 | 0.402330 |
| M3/P1/humaneval/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.297094 | 0.277427 | 0.402282 |
| M3/P1/humaneval/C2C | receiver_decode.synchronized_wall_s | 完整 | 164 | 164 | 8.307078 | 4.292158 | 29.037209 |
| M3/P1/humaneval/C2C | receiver_decode.cuda_event_s | 完整 | 164 | 164 | 8.306834 | 4.292015 | 29.036512 |
| M3/P1/humaneval/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 164 | 164 | 0.056805 | 0.056682 | 0.057981 |
| M3/P1/humaneval/C2C | input_assembly_tokenize_s | 完整 | 164 | 164 | 0.001278 | 0.001252 | 0.001764 |
| M3/P1/humaneval/C2C | input_host_to_device_s | 完整 | 164 | 164 | 0.000514 | 0.000522 | 0.000642 |
| M3/P1/humaneval/C2C | sender_device_to_host_s | 完整 | 164 | 164 | 0.009906 | 0.009305 | 0.015079 |
| M3/P1/humaneval/C2C | sender_pack_s | 完整 | 164 | 164 | 0.017621 | 0.012250 | 0.048023 |
| M3/P1/humaneval/C2C | transport_loopback_and_byte_verify_s | 完整 | 164 | 164 | 0.030798 | 0.023509 | 0.052936 |
| M3/P1/humaneval/C2C | receiver_unpack_s | 完整 | 164 | 164 | 0.008596 | 0.008324 | 0.010604 |
| M3/P1/humaneval/C2C | receiver_restore_and_host_to_device_s | 完整 | 164 | 164 | 0.011479 | 0.010502 | 0.017605 |
| M3/P1/humaneval/C2C | output_text_decode_s | 完整 | 164 | 164 | 0.000158 | 0.000125 | 0.000351 |
| M3/P1/humaneval/C2C | hot_pipeline_wall_s | 完整 | 164 | 164 | 8.608018 | 4.596173 | 29.304652 |

## C 异常及覆盖

| 组合 | 项目 | 数值 |
|---|---|---|
| M1/P1/gsm8k/C2C | input_tokens | {"known": 1319, "missing": 0} |
| M1/P1/gsm8k/C2C | output_tokens | {"known": 1319, "missing": 0} |
| M1/P1/gsm8k/C2C | communication | {"known": 1319, "missing": 0} |
| M1/P1/gsm8k/C2C | hot_pipeline_wall_s | {"known": 1319, "missing": 0} |
| M1/P1/gsm8k/C2C | 全部尝试墙钟 | {"n": 1319, "mean": 11.374570118015706, "p50": 4.102659631986171, "p95": 30.557092759152873} |
| M1/P1/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M1/P1/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M1/P1/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M1/P1/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M1/P1/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 2.066123695767269, "p50": 1.9360835019033402, "p95": 2.9123277002479875} |
| M1/P1/humaneval/C2C | input_tokens | {"known": 164, "missing": 0} |
| M1/P1/humaneval/C2C | output_tokens | {"known": 164, "missing": 0} |
| M1/P1/humaneval/C2C | communication | {"known": 164, "missing": 0} |
| M1/P1/humaneval/C2C | hot_pipeline_wall_s | {"known": 164, "missing": 0} |
| M1/P1/humaneval/C2C | 全部尝试墙钟 | {"n": 164, "mean": 5.005820512463532, "p50": 2.7132061070296913, "p95": 31.337798167183063} |
| M2/P1/gsm8k/C2C | input_tokens | {"known": 1319, "missing": 0} |
| M2/P1/gsm8k/C2C | output_tokens | {"known": 1319, "missing": 0} |
| M2/P1/gsm8k/C2C | communication | {"known": 1319, "missing": 0} |
| M2/P1/gsm8k/C2C | hot_pipeline_wall_s | {"known": 1319, "missing": 0} |
| M2/P1/gsm8k/C2C | 全部尝试墙钟 | {"n": 1319, "mean": 5.153801441360145, "p50": 4.749345175921917, "p95": 8.9562163033057} |
| M2/P1/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M2/P1/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M2/P1/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M2/P1/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M2/P1/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 2.4125946375921843, "p50": 2.3773427340202034, "p95": 3.383340228674933} |
| M2/P1/humaneval/C2C | input_tokens | {"known": 164, "missing": 0} |
| M2/P1/humaneval/C2C | output_tokens | {"known": 164, "missing": 0} |
| M2/P1/humaneval/C2C | communication | {"known": 164, "missing": 0} |
| M2/P1/humaneval/C2C | hot_pipeline_wall_s | {"known": 164, "missing": 0} |
| M2/P1/humaneval/C2C | 全部尝试墙钟 | {"n": 164, "mean": 7.1795276839132764, "p50": 6.015834826393984, "p95": 13.511762454023117} |
| M3/P1/gsm8k/C2C | input_tokens | {"known": 1319, "missing": 0} |
| M3/P1/gsm8k/C2C | output_tokens | {"known": 1319, "missing": 0} |
| M3/P1/gsm8k/C2C | communication | {"known": 1319, "missing": 0} |
| M3/P1/gsm8k/C2C | hot_pipeline_wall_s | {"known": 1319, "missing": 0} |
| M3/P1/gsm8k/C2C | 全部尝试墙钟 | {"n": 1319, "mean": 4.935946104267839, "p50": 3.5225212411023676, "p95": 19.972340391296} |
| M3/P1/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M3/P1/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M3/P1/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M3/P1/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M3/P1/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 2.7954577955656927, "p50": 2.4935546920169145, "p95": 4.115130513487383} |
| M3/P1/humaneval/C2C | input_tokens | {"known": 164, "missing": 0} |
| M3/P1/humaneval/C2C | output_tokens | {"known": 164, "missing": 0} |
| M3/P1/humaneval/C2C | communication | {"known": 164, "missing": 0} |
| M3/P1/humaneval/C2C | hot_pipeline_wall_s | {"known": 164, "missing": 0} |
| M3/P1/humaneval/C2C | 全部尝试墙钟 | {"n": 164, "mean": 9.227867163242147, "p50": 5.219682349008508, "p95": 29.9124683670816} |

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
| M1 | protocol | P1 |
| M1 | path | c2c |
| M1 | adaptation | P2双向补齐；P3/P4单向补齐；补齐后重建完整对齐输入 |
| M1 | 代码评分运行时 | {"python": "3.11.17 (main, Nov  3 2026, 23:59:51) [GCC 11.4.0]", "network_isolated": true, "project_paths_hidden": true} |
| M1 | 代码评分资源限制 | {"wall_s": 3, "cpu_s": 4, "memory_bytes": 2147483648, "outer_wall_s": 8} |
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
| M2 | protocol | P1 |
| M2 | path | c2c |
| M2 | adaptation | P2双向补齐；P3/P4单向补齐；补齐后重建完整对齐输入 |
| M2 | 代码评分运行时 | {"python": "3.11.17 (main, Nov  3 2026, 23:59:51) [GCC 11.4.0]", "network_isolated": true, "project_paths_hidden": true} |
| M2 | 代码评分资源限制 | {"wall_s": 3, "cpu_s": 4, "memory_bytes": 2147483648, "outer_wall_s": 8} |
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
| M3 | protocol | P1 |
| M3 | path | c2c |
| M3 | adaptation | P2双向补齐；P3/P4单向补齐；补齐后重建完整对齐输入 |
| M3 | 代码评分运行时 | {"python": "3.11.17 (main, Nov  3 2026, 23:59:51) [GCC 11.4.0]", "network_isolated": true, "project_paths_hidden": true} |
| M3 | 代码评分资源限制 | {"wall_s": 3, "cpu_s": 4, "memory_bytes": 2147483648, "outer_wall_s": 8} |

## E 通信

| 组合 | 字段 | n | N | 总字节 | 均值字节 | P50 | P95 |
|---|---|---|---|---|---|---|---|
| M1/P1/gsm8k/C2C | raw_kv_bytes | 1319 | 1319 | 20468482048 | 15518181.992418 | 15024128.000000 | 20529152.000000 |
| M1/P1/gsm8k/C2C | serialized_payload_bytes | 1319 | 1319 | 20489663933 | 15534241.040940 | 15040187.000000 | 20545211.000000 |
| M1/P1/gsm8k/C2C | metadata_and_container_bytes | 1319 | 1319 | 21181885 | 16059.048522 | 16059.000000 | 16059.000000 |
| M1/P1/gsm8k/C2C | framing_bytes | 1319 | 1319 | 10552 | 8.000000 | 8.000000 | 8.000000 |
| M1/P1/gsm8k/C2C | actual_sent_bytes | 1319 | 1319 | 20489674485 | 15534249.040940 | 15040195.000000 | 20545219.000000 |
| M1/P1/gsm8k/C2C | actual_received_bytes | 1319 | 1319 | 20489674485 | 15534249.040940 | 15040195.000000 | 20545219.000000 |
| M1/P1/gsm8k/C2C | generated_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P1/gsm8k/C2C | supplemental_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P1/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1277447585792 | 172511490.316273 | 168935424.000000 | 242198118.400000 |
| M1/P1/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1277567919647 | 172527740.668062 | 168951675.000000 | 242214369.400000 |
| M1/P1/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 120333855 | 16250.351789 | 16251.000000 | 16251.000000 |
| M1/P1/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 59240 | 8.000000 | 8.000000 | 8.000000 |
| M1/P1/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1277567978887 | 172527748.668062 | 168951683.000000 | 242214377.400000 |
| M1/P1/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1277567978887 | 172527748.668062 | 168951683.000000 | 242214377.400000 |
| M1/P1/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P1/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P1/humaneval/C2C | raw_kv_bytes | 164 | 164 | 4555980800 | 27780370.731707 | 25919488.000000 | 43776409.600000 |
| M1/P1/humaneval/C2C | serialized_payload_bytes | 164 | 164 | 4558617612 | 27796448.853659 | 25935547.000000 | 43792532.600000 |
| M1/P1/humaneval/C2C | metadata_and_container_bytes | 164 | 164 | 2636812 | 16078.121951 | 16059.000000 | 16123.000000 |
| M1/P1/humaneval/C2C | framing_bytes | 164 | 164 | 1312 | 8.000000 | 8.000000 | 8.000000 |
| M1/P1/humaneval/C2C | actual_sent_bytes | 164 | 164 | 4558618924 | 27796456.853659 | 25935555.000000 | 43792540.600000 |
| M1/P1/humaneval/C2C | actual_received_bytes | 164 | 164 | 4558618924 | 27796456.853659 | 25935555.000000 | 43792540.600000 |
| M1/P1/humaneval/C2C | generated_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P1/humaneval/C2C | supplemental_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P1/gsm8k/C2C | raw_kv_bytes | 1319 | 1319 | 20468482048 | 15518181.992418 | 15024128.000000 | 20529152.000000 |
| M2/P1/gsm8k/C2C | serialized_payload_bytes | 1319 | 1319 | 20489663933 | 15534241.040940 | 15040187.000000 | 20545211.000000 |
| M2/P1/gsm8k/C2C | metadata_and_container_bytes | 1319 | 1319 | 21181885 | 16059.048522 | 16059.000000 | 16059.000000 |
| M2/P1/gsm8k/C2C | framing_bytes | 1319 | 1319 | 10552 | 8.000000 | 8.000000 | 8.000000 |
| M2/P1/gsm8k/C2C | actual_sent_bytes | 1319 | 1319 | 20489674485 | 15534249.040940 | 15040195.000000 | 20545219.000000 |
| M2/P1/gsm8k/C2C | actual_received_bytes | 1319 | 1319 | 20489674485 | 15534249.040940 | 15040195.000000 | 20545219.000000 |
| M2/P1/gsm8k/C2C | generated_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P1/gsm8k/C2C | supplemental_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P1/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1277447585792 | 172511490.316273 | 168935424.000000 | 242198118.400000 |
| M2/P1/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1277567919647 | 172527740.668062 | 168951675.000000 | 242214369.400000 |
| M2/P1/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 120333855 | 16250.351789 | 16251.000000 | 16251.000000 |
| M2/P1/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 59240 | 8.000000 | 8.000000 | 8.000000 |
| M2/P1/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1277567978887 | 172527748.668062 | 168951683.000000 | 242214377.400000 |
| M2/P1/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1277567978887 | 172527748.668062 | 168951683.000000 | 242214377.400000 |
| M2/P1/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P1/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P1/humaneval/C2C | raw_kv_bytes | 164 | 164 | 4555980800 | 27780370.731707 | 25919488.000000 | 43776409.600000 |
| M2/P1/humaneval/C2C | serialized_payload_bytes | 164 | 164 | 4558617612 | 27796448.853659 | 25935547.000000 | 43792532.600000 |
| M2/P1/humaneval/C2C | metadata_and_container_bytes | 164 | 164 | 2636812 | 16078.121951 | 16059.000000 | 16123.000000 |
| M2/P1/humaneval/C2C | framing_bytes | 164 | 164 | 1312 | 8.000000 | 8.000000 | 8.000000 |
| M2/P1/humaneval/C2C | actual_sent_bytes | 164 | 164 | 4558618924 | 27796456.853659 | 25935555.000000 | 43792540.600000 |
| M2/P1/humaneval/C2C | actual_received_bytes | 164 | 164 | 4558618924 | 27796456.853659 | 25935555.000000 | 43792540.600000 |
| M2/P1/humaneval/C2C | generated_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P1/humaneval/C2C | supplemental_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P1/gsm8k/C2C | raw_kv_bytes | 1319 | 1319 | 26316619776 | 19951948.275967 | 19316736.000000 | 26394624.000000 |
| M3/P1/gsm8k/C2C | serialized_payload_bytes | 1319 | 1319 | 26343731885 | 19972503.324488 | 19337291.000000 | 26415179.000000 |
| M3/P1/gsm8k/C2C | metadata_and_container_bytes | 1319 | 1319 | 27112109 | 20555.048522 | 20555.000000 | 20555.000000 |
| M3/P1/gsm8k/C2C | framing_bytes | 1319 | 1319 | 10552 | 8.000000 | 8.000000 | 8.000000 |
| M3/P1/gsm8k/C2C | actual_sent_bytes | 1319 | 1319 | 26343742437 | 19972511.324488 | 19337299.000000 | 26415187.000000 |
| M3/P1/gsm8k/C2C | actual_received_bytes | 1319 | 1319 | 26343742437 | 19972511.324488 | 19337299.000000 | 26415187.000000 |
| M3/P1/gsm8k/C2C | generated_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P1/gsm8k/C2C | supplemental_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P1/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1642432610304 | 221800487.549494 | 217202688.000000 | 311397580.800000 |
| M3/P1/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1642586237039 | 221821233.901283 | 217223435.000000 | 311418327.800000 |
| M3/P1/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 153626735 | 20746.351789 | 20747.000000 | 20747.000000 |
| M3/P1/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 59240 | 8.000000 | 8.000000 | 8.000000 |
| M3/P1/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1642586296279 | 221821241.901283 | 217223443.000000 | 311418335.800000 |
| M3/P1/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1642586296279 | 221821241.901283 | 217223443.000000 | 311418335.800000 |
| M3/P1/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P1/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P1/humaneval/C2C | raw_kv_bytes | 164 | 164 | 5857689600 | 35717619.512195 | 33325056.000000 | 56283955.200000 |
| M3/P1/humaneval/C2C | serialized_payload_bytes | 164 | 164 | 5861063756 | 35738193.634146 | 33345611.000000 | 56304574.200000 |
| M3/P1/humaneval/C2C | metadata_and_container_bytes | 164 | 164 | 3374156 | 20574.121951 | 20555.000000 | 20619.000000 |
| M3/P1/humaneval/C2C | framing_bytes | 164 | 164 | 1312 | 8.000000 | 8.000000 | 8.000000 |
| M3/P1/humaneval/C2C | actual_sent_bytes | 164 | 164 | 5861065068 | 35738201.634146 | 33345619.000000 | 56304582.200000 |
| M3/P1/humaneval/C2C | actual_received_bytes | 164 | 164 | 5861065068 | 35738201.634146 | 33345619.000000 | 56304582.200000 |
| M3/P1/humaneval/C2C | generated_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P1/humaneval/C2C | supplemental_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |

| 组合 | K/V | n | 层数 | dtype | 序列长度[min,max] | 其余维度(batch,heads,head_dim) |
|---|---|---|---|---|---|---|
| M1/P1/gsm8k/C2C | keys | 1319 | [28] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M1/P1/gsm8k/C2C | values | 1319 | [28] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M1/P1/hotpotqa/C2C | keys | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M1/P1/hotpotqa/C2C | values | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M1/P1/humaneval/C2C | keys | 164 | [28] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M1/P1/humaneval/C2C | values | 164 | [28] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M2/P1/gsm8k/C2C | keys | 1319 | [28] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M2/P1/gsm8k/C2C | values | 1319 | [28] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M2/P1/hotpotqa/C2C | keys | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M2/P1/hotpotqa/C2C | values | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M2/P1/humaneval/C2C | keys | 164 | [28] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M2/P1/humaneval/C2C | values | 164 | [28] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M3/P1/gsm8k/C2C | keys | 1319 | [36] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M3/P1/gsm8k/C2C | values | 1319 | [36] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M3/P1/hotpotqa/C2C | keys | 7405 | [36] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M3/P1/hotpotqa/C2C | values | 7405 | [36] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M3/P1/humaneval/C2C | keys | 164 | [36] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M3/P1/humaneval/C2C | values | 164 | [36] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |

## F GPU竞争观察分项

原始总体耗时保持；以下分列观测到竞争、未观测到竞争及未覆盖监测的样本。采样间隔5秒，未观测到竞争不等于连续独占证明。

| 组合 | 监测分类 | 阶段 | n | 均值s | P50s | P95s |
|---|---|---|---|---|---|---|
| M1/gsm8k | unobserved | receiver_local_prefill.synchronized_wall_s | 1319 | 0.049856 | 0.052977 | 0.058829 |
| M1/gsm8k | unobserved | receiver_local_prefill.cuda_event_s | 1319 | 0.049826 | 0.052948 | 0.058794 |
| M1/gsm8k | unobserved | sender_prefill.synchronized_wall_s | 1319 | 0.032424 | 0.031564 | 0.036031 |
| M1/gsm8k | unobserved | sender_prefill.cuda_event_s | 1319 | 0.032398 | 0.031539 | 0.035999 |
| M1/gsm8k | unobserved | receiver_conversion_fusion_inclusive.cuda_event_s | 1319 | 0.062916 | 0.063010 | 0.064431 |
| M1/gsm8k | unobserved | receiver_conversion_fusion_inclusive.synchronized_wall_s | 1319 | 0.062923 | 0.063017 | 0.064440 |
| M1/gsm8k | unobserved | receiver_final_prompt_prefill.synchronized_wall_s | 1319 | 0.029828 | 0.029767 | 0.030554 |
| M1/gsm8k | unobserved | receiver_final_prompt_prefill.cuda_event_s | 1319 | 0.029808 | 0.029746 | 0.030537 |
| M1/gsm8k | unobserved | prefill_pipeline_inclusive.synchronized_wall_s | 1319 | 0.215022 | 0.215584 | 0.231079 |
| M1/gsm8k | unobserved | prefill_pipeline_inclusive.cuda_event_s | 1319 | 0.214983 | 0.215544 | 0.231040 |
| M1/gsm8k | unobserved | receiver_decode.synchronized_wall_s | 1319 | 10.899367 | 3.628268 | 30.062252 |
| M1/gsm8k | unobserved | receiver_decode.cuda_event_s | 1319 | 10.899242 | 3.628211 | 30.061933 |
| M1/gsm8k | unobserved | receiver_conversion_fusion_modules_nested.cuda_event_s | 1319 | 0.057523 | 0.057675 | 0.058936 |
| M1/hotpotqa | unobserved | receiver_local_prefill.synchronized_wall_s | 7405 | 0.109520 | 0.110163 | 0.147574 |
| M1/hotpotqa | unobserved | receiver_local_prefill.cuda_event_s | 7405 | 0.109491 | 0.110122 | 0.147539 |
| M1/hotpotqa | unobserved | sender_prefill.synchronized_wall_s | 7405 | 0.055238 | 0.055891 | 0.074183 |
| M1/hotpotqa | unobserved | sender_prefill.cuda_event_s | 7405 | 0.055208 | 0.055862 | 0.074155 |
| M1/hotpotqa | unobserved | receiver_conversion_fusion_inclusive.cuda_event_s | 7405 | 0.076071 | 0.074699 | 0.096760 |
| M1/hotpotqa | unobserved | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7405 | 0.076089 | 0.074714 | 0.096770 |
| M1/hotpotqa | unobserved | receiver_final_prompt_prefill.synchronized_wall_s | 7405 | 0.030001 | 0.029833 | 0.030870 |
| M1/hotpotqa | unobserved | receiver_final_prompt_prefill.cuda_event_s | 7405 | 0.029981 | 0.029814 | 0.030847 |
| M1/hotpotqa | unobserved | prefill_pipeline_inclusive.synchronized_wall_s | 7405 | 0.959168 | 0.952904 | 1.307703 |
| M1/hotpotqa | unobserved | prefill_pipeline_inclusive.cuda_event_s | 7405 | 0.959124 | 0.952835 | 1.307663 |
| M1/hotpotqa | unobserved | receiver_decode.synchronized_wall_s | 7405 | 0.587930 | 0.488257 | 1.284263 |
| M1/hotpotqa | unobserved | receiver_decode.cuda_event_s | 7405 | 0.587900 | 0.488211 | 1.284190 |
| M1/hotpotqa | unobserved | receiver_conversion_fusion_modules_nested.cuda_event_s | 7405 | 0.069869 | 0.068732 | 0.090204 |
| M1/humaneval | unobserved | receiver_local_prefill.synchronized_wall_s | 164 | 0.040217 | 0.039556 | 0.047429 |
| M1/humaneval | unobserved | receiver_local_prefill.cuda_event_s | 164 | 0.040179 | 0.039526 | 0.047399 |
| M1/humaneval | unobserved | sender_prefill.synchronized_wall_s | 164 | 0.033652 | 0.033293 | 0.035637 |
| M1/humaneval | unobserved | sender_prefill.cuda_event_s | 164 | 0.033607 | 0.033227 | 0.035606 |
| M1/humaneval | unobserved | receiver_conversion_fusion_inclusive.cuda_event_s | 164 | 0.065277 | 0.064973 | 0.067395 |
| M1/humaneval | unobserved | receiver_conversion_fusion_inclusive.synchronized_wall_s | 164 | 0.065374 | 0.065066 | 0.067491 |
| M1/humaneval | unobserved | receiver_final_prompt_prefill.synchronized_wall_s | 164 | 0.030943 | 0.030857 | 0.031629 |
| M1/humaneval | unobserved | receiver_final_prompt_prefill.cuda_event_s | 164 | 0.030917 | 0.030833 | 0.031604 |
| M1/humaneval | unobserved | prefill_pipeline_inclusive.synchronized_wall_s | 164 | 0.241225 | 0.230618 | 0.316305 |
| M1/humaneval | unobserved | prefill_pipeline_inclusive.cuda_event_s | 164 | 0.241165 | 0.230569 | 0.316255 |
| M1/humaneval | unobserved | receiver_decode.synchronized_wall_s | 164 | 4.101148 | 1.812352 | 30.418295 |
| M1/humaneval | unobserved | receiver_decode.cuda_event_s | 164 | 4.100868 | 1.812247 | 30.417159 |
| M1/humaneval | unobserved | receiver_conversion_fusion_modules_nested.cuda_event_s | 164 | 0.059241 | 0.058975 | 0.060728 |
| M2/gsm8k | unobserved | receiver_local_prefill.synchronized_wall_s | 370 | 0.057255 | 0.055762 | 0.070939 |
| M2/gsm8k | unobserved | receiver_local_prefill.cuda_event_s | 370 | 0.057224 | 0.055739 | 0.070904 |
| M2/gsm8k | unobserved | sender_prefill.synchronized_wall_s | 370 | 0.031721 | 0.031343 | 0.033861 |
| M2/gsm8k | unobserved | sender_prefill.cuda_event_s | 370 | 0.031694 | 0.031321 | 0.033828 |
| M2/gsm8k | unobserved | receiver_conversion_fusion_inclusive.cuda_event_s | 370 | 0.064674 | 0.064262 | 0.067714 |
| M2/gsm8k | unobserved | receiver_conversion_fusion_inclusive.synchronized_wall_s | 370 | 0.064688 | 0.064276 | 0.067760 |
| M2/gsm8k | unobserved | receiver_final_prompt_prefill.synchronized_wall_s | 370 | 0.039109 | 0.038843 | 0.041133 |
| M2/gsm8k | unobserved | receiver_final_prompt_prefill.cuda_event_s | 370 | 0.039086 | 0.038824 | 0.041088 |
| M2/gsm8k | unobserved | prefill_pipeline_inclusive.synchronized_wall_s | 370 | 0.234238 | 0.233096 | 0.254156 |
| M2/gsm8k | unobserved | prefill_pipeline_inclusive.cuda_event_s | 370 | 0.234198 | 0.233060 | 0.254113 |
| M2/gsm8k | unobserved | receiver_decode.synchronized_wall_s | 370 | 4.669110 | 4.123581 | 8.446914 |
| M2/gsm8k | unobserved | receiver_decode.cuda_event_s | 370 | 4.669024 | 4.123506 | 8.446791 |
| M2/gsm8k | unobserved | receiver_conversion_fusion_modules_nested.cuda_event_s | 370 | 0.058374 | 0.058107 | 0.061343 |
| M2/gsm8k | contended | receiver_local_prefill.synchronized_wall_s | 118 | 0.050510 | 0.048432 | 0.061570 |
| M2/gsm8k | contended | receiver_local_prefill.cuda_event_s | 118 | 0.050471 | 0.048403 | 0.061534 |
| M2/gsm8k | contended | sender_prefill.synchronized_wall_s | 118 | 0.033454 | 0.032778 | 0.039239 |
| M2/gsm8k | contended | sender_prefill.cuda_event_s | 118 | 0.033396 | 0.032693 | 0.039123 |
| M2/gsm8k | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 118 | 0.068579 | 0.067090 | 0.075922 |
| M2/gsm8k | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 118 | 0.068668 | 0.067226 | 0.076006 |
| M2/gsm8k | contended | receiver_final_prompt_prefill.synchronized_wall_s | 118 | 0.040852 | 0.040299 | 0.043093 |
| M2/gsm8k | contended | receiver_final_prompt_prefill.cuda_event_s | 118 | 0.040827 | 0.040278 | 0.043073 |
| M2/gsm8k | contended | prefill_pipeline_inclusive.synchronized_wall_s | 118 | 0.237930 | 0.233051 | 0.261526 |
| M2/gsm8k | contended | prefill_pipeline_inclusive.cuda_event_s | 118 | 0.237877 | 0.233012 | 0.261450 |
| M2/gsm8k | contended | receiver_decode.synchronized_wall_s | 118 | 4.738628 | 4.475540 | 7.729152 |
| M2/gsm8k | contended | receiver_decode.cuda_event_s | 118 | 4.738525 | 4.475262 | 7.729047 |
| M2/gsm8k | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 118 | 0.061501 | 0.060446 | 0.065789 |
| M2/gsm8k | no_contention_observed | receiver_local_prefill.synchronized_wall_s | 831 | 0.051688 | 0.047345 | 0.070860 |
| M2/gsm8k | no_contention_observed | receiver_local_prefill.cuda_event_s | 831 | 0.051661 | 0.047319 | 0.070828 |
| M2/gsm8k | no_contention_observed | sender_prefill.synchronized_wall_s | 831 | 0.032171 | 0.031831 | 0.034023 |
| M2/gsm8k | no_contention_observed | sender_prefill.cuda_event_s | 831 | 0.032147 | 0.031809 | 0.033997 |
| M2/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 831 | 0.064991 | 0.064860 | 0.066658 |
| M2/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 831 | 0.064998 | 0.064867 | 0.066665 |
| M2/gsm8k | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 831 | 0.039390 | 0.039280 | 0.040840 |
| M2/gsm8k | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 831 | 0.039371 | 0.039261 | 0.040819 |
| M2/gsm8k | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 831 | 0.229540 | 0.226577 | 0.249283 |
| M2/gsm8k | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 831 | 0.229503 | 0.226542 | 0.249240 |
| M2/gsm8k | no_contention_observed | receiver_decode.synchronized_wall_s | 831 | 4.627788 | 4.235488 | 8.623027 |
| M2/gsm8k | no_contention_observed | receiver_decode.cuda_event_s | 831 | 4.627728 | 4.235428 | 8.622928 |
| M2/gsm8k | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 831 | 0.058694 | 0.058634 | 0.060277 |
| M2/hotpotqa | no_contention_observed | receiver_local_prefill.synchronized_wall_s | 6689 | 0.248902 | 0.250979 | 0.338112 |
| M2/hotpotqa | no_contention_observed | receiver_local_prefill.cuda_event_s | 6689 | 0.248872 | 0.250954 | 0.338080 |
| M2/hotpotqa | no_contention_observed | sender_prefill.synchronized_wall_s | 6689 | 0.056004 | 0.056999 | 0.074888 |
| M2/hotpotqa | no_contention_observed | sender_prefill.cuda_event_s | 6689 | 0.055976 | 0.056969 | 0.074857 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 6689 | 0.077693 | 0.076393 | 0.098266 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 6689 | 0.077701 | 0.076399 | 0.098280 |
| M2/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 6689 | 0.039152 | 0.039066 | 0.040092 |
| M2/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 6689 | 0.039133 | 0.039047 | 0.040074 |
| M2/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 6689 | 1.114505 | 1.101558 | 1.532390 |
| M2/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 6689 | 1.114464 | 1.101526 | 1.532334 |
| M2/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 6689 | 0.765192 | 0.739382 | 1.552903 |
| M2/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 6689 | 0.765164 | 0.739351 | 1.552868 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 6689 | 0.070427 | 0.069169 | 0.090652 |
| M2/hotpotqa | contended | receiver_local_prefill.synchronized_wall_s | 716 | 0.274239 | 0.271460 | 0.380423 |
| M2/hotpotqa | contended | receiver_local_prefill.cuda_event_s | 716 | 0.274185 | 0.271416 | 0.380370 |
| M2/hotpotqa | contended | sender_prefill.synchronized_wall_s | 716 | 0.061803 | 0.062074 | 0.084448 |
| M2/hotpotqa | contended | sender_prefill.cuda_event_s | 716 | 0.061728 | 0.062037 | 0.084348 |
| M2/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 716 | 0.085175 | 0.083697 | 0.109713 |
| M2/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 716 | 0.085272 | 0.083839 | 0.109804 |
| M2/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 716 | 0.040631 | 0.040029 | 0.043175 |
| M2/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 716 | 0.040601 | 0.040000 | 0.043153 |
| M2/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 716 | 1.180523 | 1.152253 | 1.633412 |
| M2/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 716 | 1.180450 | 1.152196 | 1.633351 |
| M2/hotpotqa | contended | receiver_decode.synchronized_wall_s | 716 | 0.791947 | 0.792989 | 1.554240 |
| M2/hotpotqa | contended | receiver_decode.cuda_event_s | 716 | 0.791879 | 0.792941 | 1.554067 |
| M2/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 716 | 0.075968 | 0.074716 | 0.098911 |
| M2/humaneval | no_contention_observed | receiver_local_prefill.synchronized_wall_s | 164 | 0.053692 | 0.047334 | 0.073915 |
| M2/humaneval | no_contention_observed | receiver_local_prefill.cuda_event_s | 164 | 0.053663 | 0.047308 | 0.073883 |
| M2/humaneval | no_contention_observed | sender_prefill.synchronized_wall_s | 164 | 0.032683 | 0.032484 | 0.034001 |
| M2/humaneval | no_contention_observed | sender_prefill.cuda_event_s | 164 | 0.032658 | 0.032459 | 0.033954 |
| M2/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 164 | 0.065027 | 0.064829 | 0.067451 |
| M2/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 164 | 0.065037 | 0.064838 | 0.067460 |
| M2/humaneval | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 164 | 0.039438 | 0.039389 | 0.040179 |
| M2/humaneval | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 164 | 0.039415 | 0.039369 | 0.040159 |
| M2/humaneval | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 164 | 0.260973 | 0.244889 | 0.352698 |
| M2/humaneval | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 164 | 0.260927 | 0.244850 | 0.352656 |
| M2/humaneval | no_contention_observed | receiver_decode.synchronized_wall_s | 164 | 6.276222 | 5.131725 | 12.506896 |
| M2/humaneval | no_contention_observed | receiver_decode.cuda_event_s | 164 | 6.275903 | 5.131461 | 12.506292 |
| M2/humaneval | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 164 | 0.058340 | 0.058243 | 0.059740 |
| M3/gsm8k | no_contention_observed | receiver_local_prefill.synchronized_wall_s | 1313 | 0.046397 | 0.045464 | 0.060142 |
| M3/gsm8k | no_contention_observed | receiver_local_prefill.cuda_event_s | 1313 | 0.046367 | 0.045436 | 0.060103 |
| M3/gsm8k | no_contention_observed | sender_prefill.synchronized_wall_s | 1313 | 0.041905 | 0.040810 | 0.046393 |
| M3/gsm8k | no_contention_observed | sender_prefill.cuda_event_s | 1313 | 0.041879 | 0.040788 | 0.046350 |
| M3/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 1313 | 0.063107 | 0.063152 | 0.064672 |
| M3/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 1313 | 0.063113 | 0.063160 | 0.064676 |
| M3/gsm8k | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 1313 | 0.029165 | 0.029107 | 0.029937 |
| M3/gsm8k | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 1313 | 0.029145 | 0.029084 | 0.029920 |
| M3/gsm8k | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 1313 | 0.235591 | 0.234067 | 0.259505 |
| M3/gsm8k | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 1313 | 0.235552 | 0.234032 | 0.259463 |
| M3/gsm8k | no_contention_observed | receiver_decode.synchronized_wall_s | 1313 | 4.384293 | 3.014212 | 11.129672 |
| M3/gsm8k | no_contention_observed | receiver_decode.cuda_event_s | 1313 | 4.384266 | 3.014062 | 11.129723 |
| M3/gsm8k | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 1313 | 0.057270 | 0.057365 | 0.058799 |
| M3/gsm8k | contended | receiver_local_prefill.synchronized_wall_s | 6 | 0.041513 | 0.037263 | 0.061128 |
| M3/gsm8k | contended | receiver_local_prefill.cuda_event_s | 6 | 0.041485 | 0.037237 | 0.061086 |
| M3/gsm8k | contended | sender_prefill.synchronized_wall_s | 6 | 0.042120 | 0.041679 | 0.044234 |
| M3/gsm8k | contended | sender_prefill.cuda_event_s | 6 | 0.042093 | 0.041651 | 0.044207 |
| M3/gsm8k | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 6 | 0.064289 | 0.064200 | 0.065708 |
| M3/gsm8k | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 6 | 0.064322 | 0.064245 | 0.065776 |
| M3/gsm8k | contended | receiver_final_prompt_prefill.synchronized_wall_s | 6 | 0.029167 | 0.029093 | 0.029878 |
| M3/gsm8k | contended | receiver_final_prompt_prefill.cuda_event_s | 6 | 0.029149 | 0.029076 | 0.029859 |
| M3/gsm8k | contended | prefill_pipeline_inclusive.synchronized_wall_s | 6 | 0.230184 | 0.228074 | 0.250225 |
| M3/gsm8k | contended | prefill_pipeline_inclusive.cuda_event_s | 6 | 0.230147 | 0.228038 | 0.250178 |
| M3/gsm8k | contended | receiver_decode.synchronized_wall_s | 6 | 17.634997 | 19.325819 | 29.920675 |
| M3/gsm8k | contended | receiver_decode.cuda_event_s | 6 | 17.634857 | 19.325411 | 29.920666 |
| M3/gsm8k | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 6 | 0.058208 | 0.058253 | 0.059382 |
| M3/hotpotqa | no_contention_observed | receiver_local_prefill.synchronized_wall_s | 7402 | 0.057135 | 0.057362 | 0.074721 |
| M3/hotpotqa | no_contention_observed | receiver_local_prefill.cuda_event_s | 7402 | 0.057106 | 0.057333 | 0.074696 |
| M3/hotpotqa | no_contention_observed | sender_prefill.synchronized_wall_s | 7402 | 0.246532 | 0.246782 | 0.333977 |
| M3/hotpotqa | no_contention_observed | sender_prefill.cuda_event_s | 7402 | 0.246501 | 0.246752 | 0.333923 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7402 | 0.075391 | 0.074414 | 0.095852 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7402 | 0.075399 | 0.074425 | 0.095861 |
| M3/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7402 | 0.028926 | 0.028846 | 0.029515 |
| M3/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7402 | 0.028908 | 0.028828 | 0.029495 |
| M3/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7402 | 1.283304 | 1.271745 | 1.750412 |
| M3/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7402 | 1.283256 | 1.271699 | 1.750319 |
| M3/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7402 | 1.015427 | 0.679516 | 2.254817 |
| M3/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7402 | 1.015396 | 0.679483 | 2.254773 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7402 | 0.068808 | 0.067935 | 0.088771 |
| M3/hotpotqa | contended | receiver_local_prefill.synchronized_wall_s | 3 | 0.053764 | 0.049228 | 0.064519 |
| M3/hotpotqa | contended | receiver_local_prefill.cuda_event_s | 3 | 0.053603 | 0.048798 | 0.064449 |
| M3/hotpotqa | contended | sender_prefill.synchronized_wall_s | 3 | 0.244560 | 0.230416 | 0.279986 |
| M3/hotpotqa | contended | sender_prefill.cuda_event_s | 3 | 0.244313 | 0.230000 | 0.279743 |
| M3/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 3 | 0.074478 | 0.069906 | 0.083317 |
| M3/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 3 | 0.074562 | 0.069995 | 0.083401 |
| M3/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 3 | 0.029457 | 0.029632 | 0.029664 |
| M3/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 3 | 0.029436 | 0.029610 | 0.029644 |
| M3/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 3 | 1.206985 | 1.195344 | 1.286542 |
| M3/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 3 | 1.206923 | 1.195227 | 1.286488 |
| M3/hotpotqa | contended | receiver_decode.synchronized_wall_s | 3 | 2.504153 | 0.669961 | 5.656452 |
| M3/hotpotqa | contended | receiver_decode.cuda_event_s | 3 | 2.504072 | 0.669815 | 5.656367 |
| M3/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 3 | 0.066750 | 0.061635 | 0.075694 |
| M3/humaneval | no_contention_observed | receiver_local_prefill.synchronized_wall_s | 164 | 0.050969 | 0.055802 | 0.060663 |
| M3/humaneval | no_contention_observed | receiver_local_prefill.cuda_event_s | 164 | 0.050934 | 0.055763 | 0.060622 |
| M3/humaneval | no_contention_observed | sender_prefill.synchronized_wall_s | 164 | 0.051608 | 0.045045 | 0.074941 |
| M3/humaneval | no_contention_observed | sender_prefill.cuda_event_s | 164 | 0.051579 | 0.045012 | 0.074914 |
| M3/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 164 | 0.062783 | 0.062689 | 0.064063 |
| M3/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 164 | 0.062791 | 0.062697 | 0.064072 |
| M3/humaneval | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 164 | 0.029012 | 0.028935 | 0.029665 |
| M3/humaneval | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 164 | 0.028993 | 0.028916 | 0.029646 |
| M3/humaneval | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 164 | 0.297143 | 0.277476 | 0.402330 |
| M3/humaneval | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 164 | 0.297094 | 0.277427 | 0.402282 |
| M3/humaneval | no_contention_observed | receiver_decode.synchronized_wall_s | 164 | 8.307078 | 4.292158 | 29.037209 |
| M3/humaneval | no_contention_observed | receiver_decode.cuda_event_s | 164 | 8.306834 | 4.292015 | 29.036512 |
| M3/humaneval | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 164 | 0.056805 | 0.056682 | 0.057981 |

## 附录：口径与证据

- 本报告统计P1的C2C路径；协议与路径分别汇总。
- 本轮Receiver输出上限为1024；T2T沿其既定预算，成本比较同时列出实际输出token数。
- 数学首个####正则、问答整段EM/F1、代码原样补全；OOM/输入容量失败计0，触顶按实际前缀正常评分，固定分母不删除失败题。
- 质量与配对差值均为10000次seed42 percentile bootstrap；配对按同方向/协议/任务/ID及明确的基线路径，完整覆盖规定视图。
- 未测项保持未知；异常部分成本单列；inclusive/nested计时不能相加，参数联合模块去重计一次。
- 通信分列原始KV、补传原文、序列化payload、metadata及每包8字节帧；P2 C2C合计两个方向的补传。逐包方向记录在 supplemental_transfers 中。计时拓扑为同机TCP回环。
- P2–P4先记录Receiver初始Prefill，再记录补齐后的完整输入重建；P2 C2C另记录Sender初始与重建Prefill。完整重建保留所有原始任务信息。没有文本生成消息、筛选、池化或广播。
- GPU用CUDA Event与同步墙钟，CPU操作用墙钟。每任务3条合成预热、每条8tokens；每正式题单次生成。快照观测开销保留，不扣估计常数。
- 正文只列关键阶段，附件列实际已采集全部分项。逐题成绩见共享的评测记录。
