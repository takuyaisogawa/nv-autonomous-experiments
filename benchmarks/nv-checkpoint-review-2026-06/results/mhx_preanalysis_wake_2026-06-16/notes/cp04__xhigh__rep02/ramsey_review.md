# Ramsey Review: r03 det-shift short-tau run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison/model context from local evidence only: `evidence/e008.json` prior det=1.0 MHz short-tau terminal review, `evidence/e019.json` det-shift model plan, plus `evidence/e007.json` / `evidence/e009.py` as the local drift/analysis pattern reference.
- Generated local artifacts: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, `ramsey_detshift_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified `ExperimentDataEachAvg` axis contract by averaging `[scan, avg, readout, point]` back to `ExperimentData`.
- Treated readout1 as reference and readout2 as Ramsey signal, consistent with the provided project context for `ramsey.xml full_experiment=0`.
- Computed scan-order-aware common-mode drift scores using `Scan.ScanOrderEachAvg` snake ordering; no averages exceeded the 15% drift threshold.
- Computed raw signal/reference summaries, per-point SEM across 12 stored averages, detrended FFT, linear-baseline least-squares sinusoid screens from 0.25 to 2.5 MHz, target amplitudes, per-average frequency screens, and a descriptive damped-sinusoid grid fit.
- Checked the generated plot file is nonblank by image statistics.

## Key quantitative checks

- Run completed cleanly: `nv23_ramsey_20260514_015423_auto_ramsey`, 12 averages x 90000 reps, 41 tau points from 0.048 to 1.968 us, `det=1.5 MHz`, final counts `44.796 kcps`, no stop request, no monitor error.
- Sampling: tau step `48 ns`, span `1.92 us`, FFT bin spacing `0.508 MHz`, Nyquist `10.42 MHz`.
- Noise scale: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`.
- Prior det=1.0 MHz short-tau top component was `1.192 MHz`. In this det=1.5 MHz run, all-tau ratio LS top is `1.623 MHz` with ratio amplitude `0.02547` and raw-signal amplitude `1.252 kcps`.
- Target amplitudes:
  - programmed carrier `1.500 MHz`: ratio amplitude `0.02399`, raw `1.128 kcps`;
  - predicted det-tracking carrier `1.692 MHz`: ratio amplitude `0.02505`, raw `1.225 kcps`;
  - previous fixed-control `1.192 MHz`: ratio amplitude `0.00511`, raw `0.474 kcps`.
- Early-time structure remains large: first 0.75 us peak-to-peak is `6.46 kcps` in signal and `0.134` in ratio.
- The result is tau-window sensitive: skipping tau <= 0.2 us moves the top ratio screen to about `0.746 MHz`, not to the programmed carrier or det-tracking carrier.
- Per-average top frequencies are inconsistent, spanning roughly `0.25..1.94 MHz`; only some averages favor the 1.5 to 1.7 MHz region.
- Descriptive damped-sinusoid grid fit prefers `0.678 MHz`, `T2* ~0.47 us` in ratio view and `0.818 MHz`, `T2* ~0.72 us` in raw signal view. These are empirical fit values only.

## Plausible interpretation

The det-shift run is valid terminal evidence and argues against simply promoting the previous `~1.192 MHz` feature as a fixed-frequency component: after changing `det` from 1.0 to 1.5 MHz, the all-tau LS maximum moved to `~1.623 MHz`, between the programmed `1.500 MHz` carrier and the predicted `1.692 MHz` det-tracking carrier, while the old `1.192 MHz` control is weak.

That said, this is not clean Ramsey carrier evidence. The LS maximum is broad on a short `1.92 us` window, FFT resolution is coarse enough that 1.5 and 1.692 MHz share the nearest FFT bin, early-tau structure dominates, skip-transient analysis changes the preferred frequency, and stored averages are not consistent. The safest interpretation is partial compatibility with a det-dependent Ramsey response plus substantial transient/artifact/baseline sensitivity, not a supported physical carrier model.

## Claims not yet supported

- No numeric T2star claim is supported from this run or the prior r03 Ramsey runs.
- No nearby 13C claim is supported; sideband targets do not form a consistent carrier +/- 13C pattern across raw signal, ratio, and fitted-reference views.
- A clean det-tracking Ramsey carrier is not established. The old fixed `1.192 MHz` feature is disfavored in this run, but the replacement feature is not robust enough to claim.
- The descriptive damped-sinusoid fit values are not physical T2star estimates.

## Recommended next action

Do not run another blind Ramsey repeat on r03 under these conditions. Write a branch synthesis across the r03 Ramsey datasets and choose one of two explicit paths: close the current Ramsey/T2star/13C branch as unsupported under this protocol, or switch to an alternate protocol/control measurement designed to separate short-tau pulse/scan artifacts from real NV coherence before attempting a T2star or 13C claim.
