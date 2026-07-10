# Ramsey Review

## Files and data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, plus `md/knowledge.md` / `md/memory.md` for local project guardrails.
- Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submit spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Planning/status evidence checked by search: `evidence/e005.json`, `evidence/e008.json` through `evidence/e011.json`.
- Generated locally: `analyze_ramsey.py` and `ramsey_analysis.png`.

## Calculations and scripts run

- Used PowerShell/`rg` and inline Python to inspect JSON keys, project state, run metadata, and raw array dimensions.
- Wrote and ran `python analyze_ramsey.py` to parse `ExperimentData` and `ExperimentDataEachAvg`.
- Confirmed run settings: `auto__ramsey` / `ramsey.xml`, `tau = 0..6 us`, 31 points, 0.2 us step, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `full_experiment = 0`, 4 averages x 50000 repetitions. Terminal result completed normally with final counts `38.249 kcps`.
- Treated readout1 as reference and readout2 as Ramsey signal, per project context. Computed signal/reference ratio for averaged and per-average data.
- Checked sampling: standard 31-point DFT bin spacing `161.3 kHz`; span-limited resolution `1/6 us = 166.7 kHz`; nominal sampling Nyquist `2.5 MHz` with highest positive odd-N FFT bin `2.419 MHz`.
- Checked raw/readout behavior:
  - Mean reference `45.318 kcps`, mean signal `42.098 kcps`, mean ratio `0.9292`.
  - Per-average mean ratios: `0.9347`, `0.9298`, `0.9199`, `0.9377`.
  - Mean point SEM across averages: signal `1.06 kcps`, reference `1.16 kcps`, ratio `0.0262`.
  - Scan-order first/second-half ratio shifts by average: `+0.025`, `+0.039`, `+0.009`, `-0.041`, comparable to the candidate oscillation amplitudes.
- Fit checks on reference-normalized ratio:
  - Fixed `1.5 MHz` sine plus linear background: amplitude `0.0058`, `R2 = 0.030`.
  - Best sine in `0.05..2.45 MHz`: `0.949 MHz`, amplitude `0.0249`, `R2 = 0.288`.
  - Bootstrap over the 4 averages gave unstable best-frequency percentiles `[0.854, 0.860, 0.950, 1.658, 1.676] MHz`.
  - Individual-average best frequencies disagree: `0.926`, `1.652`, `1.302`, `0.854 MHz`; fixed-1.5-MHz per-average `R2` values remain weak (`0.027..0.221`).
- FFT checks on detrended/windowed ratio:
  - Top averaged FFT peaks: `0.968 MHz` (`0.0236` ratio amp), `0.806 MHz` (`0.0213`), `0.323 MHz` (`0.0206`), `1.935 MHz` (`0.0201`).
  - Planned target bins: carrier `1.5 MHz` nearest bin `1.452 MHz` amp `0.0116`; expected 13C sidebands using `~0.385 MHz` offset at `1.115 MHz` and `1.885 MHz` have nearest-bin amps `0.0124` and `0.0201`.
- Damped-cosine grid fits were model-dependent: fixed `1.5 MHz` fit preferred `T2* ~0.38 us`; free best-frequency fit preferred `T2* ~2.39 us`. Because carrier/signal presence is not stable, these are descriptive only.

## Plausible interpretation

The Ramsey scout completed and the raw counts are healthy enough to analyze, but this is not claim-grade Ramsey/T2star data. The reference-normalized signal has fluctuations at the few-percent level, yet the planned `1.5 MHz` Ramsey carrier is weak in the averaged data and not a stable feature across averages. The strongest averaged spectral feature is near `0.95 MHz`, but bootstrap resampling and per-average fits show that this frequency is not robust.

The scan-order checks show drift-like ratio shifts of `~0.01..0.04`, the same scale as the candidate FFT/fitted amplitudes. That makes the weak FFT peaks plausible as a mixture of low-SNR Ramsey contrast, drift, and fit/FFT leakage rather than a clean oscillatory decay.

The expected `13C` sideband scale is within the sampled band, but the required baseline carrier and sideband pattern are not established. A high-sideband-near bin at `1.935 MHz` is present, but without a robust `1.5 MHz` carrier or per-average consistency it should not be interpreted as nearby `13C` evidence.

## Claims not yet supported

- A well-supported `T2*` value for r03. The available damped fits are too sensitive to model choice and weak/unstable carrier evidence.
- A positive nearby `13C` coupling claim. FFT peaks near the sideband scale are not stable enough and the carrier is absent/weak.
- A negative `13C` exclusion. This scout is too drift- and SNR-limited to rule out a weak or poorly resolved coupling.
- Any invalidation of r03 alignment. The alignment conclusion still rests on the earlier strong-pi and weak-pi pODMR evidence; this Ramsey scout only says the current T2*/13C evidence is non-claim-grade.

## Recommended next action

Do not make a T2* or 13C conclusion from this scout, and do not blindly repeat the same 6 us scan. First run a fresh-track Ramsey contrast diagnostic on r03 with a shorter per-average drift window and denser early-time sampling, for example a bounded `0..2 us` scan with enough points to resolve the `1.5 MHz` programmed carrier. Keep per-average runtime below the current drift guidance by reducing repetitions per average and using more averages only if shot preservation is needed. If the carrier becomes stable, then plan a longer/higher-SNR Ramsey scan for T2* and FFT sideband analysis; if it does not, revisit the resonance/pulse calibration before further T2*/13C acquisition.
