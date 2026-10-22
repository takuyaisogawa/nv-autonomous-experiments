# Ramsey checkpoint scoring with a fixed LLM judge

The manuscript uses GPT-6.1 Sol (`gpt-6.1-sol`) at high reasoning effort to
score all 1,200 archived responses. The fixed prompt includes the existing
GitHub scoring guide verbatim. Each response was graded once in a fresh
Codex CLI session with tools disabled. The input contained the task context,
complete final response and project note. Model identities and reasoning
settings were withheld.

The judge returned **269 PASS and 931 FAIL**. Human validation on 100 randomly
sampled responses gave **96% agreement**, **Cohen's kappa 0.901**, and a
**Wilson 95% CI of 90.2–98.4%**. See [human validation](human_validation_100/).

## Manuscript pass counts

Each cell contains 100 responses (five checkpoints, twenty replicates).

| Model | Low | Medium | High | Xhigh |
| --- | ---: | ---: | ---: | ---: |
| GPT-5.4 | 7 | 10 | 16 | 22 |
| GPT-5.5 | 4 | 17 | 18 | 27 |
| GPT-5.6 Sol | 15 | 36 | 53 | 44 |

## Records

- `prompts/`: exact judge instructions, scoring prompt, guide and JSON schema.
- `config.json`: model, reasoning effort, CLI version and disabled features.
- `inputs.jsonl`: complete blinded text inputs, keyed by neutral case IDs.
- `judgments.jsonl`: unchanged verdicts, quotations, reasons and confidence.
- `execution_checks.jsonl`: original validation flags and payload hashes.
  Case `case0010` has one capitalization-only quotation difference; its
  original output is retained.
- `case_mapping.jsonl`: evaluated model, checkpoint, effort and source records.
  This metadata was not supplied to the judge.
- `input_manifest.json` and `provenance.json`: input and source hashes.
- `human_validation_100/`: human labels, sampling records,
  comparison, reading aids and four disagreement cases.
- `legacy_comparison/`: previous labels and reasons, comparison and 53
  disagreements. Agreement with previous labels is 1,147/1,200 (95.6%).
- `figures/`: manuscript Figure 3 and the unchanged previous figure.
- `checkpoint_summary.csv`: the 60 model/effort/checkpoint cells used in Figure 3.

The task context was reconstructed from the archived task prompt and runner.
The final response and project note are the complete texts supplied to the
judge. Previous score files remain at their original repository paths.

## Reproduce the reported results

From this directory, Python 3.10 or later is sufficient to verify all frozen
records, reproduce the sample, and recompute agreement and pass counts:

```shell
python scripts/reproduce.py
```

Outputs go to `reproduced/`. To rebuild Figure 3 using the repository's
plotting dependencies (Matplotlib, NumPy and PyMuPDF):

```shell
python scripts/make_figure.py
```

To run a new judgment, install/authenticate the recorded Codex CLI version
and use the portable runner. It writes new outputs under a new directory;
it never overwrites the published labels:

```shell
python scripts/run_judge.py --case case0001 --output reruns/example
```

`--all` evaluates all 1,200 inputs. Only the text payload is sent to the judge;
the public case mapping and labels are not loaded by the runner. New calls
may differ from the archived judgments, so the manuscript is reproduced
from `judgments.jsonl`. The `confidence` field is retained as returned and
does not change the binary score.
