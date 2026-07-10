# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey data/metadata:
  - `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal run status.
  - `measurement/m005.json`: run control state.
- Derived local artifacts created here:
  - `ramsey_analysis.json`: Python numerical summary.
  - `ramsey_review_plot.png`: raw readouts, normalization views, and LS frequency screen.

## Calculations/scripts run

- Used local Python to parse `measurement/m001.json`, verify the per-average axis contract, compute SEM across stored averages, inspect drift by average, screen sinusoidal components by least-squares, run simple FFT-bin checks, and attempt descriptive damped-sinusoid fits.
- Axis check: averaging `ExperimentDataEachAvg[scan, avg, readout, point]` over the 20 averages reproduced `ExperimentData` to numerical precision (`max abs diff` about `1e-14`), so readout 1 was treated as reference and readout 2 as Ramsey signal.
- Acquisition was the intended refreshed-center Ramsey: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 48 ns..8.048 us`, 41 points, `20 x 50000` shots, final counts `43.433 kcps`, no stop request.
- Median SEM across stored averages was `0.85 kcps` for the raw signal and `0.87 kcps` for the reference. Average-to-average mean levels varied substantially (`~29%` signal range and `~27%` reference range), but a simple robust 3-sigma average-mean screen did not flag individual averages.
- Full-span LS screens with linear baseline:
  - Raw signal top component: `2.271 MHz`, amplitude `0.818 kcps`, `R2 = 0.378`.
  - Fitted-reference normalization top component: `2.271 MHz`, amplitude `0.0168`, `R2 = 0.369`.
  - Programmed `1.5 MHz` carrier: raw amplitude `0.705 kcps`, fit-ref ratio amplitude `0.0145`, both below the 2.27 MHz screen and comparable to the raw per-point SEM.
  - Expected 13C sidebands from the plan (`1.115/1.885 MHz`) were weak: raw amplitudes `0.146/0.261 kcps`; fit-ref ratio amplitudes `0.0030/0.0054`.
- Skip-transient checks after dropping the first 4, 6, or 8 tau points kept the top screen near `2.27..2.29 MHz`. The carrier remained present but not dominant, and the expected sidebands stayed weak.
- FFT-bin check, after detrending, similarly put the strongest raw/fit-ref bins at `2.317` and `2.195 MHz`; the nearest carrier bins at `1.463/1.585 MHz` were visible but not cleanly dominant. Nearest sideband bins were smaller.
- Descriptive damped fits were not promoted: carrier-constrained and top-frequency fits returned model-dependent values (`T2star` from about `0.22 us` to `1.8 us`, depending on view/frequency), with only moderate `R2` and no supported physical frequency assignment.

## Plausible interpretation

- The run completed safely and produced analyzable Ramsey data at the intended refreshed pODMR center.
- There is weak carrier-like content near the programmed `1.5 MHz` detuning, stronger than in some earlier branches, but it is not the dominant spectral feature and is near the measured per-point uncertainty scale in raw kcps.
- The most reproducible combined screen in this run is instead near `2.27 MHz`, close to the upper part of the usable band (`Nyquist ~2.44 MHz`). Because that component is not the programmed carrier and was not the expected `13C` sideband, it is better treated as an empirical feature or possible measurement/analysis artifact until specifically tested.
- The expected `13C` sideband pattern around `1.115` and `1.885 MHz` is not supported in this dataset.
- Taken with the earlier Ramsey history summarized in `project/state.md`, this refreshed-center high-shot repeat still does not yield a claim-grade T2star or 13C conclusion from Ramsey alone.

## Claims not yet supported

- Do not claim a numeric `T2star` from this run. The fitted decay values depend strongly on which spectral component is fit and whether raw or normalized data are used.
- Do not claim nearby `13C` coupling. The expected sidebands are weak and not consistently dominant under raw, ratio, fit-reference, FFT, full-span, or skip-transient checks.
- Do not claim that the `2.27 MHz` feature is physical NV Ramsey precession. It may be real in the measured trace, but its assignment is unsupported.
- Do not claim that more identical Ramsey averaging will solve the ambiguity. This was already a high-shot refreshed-center repeat and still lacks a clean carrier/sideband model.

## Recommended next action

Avoid another blind Ramsey repeat under the same conditions. The next scientifically useful action is to change protocol or diagnostic axis: either run an alternate T2 baseline protocol such as Hahn/CPMG (`N=1`) to establish a coherence scale without relying on the ambiguous Ramsey carrier assignment, or deliberately test the `2.27 MHz` empirical feature with a detuning-shift Ramsey diagnostic designed to see whether the feature tracks programmed detuning or stays fixed. If the project goal requires a 13C conclusion, move toward a better-resolved coupling protocol after a coherence baseline is established.
