# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- New measurement data: `measurement/m001.json` terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Bridge/job metadata: `measurement/m002.json` through `measurement/m005.json`.
- Prior context used for comparison: accepted r03 NV, fine weak-pi pODMR grid center `mw_freq = 3.8759 GHz`, prior non-claim-grade Ramsey runs, and the planned short-tau/high-SNR Ramsey diagnostic.

## Calculations or scripts run

- Used local Python/NumPy/SciPy to inspect JSON structure, array shapes, tau grid, per-average data, and metadata.
- Confirmed measurement settings from metadata/raw export:
  - `tau = 48 ns..1.968 us`, 41 points, 48 ns step.
  - `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
  - `12 averages x 90000 repetitions`.
  - Bridge status completed, no stop request, no error message.
- Extracted aggregate `ExperimentData` as signal/reference and `ExperimentDataEachAvg` for 12 per-average traces.
- Computed signal/reference ratio, linear reference-line normalization, per-point SEM across averages, per-average mean checks, least-squares frequency screens, and target-frequency LS amplitudes at `1.000 MHz`, `0.615 MHz`, and `1.385 MHz`.
- Created scratch plot `ramsey_shorttau_review.png`.

Key quantitative checks:

- Raw signal range: `47.568..49.744 kcps`, peak-to-peak `2.176 kcps`, median SEM `1.120 kcps`.
- Reference range: `40.698..47.197 kcps`, peak-to-peak `6.499 kcps`, median SEM `1.138 kcps`.
- Point-wise ratio range: `1.0174..1.1910`, peak-to-peak `0.1736`, median SEM `0.0151`.
- Linear reference-line normalized range: `1.0509..1.1212`, peak-to-peak `0.0703`, median SEM `0.0109`.
- Per-average mean signal spans about `26.8%` relative to median, indicating substantial common-mode count variation across the 12 averages.
- Point-wise ratio LS amplitudes:
  - `1.000 MHz`: `0.0300`, `R2 = 0.256`.
  - `0.615 MHz`: `0.0313`, `R2 = 0.297`.
  - `1.385 MHz`: `0.0340`, `R2 = 0.326`.
  - Largest screened ratio component over `0.5..4.5 MHz` sits near `1.21..1.24 MHz`, not at the programmed carrier or expected 13C sidebands.
- Reference-line normalized LS amplitudes:
  - `1.000 MHz`: `0.0047`, `R2 = 0.034`.
  - `0.615 MHz`: `0.0131`, `R2 = 0.226`.
  - `1.385 MHz`: `0.0075`, `R2 = 0.089`.
  - After linear detrending of the reference-line normalized data, target amplitudes are only about `0.0032..0.0040`, below the median SEM.
- Per-average detrended ratio frequency maxima are not consistent: several averages prefer the lower scan bound, several cluster around `1.15..1.29 MHz`, and one prefers about `2.12 MHz`.
- A descriptive fixed-`1 MHz` damped fit to the point-wise ratio converges to an implausibly large early amplitude and very short decay (`T ~0.186 us`), but this is not accepted as claim-grade because it is driven by ratio/reference baseline behavior rather than a stable raw/readout-aware carrier.

## Plausible interpretation

The short-tau/high-SNR Ramsey diagnostic completed and returned analyzable data, but it still does not show a robust programmed `1.0 MHz` Ramsey carrier or a stable 13C sideband pattern. The point-wise ratio contains oscillatory-looking structure near `1.2 MHz`, but the reference channel has a large tau-dependent baseline and the per-average screens are inconsistent. Once the reference trend is handled with a simple linear reference-line normalization, the target `1.0 MHz` amplitude drops below the measured per-point SEM.

This supports the same conservative conclusion as the two earlier Ramsey runs: r03 remains a plausible aligned NV from ODMR evidence, but the current Ramsey evidence is non-claim-grade for both T2star and nearby 13C coupling. The short-tau diagnostic argues against the simple explanation that the previous long-window scans merely missed an obvious early-time `1 MHz` carrier.

## Claims that are not yet supported

- No supported numeric T2star claim from this Ramsey dataset.
- No supported nearby-13C claim from this Ramsey dataset.
- No supported claim that the largest `~1.2 MHz` ratio feature is a physical Ramsey carrier or sideband.
- No supported claim that additional blind repeats of the same Ramsey protocol will resolve the branch; the issue appears to be signal/model support, not just insufficient averaging.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Close the current r03 Ramsey/T2star/13C branch as unsupported under these conditions unless the operator wants a protocol change. If continuing experimentally, switch to an alternate diagnostic that can separate readout/baseline artifacts from coherent phase evolution, such as phase-cycled Ramsey/quadrature readout or a direct short coherence check with deliberately varied detuning and matched reference handling.
