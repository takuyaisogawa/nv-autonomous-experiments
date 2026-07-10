# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, and targeted guardrails from `md/knowledge.md`.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Execution/provenance: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` control state.
- Prior model/context: `evidence/e007.json`, `evidence/e010.json`, and the current state summary of the first non-claim-grade Ramsey scout.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.
- Checks performed:
  - Parsed raw readouts from `ExperimentData` and per-average readouts from `ExperimentDataEachAvg`.
  - Confirmed scan parameters: tau `0..8 us`, `41` points, `0.2 us` step, `8 x 50000` shots, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
  - Reviewed raw signal/reference, point-wise signal/reference, and signal normalized by a fitted reference line.
  - Computed FFT bins after linear detrending.
  - Ran linear least-squares sinusoid screens at `0.6155`, `0.884`, `1.0`, `1.3845`, and `1.5 MHz`.
  - Compared simple multi-frequency models for the planned carrier/sidebands and exploratory observed bins.

## Plausible interpretation

- The run completed normally enough for analysis: terminal status completed, no stop requested, safe shutdown OK, final count text `Final = 44.184 kcps`.
- The programmed Ramsey carrier is not supported. In signal/reference-line normalization, the `1.0 MHz` least-squares amplitude is `0.00564 +/- 0.00587` with SNR `0.96` and `R2 = 0.029`.
- The planned sideband checks are also weak: lower sideband near `0.6155 MHz` gives amplitude `0.00970 +/- 0.00587` with SNR `1.65`; upper sideband near `1.3845 MHz` gives SNR `0.92`.
- The largest exploratory FFT bins in signal/reference-line normalization are near `0.488 MHz` and `1.220 MHz`, amplitudes `0.0176` and `0.0153`. Their midpoint is about `0.854 MHz`, near the prior scout's non-claim-grade `~0.884 MHz` scale, and their half-splitting is about `0.366 MHz`, close to the locally expected `13C` Larmor scale of about `0.385 MHz`.
- A two-frequency empirical model at the observed top pair fits better than the planned carrier/sideband models (`R2 ~ 0.425`, AIC `-310.7` vs planned carrier-only `R2 ~ 0.029`, AIC `-293.3`). This is hypothesis-generating only because the frequencies are selected from the same data.
- Per-average common-mode count variation is large: reference mean ranges from `40.47` to `55.53 kcps`, signal mean from `36.20` to `50.27 kcps`; ratio means are tighter (`0.8909..0.9258`) but still variable. Average-to-average phase/amplitude consistency is not strong enough to promote the exploratory pair to a physical claim.

## Claims not yet supported

- No well-supported numeric `T2*` claim. The data do not show a clean, planned, decaying Ramsey carrier/envelope suitable for a defensible decay fit.
- No confirmed nearby `13C` claim. The observed pair is compatible with a weak sideband-like hypothesis, but it is not a preplanned positive at `1.0 MHz +/- f13C` and remains vulnerable to drift, sequence/detuning semantics, or analysis selection.
- No supported claim that the Ramsey carrier followed the programmed `det = 1.0 MHz`.
- No supported sub-grid resonance correction from this Ramsey alone.

## Recommended next action

Do not make a T2* or 13C conclusion from this run, and do not blindly repeat with more shots. The next useful action is a targeted detuning/sequence diagnostic: verify the active Ramsey detuning semantics, then run a short det-dependence Ramsey check on r03 with deliberately separated det values and the same raw/readout-aware review. A physical Ramsey carrier or coupled sidebands should shift predictably with the programmed detuning; a fixed `~0.85..0.88 MHz` scale would argue for sequence/artifact/noise or a resonance-setting issue before any longer T2* acquisition.
