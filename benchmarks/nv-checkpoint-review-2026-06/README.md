# Ramsey Checkpoint Benchmark

This benchmark packages five OpenClaw/NV Ramsey checkpoints from the completed
`image145844` case. It is designed for a reasoning-effort sweep with the same
agent-visible evidence held fixed within each checkpoint.

Each checkpoint is a pre-analysis review state: project files, memory,
knowledge, context, and prior evidence come from immediately after the target
Ramsey job was launched. The only later files added are the terminal raw
measurement export and bridge metadata for that same Ramsey. This avoids giving
the model the original agent's post-measurement review, autosave review, or next
action as a hint.

The benchmark intentionally uses neutral checkpoint and evidence filenames
(`cp01`, `e001.json`, and so on). Source filenames and wake-record provenance are
kept outside the agent-visible checkpoint folders.

## Agent Task

Each run is framed as a normal NV project wake after a Ramsey measurement has
completed. The prompt asks the model to analyze the new measurement data, use
local tools such as Python when useful, write a root-level project note, include
a compact note section in the final handoff, and choose the next action:

```text
A Ramsey measurement has just completed. Analyze the new measurement data
together with the provided project context, using quantitative checks where
they matter.

Create ramsey_review.md ...

Then reply with a short handoff summary, the next action, and a compact Project note.
```

## Reported Sweep

- Checkpoints: `cp01` through `cp05`
- Reasoning efforts: `low`, `medium`, `high`, `xhigh`
- Replicates per checkpoint-effort pair: `20`
- Total runs: `5 x 4 x 20 = 400`

The package contains inputs, prompt text, run scripts, scoring helpers, manual
scoring CSVs, recovered project notes, and the figure summary used in the
manuscript.

Each model run is launched in a temporary directory containing only one
checkpoint snapshot and the task prompt. The runner uses a writable sandbox
scoped to that temporary directory, so the agent can use shell/Python tools for
local file inspection and scratch calculations without access to labels,
provenance maps, or later checkpoints. The runner first captures root-level
`ramsey_review.md`; it also preserves legacy Markdown notes under `work/notes/`
when accessible. If file capture fails, the final response's `Project note`
section is used as the note text in `model_outputs.jsonl`.

## Layout

- `inputs/checkpoints/`: agent-visible checkpoint snapshots with neutral names.
  Each checkpoint has `project/`, `md/`, launch-time `evidence/`, and terminal
  target-Ramsey `measurement/`.
- `inputs/checkpoint_index.csv`: checkpoint provenance and leakage-audit status.
- `prompts/task.md`: exact benchmark task prompt.
- `labels/scoring_guide.md`: binary scoring rubric.
- `scripts/build_inputs.py`: rebuilds neutral pre-analysis checkpoint inputs
  from local wake-record snapshots and terminal raw measurement artifacts.
- `scripts/run_sweep.py`: runs Codex CLI over checkpoints, efforts, and
  replicates.
- `scripts/score_outputs.py`: applies an automatic first-pass binary score to
  the final response plus the captured project note.

## Build Inputs

```powershell
python scripts\build_inputs.py
```

## Run

Run one effort:

```powershell
python scripts\run_sweep.py --model gpt-5.5 --reasoning-effort high --replicates 10
```

Run all four efforts:

```powershell
python scripts\run_sweep.py --model gpt-5.5 --reasoning-effort all --replicates 10
```

Resume only failed or missing runs in an existing result file:

```powershell
python scripts\run_sweep.py --model gpt-5.5 --reasoning-effort all --replicates 10 --retry-failed
```

## Score

```powershell
python scripts\score_outputs.py results\model_outputs.jsonl
```

The manuscript uses manual scores in
`results/manual_calibration_residual_scores_2026-07-11.csv`.  This file contains
one binary calibration residual score for all 400 runs, with a short rationale
for each score.  The aggregated values used for the figure are in
`results/figures/reasoning_effort_sweep_low_to_xhigh_summary.csv`.

The automatic score script is retained as a first-pass helper.  Borderline
responses should be audited against `labels/scoring_guide.md`.
