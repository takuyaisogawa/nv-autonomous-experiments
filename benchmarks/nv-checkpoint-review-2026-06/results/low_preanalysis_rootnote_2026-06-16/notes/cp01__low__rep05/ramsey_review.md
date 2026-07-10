# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, and `md/knowledge.md` for project context and analysis rules.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: executed Ramsey job contract.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result/status/control metadata.
- Generated local analysis artifacts: `ramsey_analysis_summary.json`, `ramsey_trace.png`, and `ramsey_fft.png`.

## Calculations or scripts run

- Used inline Python to parse `measurement/m001.json`, extract tau, averaged readouts, and the four stored per-average traces.
- Checked scan geometry: `tau = 0..6 us`, `31` points, `0.2 us` step, `4 x 50000` repetitions.
- Compared raw readout levels and point-wise signal/reference ratio:
  - Mean signal readout: `45.318`, range `44.038..47.942`.
  - Mean reference readout: `42.098`, range `38.096..45.846`.
  - Mean signal/reference: `1.0776`, range `1.0055..1.1641`.
  - Per-average signal means: `46.44, 43.68, 46.59, 44.56`.
  - Per-average reference means: `43.36, 40.55, 42.80, 41.68`.
  - Per-average ratio means: `1.0745, 1.0792, 1.0911, 1.0713`.
- Detrended the averaged signal/reference ratio, applied a Hann window, and computed an FFT:
  - Bin spacing from the actual 31-point grid: `161.3 kHz`; Nyquist: `2.419 MHz`.
  - Largest averaged FFT bins: `0.968 MHz`, `0.323 MHz`, `0.806 MHz`, `1.935 MHz`, `1.774 MHz`.
  - Planned Ramsey detuning was `1.5 MHz`; expected approximate 13C sidebands from the project model were `1.115 MHz` and `1.885 MHz`.
- Fit the averaged signal/reference trace with empirical cosine, exponential-decay cosine, and Gaussian-decay cosine models:
  - Plain cosine: `f = 0.948 MHz`, amplitude `0.029`, `R2 = 0.274`.
  - Exponential-decay cosine: `f = 0.947 MHz`, `T = 2.29 +/- 1.11 us`, amplitude `0.080`, `R2 = 0.435`.
  - Gaussian-decay cosine: `f = 0.946 MHz`, `T = 3.12 +/- 1.03 us`, amplitude `0.063`, `R2 = 0.427`.
- Checked per-average FFT reproducibility. The leading bins varied by average:
  - Avg 1: `0.968 MHz`, `0.806 MHz`, `0.323 MHz`.
  - Avg 2: `1.452 MHz`, `1.935 MHz`, `0.484 MHz`.
  - Avg 3: `1.129 MHz`, `0.323 MHz`, `1.290 MHz`.
  - Avg 4: `0.806 MHz`, `0.161 MHz`, `0.323 MHz`.
- Plot generation initially hit a local Tk backend problem; reran with Matplotlib `Agg`, producing `ramsey_trace.png` and `ramsey_fft.png`.

## Plausible interpretation

- The run completed normally and produced analyzable Ramsey data, but the measurement is not claim-grade for T2star or 13C.
- There is oscillatory structure in the averaged signal/reference trace, but the strongest averaged FFT bin and empirical fits cluster near `0.95 MHz`, not near the programmed `1.5 MHz` Ramsey detuning.
- The empirical decay-cosine fits give a possible few-us decay scale, but the fit quality is poor (`R2 ~0.43`) and the fitted decay time is strongly model-dependent/uncertain. Treat `T ~2-3 us` only as a scout-scale hint, not a supported T2star.
- The FFT has power near the expected high sideband scale (`1.935 MHz` close to the rough `1.885 MHz` expectation), but comparable or larger peaks appear elsewhere, and per-average leading peaks are inconsistent. This does not support a 13C claim.
- Drift is relevant provenance: terminal final counts were `38.249 kcps`, down from the prior weak-pODMR final count of `43.890 kcps`, and the actual runtime status estimated a `492.946 s` tracking window per average, above the planned `450 s` cap.

## Claims not yet supported

- No well-supported T2star value is established from this Ramsey scout.
- No well-supported nearby-13C/coupling conclusion is established.
- The apparent `~0.95 MHz` oscillation should not yet be promoted to a physical Ramsey detuning without a repeat or frequency diagnostic, because it disagrees with the programmed detuning and lacks per-average reproducibility.
- The `~1.94 MHz` FFT component should not be assigned to a 13C sideband from this dataset alone.

## Recommended next action

Before launching a longer Ramsey, do a bounded diagnostic repeat on r03 under fresher tracking/frequency conditions: refresh tracking/counts, re-check or briefly refresh the weak-pi pODMR center if counts/frequency drift are plausible, then repeat Ramsey with a shorter per-average tracking window and enough sampling to cover `det +/- ~0.385 MHz`. The immediate goal is to test whether the carrier returns near the programmed detuning and whether any sideband-like peaks reproduce across stored averages.
