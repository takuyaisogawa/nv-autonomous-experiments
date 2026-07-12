# Method

This benchmark holds retrospective checkpoint evidence fixed and varies only
model reasoning effort.

The checkpoint construction is pre-analysis by design. For each target Ramsey,
the project snapshot is taken from immediately after that Ramsey job was
launched. The benchmark then adds only the terminal raw measurement data and
bridge job metadata for that target Ramsey. It does not add the original
post-measurement review, autosave reviews for that same target, figures, notes,
model-comparison artifacts, or the subsequent action chosen by the original
agent.

Each checkpoint package contains:

- Project state and brief from the corresponding wake-record snapshot.
- The human-advice file from that snapshot.
- The snapshot startup memory and detailed knowledge files.
- Evidence files referenced in that wake, renamed to neutral identifiers.
- Terminal raw measurement export and bridge job metadata for the target Ramsey,
  renamed to neutral identifiers under `measurement/`.
- A sanitized context metadata file with source paths and basenames replaced by
  neutral checkpoint-local names.

The five checkpoints are ordered chronologically but named only `cp01` through
`cp05` in agent-visible inputs. The agent is not given source wake names, source
artifact names, labels, or the scoring rubric.

The visible task is phrased as an ordinary project wake: a Ramsey measurement
has completed, the agent should analyze the available data with quantitative
checks, write a concise project note at root-level `ramsey_review.md`, include a
compact `Project note` section in the final handoff, and recommend the next
action. The prompt does not mention the discovery criterion, the scoring rubric,
or that outputs will be scored.

## Scoring

A run receives one binary calibration residual score. A response passes only if
the final response or captured project note suspects that the nominal Ramsey
detuning may include a residual offset from resonance frequency or microwave
frequency calibration, the `mw_freq` choice, or an equivalent calibrated
frequency basis error. A response fails if it only withholds T2star or 13C
claims, notes a frequency mismatch or detuning response without a calibration
source, proposes residual or effective detuning without connecting it to
calibration, or only requests more measurements.

The next-action recommendation is used as evidence for the binary score, not as
a separate action-quality metric.

## Leakage Controls

- The benchmark runner copies only the selected checkpoint folder and prompt
  into a temporary working directory for each model run, then launches Codex
  with a writable sandbox scoped to that temporary directory so the agent can
  use shell/Python tools for local inspection and scratch calculations.
- The runner silently preserves Markdown notes written under `work/notes/` in
  `results/notes/<run-id>/` when accessible. Root-level `ramsey_review.md` is
  the preferred captured note. If file capture fails, the runner falls back to
  the final response's `Project note` section for later scoring and manual
  audit.
- Agent-visible checkpoint folders use neutral filenames.
- All non-measurement files are from the launch-time snapshot for that target
  Ramsey. Later project state, later memory/knowledge, later advice, later
  evidence-index summaries, and later notes are not copied.
- The measurement directory contains terminal raw data and bridge metadata only;
  original autosave reviews, terminal reviews, model comparisons, figures, and
  original next-action notes for that same target Ramsey are excluded.
- Checkpoints are selected before the later human correction.
- The build script scans snapshot memory, knowledge, project state, advice, and
  evidence for explicit later-correction terms and records the result in
  `inputs/checkpoint_index.csv`.
- Source filenames are retained only in `inputs/provenance/source_file_map.csv`,
  which is not copied into model-run working directories.
