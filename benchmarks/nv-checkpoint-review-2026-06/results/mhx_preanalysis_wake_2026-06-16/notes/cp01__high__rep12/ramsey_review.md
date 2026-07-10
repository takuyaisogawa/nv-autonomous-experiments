# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior Ramsey planning context found via local search in `md/knowledge.md`, `md/memory.md`, and `evidence/e005.json`/`e009.json`/`e010.json`/`e011.json`.
- New Ramsey measurement: `measurement/m001.json` raw export and `measurement/m002.json` through `measurement/m005.json` job/spec/status/control metadata.
- Local analysis artifacts created: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `measurement/m001.json`: `ramsey.xml`, `tau = 0..6 us`, 31 points, `dt = 0.2 us`, 4 averages x 50000 repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
- Treated trace 0 as the bright/reference readout and trace 1 as the Ramsey readout, consistent with `full_experiment=0` sequence structure. Calculated raw Ramsey/reference ratio for the combined data and for each average.
- Quantitative checks:
  - Reference readout mean/std: `45.318 +/- 0.865 kcps`; Ramsey readout mean/std: `42.098 +/- 1.441 kcps`.
  - Combined ratio mean `0.9292`, peak-to-peak `0.1355`, median per-point SEM from averages `0.0256`.
  - Hann FFT on normalized ratio: actual DFT bin spacing `161.3 kHz`, Nyquist `2.419 MHz`; largest peaks at `0.968`, `0.323`, and `1.935 MHz`.
  - Nearest normalized FFT bins to expected frequencies: det `1.5 MHz -> 1.452 MHz` amplitude `0.087`; det-13C `1.115 MHz -> 1.129 MHz` amplitude `0.093`; det+13C `1.885 MHz -> 1.935 MHz` amplitude `0.151`.
  - Fixed-frequency normalized cosine projections: `1.5 MHz` amplitude `0.0057`, `R2 = 0.015`; `1.115 MHz` amplitude `0.0084`, `R2 = 0.032`; `1.885 MHz` amplitude `0.0116`, `R2 = 0.061`.
  - Damped-cosine fit to normalized ratio: exponential envelope `T2* = 2.74 +/- 1.87 us`, `f = 1.681 +/- 0.035 MHz`, amplitude `0.058 +/- 0.028`, `R2 = 0.173`; Gaussian envelope gives similar non-claim-grade behavior, `T2* = 2.89 +/- 1.21 us`, `R2 = 0.154`.
  - Per-average normalized FFT dominant bins are inconsistent: avg1 `0.968 MHz`, avg2 `1.452 MHz`, avg3 `0.323 MHz`, avg4 `0.161 MHz`.
  - Acquisition-order trends in normalized ratio show drift-like changes in at least avg1 and avg4: avg1 last-first `+0.128`, avg4 last-first `-0.075`.

## Plausible interpretation

The Ramsey run completed and is analyzable, but this first scout is not claim-grade. There is some oscillatory structure in the raw and normalized traces, yet the programmed `1.5 MHz` carrier is weak in the normalized data, the strongest normalized FFT peak is not at the carrier, and the per-average dominant frequencies are not reproducible. The normalized damped-cosine fits return a few-us decay scale, but the fit explains little variance and the fitted frequency is displaced from the programmed detuning. The data are most plausibly a weak/non-robust Ramsey response mixed with drift and shot/readout scatter, not a clean T2* measurement.

The `1.935 MHz` FFT bin lies near the expected upper det+13C sideband scale, but the corresponding carrier is not dominant and the feature is not reproduced consistently across averages. This is at most a prompt for follow-up, not 13C evidence.

## Claims not yet supported

- No well-supported `T2*` value can be claimed from this run.
- No supported nearby-`13C` conclusion can be claimed from this run.
- The `1.935 MHz` normalized FFT feature should not be called a 13C sideband without a reproducible carrier/sideband pattern in repeat data.
- The fitted `~2.7 us` normalized decay scale should not be promoted to final T2* because the fit is low-`R2`, model-dependent, and affected by per-average inconsistency/drift.

## Recommended next action

Repeat a targeted r03 Ramsey follow-up rather than moving to a final T2*/13C conclusion. Use the same accepted r03 target and weak-pi frequency basis, but reduce per-average drift exposure by splitting into shorter jobs or lowering repetitions per average while increasing averages to preserve total shots. Keep `det = 1.5 MHz` or a nearby deliberate detuning, retain FFT coverage for `det +/- ~0.385 MHz`, and require repeatable per-average carrier evidence before fitting T2* or interpreting any sideband.
