# Ramsey Review: r03 Short-Tau High-SNR Diagnostic

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective, accepted r03 context, prior non-claim-grade Ramsey history, and expected review targets.
- `evidence/e003.json`: terminal review of the prior det=1.0 MHz, 0..8 us Ramsey run.
- `evidence/e006.json` and `evidence/e017.md`: design rationale for the short-tau/high-SNR diagnostic.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: job spec/result/status/control artifacts for `nv23_ramsey_20260513_230331_auto_ramsey`.
- Derived local artifacts: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis.json`, `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_shorttau.py`.
- Parsed the Ramsey raw export as 41 tau points from 0.048 us to 1.968 us, 48 ns step, 12 averages x 90000 repetitions, total `1.08e6` shots per tau point, `mw_freq=3.8759 GHz`, programmed `det=1.0 MHz`, snake scan order saved in tau order.
- Used the project-context readout role for `ramsey.xml`/`full_experiment=0`: readout 1 reference, readout 2 Ramsey signal.
- Computed raw signal/reference traces, point-wise ratio, signal normalized to a fitted reference line, per-point SEM across stored averages, linear-baseline residuals, fixed-frequency least-squares sinusoid amplitudes, blind frequency screens, FFT screens, per-average carrier amplitudes/phases, and target-frequency separability.

## Key quantitative checks

- Run completed safely: status `completed`, finished `2026-05-14T01:23:47`, no raw-export warnings, no result/status warnings, no monitor error recorded.
- Combined readouts: reference mean `48.573 kcps`, signal mean `44.655 kcps`, ratio mean `0.9195`.
- Per-point SEM across averages: signal median `1.138 kcps`, ratio median `0.0127`.
- Raw signal linear-residual peak-to-peak is `5.25 kcps`; over the first 0.75 us it is `5.09 kcps`, so the short-tau trace contains visible early-time structure.
- Fixed 1.0 MHz carrier least-squares amplitude:
  - raw signal: `1.282 +/- 0.271 kcps`, LS SNR `4.73`, linear-residual R2 improvement `0.377`;
  - ratio: `0.0274 +/- 0.0061`, LS SNR `4.50`, R2 improvement `0.355`;
  - signal/reference-line: `0.0264 +/- 0.0056`, LS SNR `4.73`, R2 improvement `0.378`.
- Per-average 1.0 MHz raw-signal amplitudes span `0.699..2.040 kcps`, median `1.205 kcps`; carrier phase circular resultant is `0.933`, so the fixed-carrier phase is fairly coherent across averages.
- Blind single-frequency screen peaks near, but not exactly at, the programmed carrier: raw signal top near `1.187 MHz` with `1.68 kcps`; ratio top near `1.192 MHz` with `0.0363`.
- FFT screen is resolution-limited by the short span; the largest ratio bins are `0.508 MHz` and `1.016 MHz`.
- 13C sideband checks at `0.615 MHz` and `1.385 MHz` give comparable single-frequency LS amplitudes, but the short scan has only `1.92 us` span and nominal resolution `~0.521 MHz`; target sinusoid subspaces are not cleanly separable from the carrier over this window.

## Plausible interpretation

The short-tau/high-SNR diagnostic succeeds at the specific test that the earlier long-window Ramsey runs did not: it shows a measurable early-time Ramsey-like oscillation on accepted r03 in raw signal and readout-normalized views, with a coherent per-average phase at the programmed 1.0 MHz carrier. This argues against the branch being purely dead/no-signal under current conditions and suggests the earlier 0..8 us scans likely diluted or obscured the early-time contrast.

The strongest blind frequency around `1.19 MHz` rather than exactly `1.0 MHz` is plausibly due to a small resonance/detuning mismatch, short-window baseline/phase covariance, or unresolved beating. It should not be promoted as a precise detuning without a follow-up designed for frequency resolution.

## Claims not yet supported

- No numeric T2star is supported yet. The trace shows early-time oscillation, but the 1.92 us window and frequency/baseline covariance are not enough for a defensible decay-envelope fit.
- No nearby 13C claim is supported. The expected `det +/- 13C` sidebands are not resolved by this short window, and sideband-frequency LS amplitudes are not independent enough from the carrier model.
- Do not claim that the physical Ramsey frequency is exactly `1.19 MHz`; it is a blind-screen maximum from a short trace, not a calibrated frequency measurement.
- Do not close r03 as Ramsey/T2star failed; this new run provides evidence that a better-targeted Ramsey protocol can see contrast.

## Recommended next action

Run a targeted follow-up that separates frequency calibration from decay/13C interpretation: first use a short high-SNR Ramsey/detuning check or refined frequency-centering step to decide whether the effective Ramsey carrier is closer to `1.0 MHz` or `~1.19 MHz`; then run a longer, high-SNR Ramsey with adequate span/resolution for T2star and 13C sideband testing. Avoid another blind 0..8 us repeat without fixing the carrier/frequency-resolution question.
