# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json` for project state and analysis expectations.
- `evidence/e011.json`, `evidence/e012.json`, and `evidence/e013.md` for the immediate fine-pODMR/second-Ramsey setup context.
- `measurement/m001.json` for the raw savedexperiment export from `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json` through `measurement/m005.json` for the job contract, terminal bridge result, final status, and control record.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` after setting Matplotlib to the noninteractive `Agg` backend. The first plotting attempt failed because the local Tk install was incomplete; the numerical analysis was rerun successfully after the backend fix.
- Parsed the Ramsey export as 41 tau points from `0` to `8 us` with `0.2 us` spacing, `8` stored averages, `50000` repetitions per average, two readouts, snake scan order, and terminal final counts `44.184 kcps`.
- Treated readout 1 as reference-like and readout 2 as signal-like, while checking raw signal and `signal/reference` rather than relying on normalization alone.
- Computed raw signal contrast, point-wise ratio, detrended/windowed FFT, least-squares sinusoid amplitudes at the planned frequencies, per-average FFT maxima, odd/even average differences, and a descriptive damped-cosine fit only after checking the raw/FFT shape.

Key numerical checks:

- Combined raw signal mean `44.58`, reference mean `49.31`; raw signal peak-to-peak `7.72`, about `17.3%` of the signal mean.
- Combined `signal/reference` peak-to-peak `0.170`.
- Strongest combined ratio FFT bins were near `1.098 MHz` and `1.220 MHz`; the planned `1.000 MHz` carrier bin near `0.976 MHz` was present but not dominant.
- Least-squares amplitudes in `signal/reference`: prior `0.884 MHz` component `0.0074`, low sideband `0.615 MHz` `0.0111`, carrier `1.000 MHz` `0.0092`, high sideband `1.385 MHz` `0.0084`; all are small compared with residual RMS near `0.028`.
- Per-average spectra were inconsistent: strongest bins included `2.317`, `1.098`, `0.488`, `1.220`, `0.610`, and `1.463 MHz`; the 1 MHz least-squares amplitude-over-residual-RMS ranged only `0.053..0.414`.
- Average-to-average common-mode levels varied substantially: reference mean range fraction about `30.5%`, signal mean range fraction about `31.6%`. Odd/even average ratio RMS was `0.041`, comparable to the median point-wise across-average ratio standard deviation `0.053`.
- A descriptive damped-cosine fit to the combined ratio returned frequency `1.187 MHz`, `T2star = 2.27 us`, and `R2 = 0.49`; this is not claim-grade because the fit frequency is between FFT bins, average-to-average agreement is weak, and the residual structure remains large.

## Plausible interpretation

- The run completed safely and produced analyzable Ramsey-shaped data with visible combined contrast.
- The det-shift diagnostic does not cleanly validate the expected programmed `1.0 MHz` carrier. The combined spectrum moved away from the prior scout's `~0.884 MHz` feature, but it peaks around `1.1..1.2 MHz` and the per-average spectra do not agree.
- The data are compatible with a weak Ramsey oscillation plus drift/common-mode variation, but not with a robust, reproducible carrier assignment.
- The low-sideband region near `0.615 MHz` appears as a small FFT/least-squares feature, but it is not separable from residual scatter and per-average instability.

## Claims that are not yet supported

- Do not claim a measured `T2star`; the `2.27 us` damped-cosine result is descriptive only.
- Do not claim 13C coupling or sidebands from this dataset.
- Do not claim that the Ramsey carrier is confirmed at the programmed `1.0 MHz`.
- Do not claim the earlier `~0.884 MHz` scout feature was physical; this det-shift run weakens that interpretation but does not identify a clean replacement.

## Recommended next action

Do not blindly repeat the same Ramsey. First perform a short bridge-free synthesis/design step: compare this det-shift result with the first Ramsey scout and fine pODMR, then choose a diagnostic that separates sequence/readout/phase-ramp artifacts from true dephasing. A practical next experiment would be a shorter, higher-cadence Ramsey diagnostic with reduced repetitions per average to keep the tracking window comfortably below the cap, or a calibration/control Ramsey at a deliberately different `det` if the goal is specifically to verify phase-ramp fidelity before spending more shots on T2star/13C.
