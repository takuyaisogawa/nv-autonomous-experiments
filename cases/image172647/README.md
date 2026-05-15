# Case: image172647

Completed aligned-NV case study with fresh re-imaging after a stale-candidate
failure, pODMR-based candidate rejection/acceptance, weak-pi center refinement,
multi-detuning Ramsey follow-up, and CPMG N=8 corroboration of a weak
nearby-13C-like signature.

## Start Here

| Entry point | Why it matters |
| --- | --- |
| [Full walkthrough](../../docs/case_walkthrough.md) | Cross-case timeline and audit guide |
| [Main project state](project/work/state.md) | Final state, decisions, claim boundary, evidence pointers |
| [Evidence ledger](project/.manager/evidence.jsonl) | Append-only evidence index |
| [Work notes](project/work/notes/) | Time-ordered reasoning and decisions |
| [Bridge records](project/work/bridge_jobs/) | Submit/status/result records from the MATLAB bridge |
| [Analysis outputs](project/work/artifacts/analysis/) | JSON reviews, model comparisons, and case scripts |
| [Figures](project/work/artifacts/figures/) | pODMR, Ramsey, CPMG, and target-region review plots |
| [Closeout report](project/work/reports/closeout_20260515_1225/nv23_image172647_closeout_report_20260515.pdf) | Final PDF case report |
| [Recovered raw MATLAB data](project/data_recovered_20260515/matlab_23C/) | Raw saved image, imaging exports, and savedexperiment MAT files recovered for this release |

## Reading Summary

The agent began from the `image172647` saved image, but the first candidate
became low-count/stale before useful pODMR data could be acquired. It performed
a fresh re-image of the original region, rejected `reimage1804_c01` after a
healthy but no-clear-resonance strong-pi pODMR scan, and accepted
`reimage1804_c02` after a clear signal-only strong-pi pODMR resonance.

The accepted branch then proceeded through weak-pi pODMR center refinement,
three Ramsey datasets at different programmed detunings, and a CPMG N=8 tau
scan designed as an independent discriminator for the weak 13C-like candidate.

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

Final claim boundary: aligned `reimage1804_c02` found; T2star is supported as a
short/few-us order, about `2-3 us` but method-sensitive; the data support a
likely weak/moderate nearby-13C-like signature from det-shift Ramsey plus CPMG
target-region corroboration, but not precise coupling extraction or a
publication-grade single-spin claim.

## Representative Artifacts

| Artifact | Role |
| --- | --- |
| [Fresh re-image candidate map](project/work/artifacts/figures/image172647_reimage1804_candidate_peaks_20260514_1812.png) | Candidate ranking after the stale initial candidate failure |
| [Rejected c01 pODMR review](project/work/artifacts/figures/reimage1804_c01_podmr_terminal_4avg_20260514_1859.png) | Healthy-count pODMR scan used to reject `reimage1804_c01` |
| [Accepted c02 strong-pi pODMR review](project/work/artifacts/figures/reimage1804_c02_podmr_terminal_4avg_20260514_1957.png) | Alignment-screen evidence for the accepted branch |
| [Weak-pi pODMR refinement](project/work/artifacts/figures/reimage1804_c02_weak_pi_podmr_terminal_4avg_20260514_2251.png) | Microwave-center refinement used for later Ramsey/CPMG planning |
| [det=1.0 Ramsey terminal review](project/work/artifacts/figures/reimage1804_c02_ramsey_det1_terminal_16avg_20260515_0245.png) | Short/few-us T2star and weak high-sideband candidate evidence |
| [det=1.25 Ramsey terminal review](project/work/artifacts/figures/reimage1804_c02_ramsey_det1p25_terminal_16avg_20260515_0645.png) | Third-detuning artifact discriminator |
| [CPMG N=8 target-region review](project/work/artifacts/figures/reimage1804_c02_cpmg_n8_terminal_target_region_20260515_0945.png) | Independent CPMG corroboration of the weak nearby-13C-like feature |
