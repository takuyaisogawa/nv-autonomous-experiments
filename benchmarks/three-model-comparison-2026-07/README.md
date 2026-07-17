# Three Model Benchmark Comparison

This directory is the manuscript hub for the GPT-5.4, GPT-5.5, and GPT-5.6 Sol
benchmark comparison.  The three models are presented in parallel through
model specific record indexes.  The indexes retain the original source
locations, so the GPT-5.5 records do not need to be duplicated.

- [Ramsey checkpoint benchmark](../nv-checkpoint-review-2026-06/README.md)
- [pODMR data evaluation benchmark](../podmr-model-first-resonance-2026-05/README.md)

## Parallel model index

|  | GPT-5.4 | GPT-5.5 | GPT-5.6 Sol |
| --- | --- | --- | --- |
| Model argument | `gpt-5.4` | `gpt-5.5` | `gpt-5.6-sol` |
| Recorded execution date | 2026-07-16, America/New_York | pODMR 2026-06-06 UTC<br>Ramsey 2026-06-16 UTC | 2026-07-15 |
| Model record index | [GPT-5.4 records](models/gpt-5.4/) | [GPT-5.5 records](models/gpt-5.5/) | [GPT-5.6 Sol records](models/gpt-5.6-sol/) |
| Ramsey | [records](ramsey/gpt-5.4/) | [source record index](models/gpt-5.5/#ramsey-checkpoint-benchmark) | [records](ramsey/gpt-5.6-sol/) |
| pODMR | [records](podmr/gpt-5.4/) | [source record index](models/gpt-5.5/#podmr-data-evaluation-benchmark) | [records](podmr/gpt-5.6-sol/) |

The benchmark specific directories provide the same parallel view for
[Ramsey](ramsey/) and [pODMR](podmr/).

All three models received the same benchmark inputs, prompt conditions,
reasoning effort settings, replicate structure, and scoring rules.  Local
analysis tools were available.  The pODMR prompts contained no labeled
examples.

The later GPT-5.4 and GPT-5.6 Sol sweeps used the same benchmark runners.  The
original GPT-5.5 sweeps were retained from the earlier benchmark records.
Earlier GPT-5.6 Sol pilot results from an invalid setup were excluded from the
reported comparison.

## Models and run counts

| Benchmark | Models | Runs or decisions per model | Three model total |
| --- | --- | ---: | ---: |
| Ramsey checkpoint | GPT-5.4, GPT-5.5, GPT-5.6 Sol | 400 | 1,200 |
| pODMR data evaluation | GPT-5.4, GPT-5.5, GPT-5.6 Sol | 3,456 | 10,368 |

GPT-5.4 was invoked through the `gpt-5.4` alias supported by Codex with
ChatGPT authentication at execution time.  GPT-5.6 Sol was invoked as
`gpt-5.6-sol`.  See [run_conditions.json](run_conditions.json) and
[gpt-5.4_run_manifest.json](gpt-5.4_run_manifest.json) for the recorded run
conditions.

## Ramsey checkpoint comparison

Each model was evaluated at five checkpoints, four reasoning effort settings,
and twenty replicates for each checkpoint and effort pair.

| Model | Low | Medium | High | X-high |
| --- | ---: | ---: | ---: | ---: |
| [GPT-5.4](models/gpt-5.4/) | 7/100 | 13/100 | 17/100 | 20/100 |
| [GPT-5.5](models/gpt-5.5/) | 11/100 | 17/100 | 21/100 | 34/100 |
| [GPT-5.6 Sol](models/gpt-5.6-sol/) | 16/100 | 42/100 | 55/100 | 49/100 |

The combined checkpoint source data are in
[`ramsey/three_model_checkpoint_summary.csv`](ramsey/three_model_checkpoint_summary.csv).
The GPT-5.4 and GPT-5.6 Sol folders contain completion audits, checkpoint
summaries, per-run manual scores and rationales, and compact records containing
the returned handoff and project note text.  The original GPT-5.5 scores and
recovered notes are in the Ramsey benchmark results directory.

## pODMR comparison

Each model was evaluated on 96 measurements under three prompt conditions,
four reasoning effort settings, and three replicates.  Each model, condition,
and effort cell therefore contains 288 binary decisions.

The combined measurement bootstrap values used in the manuscript are in
[`podmr/three_model_case_bootstrap.csv`](podmr/three_model_case_bootstrap.csv).
Each new model folder contains all 3,456 joined predictions, completion audits,
replicate summaries, case difficulty summaries, measurement bootstrap results,
and compact prediction records with the corresponding analysis note text.

The main cross-model result is that the expected signal condition kept false
positive rates between 0 and 3.7 percent across all model and reasoning
combinations.  GPT-5.5 had no false negatives.  GPT-5.6 Sol had one false
negative in the low reasoning sequence condition.  GPT-5.4 had between two and
eleven false negatives among the 72 resonance decisions in each prompt and
reasoning cell.

## Compact note record generation

The pODMR analysis notes are stored in one CSV per model to avoid adding
thousands of small files.  They were built from the joined prediction table and
the corresponding per-run Markdown notes with
[`scripts/build_podmr_note_records.py`](scripts/build_podmr_note_records.py).
Absolute user paths are replaced with `<USER_HOME>` during this conversion.

Raw CLI stderr logs and internal execution traces are not included.  The
released records retain the model outputs needed to audit the reported binary
decisions and Ramsey manual scoring.
