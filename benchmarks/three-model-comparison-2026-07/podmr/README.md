# pODMR Benchmark Across Three Models

This directory contains pODMR records for the original three models.
The [current six-model comparison](../../additional-models-2026-10/)
includes these results and provides the code for the current Fig. 4.

|  | GPT-5.4 | GPT-5.5 | GPT-5.6 Sol |
| --- | --- | --- | --- |
| Model index | [GPT-5.4](../models/gpt-5.4/) | [GPT-5.5](../models/gpt-5.5/) | [GPT-5.6 Sol](../models/gpt-5.6-sol/) |
| Per model records | [records](gpt-5.4/) | [original source records](../models/gpt-5.5/#podmr-data-evaluation-benchmark) | [records](gpt-5.6-sol/) |
| Decisions | 3,456 | 3,456 | 3,456 |

Each model was evaluated on the same 96 measurements from two NV centers using
three prompts, four reasoning effort settings, and three replicates. The complete
point estimates and confidence intervals obtained by bootstrap resampling of
measurements are in
[three_model_case_bootstrap.csv](three_model_case_bootstrap.csv).

## Expected signal prompt

Each cell reports false positives among 216 evaluations of measurements
without a resonance and false negatives among 72 evaluations of measurements
containing a resonance.

| Reasoning effort | GPT-5.4 FP / FN | GPT-5.5 FP / FN | GPT-5.6 Sol FP / FN |
| --- | ---: | ---: | ---: |
| Low | 7 / 7 | 8 / 0 | 2 / 0 |
| Medium | 5 / 6 | 1 / 0 | 0 / 0 |
| High | 4 / 4 | 1 / 0 | 1 / 0 |
| X-high | 2 / 3 | 1 / 0 | 1 / 0 |
