# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`, plus targeted prior guidance in `md/memory.md` and `md/knowledge.md`.
- New Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` run control.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw data shape and axis contract: `ExperimentData` is `[2, 41]`, `ExperimentDataEachAvg` is `[20, 2, 41]`, and the mean of the 20 stored averages reproduces the stored mean.
- Confirmed scan setup: `tau = 0.048..8.048 us`, `0.200 us` step, 41 points, `20 x 50000` shots per tau, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, snake scan saved in tau order.
- Checked run health: terminal result/status completed, final counts `43.433 kcps`, `stop_requested=false`, monitor `last_error=""`, `safety_aborted=false`, `safe_shutdown_ok=true`.
- Computed local drift proxy from per-average mean counts. Mean total counts ranged `79.12..105.27 kcps`; robust-z max was `1.85`, with no local proxy flags. This is only a local proxy because the MATLAB scan-order drift tool is not present in the snapshot.
- Computed raw signal, point-wise signal/reference, and signal/fitted-reference-line views.
- Ran least-squares sinusoid frequency screens over `0.25..2.35 MHz`, both full-span and with the first four tau points skipped.
- Ran windowed FFT checks after linear detrending, again full-span and skip4.
- Evaluated target amplitudes at the programmed carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior det-shift top `1.623 MHz`, and prior artifact-control frequency `1.192 MHz`.

## Plausible interpretation

- The measurement is technically analyzable and completed cleanly, but it is still not claim-grade for T2star or 13C.
- The mean signal has a large early-time excursion: raw signal starts `[40.57, 46.84, 43.16, 44.01, 44.95] kcps`, much larger than a clean weak decaying sinusoid would suggest. This makes full-span and skip-transient checks necessary.
- The programmed carrier is visible only weakly:
  - Raw signal carrier LS amplitude: `0.705 kcps` full, `0.512 kcps` skip4, versus median raw-signal SEM about `0.85 kcps`.
  - Point-wise ratio carrier amplitude: `0.0157` full, `0.0123` skip4, versus median ratio SEM about `0.0116`.
  - Fitted-reference-line normalized carrier amplitude: `0.0145` full, `0.0105` skip4, versus median normalized SEM about `0.0174`.
- Frequency checks are mixed rather than model-clean:
  - LS screen in point-wise ratio peaks near `2.2705 MHz` full and `2.266 MHz` skip4, not at the programmed `1.5 MHz`.
  - FFT check after skip4 has its largest ratio component near `1.4865 MHz`, close to carrier, but this is not stable against the LS screen or per-average review.
  - Per-average top-frequency bins are broad. For point-wise ratio skip4, only `2/20` averages bin near `1.5 MHz`; the largest bin is `4/20` near `2.25 MHz`.
- Expected 13C sidebands are not supported. In point-wise ratio skip4, the lower sideband amplitude at `1.115 MHz` is `0.00068` (`0.06 x` median SEM) and the upper sideband at `1.885 MHz` is `0.00528` (`0.45 x` median SEM). Full-span values are also not strong enough for a sideband claim.
- The older `1.192 MHz` empirical/artifact-control feature is weak here (`0.0019` ratio amplitude full/skip4, about `0.16-0.17 x` median SEM), so the new long-span run does not simply reproduce that prior feature.

## Claims not yet supported

- A numeric T2star value is not supported. I did not promote a damped-sinusoid T2star fit because raw/readout-aware carrier/decay signal presence is not established.
- A nearby 13C coupling claim is not supported; the expected sidebands at `1.115/1.885 MHz` are below or near noise and inconsistent across views.
- A strong positive carrier conclusion is not supported. The `1.5 MHz` component is visible in some checks, especially FFT skip4, but it is weak relative to SEM and not the dominant/stable LS-screen component.
- A definitive negative/absence-of-13C claim is also not fully supported from this Ramsey alone, because the carrier/decay model itself remains weak.

## Recommended next action

Do not run another blind Ramsey repeat on r03 under the same branch. The refreshed-center high-shot long-span Ramsey remained non-claim-grade, matching the project gate in `project/state.md`: either switch to a deliberately different protocol for T2star/13C discrimination, or close the r03 Ramsey branch with a supported "unsupported under current Ramsey conditions" conclusion. My recommended next operational action is to stop Ramsey repetition and choose the alternate protocol path if the project still requires a positive T2star/13C determination.
