# Case: image145844

Latest completed case study for an aligned NV candidate selected from the
`image145844` region, including pODMR screening, Ramsey follow-up, and revised
Ramsey frequency reanalysis.

## Start Here

| Entry point | Why it matters |
| --- | --- |
| [Full walkthrough](../../docs/case_walkthrough.md) | Cross-case timeline and audit guide |
| [Main project state](project/work/state.md) | Final state, current findings, claim boundary |
| [Evidence ledger](project/.manager/evidence.jsonl) | Append-only evidence index |
| [Work notes](project/work/notes/) | Time-ordered reasoning and decisions |
| [Bridge records](project/work/bridge_jobs/) | Submit/status/result records from the MATLAB bridge |
| [Analysis outputs](project/work/artifacts/analysis/) | JSON reviews, model comparisons, and case scripts |
| [Figures](project/work/artifacts/figures/) | pODMR, Ramsey, drift, and model-review plots |
| [Recovered raw MATLAB data](project/data_recovered_20260514/matlab_23C/) | Raw saved image and savedexperiment MAT files recovered for this release |

## Reading Summary

The agent rejected fresh `r01` and `r02` for alignment selection after
raw/readout-aware pODMR reviews did not show clear usable resonances. It
accepted `r03` after strong-pi and weak-pi pODMR evidence, then ran multiple
Ramsey branches with changed measurement conditions rather than blind repeats.

## Model Provenance

| Field | Value |
| --- | --- |
| Project-execution agent | `nv-researcher` |
| Model | `openai-codex/gpt-5.5` |
| Thinking level | `xhigh` |

The archived `project.json` for this case uses an earlier startup metadata
shape, so the explicit model fields are recorded here and in `case.yaml` for
the public release. See
[model and agent configuration](../../docs/model_and_agent_configuration.md).

The final revised closeout is
[image145844_reimage_r03_shifted_sideband_recloseout_report_20260514_1320.pdf](project/work/artifacts/reports/20260514_1320_r03_shifted_sideband_recloseout/image145844_reimage_r03_shifted_sideband_recloseout_report_20260514_1320.pdf).

Final claim boundary: aligned `r03` found; no unconditional claim-grade numeric
T2star; the Ramsey frequency interpretation was revised after considering a
residual calibration offset, but the data do not establish an independently
confirmed nearby-13C coupling claim.

## Representative Artifacts

| Artifact | Role |
| --- | --- |
| [Candidate selection figure](project/work/artifacts/figures/image145844_reimage_candidate_selection_20260513_1550.png) | Shows the re-image candidate map used before r01/r02/r03 screening |
| [Accepted r03 strong-pi pODMR review](project/work/artifacts/figures/image145844_reimage_r03_strong_podmr_raw_review_20260513_1741.png) | Alignment-screen evidence for the accepted candidate |
| [Final refreshed-center Ramsey review](project/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.png) | Main final Ramsey dataset review |
| [Ramsey reanalysis figure](project/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_20260514_1308.png) | Revised Ramsey frequency interpretation after considering a residual calibration offset |
