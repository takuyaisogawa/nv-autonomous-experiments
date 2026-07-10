# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey data and metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: job spec for `nv23_ramsey_20260514_055148_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: run control.
- Prior local context used for targets/design: `evidence/e014.json`, `evidence/e017.json`, `evidence/e018.json`, `evidence/e019.json`.

## Calculations/scripts run

- Ran local inline Python to parse `measurement/m001.json`, verify `ExperimentDataEachAvg` axis contract, compute raw readout, point-wise ratio, fitted-reference-line normalization, per-average SEM, target least-squares amplitudes, exploratory frequency screens, FFT checks, per-average frequency screens, a descriptive damped-sinusoid grid fit, and local scan-order/common-mode drift checks.
- Created scratch outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_review_plot.png`

Key acquisition checks:

- Terminal status completed normally; final counts `43.433 kcps`; no stop requested; bridge safety `aborted=false`.
- Intended scan was present: `tau = 48 ns..8.048 us`, `41` points, `200 ns` spacing, `20 x 50000` shots, `1.0e6` shots/tau.
- Sampling: 8.0 us span gives nominal `125 kHz` resolution; FFT bin spacing `121.95 kHz`; Nyquist `2.5 MHz`.
- `ExperimentDataEachAvg[scan, avg, readout, point]` was verified by averaging over avg and reproducing `ExperimentData`.
- Local snake-order common-mode drift check flagged no averages; largest negative end-minus-start score was about `-0.064`, below the `-0.15` drop flag threshold.

Target/model checks:

- Using the project working model with `mw_freq = 3.8765 GHz`, estimated field is `359.46 G`; expected 13C Larmor is `384.8 kHz`.
- With `det = 1.5 MHz`, target frequencies were:
  - carrier: `1.500 MHz`
  - expected 13C lower sideband: `1.115 MHz`
  - expected 13C upper sideband: `1.885 MHz`

Signal checks:

- Median per-point SEM: raw signal `0.850 kcps`, point-wise ratio `0.0116`, reference-line-normalized signal `0.0174`.
- Programmed `1.5 MHz` carrier LS amplitude:
  - raw signal: `0.713 kcps`, about `0.84x` raw SEM and below the plan-level expected `2..6 kcps` raw oscillation scale.
  - point-wise ratio: `0.0148`.
  - reference-line-normalized signal: `0.0146`, about `0.84x` normalized SEM.
- Expected 13C sidebands were weaker:
  - lower sideband raw/ratio/refline amplitudes: `0.116 kcps`, `0.0036`, `0.0024`.
  - upper sideband raw/ratio/refline amplitudes: `0.250 kcps`, `0.0102`, `0.0051`.
- Exploratory full-span LS screens were not target-centered:
  - strongest raw, ratio, and reference-line-normalized screens cluster near `2.268 MHz`.
  - after skipping the first 4 tau points, raw and reference-line-normalized screens move near `1.520 MHz`, but point-wise ratio remains near `2.263 MHz`.
- FFT checks are similarly mixed: full-span ratio bins have strong components around `1.463`, `1.585`, `2.195`, and `2.317 MHz`; skip-first-4 FFT emphasizes about `1.486 MHz` and `2.297 MHz`.
- Per-average ratio top frequencies are scattered (`0.430`, `2.263`, `1.927`, `1.575`, `0.855`, `1.538`, `2.250`, `1.535`, `1.433`, `1.895`, `2.340`, `0.542`, `2.115`, `0.990`, `1.683`, `2.055`, `2.140`, `0.357`, `0.700`, `1.538 MHz`).
- A descriptive damped-ratio grid fit prefers about `2.275 MHz` with `T2star ~2.63 us` and improves BIC versus a linear baseline, but this frequency is not the programmed carrier or expected 13C sideband and is not stable enough across views/averages to promote.

## Plausible interpretation

The measurement completed cleanly and is analyzable, but it still does not provide claim-grade Ramsey evidence. The refreshed pODMR center did not turn the long-span Ramsey into a clean carrier/sideband dataset. There may be a weak carrier-like component near `1.5 MHz` in raw and fitted-reference-normalized views, especially after skipping early points, but its amplitude is near or below measured uncertainty and below the expected raw signal scale. The stronger empirical feature near `2.27 MHz` is not explained by the planned carrier/13C model and is not sufficiently consistent across normalization choices and stored averages.

## Claims not yet supported

- No numeric `T2star` is supported from this run. The descriptive `~2.63 us` fit is not promoted because the fitted frequency is not a supported physical target.
- No nearby 13C conclusion is supported; expected `1.115/1.885 MHz` sidebands are weak and inconsistent.
- The run does not support a clean programmed-carrier Ramsey model at `1.5 MHz`.
- The empirical `~2.27 MHz` feature should not be assigned to an NV/13C physical mechanism from this dataset alone.

## Recommended next action

Do not run another blind refreshed-center 8 us Ramsey repeat on r03. Treat this high-shot Ramsey branch as still non-claim-grade for T2star/13C. The next action should be a decision point: either move to an alternate protocol/diagnostic designed to separate early-transient, reference, and phase-ramp artifacts, or record the supported conclusion that under the current r03 Ramsey conditions T2star and nearby-13C claims remain unsupported. If continuing experimentally, start with a protocol change rather than more averaging of the same Ramsey shape.
