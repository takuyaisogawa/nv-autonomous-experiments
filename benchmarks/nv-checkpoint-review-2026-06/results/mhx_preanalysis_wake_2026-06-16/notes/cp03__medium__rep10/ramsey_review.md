# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`, and the recent design/start note `evidence/e017.md`.
- New terminal Ramsey data and metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: bridge job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: run control.
- Generated local analysis artifacts: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis_summary.json`, and `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Inspected `measurement/m001.json` with Python to verify array shapes and scan fields:
  - `ExperimentData` shape `[1, 2, 41]`.
  - `ExperimentDataEachAvg` shape `[1, 12, 2, 41]`.
  - Tau scan `48 ns..1.968 us`, 41 points, 12 averages, 90000 repetitions.
- Ran `python analyze_ramsey_shorttau.py`.
- Quantitative checks performed:
  - Raw signal/reference/ratio ranges and per-point empirical SEM across stored averages.
  - Least-squares sinusoid amplitudes at the planned carrier `1.0 MHz` and expected 13C sideband positions `0.615 MHz` and `1.385 MHz`, with intercept + linear baseline.
  - Dense frequency screen from `0.2..5.0 MHz`.
  - Per-average 1 MHz amplitude/phase consistency.
  - FFT after linear detrending.
  - A guarded fixed-1 MHz Gaussian-decay Ramsey fit, used only as a descriptive model check.

Key numerical results:

- Terminal run completed safely with final counts `35.122 kcps`; no stop request or monitor error is reported in the local terminal metadata.
- Raw signal spans `40.698..47.197 kcps`, peak-to-peak `6.499 kcps`; median empirical SEM across averages is `1.138 kcps`.
- Signal/reference spans `0.8396..0.9829`, peak-to-peak `0.1433`; median SEM is `0.0127`.
- Reference is comparatively flat in the combined data: actual reference range `2.176 kcps`, linear reference slope only about `-0.161 kcps/us`.
- LS amplitudes with linear baseline:
  - raw signal: `0.615 MHz = 1.103 kcps`, `1.000 MHz = 1.282 kcps`, `1.385 MHz = 1.220 kcps`.
  - signal/reference: `0.615 MHz = 0.0243`, `1.000 MHz = 0.0274`, `1.385 MHz = 0.0271`.
  - reference at `1.000 MHz` is only `0.213 kcps`.
- Per-average raw 1 MHz phases are mostly clustered; phase concentration is `0.933`, but the 1 MHz amplitudes range from `0.699..2.040 kcps`.
- Frequency screen is dominated by the lowest tested frequencies near `0.2 MHz`, consistent with a broad slow component/background over the short window.
- FFT resolution is coarse because the span is only `1.92 us`; the top raw detrended FFT bins are `1.524 MHz`, `1.016 MHz`, and `0.508 MHz`, so this dataset cannot resolve the expected 13C sidebands cleanly.
- Fixed-1 MHz Gaussian-decay fit gives a descriptive `T2* ~0.384 +/- 0.136 us`, amplitude `5.09 kcps`, `R2 = 0.564` versus a linear baseline. This is model-dependent and should not be promoted as a final T2*.

## Plausible interpretation

The short-tau/high-SNR diagnostic did change the Ramsey evidence materially relative to the prior 8 us run: the raw early-time signal is much larger than the per-point SEM, the programmed 1 MHz component is stronger than before, and its phase is fairly consistent across stored averages. This supports the idea that r03 may have a very short Ramsey coherence time, on the order of a few tenths of a microsecond, so the prior long-window datasets could have diluted the carrier.

However, the combined data are not a clean carrier-plus-decay result. The strongest broad frequency-screen response sits at the low-frequency edge, the FFT is span-limited, and a free-frequency fit prefers a long-lived component near `1.19 MHz` rather than a well-constrained decaying `1.0 MHz` carrier. A fixed-carrier fit can describe the early response, but it depends on the imposed carrier and baseline model. Treat the current result as evidence for an early-time Ramsey-like response, not as a final T2star measurement.

## Claims that are not yet supported

- A final numeric T2star for r03 is not yet supported.
- Nearby 13C coupling is not supported by this short-span Ramsey dataset; the span was not designed to resolve `0.615/1.385 MHz` sidebands from the `1.0 MHz` carrier.
- The broad low-frequency component should not be assigned to a physical nuclear-spin feature.
- The descriptive fixed-1 MHz `T2* ~0.38 us` should not be used downstream as a claim-grade value without a detuning-following or otherwise phase-controlled confirmation.
- The result does not prove that the previous non-claim-grade Ramsey runs failed only because T2star is short; baseline, pulse/timing, or readout artifacts remain plausible contributors.

## Recommended next action

Do not run another blind long-window Ramsey repeat on r03. If continuing r03, run a targeted short-tau confirmation that changes the programmed Ramsey detuning while keeping the high-SNR short-window conditions similar, so the carrier must move if it is physical. A good next test is a short-tau/high-SNR Ramsey at `det = 1.5 MHz` over the same `48 ns..1.968 us` grid or a slightly shorter early-time grid, with the same raw/readout-aware review. Promote a T2star only if the carrier follows the detuning and the decay shape remains consistent; otherwise close the r03 Ramsey/T2star/13C branch as unsupported under current conditions and switch protocol/candidate.
