# Additional Model Evaluations

This directory contains the additional evaluations in Supplementary Note 6:
GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6 Astra. The figures compare them with
the three models in the main text. Model and reasoning settings affect the
two benchmarks differently; greater reasoning effort does not consistently
improve Ramsey performance or increase pODMR false positives in these
additional models.

## Evaluation conditions

| Model | Ramsey responses | pODMR judgments | pODMR scope |
| --- | ---: | ---: | --- |
| GPT-6.1 Sol | 400 | 3,456 | All 96 measurements and three prompts |
| GPT-6.1 Terra | 400 | 3,456 | All 96 measurements and three prompts |
| GPT-6 Astra | 400 | 864 | Sequence only; 72 measurements without a resonance |

Ramsey evaluations used five checkpoints, four reasoning settings (low,
medium, high, xhigh), and 20 replicates per combination. Each pODMR
measurement was evaluated three times per prompt and reasoning setting.
The sequence only comparison uses the same 72 measurements without a
resonance for all six models: 216 judgments per model and setting.

The additional runs used Codex CLI `0.164.0-alpha.11.1`, with local analysis
tools available and web search disabled. The CLI and tool configuration
were shared by the three additional models but differed from those used
in the original three-model comparison. Inputs, task prompts, and scoring
criteria were unchanged. Each run started in a fresh session.

All Ramsey responses were scored with the same GPT-6.1 Sol judge at high
reasoning effort, using the [fixed prompts](prompts/). The judge received
the task prompt, final response, and project note, with the evaluated
model and reasoning setting withheld. The existing
[100-response human validation](../three-model-comparison-2026-07/ramsey/llm_judge/human_validation_100/)
remains unchanged at 96% agreement.

## Records and inputs

- `ramsey/<model>/responses.jsonl`: final responses and project notes.
- `ramsey/<model>/judgments.json`: verdicts, supporting quotations, and reasons.
- `ramsey/<model>/judge_mapping.json`: correspondence between anonymous judge IDs and responses.
- `podmr/<model>/responses.jsonl`: final responses, project notes, reference labels, and predictions.
- `execution_settings.json` in each model directory: model, execution settings, CLI version, executable checksum, and command templates.
- `prompts/`: the task prompts, pODMR prompt template, and judge instructions.
- `data/`: verified summary tables for the six-model comparisons.
- `provenance.json`: source checksums and path normalization in the public copies.

The existing [Ramsey inputs](../nv-checkpoint-review-2026-06/inputs/)
and [pODMR inputs](../podmr-model-first-resonance-2026-05/inputs/)
are reused. The main comparison and its original records remain in
[the three-model release](../three-model-comparison-2026-07/).

Personal directory prefixes in response text and project notes are replaced
with `<user-home>` in these public copies. Prompts, scientific content, and
scores are unchanged. The complete local execution records are preserved.

## Reproduce the analysis and figures

From the repository root, with its Python requirements installed, run:

```shell
python benchmarks/additional-models-2026-10/reproduce.py
```

This reads saved responses and judgments without making model calls. It
checks the additional results against the summary tables and writes:

- `reproduced/additional_ramsey.pdf`: six-model pass rates and checkpoint counts.
- `reproduced/additional_podmr_sequence.pdf`: false positive rates for pODMR with the sequence only prompt.
- `reproduced/additional_benchmark_correlation.pdf`: association after subtracting each model's mean.
- Matching PNG previews, `analysis.json`, and LaTeX table rows.

The pODMR error bars use 20,000 bootstrap resamples of measurements, retaining
all three judgments for each sampled measurement. Previously reported
intervals are retained for the first five models. Astra's intervals use
the same procedure, with random seed 20261028.

## Relationship between the benchmarks

For each model and reasoning setting, the Ramsey rate uses 100 responses
and the pODMR false positive rate uses 216 judgments. The raw correlation
across the 24 pairs is 0.441. Subtracting each model's mean across its four
settings from both rates gives Pearson's r = 0.806. Omitting one model at
a time gives r = 0.788 to 0.900. Each model also has a positive correlation
across its four settings.

These are descriptive associations across four settings per model and
shared benchmark inputs. The script reports the values without a
significance test or a causal interpretation.
