# GPT-5.5 Benchmark Records

| Field | Value |
| --- | --- |
| Manuscript name | GPT-5.5 |
| Model argument | `gpt-5.5` |
| pODMR execution date | 2026-06-06 UTC |
| Ramsey execution date | 2026-06-16 UTC |
| Ramsey runs | 400 |
| pODMR decisions | 3,456 |

The GPT-5.5 records were released in the original benchmark directories before
the three model comparison was assembled.  This page provides the same model
level entry points as the GPT-5.4 and GPT-5.6 Sol indexes without duplicating
those records.

## Ramsey checkpoint benchmark

- [Benchmark method and inputs](../../../nv-checkpoint-review-2026-06/)
- [LLM-judge scores used in the current manuscript](../../ramsey/llm_judge/)
- [Checkpoint counts from the LLM judge for the original three models](../../ramsey/llm_judge/checkpoint_summary.csv)
- [Previous manual scores and rationales](../../../nv-checkpoint-review-2026-06/results/manual_calibration_residual_scores_2026-07-11.csv)
- [Previous manual scores grouped by checkpoint and reasoning setting](../../../nv-checkpoint-review-2026-06/results/manual_calibration_residual_summary_2026-07-11.csv)
- [Previous checkpoint scores for all three models](../../ramsey/three_model_checkpoint_summary.csv)

## pODMR data evaluation benchmark

- [Benchmark method, inputs, and labels](../../../podmr-model-first-resonance-2026-05/)
- [Low reasoning records](../../../podmr-model-first-resonance-2026-05/results/gpt-5.5-low/)
- [Medium reasoning records](../../../podmr-model-first-resonance-2026-05/results/gpt-5.5-medium/)
- [High reasoning records](../../../podmr-model-first-resonance-2026-05/results/gpt-5.5-high/)
- [X-high reasoning records](../../../podmr-model-first-resonance-2026-05/results/gpt-5.5-xhigh/)
- [pODMR results and bootstrap confidence intervals for the original three models](../../podmr/three_model_case_bootstrap.csv)

Shared conditions and the execution dates recovered from the released output
timestamps are in [run_conditions.json](../../run_conditions.json).
