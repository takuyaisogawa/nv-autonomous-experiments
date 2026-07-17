# pODMR Benchmark Across Three Models

The model columns below follow the comparison used in Fig. 4 and Supplementary
Table S8 of the manuscript.

|  | GPT-5.4 | GPT-5.5 | GPT-5.6 Sol |
| --- | --- | --- | --- |
| Model index | [GPT-5.4](../models/gpt-5.4/) | [GPT-5.5](../models/gpt-5.5/) | [GPT-5.6 Sol](../models/gpt-5.6-sol/) |
| Per model records | [records](gpt-5.4/) | [original source records](../models/gpt-5.5/#podmr-data-evaluation-benchmark) | [records](gpt-5.6-sol/) |
| Decisions | 3,456 | 3,456 | 3,456 |

Each model was evaluated on the same 96 measurements under three prompt
conditions, four reasoning effort settings, and three replicates.  The complete
point estimates and measurement level bootstrap intervals are in
[three_model_case_bootstrap.csv](three_model_case_bootstrap.csv).

## Expected signal condition

The table gives false positives among 216 resonance absent decisions and false
negatives among 72 resonance present decisions in each cell.

| Reasoning effort | GPT-5.4 FP / FN | GPT-5.5 FP / FN | GPT-5.6 Sol FP / FN |
| --- | ---: | ---: | ---: |
| Low | 7 / 7 | 8 / 0 | 2 / 0 |
| Medium | 5 / 6 | 1 / 0 | 0 / 0 |
| High | 4 / 4 | 1 / 0 | 1 / 0 |
| X-high | 2 / 3 | 1 / 0 | 1 / 0 |
