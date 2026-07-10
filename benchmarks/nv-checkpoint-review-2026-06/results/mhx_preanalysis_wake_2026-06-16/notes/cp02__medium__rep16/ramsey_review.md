# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`.
- Measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job contract, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Planning/model context: `evidence/e007.json` for the expected detuned Ramsey carrier and 13C sideband frequencies.
- New run: `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`, `tau = 0..8 us`, 41 points, 0.2 us step, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, 8 averages x 50000 repetitions, final count text `44.184 kcps`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_review_plot.png`
  - `ramsey_analysis_stdout.json`
- Checks performed:
  - Parsed raw readouts and per-average readouts from `measurement/m001.json`; data are saved in tau order with snake scan mode.
  - Reviewed raw signal, raw reference, point-wise `signal/reference`, and `signal/reference-line` views.
  - Detrended each trace with a linear baseline and computed Hann-window FFT peaks.
  - Least-squares sinusoid screens were run at:
    - expected low 13C sideband: `0.615423 MHz`
    - prior scout component: `0.884 MHz`
    - programmed carrier: `1.000 MHz`
    - expected high 13C sideband: `1.384577 MHz`
  - Per-average count-level and target-amplitude consistency checks were run for the raw signal.

## Quantitative findings

- Raw signal mean/std: `44.580/1.338 kcps`; raw reference mean/std: `49.313/0.869 kcps`.
- Raw signal FFT strongest bins after detrending:
  - `1.219512 MHz`, `0.797 kcps`
  - `1.097561 MHz`, `0.764 kcps`
  - `0.487805 MHz`, `0.640 kcps`
  - `0.609756 MHz`, `0.398 kcps`
- Targeted raw-signal sinusoid amplitudes are weak relative to residuals:
  - `0.615423 MHz`: `0.475 kcps`, amp/RMS `0.37`
  - `0.884 MHz`: `0.286 kcps`, amp/RMS `0.22`
  - `1.000 MHz`: `0.277 kcps`, amp/RMS `0.21`
  - `1.384577 MHz`: `0.263 kcps`, amp/RMS `0.20`
- Normalized views do not rescue the carrier:
  - Point-wise ratio at `1.000 MHz`: amplitude `0.00916`, amp/RMS `0.31`.
  - Signal/reference-line at `1.000 MHz`: amplitude `0.00564`, amp/RMS `0.21`.
- Per-average common-mode drift is substantial:
  - Reference average means drift from median by up to `18.1%`.
  - Signal average means drift from median by up to `18.8%`.
  - Signal and reference move together, so this is mainly common-mode acquisition/count-level provenance, but it is large enough to make weak spectral features suspect.
- The raw signal has lower late-time detrended RMS than early-time RMS (`late/early = 0.42`), but the carrier itself is not well established and the spectrum is not clean enough to use this as a T2star fit.

## Plausible interpretation

- The measurement is complete and analyzable, with no terminal bridge failure and final counts well above the minimum count gate.
- The det-shift diagnostic does not support a clean Ramsey carrier at the programmed `1.0 MHz`. The combined raw signal's strongest exploratory peaks sit near `1.10-1.22 MHz`, while the direct `1.0 MHz` least-squares amplitude is small compared with residual structure.
- The previous scout's `~0.884 MHz` component is not reinforced here; its combined raw-signal amplitude is also weak.
- There is an exploratory feature near the low 13C sideband bin (`~0.610 MHz` FFT bin, target `0.615 MHz`), but its targeted amplitude is weak and sits in a drift/noise-contaminated spectrum. This is not enough for a 13C claim.
- The large per-average common-mode changes suggest that this run is dominated by count-level/background drift plus weak oscillatory structure rather than a clean, phase-stable Ramsey fringe.

## Claims that are not yet supported

- No well-supported T2star value is supported by this run.
- No well-supported 13C coupling/sideband conclusion is supported by this run.
- Do not claim that the detuned Ramsey carrier was observed at `1.0 MHz`.
- Do not claim that the `~0.884 MHz` component from the first scout is physical.
- Do not infer a physical 13C sideband from the `~0.610 MHz` exploratory FFT bin without a cleaner repeat or another sequence that separates it from drift/background structure.

## Recommended next action

Do not immediately repeat the same long Ramsey. First run a short bridge-free planning/review step to decide between:

1. A targeted Ramsey repeat with stronger drift control and phase/reference checks, likely fewer tau points or shorter per-average windows while preserving even averages.
2. A direct control Ramsey at a different programmed detuning chosen to test whether any peak tracks detuning.
3. A recovery/calibration step before more Ramsey, if recent count-level drift or tracking/background evidence remains poor.

The next bridge-touching experiment should be designed only after explicitly modeling the expected fringe amplitude versus the observed `~1.26 kcps` detrended raw residual scale and the observed `~18-19%` per-average count-level drift.
