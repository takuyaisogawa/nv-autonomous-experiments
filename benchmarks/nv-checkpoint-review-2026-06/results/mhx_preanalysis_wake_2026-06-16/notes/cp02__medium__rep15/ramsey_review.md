# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective, candidate history, and required review posture.
- `md/knowledge.md`, `md/memory.md`: local experiment-analysis guidance.
- `evidence/e008.json`, `evidence/e009.json`, `evidence/e010.json`: second Ramsey design/advisory/submission context.
- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`: submitted job spec.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_results.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` as two readouts over 41 tau points: 0-level reference and Ramsey signal. Parsed `ExperimentDataEachAvg` for 8 stored averages.
- Built `tau = 0..8 us` with `dt = 0.2 us`; used signal/reference normalization because the average-level reference and signal means are strongly common-mode correlated (`r = 0.995`).
- Computed combined raw means: reference `49.31 kcps`, signal `44.58 kcps`, mean signal/reference `0.9042`, ratio peak-to-peak `18.76%`.
- FFT checked the linear-detrended ratio trace. Largest ratio FFT bins:
  - `1.2195 MHz`, amplitude `2.18%` of mean ratio.
  - `0.4878 MHz`, amplitude `1.82%`.
  - `1.0976 MHz`, amplitude `1.47%`.
  - `0.9756 MHz`, amplitude `1.42%`.
  - `0.6098 MHz`, amplitude `1.24%`.
- Ran fixed-frequency sine/cosine projections on the normalized ratio:
  - Expected lower 13C sideband `0.6155 MHz`: `1.22%`, `R2 = 0.070` vs linear baseline.
  - Prior feature `0.884 MHz`: `0.82%`, `R2 = 0.032`.
  - Programmed carrier `1.000 MHz`: `1.01%`, `R2 = 0.050`.
  - Strongest ratio least-squares component near `1.178 MHz`: `2.49%`, `R2 = 0.305`.
  - Expected upper 13C sideband `1.385 MHz`: `0.93%`, `R2 = 0.043`.
- Checked per-average behavior at `1.178 MHz`: most averages have roughly aligned phase near pi, but amplitudes vary strongly (`0.69%` to `5.30%` of each average's ratio mean).

## Plausible interpretation

- The second Ramsey completed successfully and the data are analyzable.
- The raw readouts have substantial average-to-average common-mode brightness changes, but ratio normalization is appropriate and removes much of that common mode.
- The normalized trace contains a plausible Ramsey-like oscillatory component, strongest around `1.18 MHz` to `1.22 MHz` depending on least-squares vs FFT binning.
- This component is not the expected `1.000 MHz` programmed carrier. It is also not a repeat of the prior scout's weak `~0.884 MHz` feature, so the prior feature is not supported as a fixed robust component by this run.
- Expected 13C sideband positions near `0.615/1.385 MHz` are present only at weak, non-selective projection levels and are not stronger than unrelated nearby components.

## Claims that are not yet supported

- Do not claim a final T2star from this run. A damped-cosine model would be driven by a modest off-carrier component and variable per-average amplitudes, so the decay time would be model-dependent rather than well supported.
- Do not claim resolved 13C coupling. The expected sidebands are weak and not preferentially supported relative to other components.
- Do not claim that the Ramsey carrier faithfully follows the programmed detuning. The strongest normalized component is near `1.18 MHz`, not `1.00 MHz`.
- Do not claim that the prior `0.884 MHz` feature is physical; it is weak here.

## Recommended next action

Before a longer T2star/13C acquisition, run a targeted frequency/phase diagnostic on r03: either a short repeated Ramsey with two deliberately separated detunings around the observed component, or a fresh fine weak-pi pODMR check followed immediately by a Ramsey whose analysis plan explicitly tests whether the observed frequency follows `det + resonance offset`. Only proceed to a claim-grade longer Ramsey after the carrier origin is pinned down.
