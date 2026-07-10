# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md` for project objective, current r03 status, prior Ramsey results, and analysis rules.
- `measurement/m001.json`: raw export for the newly completed Ramsey run, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: executed job contract for `nv23_ramsey_20260514_015423_auto_ramsey`.
- `measurement/m003.json`: terminal job result.
- `measurement/m004.json` and `measurement/m005.json`: final run status/control.
- Analysis outputs created here:
  - `analysis/ramsey_detshift_analysis.json`
  - `analysis/ramsey_detshift_detrended.json`
  - `analysis/ramsey_detshift_review.png`

## Calculations/Scripts Run

- Used local Python/NumPy to inspect the raw JSON shape and metadata.
- Extracted `ExperimentData` as two readout channels over tau and `ExperimentDataEachAvg` as 12 stored averages.
- Confirmed run parameters from metadata:
  - `tau = 0.048..1.968 us`, 41 points, step 48 ns.
  - `mw_freq = 3.8759 GHz`.
  - `det = 1.5 MHz`.
  - `12 averages x 90000 repetitions`.
  - Final job status completed, final count text `44.796 kcps`, no stop request, no bridge error.
- Computed raw signal, reference, point-wise signal/reference ratio, and signal divided by a fitted reference line.
- Estimated across-average uncertainty:
  - Mean signal `48.084 kcps`, mean reference `44.269 kcps`.
  - Median signal SEM `0.745 kcps`.
  - Median ratio SEM `0.0146`.
  - Signal peak-to-peak over tau `2.400 kcps`.
  - Ratio peak-to-peak `0.163`.
- Ran FFT screens after linear detrending/Hann window. Top bins were grid-limited by the short record:
  - raw signal: strongest bin near `1.016 MHz`; `1.524 MHz` also present but not dominant.
  - ratio: strongest bins near `0.508`, `1.524`, and `2.033 MHz`.
  - reference-line-normalized view: strongest bin near `1.016 MHz`.
- Ran dense least-squares sinusoid screens. A naive low-frequency-inclusive screen was boundary-dominated, so a second focused screen detrended with a quadratic baseline and searched `0.6..3.0 MHz`.
  - Raw signal and reference-line-normalized residuals peaked near `0.92 MHz`.
  - Ratio residuals peaked near `0.83 MHz`.
  - Per-average ratio top frequencies were scattered: `0.68..1.778 MHz`, not a stable repeated component.
- Checked planned comparison frequencies:
  - Programmed carrier `1.5 MHz`.
  - Prior empirical component `1.192 MHz`.
  - Det-tracking prediction from prior component: `1.692 MHz`.
  - Approximate expected 13C sidebands for this det-shift check: `1.307` and `2.076 MHz`.

## Plausible Interpretation

- The det-shift Ramsey run is analyzable and completed without a hard acquisition anomaly.
- It does not support the hypothesis that the previous `~1.19 MHz` empirical feature was a clean physical Ramsey carrier that tracks the programmed detuning by `+0.5 MHz`.
- The raw and reference-line-normalized views do not show a dominant component at `1.5 MHz` or `1.692 MHz`. The strongest focused residual screen is instead around `0.92 MHz`.
- The ratio-only view gives larger apparent amplitudes near `0.83 MHz` and moderate fixed-frequency fits near `1.5..1.7 MHz`, but this is not supported by raw signal or reference-line-normalized signal and is therefore not claim-grade under the project readout rules.
- The FFT bins near `1.524` and `2.033 MHz` are compatible with some oscillatory content in the short record, but they are not dominant across readout treatments and do not establish carrier/sideband physics.
- Overall, this looks more like weak, readout/baseline-sensitive structure plus short-record spectral ambiguity than a supported Ramsey carrier or 13C sideband model.

## Claims Not Yet Supported

- No supported numeric T2star for r03 from this run.
- No supported nearby 13C conclusion from this run.
- No supported claim that the programmed `1.5 MHz` carrier is present in the raw/readout-aware data.
- No supported claim that the prior `~1.19 MHz` component det-tracked to `~1.69 MHz`.
- No supported sideband claim at `~1.307` or `~2.076 MHz`.

## Recommended Next Action

- Do not run another blind Ramsey repeat on r03 under the same route.
- Treat the r03 Ramsey branch as non-claim-grade under current conditions unless an alternate protocol can directly test coherence with stronger signal presence.
- Recommended next decision: switch to an alternate coherence protocol or close r03 Ramsey/13C as unsupported under the current Ramsey implementation, while preserving the aligned-NV finding from pODMR.
