# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json` for project context and prior conclusions.
- `measurement/m001.json`: raw savedexperiment export for completed `ramsey.xml` run.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: Ramsey job spec/result/status/control metadata.
- Relevant prior context from `evidence/e003.json` through `evidence/e011.json`, especially weak-pi pODMR support for `mw_freq = 3.876 GHz` and the Ramsey planning/advisory.
- Generated scratch outputs: `analyze_ramsey.py`, `ramsey_analysis_summary.txt`, and `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `measurement/m001.json` as a 31-point tau scan from `0` to `6 us`, step `0.2 us`, `4` averages x `50000` repetitions, snake scan order, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `full_experiment = 0`.
- Inspected embedded `ramsey.xml` sequence text: with `full_experiment = 0`, the two traces are the true 0-level reference followed by the Ramsey signal readout.
- Reduced raw signal, pointwise `signal/reference`, and `signal / linear-reference-fit`.
- Ran bounded Gaussian-envelope damped-cosine fits and FFT checks after linear detrending with a Hann window.
- Checked per-average means and per-average FFT peak ranks.

## Quantitative checks

- Readout means:
  - reference: mean `45.318 kcps`, SD across tau points `0.865 kcps`, peak-to-peak `3.904 kcps`.
  - Ramsey signal: mean `42.098 kcps`, SD `1.441 kcps`, peak-to-peak `7.750 kcps`.
  - pointwise signal/reference: mean `0.9292`, SD `0.0340`, peak-to-peak `0.1355`.
- Per-average means drift substantially:
  - avg 1: reference `46.437 kcps`, signal `43.365 kcps`.
  - avg 2: reference `43.682 kcps`, signal `40.553 kcps`.
  - avg 3: reference `46.593 kcps`, signal `42.797 kcps`.
  - avg 4: reference `44.558 kcps`, signal `41.677 kcps`.
- Descriptive damped-cosine fits:
  - raw signal: `T2star ~ 3.18 us`, fitted frequency `~0.959 MHz`, `R2 = 0.457`.
  - signal/reference: `T2star ~ 3.20 us`, fitted frequency `~0.939 MHz`, `R2 = 0.445`.
  - signal/linear-reference: `T2star ~ 3.19 us`, fitted frequency `~0.959 MHz`, `R2 = 0.463`.
- FFT checks:
  - The strongest full-trace FFT peak is near `0.968 MHz` in raw signal and normalized traces.
  - The programmed carrier `det = 1.5 MHz` maps nearest to the `1.452 MHz` bin and is only rank `12-13` in the full-trace raw/ratio FFT.
  - Expected approximate 13C sideband bins from the planning model are near `1.115 MHz` and `1.885 MHz`; nearby bins appear in some views but are not dominant or repeatable enough across averages.
  - Per-average ratio FFTs are inconsistent: avg 1 peaks at `0.968 MHz`, avg 2 at `1.452 MHz`, avg 3 at `0.323/1.129/1.290 MHz`, and avg 4 at `0.806 MHz`.

## Plausible interpretation

- The run completed normally and contains analyzable Ramsey readouts on the accepted r03 candidate.
- There is a real-looking oscillatory component in the Ramsey signal, and the raw and normalized reductions give similar descriptive fits.
- The apparent dominant oscillation is around `0.94-0.97 MHz`, not the programmed `1.5 MHz` carrier. A plausible explanation is that the actual resonance was offset from the weak-pi grid setting by roughly several hundred kHz, or that drift/reference variation and limited SNR pulled the empirical fit away from the intended carrier.
- The descriptive `T2star ~ 3.2 us` is useful for planning but is not yet a well-supported project conclusion because the fit quality is modest, average-to-average spectral content is inconsistent, and the observed carrier does not match the planned detuning.
- The data do not support a nearby 13C claim. Some FFT power occurs near expected sideband-scale bins, but those bins are comparable to unrelated peaks and are not stable across stored averages.

## Claims that are not yet supported

- A final T2star value for r03 is not yet supported.
- A nearby 13C coupling/sideband assignment is not supported.
- The `0.94-0.97 MHz` empirical Ramsey frequency should not be claimed as a physical coupling or definitive detuning without a resonance recheck or repeat Ramsey.
- The weak-pi pODMR center remains adequate as prior evidence for launching this scout, but this Ramsey result does not independently prove the microwave frequency was still centered during the run.

## Recommended next action

Do not make a final T2star or 13C conclusion from this scout. The next targeted action should be a fresh track plus narrow weak-pi pODMR recheck around the r03 resonance, then a redesigned Ramsey repeat using the confirmed center and a deliberately chosen detuning. For the repeat, preserve enough tau span and sampling to resolve the carrier and `~0.385 MHz` sideband scale, and increase claim strength by improving SNR/average consistency rather than relying on the current descriptive fit.
