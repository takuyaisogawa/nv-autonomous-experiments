# Results

This directory contains the original GPT-5.5 notes and previous manual scores
for the Ramsey checkpoint benchmark. The current manuscript uses
[LLM-judge scores](../../three-model-comparison-2026-07/ramsey/llm_judge/).
GPT-5.4, GPT-5.6 Sol, and the combined three-model tables are in
`../../three-model-comparison-2026-07/ramsey/`.

Key files:

- `manual_calibration_residual_scores_2026-07-11.csv`: manual calibration
  residual scores and rationales for all 400 runs.
- `manual_calibration_residual_summary_2026-07-11.csv`: checkpoint-level
  summaries for the single criterion.
- `figures/reasoning_effort_sweep_low_to_xhigh_summary.csv`: figure source data
  used for the previous GPT-5.5 figure.
- `figures/reasoning_effort_sweep_low_to_xhigh.pdf` and `.png`: rendered figure
  outputs.
- `low_preanalysis_rootnote_2026-06-16/notes/`: recovered project notes for the
  low reasoning runs.
- `mhx_preanalysis_wake_2026-06-16/notes/`: recovered project notes for the
  medium, high, and xhigh reasoning runs.

Raw execution logs and full model output JSONL files are not part of the public
release.
