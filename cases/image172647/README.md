# Case: image172647

This case follows the agent from new imaging after loss of the initial
candidate through NV selection, resonance frequency calibration, Ramsey
measurements at several detunings, and an N=8 CPMG measurement to investigate
a possible 13C contribution.

## Start Here

| Entry point | Why it matters |
| --- | --- |
| [Full walkthrough](../../docs/case_walkthrough.md) | Cross-case timeline and audit guide |
| [Main project state](project/work/state.md) | Final status, decisions, limitations, and links to evidence |
| [Evidence ledger](project/.manager/evidence.jsonl) | Append-only evidence index |
| [Work notes](project/work/notes/) | Time-ordered reasoning and decisions |
| [Bridge records](project/work/bridge_jobs/) | Submit/status/result records from the MATLAB bridge |
| [Analysis outputs](project/work/artifacts/analysis/) | JSON reviews, model comparisons, and case scripts |
| [Figures](project/work/artifacts/figures/) | Plots of the pODMR, Ramsey, and CPMG measurements |
| [Final report](project/work/reports/closeout_20260515_1225/nv23_image172647_closeout_report_20260515.pdf) | Final PDF case report |
| [Recovered raw MATLAB data](project/data_recovered_20260515/matlab_23C/) | Raw saved image, imaging exports, and savedexperiment MAT files recovered for this release |

## Reading Summary

The agent began from the `image172647` saved image, but the photon count from
the first candidate fell before useful pODMR data could be acquired. It acquired
a new image of the same region and rejected `reimage1804_c01` after a strong-pi
pODMR scan with adequate photon counts but no clear resonance. It accepted
`reimage1804_c02` as aligned with the magnetic field after observing a clear
resonance in the signal readout of its strong-pi pODMR scan.

The agent refined the resonance frequency with weak-pi pODMR and acquired
three Ramsey datasets at different programmed detunings. It then varied the
pulse spacing in an N=8 CPMG scan to investigate a possible 13C contribution to
the weak frequency components in the Ramsey spectra.

The agent reported a T2star estimate of about `2-3 us`, depending on the
analysis method.
It interpreted the CPMG response as supporting a 13C origin for the weak
frequency components in the Ramsey spectra. The surrounding 13C spin bath
could contribute to both signals, but the CPMG response does not establish that
the same interactions explain the Ramsey components.

## Model Provenance

| Field | Value |
| --- | --- |
| Project-execution agent | `nv-researcher` |
| Model | `openai-codex/gpt-5.5` |
| Thinking level | `xhigh` |

The archived `project.json` records the `nv-researcher` project-execution route
but does not preserve the explicit model fields in the same shape as newer
metadata. Those fields are recorded here and in `case.yaml` for the public
release. See
[model and agent configuration](../../docs/model_and_agent_configuration.md).

## Representative Artifacts

| Artifact | Role |
| --- | --- |
| [Candidates in the new image](project/work/artifacts/figures/image172647_reimage1804_candidate_peaks_20260514_1812.png) | Candidate ranking from the new image |
| [Rejected c01 pODMR review](project/work/artifacts/figures/reimage1804_c01_podmr_terminal_4avg_20260514_1859.png) | pODMR scan with adequate photon counts but no clear resonance |
| [Strong-pi pODMR measurement on c02](project/work/artifacts/figures/reimage1804_c02_podmr_terminal_4avg_20260514_1957.png) | pODMR data used to assess whether c02 was aligned with the magnetic field |
| [Weak-pi pODMR refinement](project/work/artifacts/figures/reimage1804_c02_weak_pi_podmr_terminal_4avg_20260514_2251.png) | Resonant frequency refinement used for later Ramsey and CPMG planning |
| [Ramsey measurement at 1.0 MHz detuning](project/work/artifacts/figures/reimage1804_c02_ramsey_det1_terminal_16avg_20260515_0245.png) | T2star estimate and weak frequency components in the Ramsey spectrum |
| [Ramsey measurement at 1.25 MHz detuning](project/work/artifacts/figures/reimage1804_c02_ramsey_det1p25_terminal_16avg_20260515_0645.png) | Ramsey measurement at a third detuning to test how the weak frequency components shift |
| [CPMG result (N = 8)](project/work/artifacts/figures/reimage1804_c02_cpmg_n8_terminal_target_region_20260515_0945.png) | CPMG response that the agent interpreted as supporting a possible 13C contribution |
