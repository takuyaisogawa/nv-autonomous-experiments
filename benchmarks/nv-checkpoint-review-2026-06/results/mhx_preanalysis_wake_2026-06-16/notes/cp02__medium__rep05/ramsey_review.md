# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json` for the project state and required interpretation posture.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, and `measurement/m005.json` for the second Ramsey job contract, terminal result, status, and control state.
- `measurement/m001.json` for the terminal savedexperiment raw export from `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `evidence/e013.md` and recent evidence summaries for the fine-pODMR center and Ramsey design rationale.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`; it writes `ramsey_analysis_summary.json` and `ramsey_trace_fft.png`.
- Readout roles were checked from the exported `ramsey.xml`: with `full_experiment=0`, readout 1 is the initial mS=0 reference and readout 2 is the post-Ramsey signal.
- Basic run parameters from the raw export: `tau = 0..8 us`, `dt = 0.2 us`, 41 points, snake scan order, tracking per average, `8 x 50000` repetitions, final bridge counts `44.184 kcps`.
- Combined readout checks: reference mean `49.31 kcps`, signal mean `44.58 kcps`, reference span `4.29 kcps`, signal span `7.72 kcps`, mean signal/reference ratio `0.904`.
- Per-average common-mode check: average reference means ranged `40.47..55.53 kcps` and signal means ranged `36.20..50.27 kcps`, about `30-32%` of their means; ratio means ranged only `0.8909..0.9258`, about `3.9%` of the ratio mean.
- FFT of the detrended combined raw signal had largest bins at about `1.220 MHz`, `1.098 MHz`, `0.488 MHz`, `0.122 MHz`, and `0.610 MHz`. The detrended ratio FFT had largest bins at about `1.098 MHz`, `1.220 MHz`, `0.976 MHz`, `0.488 MHz`, and `0.366 MHz`.
- Linear-plus-sinusoid least-squares checks at the planned diagnostic frequencies were weak:
  - raw signal amplitude at prior `0.884 MHz`: `0.286 +/- 0.286 kcps`, z `1.00`;
  - lower 13C sideband `0.615 MHz`: `0.477 +/- 0.287 kcps`, z `1.66`;
  - carrier `1.000 MHz`: `0.277 +/- 0.287 kcps`, z `0.96`;
  - upper 13C sideband `1.385 MHz`: `0.264 +/- 0.287 kcps`, z `0.92`.
- The same checks on ratio percent were also weak at the target frequencies: z scores about `1.10`, `1.68`, `1.39`, and `1.28`.
- Exploratory frequency-grid least-squares found the raw signal best near `0.465 MHz` with amplitude `0.914 +/- 0.253 kcps`, z `3.62`, `R2 = 0.33`; the ratio trace best near `1.18 MHz` with amplitude `2.25 +/- 0.56 percentage points`, z `4.03`, `R2 = 0.31`.
- A diagnostic damped-cosine grid search on raw signal preferred about `0.46 MHz`, `T2star ~1.6 us`, and amplitude `3.63 kcps`, but this is exploratory because the target carrier/sideband evidence is not coherent and per-average spectra disagree.

## Plausible interpretation

- The measurement completed and is analyzable; it is not a failed or zero-average run.
- The trace contains Ramsey-like oscillatory structure, but the structure is not cleanly locked to the programmed `det = 1.0 MHz` carrier. Exact-frequency least-squares at `1.0 MHz` is weak in both raw signal and normalized ratio.
- The det-shift diagnostic does not support the earlier scout's `~0.884 MHz` component as a robust physical carrier: the exact `0.884 MHz` test is weak here.
- Expected 13C sidebands near `0.615/1.385 MHz` are not supported as distinct features. The lower sideband neighborhood appears in the FFT because of the broad/competing low-frequency content, but exact-frequency least-squares is only about `1.6-1.7 sigma`, not claim-grade.
- Large per-average brightness swings make normalization useful as provenance, but not sufficient as a signal-presence criterion. Since raw and ratio frequency-grid optima disagree (`~0.46 MHz` vs `~1.18 MHz`) and per-average top FFT components vary, the safest reading is "non-claim-grade Ramsey structure with drift/common-mode and/or analysis-artifact risk."

## Claims that are not yet supported

- No well-supported `T2star` value should be claimed from this dataset. The exploratory `~1.6 us` damped-cosine result is fit-shape/provenance only.
- No well-supported nearby-13C conclusion should be claimed from this dataset.
- Do not claim that the carrier follows the programmed `det = 1.0 MHz`; the exact carrier test is weak.
- Do not claim that the fine-pODMR center was wrong solely from this Ramsey result; the measurement is affected by common-mode changes and ambiguous spectral content.

## Recommended next action

- Do not blindly repeat the same Ramsey settings. First run a bridge-free synthesis/design step: compare this completed det-shift result with the first `det = 1.5 MHz` scout, inspect whether the Ramsey phase convention or scan/readout normalization can produce the observed `~0.46/1.18 MHz` structures, and choose a targeted diagnostic.
- A reasonable next experiment, after that synthesis and any required current-frequency check, is a short Ramsey phase/detuning diagnostic using the same accepted r03 target but with deliberately separated det settings and enough repeats to test whether the dominant spectral component moves linearly with `det`. If it does not, pivot away from Ramsey T2star/13C claims and consider a different sequence or branch closure/no-13C conclusion.
