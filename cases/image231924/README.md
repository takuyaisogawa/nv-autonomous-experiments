# Case: image231924

Completed aligned-NV and T2star case study with pODMR center refinement,
corrected-center Ramsey follow-up, and closeout report.

## Start Here

| Entry point | Why it matters |
| --- | --- |
| [Full walkthrough](../../docs/case_walkthrough.md) | Cross-case timeline and audit guide |
| [Main project state](project/work/state.md) | Final state, current findings, claim boundary |
| [Evidence ledger](project/.manager/evidence.jsonl) | Append-only evidence index |
| [Work notes](project/work/notes/) | Time-ordered reasoning and decisions |
| [Bridge records](project/work/bridge_jobs/) | Submit/status/result records from the MATLAB bridge |
| [Analysis outputs](project/work/artifacts/analysis/) | JSON reviews, model comparisons, and case scripts |
| [Figures](project/work/artifacts/figures/) | pODMR, Ramsey, and corrected-center closeout plots |
| [Raw/data copy](project/data_git_20260512/) | Raw and processed data snapshot included for this case |

## Reading Summary

The agent recovered from an invalid first pODMR acquisition, re-established
trackability, passed a strong-pi pODMR alignment screen, refined the microwave
center with weak-pi pODMR, and used a corrected-center Ramsey repeat as the
closeout dataset.

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

The final closeout report is
[closeout_20260512_0525.pdf](project/summaries/closeout_20260512_0525.pdf).

Final claim boundary: aligned `image231924_c01` found; T2star scale about
`4 us`; no resolved nearby 13C coupling in the corrected-center Ramsey data.

## Representative Artifacts

| Artifact | Role |
| --- | --- |
| [Candidate map](project/work/artifacts/figures/image231924_candidate_map.png) | Candidate selection context for the image region |
| [Strong-pi pODMR retry review](project/work/artifacts/figures/image231924_c01_strong_podmr_retry1_review.png) | Alignment-screen evidence after recovery from the invalid first acquisition |
| [Narrow weak-pi pODMR review](project/work/artifacts/figures/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.png) | Microwave-center refinement used before the corrected-center Ramsey |
| [Corrected-center Ramsey terminal review](project/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_review.png) | Main closeout dataset supporting the T2star and 13C-negative boundary |
