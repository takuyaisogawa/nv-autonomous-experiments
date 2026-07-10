# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, and Ramsey-related local evidence in `evidence/e004.json`, `evidence/e007.json`, `evidence/e013.md`.
- New measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- New measurement metadata/status: `measurement/m002.json` through `measurement/m005.json`.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_diagnostic.png`, `analysis_run_output.txt`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed executed Ramsey settings from `Variable_values`: `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, `41` points, `8` averages, `50000` repetitions, `full_experiment = 0`.
- Used local planning evidence for readout roles: readout1 is the reference and readout2 is the Ramsey signal.
- Computed raw signal/reference, signal divided by a fitted reference line, stored-average summaries, snake-order common-mode drift checks, Hann-window FFT, and least-squares sinusoid amplitudes at:
  - programmed carrier: `1.000 MHz`
  - expected `13C` sidebands from the local model: `0.615423 MHz` and `1.384577 MHz`
  - prior non-claim-grade component: `0.884 MHz`
  - exploratory one-frequency scan over `0.125..2.5 MHz`.

## Quantitative checks

- Terminal bridge result completed safely with final count text `44.184 kcps`.
- Combined readouts: mean reference `49.31 kcps`, mean signal `44.58 kcps`, mean signal/reference `0.904`.
- Reference-line-normalized signal range is `0.154` and standard deviation is `0.026`; the first tau point is notably low, so the full range should not be interpreted as clean Ramsey contrast.
- Average-to-average common-mode level varies substantially: mean common-mode values span `38.34..52.90 kcps`, with coefficient of variation `10.7%`. Within-average acquisition-order slopes are smaller but nonzero, max `0.127 kcps` per acquisition point.
- FFT bin spacing is `121.95 kHz`, Nyquist `2.5 MHz`. The largest Hann/detrended FFT components are at `1.220 MHz`, `1.098 MHz`, and `0.488 MHz`; the programmed `1.0 MHz` carrier bin is not dominant.
- Least-squares target checks on reference-line-normalized signal:
  - `1.000 MHz`: combined amplitude `0.56%`, R2 improvement vs line `0.024`, per-average phase resultant `0.45`.
  - `0.615423 MHz`: combined amplitude `0.97%`, R2 improvement `0.069`, phase resultant `0.68`.
  - `0.884 MHz`: combined amplitude `0.59%`, R2 improvement `0.026`, phase resultant `0.37`.
  - `1.384577 MHz`: combined amplitude `0.54%`, R2 improvement `0.022`, phase resultant `0.29`.
- Exploratory one-frequency least-squares scan is strongest near `0.466 MHz` with amplitude `1.87%` and R2 improvement `0.260`; this does not match the programmed carrier or the expected `13C` sidebands.

## Plausible interpretation

The measurement is analyzable and the target remained bright enough, but it does not show a clean Ramsey carrier at the programmed `1.0 MHz`. The prior `~0.884 MHz` scout component is also not reproduced as a dominant fixed feature. The strongest exploratory content is instead near `0.47..0.49 MHz`, which is unexpected under the local model and could reflect weak/nonstationary contrast, residual drift/normalization artifacts, pulse/phase-ramp behavior, or an unresolved physical beat. The local `0.615 MHz` sideband check is somewhat larger than the carrier check, but it is still weak and not enough by itself to claim nearby `13C`.

## Claims not yet supported

- No supported T2star value: do not fit or report T2star until a coherent Ramsey carrier/decay is established.
- No supported `13C` conclusion: neither expected sideband is claim-grade, and the strongest exploratory frequency is not at the modeled `13C` sideband.
- No claim that the previous `~0.884 MHz` component was physical; this det-shifted follow-up does not reproduce it convincingly.
- No claim of sub-grid microwave-frequency precision beyond the already established fine-pODMR grid-supported `3.8759 GHz` center.

## Recommended next action

Do not run a longer T2star/13C acquisition yet. First run a compact Ramsey carrier-validation diagnostic on r03: keep the fine-pODMR microwave center, deliberately choose a detuning/grid that should put a carrier well inside Nyquist, and require per-average phase coherence at the programmed carrier before any T2star fit. If the programmed carrier is still absent, pause Ramsey repetition and re-check the pulse/phase-ramp/readout implementation or repeat a quick pODMR/pulse calibration before deciding whether to close this branch as no-claim/no-13C.
