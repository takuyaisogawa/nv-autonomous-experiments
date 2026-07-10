# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- New measurement data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Run metadata: `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` run status, `measurement/m005.json` control file.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_shorttau_review.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` and `ExperimentDataEachAvg` as two readouts over `tau = 48 ns..1.968 us`, 41 points, 12 averages, 90000 repetitions, snake scan order.
- Checked raw signal, raw reference, point-wise signal/reference ratio, and signal normalized by a fitted linear reference baseline.
- Ran least-squares screens with constant + linear trend + sinusoid at the planned frequencies: `0.616 MHz`, `1.000 MHz`, and `1.384 MHz`.
- Ran a dense descriptive LS frequency screen from `0.2..5.0 MHz`, a detrended FFT, per-average 1 MHz amplitude checks, and acquisition-order drift checks.

## Quantitative checks

- Run completed cleanly with final counts `35.122 kcps`; saved position was `['117.345', '117.607', '116.053'] um`.
- Raw signal mean was `48.573 kcps`; reference mean was `44.655 kcps`.
- Median SEM from average-to-average scatter was `1.120 kcps` for raw signal and `0.0151` for point-wise ratio.
- At the programmed `1.000 MHz` carrier:
  - raw signal LS amplitude: `0.213 kcps`, well below the raw-signal SEM scale;
  - raw reference LS amplitude: `1.282 kcps`;
  - point-wise ratio LS amplitude: `0.0327`;
  - fitted-reference-line-normalized signal amplitude: `0.00475`.
- Detrended ratio FFT has coarse-bin peaks at `0.508 MHz` (`0.0364` ratio amplitude) and `1.016 MHz` (`0.0337`), with frequency resolution limited by the `1.92 us` span.
- Dense point-wise ratio screen is dominated by the low edge of the search band (`0.2 MHz`), consistent with residual trend/drift sensitivity rather than a clean carrier-only spectrum.
- Scan-order drift flags appear in average 7 signal/reference and averages 9/10 reference; maximum flagged reference span is about `14.8%`.
- A descriptive damped-cosine fit to point-wise ratio returns `f = 1.201 MHz`, `T2* = 2.96 us`, `R2 = 0.712`, but this is not claim-grade because the ratio feature is reference-denominator sensitive and the fitted T2* exceeds the measured window.

## Plausible interpretation

The short-tau/high-SNR diagnostic produced stronger apparent oscillatory structure than the prior long-window Ramsey runs, and a coarse FFT bin near the programmed 1 MHz carrier is visible in the point-wise ratio. However, the raw signal channel itself has only a small carrier-scale amplitude, while the reference channel carries much larger 1 MHz structure and several averages show scan-order reference drift. The safest interpretation is that the dataset is useful for diagnosing an early-time/reference-normalization problem, but it does not yet establish a clean Ramsey carrier decay.

The data are compatible with a very short or low-contrast Ramsey response being obscured by readout/reference systematics. They are also compatible with the apparent ratio oscillation being partly or mostly reference-denominator artifact.

## Claims not yet supported

- No supported numeric `T2*` claim from this dataset.
- No supported nearby `13C` claim. The nominal sideband checks at `0.616 MHz` and `1.384 MHz` are not separable from the same ratio/reference effects affecting the carrier check.
- No supported claim that the programmed `1.0 MHz` carrier is cleanly present in raw signal.
- No supported use of the descriptive `T2* = 2.96 us` fit as a physical result.

## Recommended next action

Do not run another blind Ramsey repeat on r03 under the same readout/normalization assumptions. First choose a targeted validation that separates NV signal contrast from reference-channel structure: repeat a short-tau diagnostic with an adjusted readout/reference strategy or phase-cycled/quadrature Ramsey if available, and require the carrier to appear in raw/readout-aware signal, not only in point-wise ratio. If that is not available, close r03 Ramsey/13C as unsupported under the current protocol and move to an alternate protocol before further accumulation.
