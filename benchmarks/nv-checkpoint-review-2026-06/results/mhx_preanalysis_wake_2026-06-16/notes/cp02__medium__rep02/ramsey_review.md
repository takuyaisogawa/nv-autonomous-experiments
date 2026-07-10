# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- `project/state.md`: project context, accepted r03 target, prior pODMR/Ramsey status, expected det=1.0 MHz carrier and ~0.615/1.385 MHz 13C sidebands.
- `measurement/m001.json`: raw-exported savedexperiment for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`: submitted Ramsey job contract.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json` and `measurement/m005.json`: status/control provenance only.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Checked run metadata: job completed, `tau = 0..8 us`, 41 points, `dt = 0.2 us`, 8 averages, 50000 repetitions, snake order, final counts `44.184 kcps`.
- Treated readout 1 as the bright reference and readout 2 as the Ramsey signal, matching the `ramsey.xml` acquisition order in the export.
- Computed raw signal, signal/reference, and signal/reference-line normalized traces.
- Ran acquisition-order drift checks per average using the saved snake order.
- Ran FFT checks and least-squares sinusoid amplitudes on the detrended reference-line-normalized trace at:
  - programmed carrier: `1.000 MHz`
  - expected 13C sidebands: `0.615423 MHz` and `1.384577 MHz`
  - prior scout component: `0.884 MHz`
- Ran exploratory fixed-frequency damped-cosine grid fits; these were used only as diagnostics, not as claim-grade T2star fits.

## Quantitative checks

- Combined readouts:
  - reference mean/range: `49.31 kcps`, range `46.95..51.24 kcps`
  - Ramsey signal mean/range: `44.58 kcps`, range `39.31..47.03 kcps`
  - signal/reference range: `0.8025..0.9721`
  - median combined readout errors: reference `1.97 kcps`, signal `1.87 kcps`
- FFT of detrended signal/reference-line trace:
  - strongest bins were near `1.220 MHz` and `1.098 MHz`, not exactly the programmed `1.000 MHz` carrier.
  - bins near expected sidebands were present but small: nearest `0.610 MHz` amplitude `0.0081`, nearest `1.341 MHz` amplitude `0.0075`.
  - nearest `0.976 MHz` bin amplitude was `0.0068`.
- Least-squares amplitudes on the combined detrended normalized trace:
  - `1.000 MHz`: `0.0056`
  - `0.615423 MHz`: `0.0095`
  - `1.384577 MHz`: `0.0054`
  - `0.884 MHz`: `0.0059`
- Per-average sinusoid amplitudes/phases did not give a coherent carrier or sideband picture. The `1.000 MHz` amplitudes were nonzero in individual averages, but phases/signs varied enough that the combined carrier amplitude was small.
- Acquisition-order drift was not a single catastrophic failure, but per-average mean levels varied substantially. Mean reference ranged from `40.47` to `55.53 kcps`; mean Ramsey signal ranged from `36.20` to `50.27 kcps`. Linear start-to-end trends in acquisition order were typically below about `13%`, but this level variation supports caution.
- Exploratory damped-cosine fits selected the lower search bound `T2star = 0.5 us` for all tested fixed frequencies. That indicates the fit is being driven by short-time structure/noise/initial-point behavior rather than resolving a robust decay constant.

## Plausible interpretation

This Ramsey follow-up produced analyzable data and maintained adequate final counts, but it does not show a clean, reproducible Ramsey carrier at the programmed `1.0 MHz`. The prior scout's `~0.884 MHz` component also did not reappear as a clear dominant feature. The det-shift diagnostic therefore weakens the interpretation that the prior `~0.884 MHz` feature was a stable physical carrier.

The time trace has normalized contrast structure, including an anomalously low `tau=0` point, but the spectral content is not coherent enough across averages to support extracting T2star or identifying 13C sidebands. If there is a real Ramsey signal, it may be short-lived or being obscured by per-average level changes and early-time artifacts.

## Claims not yet supported

- No claim-grade T2star value is supported by this measurement.
- No claim-grade 13C coupling/sideband conclusion is supported.
- The strongest FFT bins near `1.10..1.22 MHz` should not be claimed as a physical carrier without repeatability and per-average phase consistency.
- The exploratory `T2star = 0.5 us` fit-bound result should not be reported as an actual T2star.
- The data do not support sub-grid refinement of the pODMR-derived `mw_freq = 3.8759 GHz`.

## Recommended next action

Do not repeat the same 0..8 us Ramsey unchanged. Run a short-window diagnostic Ramsey on accepted r03, using the fine-pODMR center `mw_freq = 3.8759 GHz`, with denser early-time sampling and the same raw/readout-aware review:

- omit or de-emphasize exact `tau=0`; scan roughly `0.1..3 us`
- use `dt <= 0.05..0.1 us` so a short T2star and 1 MHz carrier can be resolved in the first few microseconds
- keep multiple stored averages and per-average tracking
- require carrier phase/frequency consistency across averages before fitting T2star

If that short-window run still lacks a coherent programmed carrier, close the Ramsey branch as non-claim-grade for T2star/13C under the current configuration rather than accumulating more long-window averages.
