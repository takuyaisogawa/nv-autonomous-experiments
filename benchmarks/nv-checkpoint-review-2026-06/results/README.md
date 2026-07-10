# Results

This directory contains the results used for the manuscript Ramsey checkpoint
benchmark.

Key files:

- `manual_rescore_codex_2026-06-30.csv`: manual binary scores for all 400 runs,
  including the broader residual-offset score, the stricter calibration-residual
  score, and scoring rationales.
- `manual_rescore_codex_2026-06-30_summary.csv`: checkpoint-level summaries for
  both criteria.
- `figures/reasoning_effort_sweep_low_to_xhigh_summary.csv`: figure source data
  used in the manuscript.
- `figures/reasoning_effort_sweep_low_to_xhigh.pdf` and `.png`: rendered figure
  outputs.
- `low_preanalysis_rootnote_2026-06-16/notes/`: recovered project notes for the
  low reasoning runs.
- `mhx_preanalysis_wake_2026-06-16/notes/`: recovered project notes for the
  medium, high, and xhigh reasoning runs.

Raw execution logs and full model output JSONL files are not part of the public
release.
