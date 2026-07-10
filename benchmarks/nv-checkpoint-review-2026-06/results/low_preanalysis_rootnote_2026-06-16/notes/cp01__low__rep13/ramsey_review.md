# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective, accepted r03 target context, and prior spectroscopy basis.
- `md/memory.md`, `md/knowledge.md`: local Ramsey/NV analysis guidance, especially raw/readout-aware review and FFT-before-claims discipline.
- `context.json`: checkpoint context and recent evidence summaries.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: submitted Ramsey job spec.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result, final status/control, and batch state.

Generated local artifacts:

- `ramsey_analysis_summary.json`: numerical summary from the Python analysis.
- `ramsey_review_plot.png`: raw readouts, normalized ratio, damped-cosine overlay, and FFT plot.

## Calculations/Scripts Run

- Parsed `measurement/m001.json` with Python.
- Confirmed Ramsey scan shape: 31 tau points from `0` to `6 us`, step `0.2 us`, 4 stored averages, 50000 repetitions/average, snake scan order, data saved in tau order.
- Treated readout 1 as reference-like and readout 2 as Ramsey signal-like for review; checked both raw readouts and the readout2/readout1 ratio.
- Computed readout means and span:
  - readout 1 mean `45.318 kcps`, span `8.61%` of mean.
  - readout 2 mean `42.098 kcps`, span `18.41%` of mean.
  - median-normalized ratio span `14.62%`.
- Checked average-to-average behavior:
  - per-average ratio means: `0.9347`, `0.9298`, `0.9199`, `0.9377`.
  - ratio SEM median across the four averages: about `2.56%`, with pointwise SEM range about `0.94%` to `6.02%`.
- FFT of detrended median-normalized ratio:
  - actual rFFT bin spacing from the 31 inclusive points is `161.29 kHz`; Nyquist is `2.419 MHz`.
  - largest averaged FFT bins: `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `1.935 MHz`, `1.774 MHz`.
  - programmed `det = 1.5 MHz` is not the strongest component.
  - expected rough 13C sidebands at `1.5 +/- 0.385 MHz` are not cleanly isolated.
- Least-squares amplitude checks on the normalized ratio:
  - at `1.5 MHz`: amplitude `0.62%`, `R2 = 0.030`.
  - at `1.115 MHz`: amplitude `0.85%`, `R2 = 0.042`.
  - at `1.885 MHz`: amplitude `1.27%`, `R2 = 0.078`.
- Damped-cosine fits to the normalized ratio:
  - exponential envelope fit: `T ~ 2.39 us`, `f ~ 0.941 MHz`, `R2 ~ 0.446`.
  - Gaussian envelope fit: `T ~ 3.20 us`, `f ~ 0.939 MHz`, `R2 ~ 0.445`.
  - residual standard deviation after best fit is about `2.73%`.

## Plausible Interpretation

The Ramsey scout completed normally and is usable as diagnostic evidence, but it is not claim-grade for T2star or 13C. There is real point-to-point structure in the signal-like readout and ratio, with a ratio span larger than the median SEM, so the data are not blank. However, the oscillatory structure is not cleanly tied to the programmed `1.5 MHz` Ramsey detuning, and the largest FFT components are broad/inconsistent rather than a stable carrier plus sidebands.

The descriptive damped-cosine fits prefer about `0.94 MHz`, not `1.5 MHz`, and explain less than half of the variance. Per-average FFT peaks move substantially between averages, which weakens any single-frequency interpretation. The final count level in the bridge result was `38.249 kcps`, lower than the preceding weak-pODMR final count (`43.890 kcps`) but still above the configured `20 kcps` gate; drift/count change is therefore relevant provenance, not a hard invalidation.

The most plausible current interpretation is: r03 remains the aligned candidate from prior pODMR evidence, but this first Ramsey scout is non-claim-grade because of drift/noise and/or a Ramsey frequency mismatch. It justifies a redesigned follow-up rather than a T2star or 13C conclusion.

## Claims Not Yet Supported

- No well-supported numeric T2star value is established by this Ramsey run.
- The fit-derived `T ~ 2.4-3.2 us` should not be promoted; the fit quality is weak and the fitted frequency is inconsistent with the planned carrier.
- No nearby 13C claim is supported. The FFT does not show a clean, repeatable carrier with resolved sidebands at `det +/- ~0.385 MHz`.
- This run does not invalidate r03 as the aligned candidate, because prior strong-pi and weak-pi pODMR evidence established the resonance and this Ramsey result is limited by data quality/consistency.

## Recommended Next Action

Before claiming T2star or 13C, do a bounded follow-up on r03 with fresher resonance/count provenance and a shorter per-average drift window. Practically: fresh TrackCenter, preferably a compact weak-pi pODMR check if timing allows, then repeat Ramsey with the same physical goal but split into shorter tracked averages or reduced repetitions per average. Keep the 13C-resolving tau span/FFT plan explicit, and treat the observed `~0.94 MHz` component as a diagnostic hypothesis to test rather than as a confirmed Ramsey frequency.
