# Ramsey review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior/planning evidence: `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Run reviewed: `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940`.

## Calculations/scripts run

- Created and ran `analyze_ramsey.py`; outputs are `ramsey_analysis_summary.json`, `ramsey_analysis_stdout.json`, and `ramsey_analysis.png`.
- Confirmed `ramsey.xml` active path in the raw export: `full_experiment=0`, readout 1 is the `mS=0` reference and readout 2 is the Ramsey signal.
- Parsed the scan: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, 8 averages x 50000 repetitions, snake scan order, per-average tracking, `det = 1.0 MHz`, final counts `44.184 kcps`.
- Raw combined readouts: reference mean `49.31 kcps`, signal mean `44.58 kcps`, signal peak-to-peak `7.72 kcps`; median per-tau signal SEM across the 8 averages is `1.92 kcps`.
- Average-to-average brightness varied substantially: reference mean range `40.47..55.53 kcps`, signal mean range `36.20..50.27 kcps`; signal/reference average means were tighter, about `0.891..0.926`, so much of this is common-mode brightness drift.
- Least-squares sinusoid checks on the raw signal at planned frequencies, with intercept + linear trend:
  - `1.000 MHz` carrier: amplitude `0.277 kcps`, `R2 = 0.115`.
  - `0.615 MHz` lower 13C sideband: amplitude `0.475 kcps`, `R2 = 0.156`.
  - `1.385 MHz` upper 13C sideband: amplitude `0.263 kcps`, `R2 = 0.113`.
  - prior scout component `0.884 MHz`: amplitude `0.286 kcps`, `R2 = 0.117`.
- Hann-window FFT of raw signal: strongest bins were `1.220 MHz` (`0.80 kcps`) and `1.098 MHz` (`0.76 kcps`), but target-bin amplitudes were small: carrier bin `0.976 MHz` (`0.34 kcps`), lower-sideband bin `0.610 MHz` (`0.40 kcps`), upper-sideband bin `1.341 MHz` (`0.37 kcps`), prior-component bin `0.854 MHz` (`0.23 kcps`).
- A free damped-cosine fit returned a descriptive component near `0.462 MHz` with `T2star ~1.66 us` and `R2 ~0.56`, but this is post hoc, not at the programmed carrier, and changes/weakens under early-point exclusion.

## Plausible interpretation

- The experiment completed cleanly and the NV remained bright enough for analysis.
- The raw Ramsey signal has a strong early low-to-plateau transient from `tau = 0` to roughly `1 us`; after that, the trace has only weak fluctuations. The trace is not a clean `1.0 MHz` Ramsey carrier.
- The det-shift diagnostic did not recover a claim-grade carrier that follows the programmed detuning. The prior non-claim-grade `~0.884 MHz` component also does not reappear strongly.
- The weak lower-sideband-sized least-squares/FFT response near `0.615 MHz` is at most a hint. It is below the expected `2..6 kcps` raw oscillation scale from the planning model, below the per-point SEM scale, and not accompanied by a clean carrier or upper sideband.
- Brightness drift/common-mode variation across averages is significant provenance. Ratio-normalized traces are useful as a drift cross-check, but signal presence should still be judged from raw/readout-aware evidence.

## Claims not yet supported

- Do not claim a measured `T2star` from this run.
- Do not claim nearby 13C coupling from the FFT/sideband checks.
- Do not claim the programmed `1.0 MHz` Ramsey carrier was observed.
- Do not use the free damped-cosine fit as a physical T2star estimate; it is descriptive and fit-driven after signal presence failed.
- Do not infer that the fine pODMR center is wrong from this Ramsey alone; the fine pODMR still supports `mw_freq = 3.8759 GHz` as a grid-supported resonance input.

## Recommended next action

Do not blindly repeat a longer Ramsey on r03. First run a compact Ramsey route/calibration diagnostic: reconfirm the pi/2 pulse/resonance state, then verify that `ramsey.xml` produces a carrier that follows a deliberately chosen detuning in raw readout 2. If that control fails again, treat the r03 Ramsey branch as non-claim-grade and decide between an alternate sequence for 13C/T2 follow-up or closing r03 and returning to candidate search.
