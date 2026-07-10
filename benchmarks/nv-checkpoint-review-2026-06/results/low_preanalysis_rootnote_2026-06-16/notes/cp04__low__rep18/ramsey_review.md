# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, and targeted prior review `evidence/e008.json`.
- New measurement:
  - `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: run control.
- Scratch outputs created here:
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_analysis.png`

## Calculations or scripts run

- Used inline Python/NumPy/Matplotlib to inspect the JSON raw export, verify dimensions, compute LS sinusoid screens, FFT checks, per-average target amplitudes/phases, and a compact diagnostic plot.
- Axis/averaging check: `ExperimentDataEachAvg` shape is `[1, 12, 2, 41]`; averaging the average axis reproduces `ExperimentData` to max absolute difference `1.42e-14`.
- Acquisition confirmed: tau `48 ns..1968 ns`, step `48 ns`, 41 points, Nyquist `10.42 MHz`, span-limited frequency spacing about `0.521 MHz`, 12 averages x 90000 repetitions, final count `44.796 kcps`, no stop request, no bridge error.
- Readout summary: mean reference `48.08 kcps`, mean signal `44.27 kcps`; median SEM across stored averages about `0.711 kcps` for raw signal and `0.0126` for signal/reference ratio.
- Frequency checks used linear-baseline + sinusoid least squares on raw signal, point-wise ratio, and signal/reference-line-normalized views.

Key targeted LS amplitudes:

| target | raw signal amp | ratio amp | line-normalized amp |
|---|---:|---:|---:|
| prior fixed component 1.192 MHz | 0.474 kcps | 0.00511 | 0.00993 |
| programmed det 1.500 MHz | 1.128 kcps | 0.02399 | 0.02351 |
| det-tracked prior component 1.692 MHz | 1.225 kcps | 0.02505 | 0.02553 |
| programmed-det 13C low sideband 1.115 MHz | 0.814 kcps | 0.01080 | 0.01697 |
| programmed-det 13C high sideband 1.885 MHz | 0.733 kcps | 0.01729 | 0.01531 |
| det-tracked sideband low 1.307 MHz | 0.266 kcps | 0.00949 | 0.00563 |
| det-tracked sideband high 2.077 MHz | 0.251 kcps | 0.00612 | 0.00532 |

Per-average targeted fits show coherent phase at 1.5 and 1.692 MHz, but the unrestricted 0.7-2.5 MHz best-frequency screen is scattered across averages rather than cleanly locked to one frequency. The broader unconstrained screen is also strongly affected by low-frequency/baseline structure near the search lower edge.

## Plausible interpretation

- The new run is cleanly completed and analyzable. It does not show a persistent fixed artifact at the prior `~1.192 MHz`: the targeted ratio amplitude at 1.192 MHz drops to `0.00511`, far below the prior det=1.0 MHz short-tau review's `0.03631` ratio amplitude.
- There is small but coherent content near the programmed det region: ratio amplitudes are `~0.024` at 1.5 MHz and `~0.025` at the det-tracked `~1.692 MHz` hypothesis, about twice the measured median ratio SEM per tau point. Raw signal amplitudes are `~1.1-1.2 kcps`, also only modestly above the per-point signal SEM.
- This supports a cautious statement that the prior fixed `~1.19 MHz` feature is not stable as a fixed-frequency artifact in this det-shift run. It weakly favors some det-dependent Ramsey response near 1.5-1.7 MHz, but the run does not cleanly distinguish programmed carrier from the det-tracked empirical offset because the scan window is short and the frequency resolution is coarse.
- Expected 13C sideband checks are not compelling. Sideband amplitudes are smaller and not dominant in any readout-aware view.

## Claims not yet supported

- Do not claim a numerical T2star. The signal is small, baseline-sensitive, and not yet cleanly assigned to a carrier model.
- Do not claim nearby 13C coupling. Neither programmed-det sidebands nor det-tracked sidebands dominate over the carrier-region response.
- Do not claim sub-grid frequency precision from this short `1.92 us` span; the natural frequency spacing is about `0.52 MHz`.
- Do not claim that the `1.692 MHz` det-tracked hypothesis is proven. It is only slightly stronger than the programmed `1.5 MHz` carrier check and the free per-average screen is inconsistent.

## Recommended next action

Stop blind Ramsey repeats. Do a bridge-free synthesis across all four r03 Ramsey datasets and decide between:

1. A designed carrier-confirmation Ramsey with conditions chosen specifically to separate `1.5 MHz` from `1.69 MHz` and suppress baseline ambiguity, if a supported T2star remains worth pursuing on r03.
2. Closing the r03 Ramsey/T2star/13C branch as unsupported under current Ramsey conditions and switching to an alternate protocol such as echo/CPMG-style coherence or phase-readout 13C spectroscopy.

The immediate next action should be synthesis and decision, not another same-style Ramsey acquisition.
