# Ramsey Checkpoint Benchmark

This benchmark packages five OpenClaw/NV Ramsey checkpoints from the completed
`image145844` case. It is designed for a reasoning-effort sweep with the same
agent-visible evidence held fixed within each checkpoint.

Each checkpoint contains the information available before analysis of the new
Ramsey measurement. Project files, memory, knowledge, context, and prior
evidence were copied from immediately after that measurement was launched.
The completed measurement data and bridge metadata were then added. The
original agent's analyses of that measurement and its next action were excluded.

The benchmark intentionally uses neutral checkpoint and evidence filenames
(`cp01`, `e001.json`, and so on). Source filenames and wake-record provenance are
kept outside the agent-visible checkpoint folders.

## Agent Task

Each run asks the agent to resume the project after a Ramsey measurement has
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

- Models: GPT-5.4, GPT-5.5, GPT-5.6 Sol
- Checkpoints: `cp01` through `cp05`
- Reasoning efforts: `low`, `medium`, `high`, `xhigh`
- Replicates per checkpoint-effort pair: `20`
- Runs per model: `5 x 4 x 20 = 400`
- Three model total: `1,200`

This package contains the shared inputs, prompt text, run scripts, scoring
helpers, and the original GPT-5.5 records.  The GPT-5.4 and GPT-5.6 Sol records
and the combined figure source table are in the
[three model comparison release](../three-model-comparison-2026-07/README.md).

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
- `scripts/run_sweep_claude.py`: post-release Claude CLI adapter using the same
  checkpoints, task prompt, note collection, and resume format.
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

Run a small Claude pilot:

```powershell
python scripts\run_sweep_claude.py `
  --model "FULL_MODEL_ID" `
  --reasoning-effort low `
  --replicates 2 `
  --checkpoint cp01 `
  --jobs 1 `
  --max-budget-usd 10 `
  --result-dir results\claude-local\pilot
```

The Claude adapter instructs the agent to open PNG evidence with its Read tool
instead of attaching images to the first message. It records the exact model
argument, CLI version, task-prompt hash, and image-delivery method in
`run_conditions.json`. This adapter was added after the manuscript runs. A
comparison against the released Codex results should therefore report the
harness difference. For a new provider comparison with matched pODMR image
delivery, use the provider-neutral per-case runner in the pODMR benchmark.

## Current manuscript scores

The manuscript uses the fixed [GPT-6.1 Sol/high LLM judge](../three-model-comparison-2026-07/ramsey/llm_judge/).
Its 1,200 labels, full prompt, execution settings, and human validation
(96/100 agreement) are released there. The previous scores below are preserved
and compared with the judge results; they are not the human validation labels.

## Previous scoring workflow

```powershell
python scripts\score_outputs.py results\model_outputs.jsonl
```

The original GPT-5.5 sweep uses manual scores in
`results/manual_calibration_residual_scores_2026-07-11.csv`.  This file contains
a PASS/FAIL label and a short rationale for each of the 400 runs. The aggregated
values used for the figure are in
`results/figures/reasoning_effort_sweep_low_to_xhigh_summary.csv`.

The results for the three models reported in the manuscript and the corresponding
GPT-5.4 and GPT-5.6 Sol per-run records are in
`../three-model-comparison-2026-07/ramsey/`.

The automatic score script is retained as a first-pass helper.  Borderline
responses should be audited against `labels/scoring_guide.md`.
