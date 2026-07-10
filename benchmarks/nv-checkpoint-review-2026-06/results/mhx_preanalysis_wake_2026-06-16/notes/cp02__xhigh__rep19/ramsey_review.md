# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`, and relevant prior notes in `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal bridge result, plus `measurement/m004.json` status and `measurement/m005.json` control.
- Generated local artifacts: `analyze_ramsey_measurement.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_measurement.py`.
- Confirmed terminal run completed safely: job `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`, `2026-05-13T20:49:36` to `2026-05-13T22:17:11`, final counts `44.184 kcps`, `aborted=false`, `safe_shutdown_ok=true`.
- Parsed scan as `ramsey.xml`, `tau=0..8 us`, `41` points, `dt=0.2 us`, `8 x 50000` shots, `mw_freq=3.8759 GHz`, `det=1.0 MHz`.
- From the saved sequence text, readout 1 is the pre-Ramsey 0-level reference and readout 2 is the post-Ramsey signal for `full_experiment=0`.
- Combined signal/reference ratio: mean `0.9042`, std `0.0294`, min `0.8025` at `0 us`, max `0.9721` at `1.2 us`.
- Scratch common-mode drift proxy flags average `7` using a 15% drop-vs-median rule. Per-average reference means span `40.473..55.529 kcps`, signal means span `36.203..50.272 kcps`, while ratio means are tighter at `0.8909..0.9258`.
- Linear-detrended Hann FFT of the ratio has largest bins at `1.0976 MHz` (`0.0211` amp), `1.2195 MHz` (`0.0188`), and `0.9756 MHz` (`0.0133`).
- Targeted least-squares sinusoid checks on the ratio:
  - Best scanned carrier-like frequency: `1.175 MHz`, amp `0.0225`, per-average phase coherence `0.91`, approximate complex z `3.68`, RMS improvement `16.6%`.
  - Programmed `1.0 MHz` det: amp `0.00916`, coherence `0.64`, z `1.93`, RMS improvement `2.5%`.
  - Prior scout component `0.884 MHz`: amp `0.00742`, coherence `0.51`, z `1.43`.
  - Expected sidebands from programmed det, `0.6154/1.3846 MHz`: amps `0.0111/0.00843`, z `1.47/1.52`.
  - Expected sidebands from observed carrier, `0.7904/1.5596 MHz`: amps `0.00458/0.00338`, z `0.98/0.58`.
- Excluding drift-proxy-flagged average 7 keeps the ratio peak near `1.18 MHz` with amp `0.0233`; it is not created by that average.
- Bounded ratio fits give model-dependent T2* scale only: exponential envelope `T2*=2.28 us`, `f=1.187 MHz`; Gaussian envelope `T2*=4.68 us`, `f=1.182 MHz`. Bootstrap 5-95% ranges are broad: exponential `0.42..6.12 us`, Gaussian `1.23..7.68 us`.

## Plausible interpretation

- The new Ramsey run is valid and analyzable. Counts are healthy, the run completed normally, and the signal/reference trace has a reproducible carrier-like component.
- The dominant ratio component is near `1.18 MHz`, close to but not exactly the programmed `1.0 MHz` det. This is plausibly a Ramsey carrier with residual microwave detuning or finite grid/fit uncertainty around the fine pODMR center.
- The prior scout's non-claim-grade `~0.884 MHz` component is not reproduced as the dominant feature, so it is less likely to be a stable physical carrier.
- This run gives a rough T2* scale of a few microseconds, but the envelope depends strongly on model choice and average resampling.
- There is no claim-grade 13C signature in this run. Sidebands are weak and incoherent both at `1.0 MHz +/- 0.3846 MHz` and at observed-carrier `1.175 MHz +/- 0.3846 MHz`.

## Claims not yet supported

- A final numerical T2* value for r03 is not supported yet.
- Nearby 13C coupling is not supported by this Ramsey. A broad absence claim for all nearby 13C is also stronger than this single drift-affected run supports.
- The exact microwave resonance offset inferred from the `1.18 MHz` carrier is not established; the sign convention and reproducibility need confirmation.
- Average 7 should not be ignored as harmless without a formal drift-aware review, even though the main ratio peak survives excluding it.

## Recommended next action

Run one confirmation Ramsey on r03 after re-tracking, using the same `det=1.0 MHz`, `tau=0..8 us`, `41` point design and at least the same averaging if the per-average tracking window remains acceptable. Review it with the same drift-aware ratio/FFT/least-squares checks. If the `~1.18 MHz` carrier and the absence of 13C sidebands reproduce, fit the two Ramsey runs jointly for T2* and close the 13C conclusion as no claim-grade sideband in Ramsey. If it does not reproduce, do not keep repeating blindly; switch to an alternate diagnostic or close this r03 Ramsey branch as non-claim-grade.
