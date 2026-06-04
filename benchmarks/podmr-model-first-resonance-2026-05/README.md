# pODMR Calculation-Guided Resonance Benchmark

This benchmark evaluates whether calculation-guided prompting reduces
false-positive pODMR resonance calls for single NV center data.

The dataset contains 96 strong-pi pODMR measurements:

- 24 resonance-present cases
- 72 resonance-absent cases

Each prompt condition was evaluated with GPT-5.5 for three replicates at four
reasoning-effort settings: `low`, `medium`, `high`, and `xhigh`.

## Main Results

The full reasoning-effort sweep is summarized in
`results/reasoning_effort_sweep_summary.md`.

![Reasoning-effort sweep for pODMR resonance classification](results/figures/podmr_reasoning_sweep.png)

Example raw pODMR traces for one resonance-present case and one
resonance-absent case are shown below.  The figure plots the unnormalized
reference and signal readouts for each case.

![Raw pODMR resonance-present and resonance-absent examples](results/figures/podmr_present_absent_examples.png)

| Reasoning | Condition | TP | TN | FP | FN | Accuracy | False-positive rate | False-negative rate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| low | Protocol only | 72 | 184 | 32 | 0 | 88.9% | 14.81% | 0.00% |
| low | Domain facts | 72 | 201 | 15 | 0 | 94.8% | 6.94% | 0.00% |
| low | Calculation-guided | 72 | 208 | 8 | 0 | 97.2% | 3.70% | 0.00% |
| medium | Protocol only | 72 | 145 | 71 | 0 | 75.3% | 32.87% | 0.00% |
| medium | Domain facts | 72 | 196 | 20 | 0 | 93.1% | 9.26% | 0.00% |
| medium | Calculation-guided | 72 | 215 | 1 | 0 | 99.7% | 0.46% | 0.00% |
| high | Protocol only | 72 | 120 | 96 | 0 | 66.7% | 44.44% | 0.00% |
| high | Domain facts | 72 | 190 | 26 | 0 | 91.0% | 12.04% | 0.00% |
| high | Calculation-guided | 72 | 215 | 1 | 0 | 99.7% | 0.46% | 0.00% |
| xhigh | Protocol only | 72 | 101 | 115 | 0 | 60.1% | 53.24% | 0.00% |
| xhigh | Domain facts | 72 | 202 | 14 | 0 | 95.1% | 6.48% | 0.00% |
| xhigh | Calculation-guided | 72 | 215 | 1 | 0 | 99.7% | 0.46% | 0.00% |

The calculation-guided condition differs from the domain-facts condition by adding a
requirement to establish the expected physical signal with a simulation or
explicit quantitative model calculation before deciding whether a resonance is
present. In this dataset, increasing reasoning effort alone increases
false-positive resonance calls in the protocol-only condition, while the calculation-guided
condition suppresses false positives across reasoning-effort settings.

## Contents

- `inputs/`: agent-visible raw export JSON files and raw-readout figures.
- `labels/`: human resonance labels used for scoring.
- `prompts/`: exact prompt condition text.
- `results/figures/`: benchmark summary figure as PNG and PDF.
- `results/`: GPT-5.5 predictions, summaries, and per-run analysis notes for
  `low`, `medium`, `high`, and `xhigh` reasoning efforts.
- `scripts/`: scoring and package verification helpers.
