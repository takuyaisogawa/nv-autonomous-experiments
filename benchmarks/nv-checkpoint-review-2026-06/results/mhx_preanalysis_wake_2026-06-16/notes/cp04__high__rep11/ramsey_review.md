# Ramsey Review: det=1.5 MHz Short-Tau Shift Check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`.
- New terminal Ramsey data: `measurement/m001.json` raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- New job metadata/status/control: `measurement/m002.json` through `measurement/m005.json`.
- Prior comparison context: `project/state.md`, `evidence/e008.json`, `evidence/e021.json`; prior short-tau det=1.0 MHz run had top empirical ratio component near `1.192 MHz`.
- Local outputs from this review: `analyze_ramsey.py`, `ramsey_analysis_results.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw-export axis contract: `ExperimentDataEachAvg` shape `(1, 12, 2, 41)` reconstructs `ExperimentData` to numerical precision; readout 1 treated as reference and readout 2 as Ramsey signal.
- Confirmed scan/job basics: completed run, final counts `44.796 kcps`, `tau = 0.048..1.968 us` in 41 points, `12 x 90000 = 1.08e6` shots per tau, snake scan order, no lightweight common-mode drift flags.
- Computed raw signal and signal/reference summaries, per-point SEM, linear-residual peak-to-peak, FFT bins, least-squares sinusoid screens against a linear baseline, per-average frequency screens, and descriptive damped-sinusoid grid fits.
- Frequency-resolution context: FFT bin spacing `0.508 MHz`, nominal `1/span = 0.521 MHz`, Nyquist `10.42 MHz`; LS frequency peaks inside this short window should not be over-read as high-precision centers.

## Plausible interpretation

- The prior fixed-component control at `1.192 MHz` is weak in this det=1.5 MHz run: ratio LS amplitude `0.0051`, R2 improvement `0.017`.
- The combined all-tau ratio LS screen now peaks near `1.623 MHz` with ratio amplitude `0.0255`, raw-signal amplitude `1.25 kcps`, and R2 improvement `0.430`.
- Target checks are qualitatively compatible with det tracking but not cleanly discriminating: programmed `1.5 MHz` gives ratio amplitude `0.0240`; predicted carrier if the prior `1.192 MHz` feature tracks det gives `1.692 MHz` and ratio amplitude `0.0250`. Both are about `2x` the median ratio SEM (`0.0126`) and use the same nearest FFT bin (`1.524 MHz`).
- The observed top shift from prior `1.192 MHz` to `1.623 MHz` is `+0.431 MHz`, reasonably near the intended `+0.5 MHz` det change given the short time window, and argues against simply promoting a fixed `1.19 MHz` artifact.
- However, the signal is still transient/fragile: skipping `tau <= 0.2 us` moves the top ratio screen to about `0.746 MHz`, and per-average top frequencies are inconsistent. The descriptive damped fits prefer unrelated short-lived components (`0.678 MHz`, `T2* ~0.47 us` in ratio; `0.818 MHz`, `T2* ~0.72 us` in raw signal), so they are diagnostics only.

## Claims not yet supported

- No supported numeric T2star claim from this Ramsey branch.
- No supported nearby `13C` claim. Det=1.5 MHz expected sidebands at `1.115 MHz` and `1.885 MHz` have ratio amplitudes `0.0108` and `0.0173`, weaker than the carrier-region components and not consistently selected.
- No supported sub-grid or sub-resolution Ramsey carrier frequency claim; `1.623 MHz` is an empirical LS-screen maximum, not a calibrated carrier estimate.
- No supported conclusion that the line shape is a clean single damped Ramsey oscillation; early-time transient behavior remains a plausible contributor.

## Recommended next action

Stop blind Ramsey repeats on r03. Do a bridge-free synthesis of all r03 Ramsey data and either close the r03 Ramsey/T2star/13C branch as unsupported under current conditions or switch to an alternate protocol/diagnostic that directly addresses the early-time transient and carrier ambiguity before claiming T2star or `13C`.
