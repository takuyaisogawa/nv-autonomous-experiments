# Ramsey Review: r03 det=1.0 MHz, 8 us, 8 avg

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, and recent evidence note `evidence/e013.md`.
- New Ramsey measurement:
  - `measurement/m001.json`: raw export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: submitted job contract, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `tau=0..8 us`, 41 points, 8 averages x 50000 repetitions.
  - `measurement/m003.json`: terminal bridge result, status `completed`, started `2026-05-13T20:49:36`, finished `2026-05-13T22:17:11`.
  - `measurement/m004.json` and `measurement/m005.json`: terminal status/control snapshots.

## Calculations or scripts run

- Created and ran `scratch_ramsey_review.py`.
- Output summary: `scratch/ramsey_det1p0_review_summary.txt`.
- Diagnostic plot: `scratch/ramsey_det1p0_review.png`.
- Checks performed:
  - Loaded combined signal/reference and per-average signal/reference arrays from `measurement/m001.json`.
  - Built `signal/reference` and `signal / linear(reference)` traces.
  - Checked scan metadata: `tau=0..8 us`, `dt=0.2 us`, 41 points, FFT bin spacing about `0.12195 MHz`, scan order `snake`, data saved in tau order.
  - Ran FFT peak checks on ratio and reference-line-normalized traces.
  - Ran least-squares sinusoid checks at expected/diagnostic frequencies: `0.615`, `0.884`, `1.000`, and `1.385 MHz`.
  - Ran an exploratory damped-cosine fit to the ratio trace.
  - Checked per-average common-mode count shifts, correlation to the combined ratio trace, and 1 MHz LS amplitudes.

## Quantitative results

- Combined means: signal `49.313 kcps`, reference `44.580 kcps`.
- Ratio mean `1.107100`; ratio peak-to-peak span is `19.64%` of mean.
- FFT, ratio trace top bins:
  - `1.219512 MHz` amp `0.02443`
  - `0.487805 MHz` amp `0.02117`
  - `0.975610 MHz` amp `0.01698`
  - `1.097561 MHz` amp `0.01619`
  - `0.609756 MHz` amp `0.01440`
- FFT, `signal / linear(reference)` top relevant bins:
  - strongest overall is `2.439024 MHz` amp `0.01135`
  - expected carrier bin `0.975610 MHz` amp `0.00838`
  - upper-sideband-near bin `1.341463 MHz` amp `0.00623`
- Least-squares sinusoid amplitudes on ratio:
  - `0.615 MHz`: amp `0.01352`, R2 `0.073`
  - prior diagnostic `0.884 MHz`: amp `0.00950`, R2 `0.040`
  - expected carrier `1.000 MHz`: amp `0.01199`, R2 `0.061`
  - `1.385 MHz`: amp `0.01070`, R2 `0.050`
- Least-squares sinusoid amplitudes on `signal / linear(reference)`:
  - `0.615 MHz`: amp `0.00331`, R2 `0.030`
  - prior diagnostic `0.884 MHz`: amp `0.00816`, R2 `0.118`
  - expected carrier `1.000 MHz`: amp `0.00547`, R2 `0.060`
  - `1.385 MHz`: amp `0.00536`, R2 `0.058`
- Exploratory damped-cosine fit to ratio:
  - `T2star = 0.949 +/- 0.341 us`, `f = 1.2017 +/- 0.0687 MHz`, amplitude `0.1285 +/- 0.0286`, R2 `0.496`.
  - This is descriptive only; the fitted frequency is pulled toward the strongest ratio FFT component rather than the programmed `1.0 MHz` carrier.
- Per-average common-mode shifts relative to median: `+7.22%, -3.07%, -6.92%, +11.42%, +3.07%, -6.86%, -18.44%, +12.54%`.
- Per-average correlations to the combined ratio trace are all positive but moderate: `0.33..0.65`.

## Plausible interpretation

- The run completed and returned analyzable Ramsey data.
- The det-shifted experiment does show content near the expected `1.0 MHz` carrier: the closest FFT bin, `0.975610 MHz`, is present in both ratio and reference-line-normalized views.
- However, the carrier-near bin is not the dominant ratio feature, single-frequency LS R2 values at expected carrier and sidebands are low, and per-average count drift/common-mode variation is non-negligible.
- The previous scout's `~0.884 MHz` diagnostic component is not the leading ratio FFT feature here, which weakly argues against a fixed dominant artifact at exactly that frequency. It does not by itself establish the intended Ramsey carrier or a physical sideband pattern.
- The data are consistent with weak Ramsey contrast plus drift/normalization sensitivity. They are useful diagnostic evidence, but not yet a clean T2star/13C endpoint.

## Claims that are not yet supported

- Do not claim a final T2star from this run. The exploratory fit gives about `0.95 us`, but it is model-sensitive, has only moderate R2, and is tied to a fitted frequency near `1.20 MHz` rather than the programmed carrier.
- Do not claim 13C coupling. The expected sideband-near bins around `0.615/1.385 MHz` are not strong, stable, or distinctly separated from other spectral structure.
- Do not claim that the det-shifted Ramsey fully validates the refined ODMR center. The expected carrier is visible but not dominant.
- Do not claim that all observed spectral peaks are physical; drift/common-mode shifts and reference normalization sensitivity remain plausible contributors.

## Recommended next action

- Do not blindly repeat the same Ramsey as a final measurement.
- Before more long Ramsey acquisition, run a short diagnostic designed to separate frequency/sequence effects from drift:
  - either a second det-shift check at a different detuning, e.g. `det=0.5 MHz` or `1.5 MHz`, with enough tau span to resolve whether the main spectral component follows detuning;
  - or a tighter Ramsey centered on the current apparent oscillation with improved interleaving/reference handling and a pre/post ODMR or quick track/count validation.
- Treat this run as non-claim-grade for both T2star and 13C until the carrier follows detuning cleanly and sideband/decay evidence is reproducible across averages.
