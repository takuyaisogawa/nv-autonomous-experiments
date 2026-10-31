# Case: image145844

This case covers the selection of an NV center aligned with the magnetic field
in the `image145844` region, pODMR screening, Ramsey measurements, and subsequent
reanalysis of the Ramsey data.

## Start Here

| Entry point | Why it matters |
| --- | --- |
| [Full walkthrough](../../docs/case_walkthrough.md) | Cross-case timeline and audit guide |
| [Main project state](project/work/state.md) | Final status, findings, and limitations |
| [Evidence ledger](project/.manager/evidence.jsonl) | Append-only evidence index |
| [Work notes](project/work/notes/) | Time-ordered reasoning and decisions |
| [Bridge records](project/work/bridge_jobs/) | Submit/status/result records from the MATLAB bridge |
| [Analysis outputs](project/work/artifacts/analysis/) | JSON reviews, model comparisons, and case scripts |
| [Figures](project/work/artifacts/figures/) | pODMR, Ramsey, drift, and model-review plots |
| [Recovered raw MATLAB data](project/data_recovered_20260514/matlab_23C/) | Raw saved image and savedexperiment MAT files recovered for this release |

## Reading Summary

The agent rejected `r01` and `r02` because analysis of the raw pODMR readouts
showed no clear usable resonances. It accepted `r03` as aligned with the magnetic
field after strong-pi and weak-pi pODMR measurements, then varied the conditions
of subsequent Ramsey measurements.

The analysis did not establish a reliable value of T2star or identify coupling to an
individual nearby 13C nucleus. The agent later revised its interpretation of
the Ramsey frequency after considering a residual calibration error.

The revised final report is
[image145844_reimage_r03_shifted_sideband_recloseout_report_20260514_1320.pdf](project/work/artifacts/reports/20260514_1320_r03_shifted_sideband_recloseout/image145844_reimage_r03_shifted_sideband_recloseout_report_20260514_1320.pdf).

## Model Provenance

| Field | Value |
| --- | --- |
| Project-execution agent | `nv-researcher` |
| Model | `openai-codex/gpt-5.5` |
| Thinking level | `xhigh` |

The archived `project.json` for this case uses an older metadata
format, so the explicit model fields are recorded here and in `case.yaml` for
the public release. See
[model and agent configuration](../../docs/model_and_agent_configuration.md).

## Representative Artifacts

| Artifact | Role |
| --- | --- |
| [Candidate selection figure](project/work/artifacts/figures/image145844_reimage_candidate_selection_20260513_1550.png) | Candidates in the new image, before measurements on r01, r02, and r03 |
| [Strong-pi pODMR measurement on r03](project/work/artifacts/figures/image145844_reimage_r03_strong_podmr_raw_review_20260513_1741.png) | pODMR data used to assess whether r03 was aligned with the magnetic field |
| [Final Ramsey measurement after recalibration](project/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.png) | Analysis of the final Ramsey measurement |
| [Ramsey reanalysis figure](project/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_20260514_1308.png) | Reanalysis of the Ramsey frequency allowing for a residual calibration error |
