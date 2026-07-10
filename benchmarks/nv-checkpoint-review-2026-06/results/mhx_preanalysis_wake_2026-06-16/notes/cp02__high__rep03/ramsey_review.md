# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus prior fine-pODMR/Ramsey notes in `evidence/e006.md` and `evidence/e013.md`.
- New Ramsey measurement: `measurement/m001.json` raw export from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- New job metadata/status: `measurement/m002.json` through `measurement/m005.json`.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `Scan.Variable_values`; actual run settings were `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, `dt = 0.2 us`, 41 points, 8 averages, 50000 repetitions, final counts `44.184 kcps`.
- Checked embedded `ramsey.xml` instructions: with `full_experiment=0`, channel 0 is the pre-Ramsey true ms=0 reference and channel 1 is the post-Ramsey signal. The default values printed in the embedded XML header are stale; `Variable_values` and job metadata carry the actual settings.
- Computed raw channel statistics, signal/reference ratio, signal/linear-reference normalization, Hann FFT, fixed-frequency least-squares amplitudes at `1.000 MHz`, `0.6155 MHz`, `1.3845 MHz`, and prior `0.884 MHz`, a free-frequency sinusoid grid, per-average frequency checks, and a descriptive damped-cosine fit.

## Plausible interpretation

- The run completed normally and returned analyzable Ramsey data on accepted r03.
- The normalized combined trace has visible structure: signal/reference mean `0.9042`, std `0.0294`, peak-to-peak `0.1696`.
- FFT of the combined ratio has strongest bins at `1.098 MHz` and `1.220 MHz`; the best free sinusoid grid is near `1.178 MHz` with amplitude `0.0225` and `R2 = 0.308`. Excluding the simple drift-flagged average 7 keeps the best free frequency near `1.183 MHz` with similar amplitude.
- Fixed-frequency support is weak at the planned diagnostic frequencies: least-squares on signal/reference gives `R2 = 0.053` at `1.000 MHz`, `0.074` at `0.6155 MHz`, `0.046` at `1.3845 MHz`, and `0.035` at the prior `0.884 MHz` component.
- Per-average behavior is not coherent enough for a claim: best single-frequency peaks scatter across averages (`0.2675`, `1.635`, `0.455`, `0.4225`, `1.1675`, `0.635`, `2.0`, `1.4175 MHz`). A simple common-mode check flags average 7 as outside +/-15% of median combined channel mean.
- A descriptive damped-cosine fit to the combined ratio finds `freq ~1.187 MHz`, `T2* ~2.27 us`, `R2 ~0.486`, but this is not claim-grade because the fitted carrier is not strongly tied to the programmed detuning or expected 13C sidebands and the averages disagree.

## Claims not yet supported

- No well-supported T2star value should be claimed from this run.
- No 13C conclusion should be claimed; the expected `det +/- f13C` sidebands near `0.615/1.385 MHz` are not coherently supported.
- The data do not support claiming that the Ramsey carrier cleanly follows the programmed `1.0 MHz` detuning.
- The prior `~0.884 MHz` scout feature is not reproduced as the dominant feature here, but this run alone does not identify whether either feature is physical, pulse/phase related, or noise/systematic.

## Recommended next action

Do not immediately repeat the same Ramsey. First run a targeted Ramsey phase/frequency diagnostic on r03: keep the same `mw_freq = 3.8759 GHz` and 8 us span if counts/tracking remain good, but use a deliberately different detuning or a short calibration pair that can distinguish programmed phase-ramp behavior from sequence/readout/systematic structure. Treat a T2star fit as valid only after the carrier frequency is reproducible across averages and moves consistently with the programmed detuning.
