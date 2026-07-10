# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior calibration/model context: `evidence/e003.json` weak-pi pODMR review data and `evidence/e005.json` Ramsey model/advisory.
- New Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status.
- Generated local scratch artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_diagnostics.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed `ramsey.xml`, one-dimensional `tau` scan, `tau = 0..6 us`, 31 points, `dt = 0.2 us`, 4 averages x 50000 repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `full_experiment = 0`.
- Sequence text indicates readout 1 is the true 0-level/reference and readout 2 is the Ramsey signal.
- Computed raw readout statistics, per-average signal SEM, scan-order acquisition drift summaries, FFT peaks, expected 13C sideband locations, and empirical cosine / Gaussian-damped-cosine fits.

## Quantitative checks

- Ramsey terminal status: completed. Final count text was `38.249 kcps`; no abort or incomplete-run error is recorded.
- Raw reference readout: mean `45.318 kcps`, standard deviation over tau `0.865 kcps`.
- Raw Ramsey signal readout: mean `42.098 kcps`, standard deviation over tau `1.441 kcps`, min/max `38.096/45.846 kcps`, peak-to-peak `7.750 kcps`.
- Median SEM of signal across the four stored averages is `1.015 kcps`, so the time dependence is visible but not high-margin.
- Scan-order drift check by average gives common-mode end-minus-start fractions from about `-0.6%` to `-2.6%`; this does not look like a hard count-collapse failure, though the final count is lower than the pre-Ramsey weak-pODMR final count.
- Working model from the 3.876 GHz weak-pi pODMR center gives `B ~ 359.3 G`, `13C Larmor ~384.6 kHz`, and expected Ramsey sidebands around `1.115 MHz` and `1.885 MHz` for a `1.5 MHz` carrier.
- FFT bin spacing from the sampled array is `161.3 kHz` (`1/span = 166.7 kHz` planning scale), Nyquist `2.5 MHz`.
- Raw-signal FFT largest peaks are `0.968 MHz` at `1.081 kcps`, `0.161 MHz` at `0.833 kcps`, `1.613 MHz` at `0.650 kcps`, and `1.290 MHz` at `0.631 kcps`.
- The nearest bins to expected features are weak: near `det=1.5 MHz`, bin `1.452 MHz` has amplitude `0.296 kcps`; lower expected 13C sideband bin `1.129 MHz` has `0.282 kcps`; upper expected sideband bin `1.935 MHz` has `0.278 kcps`.
- Best raw-signal cosine fit: frequency `0.961 MHz`, amplitude `1.086 kcps`, `R2 = 0.292`.
- Best raw-signal Gaussian-damped cosine fit: frequency `0.961 MHz`, amplitude `2.298 kcps`, `T2star = 3.19 us`, fit stderr about `1.00 us`, `R2 = 0.455`. The same fit on reference-line-normalized signal gives similar frequency/T2star and similarly low `R2`.

## Plausible interpretation

The Ramsey experiment completed and contains a real-looking, nonflat signal readout on the accepted r03 candidate. However, the dominant spectral component is near `0.96-0.97 MHz`, not at the programmed `1.5 MHz` Ramsey carrier, and the per-average FFT maxima are not consistent enough to promote the empirical fit. This is plausibly a low-SNR Ramsey-like response affected by resonance-grid uncertainty, resonance drift, phase-ramp/effective-detuning mismatch, or ordinary acquisition noise/outliers.

The data are useful as a diagnostic: r03 still appears measurable, and the Ramsey response scale is on the order of a few kcps. The data are not yet claim-grade for a T2star value or for nearby 13C coupling.

## Claims that are not yet supported

- A project-level T2star conclusion is not supported. The `~3.2 us` damped-cosine result is an empirical fit to a low-`R2` trace with the wrong dominant carrier frequency.
- A nearby `13C` conclusion is not supported. FFT amplitudes at the expected `det +/- 384.6 kHz` sidebands are small and not dominant.
- The programmed `1.5 MHz` Ramsey carrier is not cleanly observed in this dataset.
- The Ramsey mismatch should not yet be interpreted as a physical resonance shift without a targeted resonance/frequency diagnostic.

## Recommended next action

Do a targeted frequency check before investing in a longer/higher-SNR T2star run. The cleanest next step is a narrow weak-pi pODMR recalibration around `3.876 GHz` with finer spacing than the previous 1 MHz grid, or an equivalent short Ramsey detuning diagnostic, to test whether the effective resonance is shifted by roughly the `0.5 MHz` implied by the `0.96 MHz` apparent carrier. If the resonance is updated, repeat Ramsey on r03 with the corrected `mw_freq`, preserve 13C sideband coverage below Nyquist, and use more averages rather than a longer per-average window if the advisory cap is tight.
