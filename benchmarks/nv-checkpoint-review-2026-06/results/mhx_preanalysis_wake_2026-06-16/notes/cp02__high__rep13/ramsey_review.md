# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior/relevant evidence: `evidence/e010.json` job spec for the second Ramsey, `evidence/e013.md` fine-pODMR/second-Ramsey start note, and related measurement metadata.
- New measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` status; `measurement/m005.json` control.
- Scratch outputs created here: `analyze_ramsey.py`, `scratch_ramsey/ramsey_metrics.json`, `scratch_ramsey/ramsey_trace_review.png`, `scratch_ramsey/ramsey_fft_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the raw export as 2 readouts x 41 tau points, plus 8 stored averages.
- Confirmed scan: `tau = 0..8 us`, `dt = 0.2 us`, 41 points, snake order, data saved in tau order, 8 averages x 50000 repetitions.
- Terminal result completed cleanly: final counts `44.184 kcps`, `incomplete=false`, safe shutdown OK.
- Computed combined raw readout spans, signal/reference ratio, signal/reference-line normalization, per-average normalized traces, least-squares sinusoid components at `0.6155`, `0.884`, `1.0`, and `1.3845 MHz`, a windowed FFT of detrended reference-line-normalized data, and a descriptive free damped-cosine fit.

## Quantitative checks

- Combined readout means: readout1/reference `49.31 kcps`, readout2/signal `44.58 kcps`.
- Combined spans: readout1 `8.70%` of mean, readout2 `17.32%`, raw signal/reference ratio `18.76%`, reference-line normalization `16.99%`.
- Per-average baselines vary substantially: readout1 mean ranges `40.47..55.53 kcps`; ratio mean ranges `0.8909..0.9258`.
- Least-squares components on reference-line-normalized combined data:
  - expected lower 13C sideband `0.6155 MHz`: amplitude `0.00970 +/- 0.00587`, SNR `1.65`, R2 `0.073`.
  - prior scout component `0.884 MHz`: amplitude `0.00586 +/- 0.00583`, SNR `1.00`, R2 `0.031`.
  - programmed carrier `1.0 MHz`: amplitude `0.00564 +/- 0.00587`, SNR `0.96`, R2 `0.029`.
  - expected upper 13C sideband `1.3845 MHz`: amplitude `0.00538 +/- 0.00585`, SNR `0.92`, R2 `0.027`.
- Same checks on the direct signal/reference ratio remain weak: target-frequency SNRs are `1.10..1.67` except `1.0 MHz` at `1.39`.
- Per-average target-frequency phases are not coherent enough for a claim. Circular phase concentration R is about `0.68` at `0.6155 MHz`, `0.37` at `0.884 MHz`, `0.45` at `1.0 MHz`, and `0.29` at `1.3845 MHz`.
- FFT top bins on detrended reference-line-normalized data are `1.2195`, `1.0976`, `0.4878`, `0.1220`, `0.6098`, `1.3415`, `2.1951`, and `0.9756 MHz`; the bins near the planned carrier/sidebands are present only as broad exploratory structure, not as clean isolated peaks.
- A free damped-cosine fit to the combined reference-line-normalized trace gives `f = 0.461 +/- 0.041 MHz`, `T2* = 1.64 +/- 0.55 us`, but this is descriptive only because the fitted frequency is not det-locked to the programmed `1.0 MHz` and the per-average/target-frequency checks are weak.

## Plausible interpretation

- The new Ramsey run is analyzable and not invalidated by terminal status, counts, or safety metadata.
- It does not provide claim-grade evidence for a Ramsey carrier at the programmed `1.0 MHz`.
- The prior non-claim-grade `~0.884 MHz` component is not reproduced strongly after changing det from `1.5 MHz` to `1.0 MHz`.
- The expected 13C sidebands near `0.615/1.385 MHz` are not supported: amplitudes are low-SNR, explain little variance, and lack convincing per-average phase consistency.
- The strongest visual/descriptive behavior is a low-frequency/early-time modulation captured by a free fit near `0.46 MHz`, but treating that as physical T2* would be premature because it does not follow the deliberate detuning diagnostic.

## Claims not yet supported

- A well-supported T2* value for r03.
- Nearby 13C coupling or resolved 13C sidebands.
- A clean Ramsey carrier at `1.0 MHz`.
- A physical interpretation of the `0.46 MHz` descriptive fit or the earlier `~0.884 MHz` scout component.
- Improvement by simply taking more averages; the current failure mode is det-response/consistency, not only shot noise.

## Recommended next action

Do not claim T2* or 13C and do not blindly repeat a longer Ramsey. First run or design a bounded Ramsey detuning-response sanity check on the same accepted r03: keep the fine-pODMR microwave frequency, use a short tau span with enough points, and compare at least two deliberate detunings such as `det = 0` and `det = +/-1 MHz` or `det = 0.5/1.0 MHz`. Require the extracted carrier to move with programmed det and to be phase-consistent across stored averages before any T2* fit or 13C FFT claim. If the carrier still fails to track det, inspect the Ramsey sequence/IQ detuning path or switch to an alternate validated sequence before more T2*/13C acquisition.
