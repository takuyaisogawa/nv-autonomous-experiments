# Ramsey review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior relevant evidence: `evidence/e004.json`, `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New Ramsey measurement: `measurement/m001.json` raw export from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- New run metadata/status/control: `measurement/m002.json` through `measurement/m005.json`.
- Local outputs from this review: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- The first run failed only at plotting because matplotlib selected an unavailable Tk backend; patched the script to use `Agg` and reran successfully.
- Extracted combined and per-average `ExperimentDataEachAvg` for 8 averages, 2 readouts, 41 tau points.
- Confirmed from the embedded `ramsey.xml` and `full_experiment=0` that readout1 is the pre-Ramsey mS=0 reference and readout2 is the post-Ramsey Ramsey signal.
- Computed raw signal, signal/reference ratio, linear reference-line normalization, per-average FFTs, scan-order first/last-quarter drift checks, and least-squares sinusoid amplitudes at:
  - programmed carrier: 1.000 MHz
  - expected 13C sidebands from the prior model: 0.615423 MHz and 1.384577 MHz
  - prior scout component: 0.884 MHz
- Tried an orientation-only damped-cosine fit after the signal checks.

## Quantitative checks

- Run completed normally with final counts reported as 44.184 kcps; no stop was requested.
- Scan: tau = 0 to 8 us, step = 0.2 us, 41 points, 8 x 50000 repetitions. The sampled DFT bin spacing from the 41-point grid is 121.95 kHz; the nominal 8 us span corresponds to about 125 kHz.
- Combined readouts:
  - reference mean: 49.313 kcps
  - signal mean: 44.580 kcps
  - signal min/max: 39.308/47.029 kcps
  - raw signal peak-to-peak: 7.721 kcps, but much of this comes from tau = 0 and low-frequency/scattered structure rather than a stable 1 MHz fringe.
  - signal/reference ratio peak-to-peak: 0.1696 overall; 0.1061 if tau = 0 is excluded.
- Combined FFT of the raw signal has its largest non-DC windowed component at 1.2195 MHz with amplitude 0.797 kcps, not at the programmed 1.000 MHz bin.
- Least-squares raw-signal amplitudes versus residual RMS:
  - 1.000 MHz: amp 0.301 kcps, residual RMS 1.304 kcps, amp/RMS 0.23.
  - 0.615423 MHz: amp 0.553 kcps, residual RMS 1.262 kcps, amp/RMS 0.44.
  - 1.384577 MHz: amp 0.265 kcps, residual RMS 1.308 kcps, amp/RMS 0.20.
  - 0.884 MHz: amp 0.279 kcps, residual RMS 1.306 kcps, amp/RMS 0.21.
- Ratio/reference-line-normalized target amplitudes are similarly weak: target amp/RMS values are about 0.21 to 0.40, not claim-grade.
- Per-average strongest FFT frequencies are inconsistent: 0.122, 0.488, 0.488, 0.244, 1.707, 0.244, 1.220, and 0.366 MHz. The 1 MHz component is not consistently dominant.
- Per-average mean signal varies strongly across averages, from 36.203 to 50.272 kcps; the mean signal/reference ratio is more stable but still spans about 0.891 to 0.926.
- Scan-order first/last-quarter signal changes are below a 15% hard-drift threshold in all averages; the largest was +11.5% in average 5. This is provenance/drift caution, not a hard invalidation.
- The orientation-only damped-cosine fit is not physically reliable: it pushes T2star to the lower bound of 0.2 us and has amplitude uncertainty comparable to amplitude. Do not use it as a T2star estimate.

## Plausible interpretation

- The new det=1.0 MHz Ramsey follow-up is analyzable but still non-claim-grade.
- It does not show a coherent Ramsey carrier following the programmed 1.0 MHz detuning.
- It also does not support the expected 13C sidebands near 0.615/1.385 MHz.
- The prior scout's weak ~0.884 MHz component is not reproduced as a coherent fixed feature here.
- The low tau=0 point, slow/scattered structure, inter-average brightness changes, and inconsistent per-average spectra make a simple T2star/13C interpretation unsafe.
- Prior pODMR context still supports r03 as the aligned candidate; this Ramsey result mainly says the current Ramsey evidence is insufficient, not that r03 is invalid.

## Claims not yet supported

- No supported numeric T2star value from this run.
- No supported nearby 13C conclusion from this run.
- No supported claim that the Ramsey carrier is at 1.0 MHz.
- No supported claim that the previous ~0.884 MHz scout feature is physical.
- No supported interpretation of the orientation-only damped-cosine fit parameters.

## Recommended next action

Do not blindly repeat the same long 8 us Ramsey. First run a short calibration/control path on r03: re-check tracking/counts and the fine weak-pi pODMR center near 3.8759 GHz, then only if that remains valid run a compact Ramsey carrier-visibility diagnostic before attempting another 13C/T2star claim scan. If a compact carrier check also fails, treat r03 Ramsey/T2star/13C as unsupported with the current route and choose between an alternate Ramsey/phase-cycling route or closing/moving the branch.
