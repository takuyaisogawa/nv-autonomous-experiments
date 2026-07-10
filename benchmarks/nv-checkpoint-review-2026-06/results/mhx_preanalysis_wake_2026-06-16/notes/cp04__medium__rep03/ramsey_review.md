# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective and prior r03 Ramsey context.
- `context.json`: checkpoint scope; measurement directory contains the later terminal data for the target det-shift Ramsey.
- `evidence/e019.json`: det-shift design/model note and required target frequencies.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json` through `measurement/m005.json`: job, result, status, and control metadata for `nv23_ramsey_20260514_015423_auto_ramsey`.
- Scratch outputs created here: `analyze_ramsey_detshift.py`, `ramsey_detshift_review.json`, `ramsey_detshift_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified raw array contract: `ExperimentDataEachAvg` averages back to `ExperimentData` with readout1 as reference and readout2 as Ramsey signal.
- Computed point-wise `signal/reference`, `signal/fitted-reference-line`, per-point SEM across 12 stored averages, linear-detrended FFT, and least-squares sinusoid screens.
- Checked target frequencies from the det-shift plan:
  - programmed carrier: `1.500 MHz`
  - programmed 13C sidebands: `1.115/1.885 MHz`
  - predicted det-tracking carrier from prior `1.192 MHz` feature: `1.692 MHz`
  - predicted det-tracking 13C sidebands: `1.307/2.077 MHz`
  - previous fixed-artifact control: `1.192 MHz`
- Ran a local common-mode/per-average sanity check using scan-order metadata (`snake`); no averages were flagged by that simple check.

## Plausible interpretation

- The run completed cleanly: `12 x 90000` repetitions, `1.08e6` shots per tau point, `tau=0.048..1.968 us` in 41 points, `mw_freq=3.8759 GHz`, `det=1.5 MHz`, final counts `44.796 kcps`, no monitor error, and no stop request.
- Noise scale improved relative to the prior short-tau run: median SEM was about `0.71 kcps` for raw signal and `0.0126` in ratio.
- The previous fixed `1.192 MHz` control is not the dominant component in the combined data. Its ratio LS amplitude is only `0.00511`, versus `0.02399` at the programmed `1.500 MHz`, `0.02505` at the predicted det-tracking `1.692 MHz`, and a top combined ratio screen near `1.623 MHz` with ratio amplitude `0.02547` and raw-signal amplitude `1.25 kcps`.
- This argues against simply treating the old `~1.19 MHz` component as a fixed analysis artifact. It is qualitatively compatible with det-sensitive behavior, but the peak is broad/offset on this short window and does not establish a clean physical carrier.
- The 13C sideband checks are not compelling: programmed sidebands have ratio amplitudes `0.01076/0.01732`, while det-tracking sidebands have `0.00953/0.00614`; none dominate the carrier-region response or show a robust sideband pattern.
- A descriptive damped-sinusoid grid fit to the ratio view preferred `0.678 MHz` and `T2* ~0.469 us`, but this is likely early-transient/model-sensitive and should not be promoted as a physical T2star.

## Claims not yet supported

- No well-supported numeric `T2*` has been established from the Ramsey data.
- No well-supported nearby `13C` coupling conclusion has been established.
- The det-shift run does not by itself prove that the `1.62..1.69 MHz` response is the true Ramsey carrier; per-average frequency screens are inconsistent, including several low-frequency/transient-dominated averages.
- Do not claim sub-grid frequency precision or a resolved carrier/sideband model from the short-tau FFT/LS screens.

## Recommended next action

Stop blind Ramsey repeats on r03 under this protocol. Do a bridge-free branch synthesis across all r03 Ramsey datasets and either close the current Ramsey/T2star/13C branch as unsupported under these conditions, or switch deliberately to an alternate targeted protocol/readout diagnostic that can separate early-time transient/baseline behavior from a physical Ramsey carrier before spending more bridge time.
