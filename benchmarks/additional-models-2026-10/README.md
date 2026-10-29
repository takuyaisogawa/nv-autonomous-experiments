# Additional Model Evaluations

This directory contains the complete Ramsey and pODMR evaluations for
GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6 Astra. Together with the original
three-model records, these results form the six-model comparison in
manuscript Figs. 3–5. Supplementary Note 6 describes the execution
environments and further analyses of the relationship between the benchmarks.

## Evaluation conditions

| Model | Ramsey responses | pODMR judgments | pODMR scope |
| --- | ---: | ---: | --- |
| GPT-6.1 Sol | 400 | 3,456 | All 96 measurements and three prompts |
| GPT-6.1 Terra | 400 | 3,456 | All 96 measurements and three prompts |
| GPT-6 Astra | 400 | 3,456 | All 96 measurements and three prompts |

Ramsey evaluations used five checkpoints, four reasoning settings (low,
medium, high, xhigh), and 20 replicates per combination. Each pODMR
measurement was evaluated three times per prompt and reasoning setting.
The sequence only comparison uses the same 72 measurements without a
resonance for all six models, giving 216 judgments per model and setting.

Astra's full pODMR record retains the 864 previously published judgments
and adds the remaining 2,592. The earlier responses and scores are unchanged.

The additional runs used Codex CLI `0.164.0-alpha.11.1`, with local analysis
tools available and web search disabled. The CLI and tool configuration
were shared by the three additional models but differed from those used
in the original three-model comparison. Inputs, task prompts, and scoring
criteria were unchanged. Each run started in a fresh session.

Astra's pODMR runs used two builds of the same CLI version. The first 864
judgments used the app-distributed build; the remaining 2,592 used the
official release. Both executable hashes and the changes in concurrency
are recorded in `podmr/gpt-6-astra/execution_settings.json`.

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
- `podmr/gpt-6-astra/validation.json`: checks of all 3,456 results, inputs, prompts, commands, and scores.
- `prompts/`: the task prompts, pODMR prompt template, and judge instructions.
- `data/`: verified summary tables for the six-model comparisons.
- `provenance.json`: source checksums and path normalization in the public copies.

The existing [Ramsey inputs](../nv-checkpoint-review-2026-06/inputs/)
and [pODMR inputs](../podmr-model-first-resonance-2026-05/inputs/)
are reused. The original three-model results remain in
[the three-model release](../three-model-comparison-2026-07/).

Personal directory prefixes in response text and project notes are replaced
with `<user-home>` in these public copies. Prompts, scientific content, and
scores are unchanged. The complete local execution records are preserved.

## Reproduce the analysis and figures

From the repository root, with its Python requirements installed, run:

```shell
python benchmarks/additional-models-2026-10/reproduce.py
python benchmarks/additional-models-2026-10/make_main_figures.py
```

These commands read saved responses and judgments without making model calls.
They check the additional results against the summary tables. The second
command recreates the current manuscript figures in `reproduced/main_figures/`:

- `figure3_ramsey_benchmark.pdf`: pass rates and checkpoint counts for all six models.
- `figure4_podmr_benchmark.pdf`: false positive rates and accuracy for all six models and prompts.
- `figure5_benchmark_relationship.pdf`: the 24 pairs after subtracting each model's mean.
- `benchmark_observed_rates.pdf`: the same pairs before subtracting model means.

The original vector artwork for panels 3a and 4a is retained in `figure_sources/`.
Matching PNG previews, counts, correlations, and source hashes are saved with
the figures. The first command also produces plots in `reproduced/`:

- `reproduced/additional_ramsey.pdf`: pass rates and checkpoint counts for the three additional models.
- `reproduced/additional_podmr_sequence.pdf`: pODMR false positive rates for the additional models with all three prompts.
- `reproduced/additional_benchmark_correlation.pdf`: association before and after subtracting each model's mean.
- Matching PNG previews, `analysis.json`, and LaTeX table rows.

The pODMR error bars use 20,000 bootstrap resamples of measurements, retaining
all three judgments for each sampled measurement. The figures retain the
intervals used in the manuscript. Astra's new intervals use random seed
20261028; its previously reported sequence only intervals are retained.
To recompute and check Astra's intervals from the saved judgments, run
`python benchmarks/additional-models-2026-10/verify_astra_intervals.py`.

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
