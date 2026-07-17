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
- [Per run manual scores and rationales](../../../nv-checkpoint-review-2026-06/results/manual_calibration_residual_scores_2026-07-11.csv)
- [Aggregate score table](../../../nv-checkpoint-review-2026-06/results/manual_calibration_residual_summary_2026-07-11.csv)
- [Combined three model checkpoint table](../../ramsey/three_model_checkpoint_summary.csv)

## pODMR data evaluation benchmark

- [Benchmark method, inputs, and labels](../../../podmr-model-first-resonance-2026-05/)
- [Low reasoning records](../../../podmr-model-first-resonance-2026-05/results/gpt-5.5-low/readout_only_three_conditions/)
- [Medium reasoning records](../../../podmr-model-first-resonance-2026-05/results/gpt-5.5-medium/readout_only_three_conditions/)
- [High reasoning records](../../../podmr-model-first-resonance-2026-05/results/gpt-5.5-high/readout_only_three_conditions/)
- [X-high reasoning records](../../../podmr-model-first-resonance-2026-05/results/gpt-5.5-xhigh/readout_only_three_conditions/)
- [Combined three model measurement bootstrap table](../../podmr/three_model_case_bootstrap.csv)

Shared conditions and the execution dates recovered from the released output
timestamps are in [run_conditions.json](../../run_conditions.json).
