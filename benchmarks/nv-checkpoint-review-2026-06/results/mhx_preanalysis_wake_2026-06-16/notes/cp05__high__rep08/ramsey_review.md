# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`.
- New terminal Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Planning/provenance context: `evidence/e014.json`, `evidence/e016.json`, `evidence/e017.json`, plus prior state summaries in `project/state.md`.
- Scratch outputs created here: `analyze_ramsey.py`, `analysis_summary.json`, and `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw axis contract: `ExperimentDataEachAvg` shape is `[20, 2, 41]`; averaging over the 20 stored averages reproduces `ExperimentData` with max absolute mismatch `0.0`.
- Used embedded sequence/readout logic: `full_experiment=0`, so readout 1 is the true `mS=0` reference and readout 2 is the Ramsey signal.
- Confirmed scan settings: `tau = 48 ns..8.048 us`, step `200 ns`, 41 points; Nyquist `2.5 MHz`, FFT bin spacing `0.122 MHz`; `20 x 50000` shots; `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
- Computed raw signal, point-wise `signal/reference`, fitted-reference-line normalization, scan-order-aware drift proxy, FFT peaks, linear-background least-squares sinusoid screens, fixed target amplitudes, and carrier-constrained damped fits.
- Terminal/run checks: job completed, final count text `43.433 kcps`, no stop request, no bridge error, no incomplete run. Drift proxy using snake scan order flagged no averages.

## Plausible interpretation

- The new high-shot Ramsey is analyzable and healthier than a failed run: counts stayed usable, the run completed, and no drift average was flagged by the local proxy.
- There is some weak carrier-like evidence near the programmed `1.5 MHz` detuning. FFT bins near the carrier are prominent: full-span ratio FFT peaks at `1.463` and `1.585 MHz`, and skip-first-4 peak is `1.486 MHz`.
- The carrier is still not clean enough to promote a T2star. Least-squares target amplitudes are small: raw carrier amplitude `0.705 kcps`, which is only `0.83 x` the median per-tau signal SEM (`0.850 kcps`); ratio carrier amplitude `0.0157`, about `1.36 x` median ratio SEM (`0.0116`). A continuous LS screen is instead largest near `2.27 MHz` in raw, point-wise ratio, and reference-line-normalized views.
- The first tau point is a strong low-signal transient/outlier (`40.57 kcps` signal at `48 ns` versus a later mean near `44.8 kcps`). Carrier-constrained damped fits are consequently not stable: raw fixed-carrier best `T2star` moves from about `0.98 us` with all points to `2.94 us` after skipping the first 4 points; ratio fits move from about `2.13 us` to `5.39 us`, with a broad near-best interval reaching the grid ceiling for the skip-4 ratio case.
- The previous fixed artifact control near `1.192 MHz` remains weak in this run. That supports the idea that the data are not simply repeating the old `~1.19 MHz` feature, but it does not by itself establish a physical Ramsey model.
- The expected 13C sidebands at `1.115 MHz` and `1.885 MHz` are not supported. The lower sideband is near zero in ratio (`0.0028`, skip-4 `0.0007`), and the upper sideband weakens with transient skipping (`0.0096` full to `0.0053` skip-4) and is not a consistent sideband pattern.

## Claims not yet supported

- No numeric T2star claim is supported from this run.
- No nearby 13C coupling/sideband claim is supported.
- Do not claim the `2.27 MHz` LS-screen maximum as a physical frequency; it is a screen result that is not aligned with the programmed carrier or expected 13C sidebands.
- Do not claim that the refreshed `3.8765 GHz` pODMR center has sub-grid precision; it remains a grid-supported Ramsey frequency.
- Do not claim that additional identical 8 us detuned Ramsey averaging is likely to resolve the issue; this was already the higher-shot refreshed-center follow-up.

## Recommended next action

Stop blind repeats of the same long-span `auto__ramsey` condition. Record the r03 Ramsey/T2star/13C branch as still non-claim-grade under current Ramsey conditions, then either:

1. switch to an alternate targeted protocol/diagnostic that directly tests the Ramsey readout/phase/transient failure mode, such as phase-cycled or quadrature Ramsey with explicit early-time handling; or
2. if the project needs a bounded conclusion now, report an unsupported/negative T2star and 13C conclusion for r03 under the tested conditions, while preserving the aligned-NV and pODMR resonance claims.
