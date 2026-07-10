# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, and `context.json` for project objective, prior decisions, and expected checks.
- `measurement/m002.json` for the executed Ramsey contract: accepted r03, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, 41 points, 8 averages x 50000 repetitions.
- `measurement/m003.json`, `measurement/m004.json`, and `measurement/m005.json` for terminal/run status: job completed, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`, final counts `44.184 kcps`, no abort, safe shutdown ok.
- `measurement/m001.json` for raw exported scan data. The embedded `ramsey.xml` sequence shows readout 0 is the 0-level reference and readout 1 is the Ramsey signal when `full_experiment = 0`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs created:
  - `ramsey_analysis_summary.json`
  - `ramsey_trace_summary.csv`
  - `ramsey_diagnostic.png`
  - `analysis_stdout.txt`
- Quantitative checks:
  - Confirmed scan grid: 41 tau points from `0` to `8 us`, `dt = 0.2 us`, Nyquist `2.5 MHz`, FFT bin spacing about `0.122 MHz`.
  - Combined raw means: reference `49.31 kcps`, Ramsey signal `44.58 kcps`.
  - Combined raw signal span `7.72 kcps`, signal standard deviation `1.34 kcps`; signal/reference ratio mean `0.904`, ratio span `0.170`.
  - Detrended-signal FFT strongest bins: `0.488 MHz` (largest), `1.220 MHz`, `0.122 MHz`, `1.098 MHz`, `0.610 MHz`, then weaker components including `0.854 MHz`.
  - Linear-baseline plus sinusoid fits at the planned diagnostic frequencies:
    - `0.615 MHz`: signal amplitude `0.477 kcps`, `R2 = 0.156`; ratio amplitude `0.0111`, `R2 = 0.074`.
    - `0.884 MHz`: signal amplitude `0.286 kcps`, `R2 = 0.117`; ratio amplitude `0.0074`, `R2 = 0.035`.
    - `1.000 MHz`: signal amplitude `0.277 kcps`, `R2 = 0.115`; ratio amplitude `0.0092`, `R2 = 0.053`.
    - `1.385 MHz`: signal amplitude `0.264 kcps`, `R2 = 0.113`; ratio amplitude `0.0084`, `R2 = 0.046`.
  - Per-average mean counts varied substantially in common mode: signal means ranged `36.20..50.27 kcps`, reference means `40.47..55.53 kcps`. A robust MAD threshold did not flag a single isolated outlier, but the average-to-average common-mode swing is large provenance against over-interpreting weak spectral features.

## Plausible interpretation

- The run completed successfully and produced analyzable Ramsey data on the accepted r03 branch.
- The det-shift diagnostic does not show a clean, dominant carrier at the programmed `1.0 MHz`. The strongest FFT component is near `0.488 MHz`; components near the expected low sideband bin (`0.610 MHz`) and near/carrier-adjacent bins (`1.098` and `1.220 MHz`) are present but not uniquely dominant.
- The prior scout's non-claim-grade `~0.884 MHz` component is not reproduced as a strong feature here; its nearest FFT bin at `0.854 MHz` is weaker, and the direct 0.884 MHz sinusoid fit is low-amplitude/low-`R2`.
- The expected 13C sideband positions near `0.615` and `1.385 MHz` are not supported as coherent sidebands by these checks. The low-sideband-adjacent FFT bin exists, but the targeted least-squares fit explains little variance and there is no matching high-sideband support.
- The data are consistent with weak Ramsey contrast mixed with drift/common-mode count variation and/or nonphysical spectral structure. A T2star fit should not be promoted from this trace because signal presence at a physically expected carrier/sideband pattern is not established.

## Claims not yet supported

- No well-supported T2star value.
- No well-supported nearby 13C coupling conclusion.
- No claim that the Ramsey oscillation follows the programmed `1.0 MHz` detuning.
- No claim that the `0.488 MHz`, `0.610 MHz`, `1.098 MHz`, or `1.220 MHz` FFT features are physical without repeatability or a cleaner detuning response.

## Recommended next action

Do not blindly repeat the same Ramsey. First run a control or recalibration step that can separate sequence/timing/artifact behavior from NV dephasing: verify the Ramsey phase-ramp behavior using a short, high-SNR detuning sweep on the same r03 branch, such as two or three Ramsey scans with identical tau grid/shot budget but different programmed detunings, and require the dominant spectral component to shift with det before fitting T2star or making any 13C claim. If bridge time is constrained, start with a brief pODMR/check of the resonance center and then a shorter Ramsey detuning diagnostic.
