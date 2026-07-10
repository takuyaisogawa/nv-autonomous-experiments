# Batch-context main-input pODMR benchmark summary

All 96 cases were provided together for each condition and replicate. Each case had the same file types as the main per-case pODMR benchmark: raw export JSON, raw-readout PNG, and sequence XML. Output was CSV prediction only. Counts pool three replicates, giving 288 decisions per row.

| Reasoning | Condition | TP | TN | FP | FN | Parse failed | Accuracy | FP rate | FN rate |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| low | Sequence | 72 | 216 | 0 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| low | Facts | 72 | 216 | 0 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| low | Expected signal | 72 | 214 | 2 | 0 | 0 | 99.3% | 0.9% | 0.0% |
| medium | Sequence | 72 | 215 | 1 | 0 | 0 | 99.7% | 0.5% | 0.0% |
| medium | Facts | 72 | 213 | 3 | 0 | 0 | 99.0% | 1.4% | 0.0% |
| medium | Expected signal | 72 | 204 | 12 | 0 | 0 | 95.8% | 5.6% | 0.0% |
| high | Sequence | 72 | 213 | 3 | 0 | 0 | 99.0% | 1.4% | 0.0% |
| high | Facts | 72 | 215 | 1 | 0 | 0 | 99.7% | 0.5% | 0.0% |
| high | Expected signal | 72 | 214 | 2 | 0 | 0 | 99.3% | 0.9% | 0.0% |
| xhigh | Sequence | 72 | 213 | 3 | 0 | 0 | 99.0% | 1.4% | 0.0% |
| xhigh | Facts | 72 | 210 | 6 | 0 | 0 | 97.9% | 2.8% | 0.0% |
| xhigh | Expected signal | 72 | 213 | 3 | 0 | 0 | 99.0% | 1.4% | 0.0% |
