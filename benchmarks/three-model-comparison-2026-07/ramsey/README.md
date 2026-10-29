# Ramsey Checkpoint Benchmark Across Three Models

This directory contains Ramsey records for the original three models.
The [current six-model comparison](../../additional-models-2026-10/)
includes these results and provides the code for the current Fig. 3.

|  | GPT-5.4 | GPT-5.5 | GPT-5.6 Sol |
| --- | --- | --- | --- |
| Model index | [GPT-5.4](../models/gpt-5.4/) | [GPT-5.5](../models/gpt-5.5/) | [GPT-5.6 Sol](../models/gpt-5.6-sol/) |
| Per model records | [records](gpt-5.4/) | [original source records](../models/gpt-5.5/#ramsey-checkpoint-benchmark) | [records](gpt-5.6-sol/) |
| Runs | 400 | 400 | 400 |

## LLM-judge passes used in the manuscript

All 1,200 responses were scored by the fixed [GPT-6.1 Sol/high judge](llm_judge/).
Human validation gave 96% agreement on 100 responses.

Each value is the number of passing responses out of 100 for one model
and reasoning setting, with 20 responses from each of five checkpoints.

| Reasoning effort | GPT-5.4 | GPT-5.5 | GPT-5.6 Sol |
| --- | ---: | ---: | ---: |
| Low | 7 | 4 | 15 |
| Medium | 10 | 17 | 36 |
| High | 16 | 18 | 53 |
| X-high | 22 | 27 | 44 |

The current checkpoint table is [llm_judge/checkpoint_summary.csv](llm_judge/checkpoint_summary.csv).
The previous [three_model_checkpoint_summary.csv](three_model_checkpoint_summary.csv)
and per-model score files are unchanged. The [comparison](llm_judge/legacy_comparison/comparison.json)
records both sets of labels and reasons.
