# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Ramsey execution metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` completed status, `measurement/m005.json` run control.
- Ramsey raw export: `measurement/m001.json`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Supporting recent context: `evidence/e009.json` and `evidence/e010.json` for the Ramsey launch/run status; `evidence/e011.json` is a stale batch state captured while the batch was still marked running and was not used as terminal evidence.

## Calculations or scripts run

- Ran `python .\ramsey_analysis.py`.
- Created `ramsey_analysis_summary.json` and `ramsey_trace_fft.png`.
- Checked the raw readouts, signal/reference normalization, per-average normalized traces, first-to-last average drift, a linear-detrended FFT, target FFT bins at `det = 1.5 MHz` and `det +/- 0.385 MHz`, and a descriptive damped-cosine fit to the normalized Ramsey trace.

Key quantitative checks:

- Scan was `tau = 0..6 us`, `31` points, `dt = 0.2 us`, `4 x 50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `full_experiment = 0`.
- Sequence readout roles from `ramsey.xml`: readout 1 is the `mS=0` reference, readout 2 is the Ramsey signal.
- Mean reference/readout signal: `45.318 kcps` / `42.098 kcps`; mean normalized signal/reference `0.9292`.
- Combined normalized trace has `0.0340` point-to-point standard deviation and `0.1336` detrended peak-to-peak range. Median per-point SEM across four averages is `0.0256`, so the largest detrended excursion is only about `2.6 x` that SEM.
- First-to-last average common-mode drift is about `-4.0%` in reference and `-3.9%` in signal; normalized ratio mean changes only `+0.3%`.
- Combined normalized FFT after linear detrend has top peaks at `0.968`, `0.806`, `0.323`, `1.935`, and `1.774 MHz`. The intended carrier bin near `1.452 MHz` is only `0.77 x` the median nonzero FFT amplitude. The expected lower sideband near `1.129 MHz` is `0.83 x` median; the upper sideband near `1.935 MHz` is `1.34 x` median but is not paired with a carrier/lower sideband and is not stable across averages.
- Per-average FFTs are inconsistent: only one average has the carrier bin as the top feature; other averages peak near lower-frequency or sideband-like bins.
- Descriptive damped-cosine fit to signal/reference gives `f = 1.472 MHz`, `T2* = 7.5 us`, but with `R2 = 0.020`, amplitude `-0.0109 +/- 0.0203`, and `T2*` uncertainty `39 us`; this fit is not usable as a T2* estimate.

## Plausible interpretation

The Ramsey job completed cleanly and produced analyzable data on the accepted r03 candidate, but this first scout is non-claim-grade. The raw and normalized traces show weak structure on top of noise and residual drift. The planned `1.5 MHz` Ramsey carrier is not a dominant combined FFT feature, the expected `13C` sideband pattern is not coherent, and per-average spectra do not repeat a stable carrier/sideband structure.

This is most plausibly a weak/noisy Ramsey scout under drift and finite SNR, possibly compounded by resonance detuning during the run or by a T2* envelope that is too poorly resolved in this shot budget. The completed run does not invalidate the prior pODMR-based alignment of r03, but it also does not establish a T2* or nearby-13C conclusion.

## Claims that are not yet supported

- No well-supported numeric `T2*` value is established from this Ramsey run.
- No nearby `13C` coupling or sideband assignment is supported.
- No claim of absent `13C` coupling is supported; the data quality is insufficient for that negative conclusion.
- The descriptive damped-cosine fit should not be used downstream.
- The upper FFT feature near `1.94 MHz` should not be promoted to a physical sideband without a stable carrier and repeatable sideband pattern.

## Recommended next action

Before another long Ramsey acquisition, re-check the current r03 resonance/track state with a short weak-pi pODMR or equivalent resonance diagnostic. If the resonance remains near `3.876 GHz` and counts are healthy, repeat Ramsey with better statistics but shorter per-average drift windows, preferably by increasing the number of averages rather than lengthening each average. Keep the FFT design explicit: preserve coverage of `det` and `det +/- f13C`, and require a stable raw/normalized carrier before fitting T2* or assigning `13C` sidebands.
