# GPT-5.5 Reasoning-Effort Sweep

Each row pools three replicates over the same 96 pODMR cases.

| Reasoning | Condition | TP | TN | FP | FN | Accuracy | FPR | FNR |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| low | protocol_only | 72 | 184 | 32 | 0 | 88.9% | 14.81% | 0.00% |
| low | domain_facts | 72 | 201 | 15 | 0 | 94.8% | 6.94% | 0.00% |
| low | model_first | 72 | 208 | 8 | 0 | 97.2% | 3.70% | 0.00% |
| medium | protocol_only | 72 | 145 | 71 | 0 | 75.3% | 32.87% | 0.00% |
| medium | domain_facts | 72 | 196 | 20 | 0 | 93.1% | 9.26% | 0.00% |
| medium | model_first | 72 | 215 | 1 | 0 | 99.7% | 0.46% | 0.00% |
| high | protocol_only | 72 | 120 | 96 | 0 | 66.7% | 44.44% | 0.00% |
| high | domain_facts | 72 | 190 | 26 | 0 | 91.0% | 12.04% | 0.00% |
| high | model_first | 72 | 215 | 1 | 0 | 99.7% | 0.46% | 0.00% |
| xhigh | protocol_only | 72 | 101 | 115 | 0 | 60.1% | 53.24% | 0.00% |
| xhigh | domain_facts | 72 | 202 | 14 | 0 | 95.1% | 6.48% | 0.00% |
| xhigh | model_first | 72 | 215 | 1 | 0 | 99.7% | 0.46% | 0.00% |
