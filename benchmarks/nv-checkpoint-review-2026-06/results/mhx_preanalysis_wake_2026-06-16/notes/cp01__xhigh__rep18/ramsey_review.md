# Ramsey Review: r03 T2star/13C Scout

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective and prior context. The active target is accepted aligned candidate `image145844_reimage_r03`, with strong/weak pODMR support and weak-pi grid resonance at `3.876 GHz`.
- `measurement/m002.json`: Ramsey job contract. Scan was `tau = 0..6 us`, `31` points, `det = 1.5 MHz`, `mw_freq = 3.876 GHz`, `length_pi_pulse = 52 ns`, `4 averages x 50000 repetitions`, `full_experiment = 0`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result/status/control. Job completed, not aborted or incomplete. Final count text was `38.249 kcps`; this is below the fresh r03 track/weak-pODMR level (`43.535/43.890 kcps`) but above the `20 kcps` run gate.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`. It contains two readouts: readout 1 optical reference, readout 2 Ramsey signal. Saved scan position is `["117.279", "117.294", "115.535"]`.
- Generated local analysis artifacts: `ramsey_analysis.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_stdout.txt`, and `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python ramsey_analysis.py` to parse `measurement/m001.json`, compute readout summaries, normalize `signal/reference`, inspect per-average consistency, reconstruct acquisition-order slopes from `ScanOrderEachAvg`, run FFT checks, and run descriptive sinusoid/damped-cosine fits.
- Basic readout statistics:
  - Reference mean/range: `45.318 kcps`, range `44.038..47.942 kcps`.
  - Signal mean/range: `42.098 kcps`, range `38.096..45.846 kcps`.
  - Normalized ratio mean/range: `0.92919`, range `0.85906..0.99458`, peak-to-peak `14.58%` of mean.
  - Median per-tau SEM across the 4 averages: `0.02557` in normalized ratio; half peak-to-peak is `2.65x` this median SEM.
- Per-average checks:
  - Per-average ratio means: `0.93474`, `0.92983`, `0.91990`, `0.93773`.
  - Correlation of each average with the averaged ratio trace: `0.684`, `0.424`, `0.581`, `0.561`; not cleanly repeatable.
  - Acquisition-order ratio slopes per scan point: `+0.00143`, `+0.00199`, `+0.00040`, `-0.00174`; modest drift/order structure remains after normalization.
- FFT checks:
  - Actual FFT grid from the saved data is `N=31`, `dt=0.2 us`, bin spacing `161.29 kHz`, highest rFFT bin `2.419 MHz`.
  - Windowed, linear-detrended ratio FFT strongest bins: `0.9677 MHz`, `0.8065 MHz`, `0.3226 MHz`, `1.9355 MHz`, `1.7742 MHz`.
  - The planned Ramsey carrier `1.5 MHz` is not a dominant ratio FFT peak. Expected rough 13C sidebands from the project model would be near `1.115 MHz` and `1.885 MHz`; nearby FFT content exists but is not dominant, isolated, or per-average consistent.
- Fit checks:
  - Best offset+linear+sin/cos scan to the averaged normalized trace prefers about `0.948 MHz` with `R2 = 0.288`.
  - Fixed-frequency checks are poor at planned/expected frequencies: `1.500 MHz` gives `R2 = 0.030`; `1.115 MHz` gives `R2 = 0.042`; `1.885 MHz` gives `R2 = 0.078`.
  - A descriptive Gaussian damped-cosine plus linear drift fit gives `T2star = 3.20 us`, `f = 0.939 MHz`, amplitude `0.0529`, `R2 = 0.445`. This is a descriptive feature of this trace only, not a supported T2star claim, because the fitted carrier is inconsistent with the programmed `det = 1.5 MHz`, the fit quality is limited, and the four averages are not mutually consistent.

## Plausible interpretation

- The Ramsey job completed and produced analyzable readouts; this is not a zero-average, abort, or count-gate failure.
- There is visible modulation in the normalized Ramsey signal, but it does not cleanly appear at the intended `1.5 MHz` detuned Ramsey carrier. The most plausible interpretations are a non-claim-grade Ramsey trace affected by drift/SNR/normalization sensitivity, or a resonance/phase condition that shifted during the run relative to the weak-pODMR center used for setup.
- The run may be hinting at an oscillatory decay on a few-us scale, but the only quantitative damped fit lands near `0.94 MHz`, not the planned carrier, and explains less than half the variance. Treat the fitted `~3.2 us` as a planning number only.
- The FFT does not support a nearby 13C conclusion. Peaks near the rough expected upper sideband region are not isolated, the lower sideband check is weak, and the individual averages disagree.

## Claims not yet supported

- A well-supported numerical T2star for r03.
- A claim that the `0.94 MHz` feature is the true Ramsey detuning, a stable physical coupling, or a calibrated resonance offset.
- A claim of resolved nearby `13C` coupling from this Ramsey FFT.
- A negative claim that r03 has no useful T2star or no nearby `13C`; this scout is inconclusive rather than exclusionary.
- Any invalidation of the prior pODMR-based alignment conclusion for r03.

## Recommended next action

Do not use this Ramsey scout for final T2star/13C claims. Keep focus on r03, but first re-establish the current resonance/phase condition: fresh TrackCenter, then a quick narrow weak-pi pODMR or short high-SNR Ramsey frequency scout around the current `3.876 GHz` setting. If the carrier is then stable and matches the programmed detuning, run a confirmation Ramsey/T2star acquisition with improved per-average consistency before fitting T2star or interpreting FFT sidebands.
