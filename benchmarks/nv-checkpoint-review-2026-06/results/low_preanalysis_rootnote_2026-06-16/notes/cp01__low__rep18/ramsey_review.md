# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md` for project objective, prior candidate decisions, Ramsey plan, and analysis rules.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: submitted Ramsey job spec.
- `measurement/m003.json`: terminal bridge result; run completed normally, final counts `38.249 kcps`, saved data path recorded.
- `measurement/m004.json`: final bridge status; completed after `2124 s`.
- `measurement/m005.json`: run control; no stop requested.
- `evidence/e011.json`: batch state/advisory provenance.
- Generated local scratch outputs: `scratch_ramsey_analysis.json` and `ramsey_review_plot.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with local Python.
- Confirmed Ramsey export shape:
  - `ExperimentData`: `[1, 2, 31]`.
  - `ExperimentDataEachAvg`: `[1, 4, 2, 31]`.
  - `tau = 0..6 us`, `31` points, `dt = 0.2 us`, `4 x 50000` repetitions, snake scan, tracking per average.
- Treated readout 1 as reference and readout 2 as signal, then checked:
  - raw reference and signal traces,
  - signal/reference ratio,
  - signal normalized against a linear reference baseline,
  - per-average ratio consistency,
  - linear detrended FFT with Hann window,
  - empirical Gaussian-decay cosine fits after signal inspection.
- Quantitative highlights:
  - Mean readouts: reference `45.318 kcps`, signal `42.098 kcps`, ratio `0.9292`.
  - Peak-to-peak variation: reference `3.904 kcps`, signal `7.750 kcps`, ratio `0.1355`.
  - Exported per-point errors average about `1.89 kcps` for reference and `1.82 kcps` for signal; signal peak-to-peak is about `4.3x` the mean signal error, but the shape is not a clean Ramsey decay.
  - Reference linear slope is small over the scan, about `-0.052 kcps/us`, so reference drift alone does not explain all signal variation.
  - Actual FFT spacing from the 31-point sampled grid is `161.29 kHz`; Nyquist is `2.419 MHz`.
  - Using `mw_freq = 3.876 GHz`, rough `B = 359.3 G` and `13C` Larmor scale `~384.6 kHz`; expected Ramsey bins are near `1.5 MHz`, `1.115 MHz`, and `1.885 MHz`.
  - Detrended ratio FFT largest bins are `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `1.935 MHz`, `1.774 MHz`; expected bins have ranks `12` for carrier, `11` for lower sideband, and `4` for upper sideband.
  - Empirical damped-cosine fits are not claim-grade: raw signal fit `R2 ~ 0.10`, ratio fit `R2 ~ 0.19`, reference-line-normalized signal fit `R2 ~ 0.11`; fitted frequencies/T2star are unstable or effectively boundary/noise driven.
  - Per-average detrended ratio correlations against the mean trace are positive but modest: about `0.49..0.68`, with large per-average ratio peak-to-peak scatter `0.22..0.29`.

## Plausible interpretation

- The Ramsey experiment completed and contains analyzable data from the accepted aligned r03 NV, with no bridge stop or terminal hardware failure.
- There is real contrast-scale fluctuation in the signal readout, but this scout does not show a clean, stable Ramsey oscillation/decay at the programmed `det = 1.5 MHz`.
- The FFT does not support a clear carrier peak at `1.5 MHz`. It also does not support a robust nearby `13C` assignment: the upper expected sideband bin is among the larger bins, but it is not isolated and the lower sideband/carrier are weak.
- The result is best treated as a completed but non-claim-grade Ramsey scout. It is useful for diagnosing that the current settings/data quality are insufficient for a supported T2star or `13C` conclusion.

## Claims not yet supported

- No supported numeric `T2star` value from this dataset.
- No supported `13C` coupling/nearby-spin conclusion from this dataset.
- No supported statement that r03 lacks `13C` coupling; the measurement is not clean enough to exclude it.
- No supported conclusion that the weak-pi pODMR resonance or aligned-candidate assignment is invalidated by this Ramsey scout.

## Recommended next action

Run one targeted Ramsey follow-up on r03 rather than making a T2star/13C claim from this scout. Keep the weak-pi `mw_freq = 3.876 GHz`, but redesign for cleaner Fourier evidence and drift control: use a longer span if the current advisory allows it, preserve enough sampling to cover `det +/- ~0.385 MHz`, and reduce per-average tracking window by lowering repetitions per average and increasing averages if needed. If the next Ramsey remains non-claim-grade, switch to a diagnostic step such as a fresh weak-pi pODMR/resonance check before further T2star repeats.
