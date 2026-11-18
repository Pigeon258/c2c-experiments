# 完整指标与统计口径

- **批次**：`P4`。
- **对应正文**：[正式报告](<P4.md>)。
- **范围**：本协议、路径的完整分项与覆盖情况。

## A 配置与结果

| 组合 | 视图 | 计划N | 已评分n | 指标 | 均值 | 95% CI |
|---|---|---|---|---|---|---|
| M1/P4/gsm8k/C2C | full | 1319 | 1319 | accuracy | 0.269143 | [0.244882486732373, 0.2934040940106141] |
| M1/P4/hotpotqa/C2C | full | 7405 | 7405 | em | 0.108170 | [0.1012829169480081, 0.11532748143146522] |
| M1/P4/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.107828 | [0.10074880871341048, 0.11504424778761062] |
| M1/P4/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.240721 | [0.23335464308848075, 0.2482068002010702] |
| M1/P4/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.240365 | [0.23278845431436807, 0.2477856525871724] |
| M1/P4/humaneval/C2C | full | 164 | 164 | pass@1 | 0.432927 | [0.3597560975609756, 0.5121951219512195] |
| M2/P4/gsm8k/C2C | full | 1319 | 1319 | accuracy | 0.699773 | [0.6747536012130402, 0.7240523123578466] |
| M2/P4/hotpotqa/C2C | full | 7405 | 7405 | em | 0.091560 | [0.08507765023632681, 0.09804186360567184] |
| M2/P4/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.092035 | [0.085500340367597, 0.0987066031313819] |
| M2/P4/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.276049 | [0.26934856956447545, 0.28283269003987904] |
| M2/P4/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.276202 | [0.26924102875049, 0.2828945782066278] |
| M2/P4/humaneval/C2C | full | 164 | 164 | pass@1 | 0.585366 | [0.5121951219512195, 0.6585365853658537] |
| M3/P4/gsm8k/C2C | full | 1319 | 1319 | accuracy | 0.075057 | [0.06141015921152388, 0.0887035633055345] |
| M3/P4/hotpotqa/C2C | full | 7405 | 7405 | em | 0.004862 | [0.00337609723160027, 0.006482106684672519] |
| M3/P4/hotpotqa/C2C | common_7345 | 7345 | 7345 | em | 0.004901 | [0.0034036759700476512, 0.006535057862491491] |
| M3/P4/hotpotqa/C2C | full | 7405 | 7405 | f1 | 0.133725 | [0.1300072938726543, 0.1374455520450355] |
| M3/P4/hotpotqa/C2C | common_7345 | 7345 | 7345 | f1 | 0.133471 | [0.12973439221694455, 0.13720172646993634] |
| M3/P4/humaneval/C2C | full | 164 | 164 | pass@1 | 0.256098 | [0.18902439024390244, 0.3231707317073171] |

| 组合 | 字段 | 已知n | N | 总tokens |
|---|---|---|---|---|
| M1/P4/gsm8k/C2C | sender_input_tokens | 1319 | 1319 | 178471 |
| M1/P4/gsm8k/C2C | input_tokens | 1319 | 1319 | 179790 |
| M1/P4/gsm8k/C2C | output_tokens | 1319 | 1319 | 494436 |
| M1/P4/gsm8k/C2C | receiver_initial_prefill | 1319 | 1319 | 63312 |
| M1/P4/gsm8k/C2C | receiver_visible | 1319 | 1319 | 63312 |
| M1/P4/gsm8k/C2C | sender_visible | 1319 | 1319 | 179790 |
| M1/P4/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M1/P4/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M1/P4/hotpotqa/C2C | output_tokens | 7405 | 7405 | 156391 |
| M1/P4/hotpotqa/C2C | receiver_initial_prefill | 7405 | 7405 | 555375 |
| M1/P4/hotpotqa/C2C | receiver_visible | 7405 | 7405 | 555375 |
| M1/P4/hotpotqa/C2C | sender_visible | 7405 | 7405 | 11145864 |
| M1/P4/humaneval/C2C | sender_input_tokens | 164 | 164 | 39725 |
| M1/P4/humaneval/C2C | input_tokens | 164 | 164 | 39889 |
| M1/P4/humaneval/C2C | output_tokens | 164 | 164 | 22511 |
| M1/P4/humaneval/C2C | receiver_initial_prefill | 164 | 164 | 12300 |
| M1/P4/humaneval/C2C | receiver_visible | 164 | 164 | 12300 |
| M1/P4/humaneval/C2C | sender_visible | 164 | 164 | 39889 |
| M2/P4/gsm8k/C2C | sender_input_tokens | 1319 | 1319 | 178471 |
| M2/P4/gsm8k/C2C | input_tokens | 1319 | 1319 | 179790 |
| M2/P4/gsm8k/C2C | output_tokens | 1319 | 1319 | 158966 |
| M2/P4/gsm8k/C2C | receiver_initial_prefill | 1319 | 1319 | 63312 |
| M2/P4/gsm8k/C2C | receiver_visible | 1319 | 1319 | 63312 |
| M2/P4/gsm8k/C2C | sender_visible | 1319 | 1319 | 179790 |
| M2/P4/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M2/P4/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M2/P4/hotpotqa/C2C | output_tokens | 7405 | 7405 | 154491 |
| M2/P4/hotpotqa/C2C | receiver_initial_prefill | 7405 | 7405 | 555375 |
| M2/P4/hotpotqa/C2C | receiver_visible | 7405 | 7405 | 555375 |
| M2/P4/hotpotqa/C2C | sender_visible | 7405 | 7405 | 11145864 |
| M2/P4/humaneval/C2C | sender_input_tokens | 164 | 164 | 39725 |
| M2/P4/humaneval/C2C | input_tokens | 164 | 164 | 39889 |
| M2/P4/humaneval/C2C | output_tokens | 164 | 164 | 26647 |
| M2/P4/humaneval/C2C | receiver_initial_prefill | 164 | 164 | 12300 |
| M2/P4/humaneval/C2C | receiver_visible | 164 | 164 | 12300 |
| M2/P4/humaneval/C2C | sender_visible | 164 | 164 | 39889 |
| M3/P4/gsm8k/C2C | sender_input_tokens | 1319 | 1319 | 178471 |
| M3/P4/gsm8k/C2C | input_tokens | 1319 | 1319 | 179790 |
| M3/P4/gsm8k/C2C | output_tokens | 1319 | 1319 | 207075 |
| M3/P4/gsm8k/C2C | receiver_initial_prefill | 1319 | 1319 | 63312 |
| M3/P4/gsm8k/C2C | receiver_visible | 1319 | 1319 | 63312 |
| M3/P4/gsm8k/C2C | sender_visible | 1319 | 1319 | 179790 |
| M3/P4/hotpotqa/C2C | sender_input_tokens | 7405 | 7405 | 11138459 |
| M3/P4/hotpotqa/C2C | input_tokens | 7405 | 7405 | 11145864 |
| M3/P4/hotpotqa/C2C | output_tokens | 7405 | 7405 | 274274 |
| M3/P4/hotpotqa/C2C | receiver_initial_prefill | 7405 | 7405 | 555375 |
| M3/P4/hotpotqa/C2C | receiver_visible | 7405 | 7405 | 555375 |
| M3/P4/hotpotqa/C2C | sender_visible | 7405 | 7405 | 11145864 |
| M3/P4/humaneval/C2C | sender_input_tokens | 164 | 164 | 39725 |
| M3/P4/humaneval/C2C | input_tokens | 164 | 164 | 39889 |
| M3/P4/humaneval/C2C | output_tokens | 164 | 164 | 48319 |
| M3/P4/humaneval/C2C | receiver_initial_prefill | 164 | 164 | 12300 |
| M3/P4/humaneval/C2C | receiver_visible | 164 | 164 | 12300 |
| M3/P4/humaneval/C2C | sender_visible | 164 | 164 | 39889 |

## B 全部分项耗时

| 组合 | 阶段/计时口径 | 完整/部分 | n | N | 均值s | P50s | P95s |
|---|---|---|---|---|---|---|---|
| M1/P4/gsm8k/C2C | sender_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.031537 | 0.031094 | 0.034187 |
| M1/P4/gsm8k/C2C | sender_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.031513 | 0.031070 | 0.034162 |
| M1/P4/gsm8k/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.063331 | 0.063180 | 0.065851 |
| M1/P4/gsm8k/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.063338 | 0.063186 | 0.065858 |
| M1/P4/gsm8k/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.029754 | 0.029597 | 0.031012 |
| M1/P4/gsm8k/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.029736 | 0.029581 | 0.030992 |
| M1/P4/gsm8k/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.198475 | 0.197169 | 0.211769 |
| M1/P4/gsm8k/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.198450 | 0.197147 | 0.211746 |
| M1/P4/gsm8k/C2C | receiver_decode.synchronized_wall_s | 完整 | 1319 | 1319 | 10.955755 | 3.600300 | 30.303706 |
| M1/P4/gsm8k/C2C | receiver_decode.cuda_event_s | 完整 | 1319 | 1319 | 10.955689 | 3.600241 | 30.303247 |
| M1/P4/gsm8k/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 1319 | 1319 | 0.057896 | 0.057804 | 0.060285 |
| M1/P4/gsm8k/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.033568 | 0.031791 | 0.038386 |
| M1/P4/gsm8k/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.033546 | 0.031766 | 0.038359 |
| M1/P4/gsm8k/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.047114 | 0.046337 | 0.056407 |
| M1/P4/gsm8k/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.047070 | 0.046291 | 0.056355 |
| M1/P4/gsm8k/C2C | input_assembly_tokenize_s | 完整 | 1319 | 1319 | 0.000410 | 0.000376 | 0.000617 |
| M1/P4/gsm8k/C2C | input_host_to_device_s | 完整 | 1319 | 1319 | 0.000205 | 0.000185 | 0.000285 |
| M1/P4/gsm8k/C2C | sender_device_to_host_s | 完整 | 1319 | 1319 | 0.004877 | 0.004775 | 0.006115 |
| M1/P4/gsm8k/C2C | sender_pack_s | 完整 | 1319 | 1319 | 0.006342 | 0.006127 | 0.008071 |
| M1/P4/gsm8k/C2C | transport_loopback_and_byte_verify_s | 完整 | 1319 | 1319 | 0.006604 | 0.006293 | 0.009041 |
| M1/P4/gsm8k/C2C | receiver_unpack_s | 完整 | 1319 | 1319 | 0.005550 | 0.005490 | 0.006161 |
| M1/P4/gsm8k/C2C | receiver_restore_and_host_to_device_s | 完整 | 1319 | 1319 | 0.005696 | 0.005455 | 0.006991 |
| M1/P4/gsm8k/C2C | output_text_decode_s | 完整 | 1319 | 1319 | 0.000151 | 0.000109 | 0.000291 |
| M1/P4/gsm8k/C2C | sender_to_receiver_text_pack_s | 完整 | 1319 | 1319 | 0.000022 | 0.000019 | 0.000032 |
| M1/P4/gsm8k/C2C | sender_to_receiver_text_transport_s | 完整 | 1319 | 1319 | 0.000200 | 0.000177 | 0.000373 |
| M1/P4/gsm8k/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 1319 | 1319 | 0.000041 | 0.000039 | 0.000058 |
| M1/P4/gsm8k/C2C | hot_pipeline_wall_s | 完整 | 1319 | 1319 | 11.205930 | 3.860001 | 30.562788 |
| M1/P4/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.054612 | 0.055414 | 0.072580 |
| M1/P4/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.054584 | 0.055386 | 0.072549 |
| M1/P4/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.076082 | 0.074832 | 0.096290 |
| M1/P4/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.076090 | 0.074840 | 0.096293 |
| M1/P4/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.029915 | 0.029751 | 0.031128 |
| M1/P4/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.029897 | 0.029732 | 0.031109 |
| M1/P4/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.956837 | 0.945921 | 1.321262 |
| M1/P4/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.956804 | 0.945885 | 1.321226 |
| M1/P4/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 0.586739 | 0.486008 | 1.283137 |
| M1/P4/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 0.586710 | 0.485987 | 1.283109 |
| M1/P4/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.070011 | 0.068861 | 0.089771 |
| M1/P4/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.107893 | 0.108712 | 0.143292 |
| M1/P4/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.107868 | 0.108684 | 0.143265 |
| M1/P4/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.037782 | 0.034260 | 0.053635 |
| M1/P4/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.037739 | 0.034216 | 0.053585 |
| M1/P4/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.002937 | 0.002836 | 0.004254 |
| M1/P4/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000332 | 0.000323 | 0.000429 |
| M1/P4/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.074178 | 0.071737 | 0.133333 |
| M1/P4/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.143751 | 0.143326 | 0.193439 |
| M1/P4/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.268567 | 0.263587 | 0.372972 |
| M1/P4/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.075401 | 0.074125 | 0.119904 |
| M1/P4/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.022720 | 0.022289 | 0.030516 |
| M1/P4/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000067 | 0.000066 | 0.000085 |
| M1/P4/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7405 | 7405 | 0.000129 | 0.000128 | 0.000161 |
| M1/P4/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7405 | 7405 | 0.000205 | 0.000195 | 0.000348 |
| M1/P4/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7405 | 7405 | 0.000055 | 0.000054 | 0.000067 |
| M1/P4/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 1.619127 | 1.490973 | 2.443894 |
| M1/P4/humaneval/C2C | sender_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.032405 | 0.031904 | 0.034218 |
| M1/P4/humaneval/C2C | sender_prefill.cuda_event_s | 完整 | 164 | 164 | 0.032381 | 0.031880 | 0.034180 |
| M1/P4/humaneval/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.063157 | 0.063039 | 0.064435 |
| M1/P4/humaneval/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.063164 | 0.063046 | 0.064443 |
| M1/P4/humaneval/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.029962 | 0.029847 | 0.030777 |
| M1/P4/humaneval/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 164 | 164 | 0.029944 | 0.029828 | 0.030755 |
| M1/P4/humaneval/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.230545 | 0.220301 | 0.316256 |
| M1/P4/humaneval/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.230519 | 0.220274 | 0.316233 |
| M1/P4/humaneval/C2C | receiver_decode.synchronized_wall_s | 完整 | 164 | 164 | 4.004006 | 1.765612 | 29.739591 |
| M1/P4/humaneval/C2C | receiver_decode.cuda_event_s | 完整 | 164 | 164 | 4.003946 | 1.765573 | 29.739239 |
| M1/P4/humaneval/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 164 | 164 | 0.057565 | 0.057378 | 0.058626 |
| M1/P4/humaneval/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.035085 | 0.034515 | 0.040151 |
| M1/P4/humaneval/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 164 | 164 | 0.035062 | 0.034492 | 0.040127 |
| M1/P4/humaneval/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.047901 | 0.050598 | 0.056676 |
| M1/P4/humaneval/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 164 | 164 | 0.047856 | 0.050554 | 0.056626 |
| M1/P4/humaneval/C2C | input_assembly_tokenize_s | 完整 | 164 | 164 | 0.000752 | 0.000715 | 0.001104 |
| M1/P4/humaneval/C2C | input_host_to_device_s | 完整 | 164 | 164 | 0.000220 | 0.000198 | 0.000304 |
| M1/P4/humaneval/C2C | sender_device_to_host_s | 完整 | 164 | 164 | 0.007874 | 0.007277 | 0.011465 |
| M1/P4/humaneval/C2C | sender_pack_s | 完整 | 164 | 164 | 0.011914 | 0.009590 | 0.039375 |
| M1/P4/humaneval/C2C | transport_loopback_and_byte_verify_s | 完整 | 164 | 164 | 0.015699 | 0.010865 | 0.044160 |
| M1/P4/humaneval/C2C | receiver_unpack_s | 完整 | 164 | 164 | 0.006906 | 0.006632 | 0.008769 |
| M1/P4/humaneval/C2C | receiver_restore_and_host_to_device_s | 完整 | 164 | 164 | 0.009295 | 0.008127 | 0.014226 |
| M1/P4/humaneval/C2C | output_text_decode_s | 完整 | 164 | 164 | 0.000111 | 0.000089 | 0.000331 |
| M1/P4/humaneval/C2C | sender_to_receiver_text_pack_s | 完整 | 164 | 164 | 0.000026 | 0.000022 | 0.000047 |
| M1/P4/humaneval/C2C | sender_to_receiver_text_transport_s | 完整 | 164 | 164 | 0.000161 | 0.000134 | 0.000330 |
| M1/P4/humaneval/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 164 | 164 | 0.000046 | 0.000045 | 0.000067 |
| M1/P4/humaneval/C2C | hot_pipeline_wall_s | 完整 | 164 | 164 | 4.288741 | 2.046899 | 30.018407 |
| M2/P4/gsm8k/C2C | sender_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.031706 | 0.031360 | 0.033712 |
| M2/P4/gsm8k/C2C | sender_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.031682 | 0.031336 | 0.033688 |
| M2/P4/gsm8k/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.064964 | 0.064797 | 0.067243 |
| M2/P4/gsm8k/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.064972 | 0.064805 | 0.067251 |
| M2/P4/gsm8k/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.039167 | 0.039017 | 0.040883 |
| M2/P4/gsm8k/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.039148 | 0.038998 | 0.040863 |
| M2/P4/gsm8k/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.217481 | 0.215875 | 0.229484 |
| M2/P4/gsm8k/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.217457 | 0.215846 | 0.229448 |
| M2/P4/gsm8k/C2C | receiver_decode.synchronized_wall_s | 完整 | 1319 | 1319 | 4.588125 | 4.168170 | 8.356223 |
| M2/P4/gsm8k/C2C | receiver_decode.cuda_event_s | 完整 | 1319 | 1319 | 4.588074 | 4.168131 | 8.356125 |
| M2/P4/gsm8k/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 1319 | 1319 | 0.058688 | 0.058652 | 0.060580 |
| M2/P4/gsm8k/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.040466 | 0.040092 | 0.043168 |
| M2/P4/gsm8k/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.040444 | 0.040070 | 0.043145 |
| M2/P4/gsm8k/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.056396 | 0.056298 | 0.065345 |
| M2/P4/gsm8k/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.056352 | 0.056262 | 0.065295 |
| M2/P4/gsm8k/C2C | input_assembly_tokenize_s | 完整 | 1319 | 1319 | 0.000403 | 0.000371 | 0.000614 |
| M2/P4/gsm8k/C2C | input_host_to_device_s | 完整 | 1319 | 1319 | 0.000197 | 0.000184 | 0.000329 |
| M2/P4/gsm8k/C2C | sender_device_to_host_s | 完整 | 1319 | 1319 | 0.004908 | 0.004842 | 0.006239 |
| M2/P4/gsm8k/C2C | sender_pack_s | 完整 | 1319 | 1319 | 0.006273 | 0.006152 | 0.007615 |
| M2/P4/gsm8k/C2C | transport_loopback_and_byte_verify_s | 完整 | 1319 | 1319 | 0.006683 | 0.006312 | 0.008990 |
| M2/P4/gsm8k/C2C | receiver_unpack_s | 完整 | 1319 | 1319 | 0.005556 | 0.005504 | 0.006138 |
| M2/P4/gsm8k/C2C | receiver_restore_and_host_to_device_s | 完整 | 1319 | 1319 | 0.005708 | 0.005402 | 0.007034 |
| M2/P4/gsm8k/C2C | output_text_decode_s | 完整 | 1319 | 1319 | 0.000106 | 0.000102 | 0.000141 |
| M2/P4/gsm8k/C2C | sender_to_receiver_text_pack_s | 完整 | 1319 | 1319 | 0.000021 | 0.000019 | 0.000032 |
| M2/P4/gsm8k/C2C | sender_to_receiver_text_transport_s | 完整 | 1319 | 1319 | 0.000152 | 0.000125 | 0.000306 |
| M2/P4/gsm8k/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 1319 | 1319 | 0.000044 | 0.000041 | 0.000060 |
| M2/P4/gsm8k/C2C | hot_pipeline_wall_s | 完整 | 1319 | 1319 | 4.866605 | 4.445616 | 8.638354 |
| M2/P4/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.055359 | 0.056112 | 0.074024 |
| M2/P4/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.055331 | 0.056082 | 0.073997 |
| M2/P4/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.076821 | 0.075904 | 0.097558 |
| M2/P4/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.076829 | 0.075914 | 0.097567 |
| M2/P4/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.039173 | 0.038894 | 0.040592 |
| M2/P4/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.039154 | 0.038875 | 0.040574 |
| M2/P4/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 1.105079 | 1.095089 | 1.523502 |
| M2/P4/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 1.105045 | 1.095064 | 1.523460 |
| M2/P4/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 0.760185 | 0.735598 | 1.554614 |
| M2/P4/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 0.760153 | 0.735561 | 1.554584 |
| M2/P4/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.069595 | 0.068754 | 0.089963 |
| M2/P4/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.245979 | 0.247881 | 0.335175 |
| M2/P4/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.245943 | 0.247844 | 0.335149 |
| M2/P4/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.050341 | 0.047220 | 0.063011 |
| M2/P4/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.050296 | 0.047166 | 0.062961 |
| M2/P4/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.002761 | 0.002654 | 0.004020 |
| M2/P4/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000329 | 0.000324 | 0.000398 |
| M2/P4/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.061065 | 0.057312 | 0.106057 |
| M2/P4/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.142859 | 0.141407 | 0.193167 |
| M2/P4/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.273120 | 0.268006 | 0.382638 |
| M2/P4/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.081175 | 0.081120 | 0.122533 |
| M2/P4/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.022888 | 0.022403 | 0.030683 |
| M2/P4/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000069 | 0.000068 | 0.000083 |
| M2/P4/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7405 | 7405 | 0.000129 | 0.000126 | 0.000160 |
| M2/P4/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7405 | 7405 | 0.000161 | 0.000129 | 0.000307 |
| M2/P4/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7405 | 7405 | 0.000053 | 0.000052 | 0.000064 |
| M2/P4/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 1.943338 | 1.909345 | 2.867068 |
| M2/P4/humaneval/C2C | sender_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.032174 | 0.031893 | 0.033637 |
| M2/P4/humaneval/C2C | sender_prefill.cuda_event_s | 完整 | 164 | 164 | 0.032151 | 0.031870 | 0.033614 |
| M2/P4/humaneval/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.064360 | 0.064066 | 0.066905 |
| M2/P4/humaneval/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.064367 | 0.064072 | 0.066916 |
| M2/P4/humaneval/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.038971 | 0.038864 | 0.039647 |
| M2/P4/humaneval/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 164 | 164 | 0.038953 | 0.038846 | 0.039628 |
| M2/P4/humaneval/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.255071 | 0.237212 | 0.354524 |
| M2/P4/humaneval/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.255049 | 0.237190 | 0.354501 |
| M2/P4/humaneval/C2C | receiver_decode.synchronized_wall_s | 完整 | 164 | 164 | 6.139875 | 5.037773 | 12.328843 |
| M2/P4/humaneval/C2C | receiver_decode.cuda_event_s | 完整 | 164 | 164 | 6.139836 | 5.037704 | 12.328823 |
| M2/P4/humaneval/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 164 | 164 | 0.057693 | 0.057448 | 0.059595 |
| M2/P4/humaneval/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.047886 | 0.040149 | 0.070548 |
| M2/P4/humaneval/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 164 | 164 | 0.047865 | 0.040128 | 0.070528 |
| M2/P4/humaneval/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.058576 | 0.062895 | 0.066259 |
| M2/P4/humaneval/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 164 | 164 | 0.058530 | 0.062846 | 0.066209 |
| M2/P4/humaneval/C2C | input_assembly_tokenize_s | 完整 | 164 | 164 | 0.000696 | 0.000659 | 0.001002 |
| M2/P4/humaneval/C2C | input_host_to_device_s | 完整 | 164 | 164 | 0.000198 | 0.000192 | 0.000217 |
| M2/P4/humaneval/C2C | sender_device_to_host_s | 完整 | 164 | 164 | 0.007795 | 0.007237 | 0.012662 |
| M2/P4/humaneval/C2C | sender_pack_s | 完整 | 164 | 164 | 0.011908 | 0.009440 | 0.037236 |
| M2/P4/humaneval/C2C | transport_loopback_and_byte_verify_s | 完整 | 164 | 164 | 0.017014 | 0.011295 | 0.044362 |
| M2/P4/humaneval/C2C | receiver_unpack_s | 完整 | 164 | 164 | 0.006925 | 0.006765 | 0.008523 |
| M2/P4/humaneval/C2C | receiver_restore_and_host_to_device_s | 完整 | 164 | 164 | 0.008644 | 0.008100 | 0.012987 |
| M2/P4/humaneval/C2C | output_text_decode_s | 完整 | 164 | 164 | 0.000128 | 0.000118 | 0.000199 |
| M2/P4/humaneval/C2C | sender_to_receiver_text_pack_s | 完整 | 164 | 164 | 0.000025 | 0.000020 | 0.000046 |
| M2/P4/humaneval/C2C | sender_to_receiver_text_transport_s | 完整 | 164 | 164 | 0.000136 | 0.000116 | 0.000286 |
| M2/P4/humaneval/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 164 | 164 | 0.000047 | 0.000045 | 0.000064 |
| M2/P4/humaneval/C2C | hot_pipeline_wall_s | 完整 | 164 | 164 | 6.459451 | 5.332571 | 12.658259 |
| M3/P4/gsm8k/C2C | sender_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.041019 | 0.040578 | 0.044273 |
| M3/P4/gsm8k/C2C | sender_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.040995 | 0.040555 | 0.044250 |
| M3/P4/gsm8k/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.062990 | 0.062920 | 0.065750 |
| M3/P4/gsm8k/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.062997 | 0.062927 | 0.065755 |
| M3/P4/gsm8k/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.029074 | 0.028952 | 0.030463 |
| M3/P4/gsm8k/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.029056 | 0.028933 | 0.030444 |
| M3/P4/gsm8k/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 1319 | 1319 | 0.220919 | 0.219449 | 0.236362 |
| M3/P4/gsm8k/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 1319 | 1319 | 0.220893 | 0.219422 | 0.236333 |
| M3/P4/gsm8k/C2C | receiver_decode.synchronized_wall_s | 完整 | 1319 | 1319 | 4.395842 | 2.976508 | 19.637559 |
| M3/P4/gsm8k/C2C | receiver_decode.cuda_event_s | 完整 | 1319 | 1319 | 4.395772 | 2.976515 | 19.636782 |
| M3/P4/gsm8k/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 1319 | 1319 | 0.057164 | 0.057176 | 0.059507 |
| M3/P4/gsm8k/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.033154 | 0.031731 | 0.037763 |
| M3/P4/gsm8k/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.033132 | 0.031712 | 0.037742 |
| M3/P4/gsm8k/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 1319 | 1319 | 0.047110 | 0.050597 | 0.055832 |
| M3/P4/gsm8k/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 1319 | 1319 | 0.047065 | 0.050554 | 0.055782 |
| M3/P4/gsm8k/C2C | input_assembly_tokenize_s | 完整 | 1319 | 1319 | 0.000417 | 0.000383 | 0.000617 |
| M3/P4/gsm8k/C2C | input_host_to_device_s | 完整 | 1319 | 1319 | 0.000205 | 0.000185 | 0.000287 |
| M3/P4/gsm8k/C2C | sender_device_to_host_s | 完整 | 1319 | 1319 | 0.006259 | 0.006131 | 0.007801 |
| M3/P4/gsm8k/C2C | sender_pack_s | 完整 | 1319 | 1319 | 0.007808 | 0.007613 | 0.009561 |
| M3/P4/gsm8k/C2C | transport_loopback_and_byte_verify_s | 完整 | 1319 | 1319 | 0.013035 | 0.012467 | 0.017353 |
| M3/P4/gsm8k/C2C | receiver_unpack_s | 完整 | 1319 | 1319 | 0.006836 | 0.006762 | 0.007621 |
| M3/P4/gsm8k/C2C | receiver_restore_and_host_to_device_s | 完整 | 1319 | 1319 | 0.007185 | 0.006978 | 0.008959 |
| M3/P4/gsm8k/C2C | output_text_decode_s | 完整 | 1319 | 1319 | 0.000110 | 0.000099 | 0.000268 |
| M3/P4/gsm8k/C2C | sender_to_receiver_text_pack_s | 完整 | 1319 | 1319 | 0.000021 | 0.000019 | 0.000031 |
| M3/P4/gsm8k/C2C | sender_to_receiver_text_transport_s | 完整 | 1319 | 1319 | 0.000200 | 0.000176 | 0.000385 |
| M3/P4/gsm8k/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 1319 | 1319 | 0.000042 | 0.000040 | 0.000057 |
| M3/P4/gsm8k/C2C | hot_pipeline_wall_s | 完整 | 1319 | 1319 | 4.668822 | 3.251081 | 19.915043 |
| M3/P4/hotpotqa/C2C | sender_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.246309 | 0.246606 | 0.332857 |
| M3/P4/hotpotqa/C2C | sender_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.246277 | 0.246577 | 0.332817 |
| M3/P4/hotpotqa/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 0.075932 | 0.074716 | 0.095684 |
| M3/P4/hotpotqa/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 0.075940 | 0.074722 | 0.095687 |
| M3/P4/hotpotqa/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.029066 | 0.028928 | 0.030040 |
| M3/P4/hotpotqa/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.029047 | 0.028911 | 0.030021 |
| M3/P4/hotpotqa/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 7405 | 7405 | 1.302416 | 1.287548 | 1.788417 |
| M3/P4/hotpotqa/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 7405 | 7405 | 1.302376 | 1.287516 | 1.788359 |
| M3/P4/hotpotqa/C2C | receiver_decode.synchronized_wall_s | 完整 | 7405 | 7405 | 1.013592 | 0.679194 | 2.264780 |
| M3/P4/hotpotqa/C2C | receiver_decode.cuda_event_s | 完整 | 7405 | 7405 | 1.013558 | 0.679163 | 2.264783 |
| M3/P4/hotpotqa/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 7405 | 7405 | 0.069396 | 0.068228 | 0.088613 |
| M3/P4/hotpotqa/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.055066 | 0.055123 | 0.073925 |
| M3/P4/hotpotqa/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.055042 | 0.055102 | 0.073901 |
| M3/P4/hotpotqa/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 7405 | 7405 | 0.036594 | 0.031935 | 0.052627 |
| M3/P4/hotpotqa/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 7405 | 7405 | 0.036553 | 0.031896 | 0.052573 |
| M3/P4/hotpotqa/C2C | input_assembly_tokenize_s | 完整 | 7405 | 7405 | 0.003011 | 0.002920 | 0.004351 |
| M3/P4/hotpotqa/C2C | input_host_to_device_s | 完整 | 7405 | 7405 | 0.000333 | 0.000324 | 0.000436 |
| M3/P4/hotpotqa/C2C | sender_device_to_host_s | 完整 | 7405 | 7405 | 0.097953 | 0.094617 | 0.174161 |
| M3/P4/hotpotqa/C2C | sender_pack_s | 完整 | 7405 | 7405 | 0.191337 | 0.188649 | 0.260267 |
| M3/P4/hotpotqa/C2C | transport_loopback_and_byte_verify_s | 完整 | 7405 | 7405 | 0.344039 | 0.338255 | 0.478373 |
| M3/P4/hotpotqa/C2C | receiver_unpack_s | 完整 | 7405 | 7405 | 0.101796 | 0.099462 | 0.152730 |
| M3/P4/hotpotqa/C2C | receiver_restore_and_host_to_device_s | 完整 | 7405 | 7405 | 0.028005 | 0.027502 | 0.037302 |
| M3/P4/hotpotqa/C2C | output_text_decode_s | 完整 | 7405 | 7405 | 0.000077 | 0.000070 | 0.000102 |
| M3/P4/hotpotqa/C2C | sender_to_receiver_text_pack_s | 完整 | 7405 | 7405 | 0.000129 | 0.000128 | 0.000160 |
| M3/P4/hotpotqa/C2C | sender_to_receiver_text_transport_s | 完整 | 7405 | 7405 | 0.000240 | 0.000212 | 0.000433 |
| M3/P4/hotpotqa/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 7405 | 7405 | 0.000055 | 0.000054 | 0.000067 |
| M3/P4/hotpotqa/C2C | hot_pipeline_wall_s | 完整 | 7405 | 7405 | 2.397211 | 2.089217 | 3.659243 |
| M3/P4/humaneval/C2C | sender_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.050805 | 0.042901 | 0.075526 |
| M3/P4/humaneval/C2C | sender_prefill.cuda_event_s | 完整 | 164 | 164 | 0.050780 | 0.042876 | 0.075498 |
| M3/P4/humaneval/C2C | receiver_conversion_fusion_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.063495 | 0.063153 | 0.067152 |
| M3/P4/humaneval/C2C | receiver_conversion_fusion_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.063501 | 0.063160 | 0.067167 |
| M3/P4/humaneval/C2C | receiver_final_prompt_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.029693 | 0.029477 | 0.031087 |
| M3/P4/humaneval/C2C | receiver_final_prompt_prefill.cuda_event_s | 完整 | 164 | 164 | 0.029675 | 0.029459 | 0.031068 |
| M3/P4/humaneval/C2C | prefill_pipeline_inclusive.synchronized_wall_s | 完整 | 164 | 164 | 0.279220 | 0.260702 | 0.388746 |
| M3/P4/humaneval/C2C | prefill_pipeline_inclusive.cuda_event_s | 完整 | 164 | 164 | 0.279197 | 0.260666 | 0.388728 |
| M3/P4/humaneval/C2C | receiver_decode.synchronized_wall_s | 完整 | 164 | 164 | 8.521769 | 4.423194 | 29.775579 |
| M3/P4/humaneval/C2C | receiver_decode.cuda_event_s | 完整 | 164 | 164 | 8.521756 | 4.423193 | 29.775333 |
| M3/P4/humaneval/C2C | receiver_conversion_fusion_modules_nested.cuda_event_s | 完整 | 164 | 164 | 0.057476 | 0.057180 | 0.060774 |
| M3/P4/humaneval/C2C | receiver_additional_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.033432 | 0.031822 | 0.038404 |
| M3/P4/humaneval/C2C | receiver_additional_prefill.cuda_event_s | 完整 | 164 | 164 | 0.033410 | 0.031802 | 0.038381 |
| M3/P4/humaneval/C2C | receiver_initial_prefill.synchronized_wall_s | 完整 | 164 | 164 | 0.045318 | 0.044985 | 0.055658 |
| M3/P4/humaneval/C2C | receiver_initial_prefill.cuda_event_s | 完整 | 164 | 164 | 0.045275 | 0.044942 | 0.055609 |
| M3/P4/humaneval/C2C | input_assembly_tokenize_s | 完整 | 164 | 164 | 0.000621 | 0.000588 | 0.000872 |
| M3/P4/humaneval/C2C | input_host_to_device_s | 完整 | 164 | 164 | 0.000212 | 0.000197 | 0.000300 |
| M3/P4/humaneval/C2C | sender_device_to_host_s | 完整 | 164 | 164 | 0.009925 | 0.009342 | 0.015100 |
| M3/P4/humaneval/C2C | sender_pack_s | 完整 | 164 | 164 | 0.018002 | 0.011588 | 0.053211 |
| M3/P4/humaneval/C2C | transport_loopback_and_byte_verify_s | 完整 | 164 | 164 | 0.030410 | 0.023367 | 0.052664 |
| M3/P4/humaneval/C2C | receiver_unpack_s | 完整 | 164 | 164 | 0.008694 | 0.008461 | 0.010850 |
| M3/P4/humaneval/C2C | receiver_restore_and_host_to_device_s | 完整 | 164 | 164 | 0.011316 | 0.010517 | 0.017048 |
| M3/P4/humaneval/C2C | output_text_decode_s | 完整 | 164 | 164 | 0.000163 | 0.000127 | 0.000361 |
| M3/P4/humaneval/C2C | sender_to_receiver_text_pack_s | 完整 | 164 | 164 | 0.000026 | 0.000022 | 0.000049 |
| M3/P4/humaneval/C2C | sender_to_receiver_text_transport_s | 完整 | 164 | 164 | 0.000199 | 0.000173 | 0.000385 |
| M3/P4/humaneval/C2C | sender_to_receiver_text_unpack_reconstruct_s | 完整 | 164 | 164 | 0.000043 | 0.000041 | 0.000058 |
| M3/P4/humaneval/C2C | hot_pipeline_wall_s | 完整 | 164 | 164 | 8.851917 | 4.744627 | 30.127285 |

## C 异常及覆盖

| 组合 | 项目 | 数值 |
|---|---|---|
| M1/P4/gsm8k/C2C | input_tokens | {"known": 1319, "missing": 0} |
| M1/P4/gsm8k/C2C | output_tokens | {"known": 1319, "missing": 0} |
| M1/P4/gsm8k/C2C | communication | {"known": 1319, "missing": 0} |
| M1/P4/gsm8k/C2C | hot_pipeline_wall_s | {"known": 1319, "missing": 0} |
| M1/P4/gsm8k/C2C | 全部尝试墙钟 | {"n": 1319, "mean": 11.473930930105018, "p50": 4.140055179130286, "p95": 30.85034999914933} |
| M1/P4/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M1/P4/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M1/P4/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M1/P4/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M1/P4/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 2.1126780415794597, "p50": 1.9811128738801926, "p95": 2.9867261284030966} |
| M1/P4/humaneval/C2C | input_tokens | {"known": 164, "missing": 0} |
| M1/P4/humaneval/C2C | output_tokens | {"known": 164, "missing": 0} |
| M1/P4/humaneval/C2C | communication | {"known": 164, "missing": 0} |
| M1/P4/humaneval/C2C | hot_pipeline_wall_s | {"known": 164, "missing": 0} |
| M1/P4/humaneval/C2C | 全部尝试墙钟 | {"n": 164, "mean": 4.9436015639817565, "p50": 2.7115508490242064, "p95": 30.664774411777035} |
| M2/P4/gsm8k/C2C | input_tokens | {"known": 1319, "missing": 0} |
| M2/P4/gsm8k/C2C | output_tokens | {"known": 1319, "missing": 0} |
| M2/P4/gsm8k/C2C | communication | {"known": 1319, "missing": 0} |
| M2/P4/gsm8k/C2C | hot_pipeline_wall_s | {"known": 1319, "missing": 0} |
| M2/P4/gsm8k/C2C | 全部尝试墙钟 | {"n": 1319, "mean": 5.13344714938048, "p50": 4.715161381056532, "p95": 8.914409147459082} |
| M2/P4/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M2/P4/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M2/P4/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M2/P4/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M2/P4/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 2.3298000365917324, "p50": 2.2979198819957674, "p95": 3.2868970990180957} |
| M2/P4/humaneval/C2C | input_tokens | {"known": 164, "missing": 0} |
| M2/P4/humaneval/C2C | output_tokens | {"known": 164, "missing": 0} |
| M2/P4/humaneval/C2C | communication | {"known": 164, "missing": 0} |
| M2/P4/humaneval/C2C | hot_pipeline_wall_s | {"known": 164, "missing": 0} |
| M2/P4/humaneval/C2C | 全部尝试墙钟 | {"n": 164, "mean": 6.889856698542333, "p50": 5.771105408552103, "p95": 13.080991707381326} |
| M3/P4/gsm8k/C2C | input_tokens | {"known": 1319, "missing": 0} |
| M3/P4/gsm8k/C2C | output_tokens | {"known": 1319, "missing": 0} |
| M3/P4/gsm8k/C2C | communication | {"known": 1319, "missing": 0} |
| M3/P4/gsm8k/C2C | hot_pipeline_wall_s | {"known": 1319, "missing": 0} |
| M3/P4/gsm8k/C2C | 全部尝试墙钟 | {"n": 1319, "mean": 4.934477087179654, "p50": 3.5309930639341474, "p95": 20.20679100865876} |
| M3/P4/hotpotqa/C2C | input_tokens | {"known": 7405, "missing": 0} |
| M3/P4/hotpotqa/C2C | output_tokens | {"known": 7405, "missing": 0} |
| M3/P4/hotpotqa/C2C | communication | {"known": 7405, "missing": 0} |
| M3/P4/hotpotqa/C2C | hot_pipeline_wall_s | {"known": 7405, "missing": 0} |
| M3/P4/hotpotqa/C2C | 全部尝试墙钟 | {"n": 7405, "mean": 2.942763598180067, "p50": 2.640128209022805, "p95": 4.246603546431286} |
| M3/P4/humaneval/C2C | input_tokens | {"known": 164, "missing": 0} |
| M3/P4/humaneval/C2C | output_tokens | {"known": 164, "missing": 0} |
| M3/P4/humaneval/C2C | communication | {"known": 164, "missing": 0} |
| M3/P4/humaneval/C2C | hot_pipeline_wall_s | {"known": 164, "missing": 0} |
| M3/P4/humaneval/C2C | 全部尝试墙钟 | {"n": 164, "mean": 9.294752632621279, "p50": 5.31418168253731, "p95": 30.554159214778338} |

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
| M1 | protocol | P4 |
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
| M2 | protocol | P4 |
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
| M3 | protocol | P4 |
| M3 | path | c2c |
| M3 | adaptation | P2双向补齐；P3/P4单向补齐；补齐后重建完整对齐输入 |
| M3 | 代码评分运行时 | {"python": "3.11.17 (main, Nov  3 2026, 23:59:51) [GCC 11.4.0]", "network_isolated": true, "project_paths_hidden": true} |
| M3 | 代码评分资源限制 | {"wall_s": 3, "cpu_s": 4, "memory_bytes": 2147483648, "outer_wall_s": 8} |

## E 通信

| 组合 | 字段 | n | N | 总字节 | 均值字节 | P50 | P95 |
|---|---|---|---|---|---|---|---|
| M1/P4/gsm8k/C2C | raw_kv_bytes | 1319 | 1319 | 20468482048 | 15518181.992418 | 15024128.000000 | 20529152.000000 |
| M1/P4/gsm8k/C2C | serialized_payload_bytes | 1319 | 1319 | 20490293109 | 15534718.050796 | 15040670.000000 | 20545849.400000 |
| M1/P4/gsm8k/C2C | metadata_and_container_bytes | 1319 | 1319 | 21494509 | 16296.064443 | 16296.000000 | 16296.000000 |
| M1/P4/gsm8k/C2C | framing_bytes | 1319 | 1319 | 21104 | 16.000000 | 16.000000 | 16.000000 |
| M1/P4/gsm8k/C2C | actual_sent_bytes | 1319 | 1319 | 20490314213 | 15534734.050796 | 15040686.000000 | 20545865.400000 |
| M1/P4/gsm8k/C2C | actual_received_bytes | 1319 | 1319 | 20490314213 | 15534734.050796 | 15040686.000000 | 20545865.400000 |
| M1/P4/gsm8k/C2C | generated_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P4/gsm8k/C2C | supplemental_text_bytes | 1319 | 1319 | 316552 | 239.993935 | 222.000000 | 431.000000 |
| M1/P4/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1277447585792 | 172511490.316273 | 168935424.000000 | 242198118.400000 |
| M1/P4/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1277616593187 | 172534313.732208 | 168958399.000000 | 242223897.200000 |
| M1/P4/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 126206483 | 17043.414315 | 17040.000000 | 17129.000000 |
| M1/P4/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 118480 | 16.000000 | 16.000000 | 16.000000 |
| M1/P4/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1277616711667 | 172534329.732208 | 168958415.000000 | 242223913.200000 |
| M1/P4/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1277616711667 | 172534329.732208 | 168958415.000000 | 242223913.200000 |
| M1/P4/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P4/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 42800912 | 5780.001621 | 5672.000000 | 8431.800000 |
| M1/P4/humaneval/C2C | raw_kv_bytes | 164 | 164 | 4555980800 | 27780370.731707 | 25919488.000000 | 43776409.600000 |
| M1/P4/humaneval/C2C | serialized_payload_bytes | 164 | 164 | 4558733499 | 27797155.481707 | 25936176.500000 | 43793669.650000 |
| M1/P4/humaneval/C2C | metadata_and_container_bytes | 164 | 164 | 2678719 | 16333.652439 | 16312.000000 | 16393.850000 |
| M1/P4/humaneval/C2C | framing_bytes | 164 | 164 | 2624 | 16.000000 | 16.000000 | 16.000000 |
| M1/P4/humaneval/C2C | actual_sent_bytes | 164 | 164 | 4558736123 | 27797171.481707 | 25936192.500000 | 43793685.650000 |
| M1/P4/humaneval/C2C | actual_received_bytes | 164 | 164 | 4558736123 | 27797171.481707 | 25936192.500000 | 43793685.650000 |
| M1/P4/humaneval/C2C | generated_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M1/P4/humaneval/C2C | supplemental_text_bytes | 164 | 164 | 73980 | 451.097561 | 396.000000 | 914.750000 |
| M2/P4/gsm8k/C2C | raw_kv_bytes | 1319 | 1319 | 20468482048 | 15518181.992418 | 15024128.000000 | 20529152.000000 |
| M2/P4/gsm8k/C2C | serialized_payload_bytes | 1319 | 1319 | 20490293109 | 15534718.050796 | 15040670.000000 | 20545849.400000 |
| M2/P4/gsm8k/C2C | metadata_and_container_bytes | 1319 | 1319 | 21494509 | 16296.064443 | 16296.000000 | 16296.000000 |
| M2/P4/gsm8k/C2C | framing_bytes | 1319 | 1319 | 21104 | 16.000000 | 16.000000 | 16.000000 |
| M2/P4/gsm8k/C2C | actual_sent_bytes | 1319 | 1319 | 20490314213 | 15534734.050796 | 15040686.000000 | 20545865.400000 |
| M2/P4/gsm8k/C2C | actual_received_bytes | 1319 | 1319 | 20490314213 | 15534734.050796 | 15040686.000000 | 20545865.400000 |
| M2/P4/gsm8k/C2C | generated_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P4/gsm8k/C2C | supplemental_text_bytes | 1319 | 1319 | 316552 | 239.993935 | 222.000000 | 431.000000 |
| M2/P4/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1277447585792 | 172511490.316273 | 168935424.000000 | 242198118.400000 |
| M2/P4/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1277616593187 | 172534313.732208 | 168958399.000000 | 242223897.200000 |
| M2/P4/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 126206483 | 17043.414315 | 17040.000000 | 17129.000000 |
| M2/P4/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 118480 | 16.000000 | 16.000000 | 16.000000 |
| M2/P4/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1277616711667 | 172534329.732208 | 168958415.000000 | 242223913.200000 |
| M2/P4/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1277616711667 | 172534329.732208 | 168958415.000000 | 242223913.200000 |
| M2/P4/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P4/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 42800912 | 5780.001621 | 5672.000000 | 8431.800000 |
| M2/P4/humaneval/C2C | raw_kv_bytes | 164 | 164 | 4555980800 | 27780370.731707 | 25919488.000000 | 43776409.600000 |
| M2/P4/humaneval/C2C | serialized_payload_bytes | 164 | 164 | 4558733499 | 27797155.481707 | 25936176.500000 | 43793669.650000 |
| M2/P4/humaneval/C2C | metadata_and_container_bytes | 164 | 164 | 2678719 | 16333.652439 | 16312.000000 | 16393.850000 |
| M2/P4/humaneval/C2C | framing_bytes | 164 | 164 | 2624 | 16.000000 | 16.000000 | 16.000000 |
| M2/P4/humaneval/C2C | actual_sent_bytes | 164 | 164 | 4558736123 | 27797171.481707 | 25936192.500000 | 43793685.650000 |
| M2/P4/humaneval/C2C | actual_received_bytes | 164 | 164 | 4558736123 | 27797171.481707 | 25936192.500000 | 43793685.650000 |
| M2/P4/humaneval/C2C | generated_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M2/P4/humaneval/C2C | supplemental_text_bytes | 164 | 164 | 73980 | 451.097561 | 396.000000 | 914.750000 |
| M3/P4/gsm8k/C2C | raw_kv_bytes | 1319 | 1319 | 26316619776 | 19951948.275967 | 19316736.000000 | 26394624.000000 |
| M3/P4/gsm8k/C2C | serialized_payload_bytes | 1319 | 1319 | 26344361061 | 19972980.334344 | 19337774.000000 | 26415817.400000 |
| M3/P4/gsm8k/C2C | metadata_and_container_bytes | 1319 | 1319 | 27424733 | 20792.064443 | 20792.000000 | 20792.000000 |
| M3/P4/gsm8k/C2C | framing_bytes | 1319 | 1319 | 21104 | 16.000000 | 16.000000 | 16.000000 |
| M3/P4/gsm8k/C2C | actual_sent_bytes | 1319 | 1319 | 26344382165 | 19972996.334344 | 19337790.000000 | 26415833.400000 |
| M3/P4/gsm8k/C2C | actual_received_bytes | 1319 | 1319 | 26344382165 | 19972996.334344 | 19337790.000000 | 26415833.400000 |
| M3/P4/gsm8k/C2C | generated_text_bytes | 1319 | 1319 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P4/gsm8k/C2C | supplemental_text_bytes | 1319 | 1319 | 316552 | 239.993935 | 222.000000 | 431.000000 |
| M3/P4/hotpotqa/C2C | raw_kv_bytes | 7405 | 7405 | 1642432610304 | 221800487.549494 | 217202688.000000 | 311397580.800000 |
| M3/P4/hotpotqa/C2C | serialized_payload_bytes | 7405 | 7405 | 1642634910579 | 221827806.965429 | 217230159.000000 | 311427855.600000 |
| M3/P4/hotpotqa/C2C | metadata_and_container_bytes | 7405 | 7405 | 159499363 | 21539.414315 | 21536.000000 | 21625.000000 |
| M3/P4/hotpotqa/C2C | framing_bytes | 7405 | 7405 | 118480 | 16.000000 | 16.000000 | 16.000000 |
| M3/P4/hotpotqa/C2C | actual_sent_bytes | 7405 | 7405 | 1642635029059 | 221827822.965429 | 217230175.000000 | 311427871.600000 |
| M3/P4/hotpotqa/C2C | actual_received_bytes | 7405 | 7405 | 1642635029059 | 221827822.965429 | 217230175.000000 | 311427871.600000 |
| M3/P4/hotpotqa/C2C | generated_text_bytes | 7405 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P4/hotpotqa/C2C | supplemental_text_bytes | 7405 | 7405 | 42800912 | 5780.001621 | 5672.000000 | 8431.800000 |
| M3/P4/humaneval/C2C | raw_kv_bytes | 164 | 164 | 5857689600 | 35717619.512195 | 33325056.000000 | 56283955.200000 |
| M3/P4/humaneval/C2C | serialized_payload_bytes | 164 | 164 | 5861179643 | 35738900.262195 | 33346240.500000 | 56305711.250000 |
| M3/P4/humaneval/C2C | metadata_and_container_bytes | 164 | 164 | 3416063 | 20829.652439 | 20808.000000 | 20889.850000 |
| M3/P4/humaneval/C2C | framing_bytes | 164 | 164 | 2624 | 16.000000 | 16.000000 | 16.000000 |
| M3/P4/humaneval/C2C | actual_sent_bytes | 164 | 164 | 5861182267 | 35738916.262195 | 33346256.500000 | 56305727.250000 |
| M3/P4/humaneval/C2C | actual_received_bytes | 164 | 164 | 5861182267 | 35738916.262195 | 33346256.500000 | 56305727.250000 |
| M3/P4/humaneval/C2C | generated_text_bytes | 164 | 164 | 0 | 0.000000 | 0.000000 | 0.000000 |
| M3/P4/humaneval/C2C | supplemental_text_bytes | 164 | 164 | 73980 | 451.097561 | 396.000000 | 914.750000 |

| 组合 | K/V | n | 层数 | dtype | 序列长度[min,max] | 其余维度(batch,heads,head_dim) |
|---|---|---|---|---|---|---|
| M1/P4/gsm8k/C2C | keys | 1319 | [28] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M1/P4/gsm8k/C2C | values | 1319 | [28] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M1/P4/hotpotqa/C2C | keys | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M1/P4/hotpotqa/C2C | values | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M1/P4/humaneval/C2C | keys | 164 | [28] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M1/P4/humaneval/C2C | values | 164 | [28] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M2/P4/gsm8k/C2C | keys | 1319 | [28] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M2/P4/gsm8k/C2C | values | 1319 | [28] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M2/P4/hotpotqa/C2C | keys | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M2/P4/hotpotqa/C2C | values | 7405 | [28] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M2/P4/humaneval/C2C | keys | 164 | [28] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M2/P4/humaneval/C2C | values | 164 | [28] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M3/P4/gsm8k/C2C | keys | 1319 | [36] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M3/P4/gsm8k/C2C | values | 1319 | [36] | ["torch.bfloat16"] | [97, 262] | [[1, 8, 128]] |
| M3/P4/hotpotqa/C2C | keys | 7405 | [36] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M3/P4/hotpotqa/C2C | values | 7405 | [36] | ["torch.bfloat16"] | [193, 3666] | [[1, 8, 128]] |
| M3/P4/humaneval/C2C | keys | 164 | [36] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |
| M3/P4/humaneval/C2C | values | 164 | [36] | ["torch.bfloat16"] | [146, 499] | [[1, 8, 128]] |

## F GPU竞争观察分项

原始总体耗时保持；以下分列观测到竞争、未观测到竞争及未覆盖监测的样本。采样间隔5秒，未观测到竞争不等于连续独占证明。

| 组合 | 监测分类 | 阶段 | n | 均值s | P50s | P95s |
|---|---|---|---|---|---|---|
| M1/gsm8k | no_contention_observed | sender_prefill.synchronized_wall_s | 1311 | 0.031518 | 0.031092 | 0.034097 |
| M1/gsm8k | no_contention_observed | sender_prefill.cuda_event_s | 1311 | 0.031494 | 0.031069 | 0.034073 |
| M1/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 1311 | 0.063286 | 0.063178 | 0.065657 |
| M1/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 1311 | 0.063293 | 0.063185 | 0.065664 |
| M1/gsm8k | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 1311 | 0.029734 | 0.029596 | 0.030924 |
| M1/gsm8k | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 1311 | 0.029715 | 0.029578 | 0.030904 |
| M1/gsm8k | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 1311 | 0.198334 | 0.197144 | 0.211612 |
| M1/gsm8k | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 1311 | 0.198310 | 0.197134 | 0.211582 |
| M1/gsm8k | no_contention_observed | receiver_decode.synchronized_wall_s | 1311 | 10.835540 | 3.583772 | 30.268893 |
| M1/gsm8k | no_contention_observed | receiver_decode.cuda_event_s | 1311 | 10.835474 | 3.583720 | 30.268592 |
| M1/gsm8k | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 1311 | 0.057854 | 0.057804 | 0.060058 |
| M1/gsm8k | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 1311 | 0.033552 | 0.031783 | 0.038378 |
| M1/gsm8k | no_contention_observed | receiver_additional_prefill.cuda_event_s | 1311 | 0.033530 | 0.031761 | 0.038351 |
| M1/gsm8k | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 1311 | 0.047118 | 0.046337 | 0.056405 |
| M1/gsm8k | no_contention_observed | receiver_initial_prefill.cuda_event_s | 1311 | 0.047073 | 0.046291 | 0.056353 |
| M1/gsm8k | contended | sender_prefill.synchronized_wall_s | 8 | 0.034704 | 0.031551 | 0.048072 |
| M1/gsm8k | contended | sender_prefill.cuda_event_s | 8 | 0.034664 | 0.031524 | 0.047974 |
| M1/gsm8k | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 8 | 0.070741 | 0.065844 | 0.095955 |
| M1/gsm8k | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 8 | 0.070758 | 0.065851 | 0.096012 |
| M1/gsm8k | contended | receiver_final_prompt_prefill.synchronized_wall_s | 8 | 0.033052 | 0.029901 | 0.045145 |
| M1/gsm8k | contended | receiver_final_prompt_prefill.cuda_event_s | 8 | 0.033031 | 0.029882 | 0.045118 |
| M1/gsm8k | contended | prefill_pipeline_inclusive.synchronized_wall_s | 8 | 0.221491 | 0.206777 | 0.293198 |
| M1/gsm8k | contended | prefill_pipeline_inclusive.cuda_event_s | 8 | 0.221463 | 0.206746 | 0.293175 |
| M1/gsm8k | contended | receiver_decode.synchronized_wall_s | 8 | 30.656072 | 32.837608 | 39.734470 |
| M1/gsm8k | contended | receiver_decode.cuda_event_s | 8 | 30.655921 | 32.837032 | 39.735014 |
| M1/gsm8k | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 8 | 0.064709 | 0.060184 | 0.087963 |
| M1/gsm8k | contended | receiver_additional_prefill.synchronized_wall_s | 8 | 0.036186 | 0.034682 | 0.045321 |
| M1/gsm8k | contended | receiver_additional_prefill.cuda_event_s | 8 | 0.036158 | 0.034656 | 0.045287 |
| M1/gsm8k | contended | receiver_initial_prefill.synchronized_wall_s | 8 | 0.046564 | 0.047042 | 0.059324 |
| M1/gsm8k | contended | receiver_initial_prefill.cuda_event_s | 8 | 0.046522 | 0.047003 | 0.059276 |
| M1/hotpotqa | no_contention_observed | sender_prefill.synchronized_wall_s | 7405 | 0.054612 | 0.055414 | 0.072580 |
| M1/hotpotqa | no_contention_observed | sender_prefill.cuda_event_s | 7405 | 0.054584 | 0.055386 | 0.072549 |
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7405 | 0.076082 | 0.074832 | 0.096290 |
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7405 | 0.076090 | 0.074840 | 0.096293 |
| M1/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7405 | 0.029915 | 0.029751 | 0.031128 |
| M1/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7405 | 0.029897 | 0.029732 | 0.031109 |
| M1/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7405 | 0.956837 | 0.945921 | 1.321262 |
| M1/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7405 | 0.956804 | 0.945885 | 1.321226 |
| M1/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7405 | 0.586739 | 0.486008 | 1.283137 |
| M1/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7405 | 0.586710 | 0.485987 | 1.283109 |
| M1/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7405 | 0.070011 | 0.068861 | 0.089771 |
| M1/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7405 | 0.107893 | 0.108712 | 0.143292 |
| M1/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7405 | 0.107868 | 0.108684 | 0.143265 |
| M1/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7405 | 0.037782 | 0.034260 | 0.053635 |
| M1/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7405 | 0.037739 | 0.034216 | 0.053585 |
| M1/humaneval | no_contention_observed | sender_prefill.synchronized_wall_s | 164 | 0.032405 | 0.031904 | 0.034218 |
| M1/humaneval | no_contention_observed | sender_prefill.cuda_event_s | 164 | 0.032381 | 0.031880 | 0.034180 |
| M1/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 164 | 0.063157 | 0.063039 | 0.064435 |
| M1/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 164 | 0.063164 | 0.063046 | 0.064443 |
| M1/humaneval | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 164 | 0.029962 | 0.029847 | 0.030777 |
| M1/humaneval | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 164 | 0.029944 | 0.029828 | 0.030755 |
| M1/humaneval | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 164 | 0.230545 | 0.220301 | 0.316256 |
| M1/humaneval | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 164 | 0.230519 | 0.220274 | 0.316233 |
| M1/humaneval | no_contention_observed | receiver_decode.synchronized_wall_s | 164 | 4.004006 | 1.765612 | 29.739591 |
| M1/humaneval | no_contention_observed | receiver_decode.cuda_event_s | 164 | 4.003946 | 1.765573 | 29.739239 |
| M1/humaneval | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 164 | 0.057565 | 0.057378 | 0.058626 |
| M1/humaneval | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 164 | 0.035085 | 0.034515 | 0.040151 |
| M1/humaneval | no_contention_observed | receiver_additional_prefill.cuda_event_s | 164 | 0.035062 | 0.034492 | 0.040127 |
| M1/humaneval | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 164 | 0.047901 | 0.050598 | 0.056676 |
| M1/humaneval | no_contention_observed | receiver_initial_prefill.cuda_event_s | 164 | 0.047856 | 0.050554 | 0.056626 |
| M2/gsm8k | no_contention_observed | sender_prefill.synchronized_wall_s | 1319 | 0.031706 | 0.031360 | 0.033712 |
| M2/gsm8k | no_contention_observed | sender_prefill.cuda_event_s | 1319 | 0.031682 | 0.031336 | 0.033688 |
| M2/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 1319 | 0.064964 | 0.064797 | 0.067243 |
| M2/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 1319 | 0.064972 | 0.064805 | 0.067251 |
| M2/gsm8k | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 1319 | 0.039167 | 0.039017 | 0.040883 |
| M2/gsm8k | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 1319 | 0.039148 | 0.038998 | 0.040863 |
| M2/gsm8k | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 1319 | 0.217481 | 0.215875 | 0.229484 |
| M2/gsm8k | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 1319 | 0.217457 | 0.215846 | 0.229448 |
| M2/gsm8k | no_contention_observed | receiver_decode.synchronized_wall_s | 1319 | 4.588125 | 4.168170 | 8.356223 |
| M2/gsm8k | no_contention_observed | receiver_decode.cuda_event_s | 1319 | 4.588074 | 4.168131 | 8.356125 |
| M2/gsm8k | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 1319 | 0.058688 | 0.058652 | 0.060580 |
| M2/gsm8k | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 1319 | 0.040466 | 0.040092 | 0.043168 |
| M2/gsm8k | no_contention_observed | receiver_additional_prefill.cuda_event_s | 1319 | 0.040444 | 0.040070 | 0.043145 |
| M2/gsm8k | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 1319 | 0.056396 | 0.056298 | 0.065345 |
| M2/gsm8k | no_contention_observed | receiver_initial_prefill.cuda_event_s | 1319 | 0.056352 | 0.056262 | 0.065295 |
| M2/hotpotqa | no_contention_observed | sender_prefill.synchronized_wall_s | 7392 | 0.055317 | 0.056106 | 0.074008 |
| M2/hotpotqa | no_contention_observed | sender_prefill.cuda_event_s | 7392 | 0.055289 | 0.056078 | 0.073979 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7392 | 0.076768 | 0.075899 | 0.097509 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7392 | 0.076777 | 0.075908 | 0.097520 |
| M2/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7392 | 0.039143 | 0.038893 | 0.040555 |
| M2/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7392 | 0.039124 | 0.038873 | 0.040535 |
| M2/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7392 | 1.104386 | 1.094944 | 1.522935 |
| M2/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7392 | 1.104352 | 1.094896 | 1.522898 |
| M2/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7392 | 0.759814 | 0.735406 | 1.553447 |
| M2/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7392 | 0.759783 | 0.735364 | 1.553416 |
| M2/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7392 | 0.069553 | 0.068751 | 0.089943 |
| M2/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7392 | 0.245862 | 0.247854 | 0.334943 |
| M2/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7392 | 0.245827 | 0.247823 | 0.334922 |
| M2/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7392 | 0.050288 | 0.047213 | 0.062993 |
| M2/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7392 | 0.050243 | 0.047164 | 0.062944 |
| M2/hotpotqa | contended | sender_prefill.synchronized_wall_s | 13 | 0.079130 | 0.070170 | 0.133211 |
| M2/hotpotqa | contended | sender_prefill.cuda_event_s | 13 | 0.078843 | 0.070126 | 0.132036 |
| M2/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 13 | 0.106668 | 0.094192 | 0.140314 |
| M2/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 13 | 0.106755 | 0.094277 | 0.140407 |
| M2/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 13 | 0.056218 | 0.042780 | 0.081462 |
| M2/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 13 | 0.056188 | 0.042758 | 0.081419 |
| M2/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 13 | 1.499135 | 1.289707 | 2.430297 |
| M2/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 13 | 1.498954 | 1.289634 | 2.430222 |
| M2/hotpotqa | contended | receiver_decode.synchronized_wall_s | 13 | 0.970687 | 0.888578 | 2.307156 |
| M2/hotpotqa | contended | receiver_decode.cuda_event_s | 13 | 0.970601 | 0.888554 | 2.306987 |
| M2/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 13 | 0.093026 | 0.083551 | 0.121892 |
| M2/hotpotqa | contended | receiver_additional_prefill.synchronized_wall_s | 13 | 0.312468 | 0.293250 | 0.458365 |
| M2/hotpotqa | contended | receiver_additional_prefill.cuda_event_s | 13 | 0.312406 | 0.293222 | 0.458270 |
| M2/hotpotqa | contended | receiver_initial_prefill.synchronized_wall_s | 13 | 0.080771 | 0.077001 | 0.161193 |
| M2/hotpotqa | contended | receiver_initial_prefill.cuda_event_s | 13 | 0.080478 | 0.076937 | 0.159652 |
| M2/humaneval | no_contention_observed | sender_prefill.synchronized_wall_s | 164 | 0.032174 | 0.031893 | 0.033637 |
| M2/humaneval | no_contention_observed | sender_prefill.cuda_event_s | 164 | 0.032151 | 0.031870 | 0.033614 |
| M2/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 164 | 0.064360 | 0.064066 | 0.066905 |
| M2/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 164 | 0.064367 | 0.064072 | 0.066916 |
| M2/humaneval | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 164 | 0.038971 | 0.038864 | 0.039647 |
| M2/humaneval | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 164 | 0.038953 | 0.038846 | 0.039628 |
| M2/humaneval | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 164 | 0.255071 | 0.237212 | 0.354524 |
| M2/humaneval | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 164 | 0.255049 | 0.237190 | 0.354501 |
| M2/humaneval | no_contention_observed | receiver_decode.synchronized_wall_s | 164 | 6.139875 | 5.037773 | 12.328843 |
| M2/humaneval | no_contention_observed | receiver_decode.cuda_event_s | 164 | 6.139836 | 5.037704 | 12.328823 |
| M2/humaneval | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 164 | 0.057693 | 0.057448 | 0.059595 |
| M2/humaneval | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 164 | 0.047886 | 0.040149 | 0.070548 |
| M2/humaneval | no_contention_observed | receiver_additional_prefill.cuda_event_s | 164 | 0.047865 | 0.040128 | 0.070528 |
| M2/humaneval | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 164 | 0.058576 | 0.062895 | 0.066259 |
| M2/humaneval | no_contention_observed | receiver_initial_prefill.cuda_event_s | 164 | 0.058530 | 0.062846 | 0.066209 |
| M3/gsm8k | no_contention_observed | sender_prefill.synchronized_wall_s | 1319 | 0.041019 | 0.040578 | 0.044273 |
| M3/gsm8k | no_contention_observed | sender_prefill.cuda_event_s | 1319 | 0.040995 | 0.040555 | 0.044250 |
| M3/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 1319 | 0.062990 | 0.062920 | 0.065750 |
| M3/gsm8k | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 1319 | 0.062997 | 0.062927 | 0.065755 |
| M3/gsm8k | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 1319 | 0.029074 | 0.028952 | 0.030463 |
| M3/gsm8k | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 1319 | 0.029056 | 0.028933 | 0.030444 |
| M3/gsm8k | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 1319 | 0.220919 | 0.219449 | 0.236362 |
| M3/gsm8k | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 1319 | 0.220893 | 0.219422 | 0.236333 |
| M3/gsm8k | no_contention_observed | receiver_decode.synchronized_wall_s | 1319 | 4.395842 | 2.976508 | 19.637559 |
| M3/gsm8k | no_contention_observed | receiver_decode.cuda_event_s | 1319 | 4.395772 | 2.976515 | 19.636782 |
| M3/gsm8k | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 1319 | 0.057164 | 0.057176 | 0.059507 |
| M3/gsm8k | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 1319 | 0.033154 | 0.031731 | 0.037763 |
| M3/gsm8k | no_contention_observed | receiver_additional_prefill.cuda_event_s | 1319 | 0.033132 | 0.031712 | 0.037742 |
| M3/gsm8k | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 1319 | 0.047110 | 0.050597 | 0.055832 |
| M3/gsm8k | no_contention_observed | receiver_initial_prefill.cuda_event_s | 1319 | 0.047065 | 0.050554 | 0.055782 |
| M3/hotpotqa | no_contention_observed | sender_prefill.synchronized_wall_s | 7404 | 0.246308 | 0.246605 | 0.332857 |
| M3/hotpotqa | no_contention_observed | sender_prefill.cuda_event_s | 7404 | 0.246277 | 0.246575 | 0.332819 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 7404 | 0.075921 | 0.074715 | 0.095675 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 7404 | 0.075930 | 0.074721 | 0.095681 |
| M3/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 7404 | 0.029062 | 0.028928 | 0.030037 |
| M3/hotpotqa | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 7404 | 0.029044 | 0.028911 | 0.030019 |
| M3/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 7404 | 1.302330 | 1.287519 | 1.788124 |
| M3/hotpotqa | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 7404 | 1.302290 | 1.287480 | 1.788059 |
| M3/hotpotqa | no_contention_observed | receiver_decode.synchronized_wall_s | 7404 | 1.013618 | 0.679068 | 2.265411 |
| M3/hotpotqa | no_contention_observed | receiver_decode.cuda_event_s | 7404 | 1.013584 | 0.679038 | 2.265408 |
| M3/hotpotqa | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 7404 | 0.069386 | 0.068227 | 0.088610 |
| M3/hotpotqa | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 7404 | 0.055066 | 0.055121 | 0.073925 |
| M3/hotpotqa | no_contention_observed | receiver_additional_prefill.cuda_event_s | 7404 | 0.055042 | 0.055100 | 0.073901 |
| M3/hotpotqa | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 7404 | 0.036584 | 0.031935 | 0.052627 |
| M3/hotpotqa | no_contention_observed | receiver_initial_prefill.cuda_event_s | 7404 | 0.036543 | 0.031895 | 0.052570 |
| M3/hotpotqa | contended | sender_prefill.synchronized_wall_s | 1 | 0.250318 | 0.250318 | 0.250318 |
| M3/hotpotqa | contended | sender_prefill.cuda_event_s | 1 | 0.250126 | 0.250126 | 0.250126 |
| M3/hotpotqa | contended | receiver_conversion_fusion_inclusive.cuda_event_s | 1 | 0.152078 | 0.152078 | 0.152078 |
| M3/hotpotqa | contended | receiver_conversion_fusion_inclusive.synchronized_wall_s | 1 | 0.152166 | 0.152166 | 0.152166 |
| M3/hotpotqa | contended | receiver_final_prompt_prefill.synchronized_wall_s | 1 | 0.056437 | 0.056437 | 0.056437 |
| M3/hotpotqa | contended | receiver_final_prompt_prefill.cuda_event_s | 1 | 0.056395 | 0.056395 | 0.056395 |
| M3/hotpotqa | contended | prefill_pipeline_inclusive.synchronized_wall_s | 1 | 1.938959 | 1.938959 | 1.938959 |
| M3/hotpotqa | contended | prefill_pipeline_inclusive.cuda_event_s | 1 | 1.938883 | 1.938883 | 1.938883 |
| M3/hotpotqa | contended | receiver_decode.synchronized_wall_s | 1 | 0.819680 | 0.819680 | 0.819680 |
| M3/hotpotqa | contended | receiver_decode.cuda_event_s | 1 | 0.819622 | 0.819622 | 0.819622 |
| M3/hotpotqa | contended | receiver_conversion_fusion_modules_nested.cuda_event_s | 1 | 0.137834 | 0.137834 | 0.137834 |
| M3/hotpotqa | contended | receiver_additional_prefill.synchronized_wall_s | 1 | 0.056686 | 0.056686 | 0.056686 |
| M3/hotpotqa | contended | receiver_additional_prefill.cuda_event_s | 1 | 0.056643 | 0.056643 | 0.056643 |
| M3/hotpotqa | contended | receiver_initial_prefill.synchronized_wall_s | 1 | 0.106476 | 0.106476 | 0.106476 |
| M3/hotpotqa | contended | receiver_initial_prefill.cuda_event_s | 1 | 0.106415 | 0.106415 | 0.106415 |
| M3/humaneval | no_contention_observed | sender_prefill.synchronized_wall_s | 164 | 0.050805 | 0.042901 | 0.075526 |
| M3/humaneval | no_contention_observed | sender_prefill.cuda_event_s | 164 | 0.050780 | 0.042876 | 0.075498 |
| M3/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.cuda_event_s | 164 | 0.063495 | 0.063153 | 0.067152 |
| M3/humaneval | no_contention_observed | receiver_conversion_fusion_inclusive.synchronized_wall_s | 164 | 0.063501 | 0.063160 | 0.067167 |
| M3/humaneval | no_contention_observed | receiver_final_prompt_prefill.synchronized_wall_s | 164 | 0.029693 | 0.029477 | 0.031087 |
| M3/humaneval | no_contention_observed | receiver_final_prompt_prefill.cuda_event_s | 164 | 0.029675 | 0.029459 | 0.031068 |
| M3/humaneval | no_contention_observed | prefill_pipeline_inclusive.synchronized_wall_s | 164 | 0.279220 | 0.260702 | 0.388746 |
| M3/humaneval | no_contention_observed | prefill_pipeline_inclusive.cuda_event_s | 164 | 0.279197 | 0.260666 | 0.388728 |
| M3/humaneval | no_contention_observed | receiver_decode.synchronized_wall_s | 164 | 8.521769 | 4.423194 | 29.775579 |
| M3/humaneval | no_contention_observed | receiver_decode.cuda_event_s | 164 | 8.521756 | 4.423193 | 29.775333 |
| M3/humaneval | no_contention_observed | receiver_conversion_fusion_modules_nested.cuda_event_s | 164 | 0.057476 | 0.057180 | 0.060774 |
| M3/humaneval | no_contention_observed | receiver_additional_prefill.synchronized_wall_s | 164 | 0.033432 | 0.031822 | 0.038404 |
| M3/humaneval | no_contention_observed | receiver_additional_prefill.cuda_event_s | 164 | 0.033410 | 0.031802 | 0.038381 |
| M3/humaneval | no_contention_observed | receiver_initial_prefill.synchronized_wall_s | 164 | 0.045318 | 0.044985 | 0.055658 |
| M3/humaneval | no_contention_observed | receiver_initial_prefill.cuda_event_s | 164 | 0.045275 | 0.044942 | 0.055609 |

## 附录：口径与证据

- 本报告统计P4的C2C路径；协议与路径分别汇总。
- 本轮Receiver输出上限为1024；T2T沿其既定预算，成本比较同时列出实际输出token数。
- 数学首个####正则、问答整段EM/F1、代码原样补全；OOM/输入容量失败计0，触顶按实际前缀正常评分，固定分母不删除失败题。
- 质量与配对差值均为10000次seed42 percentile bootstrap；配对按同方向/协议/任务/ID及明确的基线路径，完整覆盖规定视图。
- 未测项保持未知；异常部分成本单列；inclusive/nested计时不能相加，参数联合模块去重计一次。
- 通信分列原始KV、补传原文、序列化payload、metadata及每包8字节帧；P2 C2C合计两个方向的补传。逐包方向记录在 supplemental_transfers 中。计时拓扑为同机TCP回环。
- P2–P4先记录Receiver初始Prefill，再记录补齐后的完整输入重建；P2 C2C另记录Sender初始与重建Prefill。完整重建保留所有原始任务信息。没有文本生成消息、筛选、池化或广播。
- GPU用CUDA Event与同步墙钟，CPU操作用墙钟。每任务3条合成预热、每条8tokens；每正式题单次生成。快照观测开销保留，不扣估计常数。
- 正文只列关键阶段，附件列实际已采集全部分项。逐题成绩见共享的评测记录。
