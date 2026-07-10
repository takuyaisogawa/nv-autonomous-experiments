# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted Ramsey job, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Scratch outputs from this review: `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Loaded `measurement/m001.json` with Python and inspected `ExperimentData` and `ExperimentDataEachAvg`.
- Confirmed scan: Ramsey `tau = 0..6 us`, 31 points, 0.2 us step, snake order, 4 averages x 50000 repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, tracking per average.
- Computed raw signal/reference and per-average signal/reference ratios.
- Ran simple descriptive fits on the combined ratio:
  - Damped cosine: frequency `0.947 MHz`, `T2* = 2.29 us`, amplitude `0.080`, `R2 = 0.435`.
  - Non-oscillatory exponential reached the lower `T2` bound of `0.2 us`, `R2 = 0.127`, so it is not a useful physical claim.
- Ran Hann-window FFT checks after mean and linear detrending. Frequency bin spacing is `161.3 kHz` from the actual 31-point, 0.2 us sampled trace.
- Compared FFT bins near the planned carrier and expected 13C scale: det `1.5 MHz` maps to the `1.452 MHz` bin; det +/- 13C scale maps near `1.129 MHz` and `1.935 MHz`; direct 13C scale maps near `0.323 MHz`.

## Plausible interpretation

- The Ramsey scout is analyzable and has some oscillatory structure in the combined normalized trace, but it is not claim-grade.
- The strongest fitted/FFT component is near `0.95-0.97 MHz`, not at the programmed `1.5 MHz` detuning. This could reflect a real detuning mismatch from the weak-pODMR grid center, scan drift, or an artifact of low-SNR/per-average variation.
- Count/focus drift is material: final count was `38.249 kcps`, about `12.1%` below the fresh tracked `43.535 kcps`; the reference readout range across tau is about `18.4%` of its median.
- Per-average ratios do not show a robust shared waveform. Average minima occur at `2.6, 2.2, 2.8, 5.2 us`, and pairwise per-average ratio correlations are weak (`-0.067` to `0.364`).
- FFT peaks near the expected sideband bins exist but are not selective. Linear-detrended top FFT amplitudes include `0.968 MHz` (`0.200`), `0.323 MHz` (`0.185`), `0.806 MHz` (`0.184`), `1.935 MHz` (`0.176`), and `1.774 MHz` (`0.165`). The candidate det+13C bin at `1.935 MHz` is present but comparable to unrelated nearby/low-frequency components.

## Claims that are not yet supported

- Do not claim a well-supported `T2*` from this scout. The `2.29 us` damped-cosine value is only descriptive because fit quality is modest and per-average reproducibility is weak.
- Do not claim 13C coupling. The FFT does not show a clean, selective carrier-plus-sideband pattern, and the expected 13C-scale bins are not separated from drift/low-frequency and other comparable peaks.
- Do not claim the Ramsey carrier frequency is established. The observed dominant component near `0.95 MHz` disagrees with the planned `1.5 MHz` detuning.
- Do not treat this as evidence against r03 alignment; the prior pODMR evidence still supports r03 as the aligned candidate, while this Ramsey result mainly shows that the current scout is insufficient for final T2*/13C conclusions.

## Recommended next action

Repeat targeted Ramsey on r03 with the microwave frequency adjusted to make the observed Ramsey beat closer to the intended analysis band: use the observed `~0.95 MHz` beat to update the center frequency estimate, then run a shorter/higher-SNR confirmation Ramsey under better drift control before attempting a longer T2*/13C acquisition. Keep the same raw-readout, per-average, and FFT review gates before making final claims.
