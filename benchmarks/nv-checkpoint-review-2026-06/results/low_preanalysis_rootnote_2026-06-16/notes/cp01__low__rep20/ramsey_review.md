# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`, selected guidance from `md/memory.md`.
- New Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job plan, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Generated analysis artifacts in this working directory: `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Inspected JSON structure and project-state pointers with PowerShell/Python.
- Parsed `measurement/m001.json` in Python:
  - tau scan: 31 points, 0 to 6 us, 0.2 us nominal spacing.
  - readouts: two raw lines, four stored averages.
  - computed raw contrast as `(readout0 - readout1) / readout0`.
  - checked per-average contrast means, ranges, and correlation with the mean trace.
  - computed a Hann-windowed FFT of mean contrast after DC removal.
  - fit a descriptive damped cosine to contrast with scipy.
- Plotting initially failed because matplotlib tried to use a broken local Tk backend; reran with `MPLBACKEND=Agg` and saved `ramsey_analysis.png`.

## Quantitative checks

- Run completion: bridge status completed, no abort/error; saved artifact `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Acquisition: `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `length_pi_pulse = 52 ns`, `4 x 50000` repetitions, snake order with even averages and data saved in tau order.
- Runtime/drift provenance: status expected `492.9461 s` per average and elapsed `2124 s`; this exceeded the earlier 450 s drift target. Final counts were `38.249 kcps`, below the fresh r03 track/weak-pODMR text counts near `43.5-43.9 kcps`.
- Raw readout means: readout0 mean `45.318 kcps`, readout1 mean `42.098 kcps`; relative ranges were `8.6%` and `18.4%`.
- Mean contrast: `0.0708` average contrast, peak-to-peak `0.1355`; median SEM across stored averages `0.0256`, so the observed modulation is only about 5.3 median-SEM peak-to-peak before accounting for model/scan correlations.
- Stored averages: mean contrast per average `[0.0653, 0.0702, 0.0801, 0.0623]`; correlation with the final mean trace `[0.684, 0.424, 0.581, 0.561]`. The feature is not dominated by one average, but per-average agreement is only moderate.
- FFT: actual bin spacing from the sampled 31-point record is `161.3 kHz`, Nyquist `2.419 MHz`. Largest windowed FFT components are near `0.968`, `0.806`, `0.323`, `0.161`, `1.935`, and `1.774 MHz`. The requested detuning bin near `1.452 MHz` is not a dominant peak.
- 13C sideband check: expected sideband scale from project context is about `0.385 MHz`, so det +/- 13C would be near `1.115` and `1.885 MHz`. The upper-side nearest bin at `1.935 MHz` has some amplitude, but comparable or larger peaks occur elsewhere; this is not specific evidence for 13C coupling.
- Descriptive damped-cosine fit: offset `0.0715`, amplitude `0.0734`, frequency `0.9005 MHz`, envelope `T = 2.04 +/- 0.69 us`, reduced chi-square `1.75`, `R2 = 0.397`. This fit is not strong enough to support a final T2star claim.

## Plausible interpretation

The Ramsey scout is usable as a diagnostic: it shows real contrast variation and a short-timescale oscillatory component that appears in all stored averages at least moderately. However, the dominant frequency content is not centered on the intended `1.5 MHz` detuning, and the low `R2`, moderate average-to-average consistency, count drop, and above-target per-average runtime make this measurement non-claim-grade.

A plausible working interpretation is that r03 remains the aligned NV target, but this first Ramsey was affected by detuning mismatch and/or drift/noise enough that it should guide the next Ramsey settings rather than close the T2star/13C objective.

## Claims not yet supported

- No well-supported T2star conclusion. The descriptive `~2.0 us` envelope is provisional and fit-quality limited.
- No well-supported 13C conclusion. The FFT does not show a specific det +/- 0.385 MHz sideband pattern distinguishable from other comparable peaks.
- No claim that the Ramsey carrier is the intended `1.5 MHz` detuning; the strongest fitted/FFT features are closer to `0.8-1.0 MHz`.
- No evidence here that r03 is invalidated as the aligned candidate; prior strong/weak pODMR support still stands unless new spectroscopy or tracking contradicts it.

## Recommended next action

Before another long Ramsey, run a fresh track and a narrow weak-pi pODMR/frequency check around the r03 resonance to verify the microwave center after the observed count drop. Then repeat Ramsey with an adjusted detuning based on the fresh resonance, shorter per-average tracking window if possible, and enough tau span/points to separate the carrier from the expected `~0.385 MHz` 13C sideband. If the fresh center is stable, a follow-up Ramsey centered on a cleaner detuning near the observed `0.9-1.0 MHz` oscillation scale would be more informative than blindly repeating the same `1.5 MHz` scout.
