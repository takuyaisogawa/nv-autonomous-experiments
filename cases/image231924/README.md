# Case: image231924

This case records how the agent selected an NV center aligned with the
magnetic field, calibrated its resonance frequency, and estimated T2star.

## Start Here

| Entry point | Why it matters |
| --- | --- |
| [Full walkthrough](../../docs/case_walkthrough.md) | Cross-case timeline and audit guide |
| [Main project state](project/work/state.md) | Final status, findings, and limitations |
| [Evidence ledger](project/.manager/evidence.jsonl) | Append-only evidence index |
| [Work notes](project/work/notes/) | Time-ordered reasoning and decisions |
| [Bridge records](project/work/bridge_jobs/) | Submit/status/result records from the MATLAB bridge |
| [Analysis outputs](project/work/artifacts/analysis/) | JSON reviews, model comparisons, and case scripts |
| [Figures](project/work/artifacts/figures/) | pODMR, Ramsey, and final summary plots |
| [Raw/data copy](project/data_git_20260512/) | Raw and processed data snapshot included for this case |

## Reading Summary

After a failed pODMR measurement, the agent restored tracking and used
strong-pi pODMR to identify an NV center aligned with the magnetic field.
It refined the resonance frequency with weak-pi pODMR and repeated the
Ramsey measurement using the updated microwave frequency.

## Model Provenance

| Field | Value |
| --- | --- |
| Project-execution agent | `nv-researcher` |
| Model | `openai-codex/gpt-5.5` |
| Thinking level | `xhigh` |

The archived `project.json` for this case includes
`project_execution_agent_model` and `project_execution_agent_thinking` under
`research_architecture`. See
[model and agent configuration](../../docs/model_and_agent_configuration.md).

The final report is
[closeout_20260512_0525.pdf](project/summaries/closeout_20260512_0525.pdf).

The agent identified `image231924_c01` as aligned with the magnetic field and
estimated T2star at about `4 us`. It did not resolve coupling to an individual
nearby 13C nucleus in the repeated Ramsey measurement.

## Representative Artifacts

| Artifact | Role |
| --- | --- |
| [Candidate map](project/work/artifacts/figures/image231924_candidate_map.png) | Candidate selection context for the image region |
| [Strong-pi pODMR retry review](project/work/artifacts/figures/image231924_c01_strong_podmr_retry1_review.png) | Alignment-screen evidence after recovery from the invalid first acquisition |
| [Narrow weak-pi pODMR review](project/work/artifacts/figures/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.png) | Resonant frequency refinement used before the repeated Ramsey measurement |
| [Ramsey measurement after recalibration](project/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_review.png) | Final Ramsey dataset used to estimate T2star and assess possible 13C coupling |
