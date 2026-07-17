# Ramsey Checkpoint Benchmark Across Three Models

The model columns below follow the comparison used in Fig. 3 and Supplementary
Table S7 of the manuscript.

|  | GPT-5.4 | GPT-5.5 | GPT-5.6 Sol |
| --- | --- | --- | --- |
| Model index | [GPT-5.4](../models/gpt-5.4/) | [GPT-5.5](../models/gpt-5.5/) | [GPT-5.6 Sol](../models/gpt-5.6-sol/) |
| Per model records | [records](gpt-5.4/) | [original source records](../models/gpt-5.5/#ramsey-checkpoint-benchmark) | [records](gpt-5.6-sol/) |
| Runs | 400 | 400 | 400 |

## Aggregate passes

Values are passing runs out of 100 across five checkpoints and twenty
replicates per checkpoint at each reasoning effort.

| Reasoning effort | GPT-5.4 | GPT-5.5 | GPT-5.6 Sol |
| --- | ---: | ---: | ---: |
| Low | 7 | 11 | 16 |
| Medium | 13 | 17 | 42 |
| High | 17 | 21 | 55 |
| X-high | 20 | 34 | 49 |

The complete checkpoint level source table is
[three_model_checkpoint_summary.csv](three_model_checkpoint_summary.csv).
