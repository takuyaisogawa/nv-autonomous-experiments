# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, and relevant prior notes/evidence under `evidence/` and `md/`.
- New Ramsey raw export: `measurement/m001.json`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- New run metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.

## Calculations/scripts run

- Ran local Python analysis in `scratch_ramsey_analysis.py`.
- Parsed combined and per-average raw readouts from `ExperimentData` and `ExperimentDataEachAvg`.
- Used the sequence/readout model from project evidence: readout 1 is the reference and readout 2 is the Ramsey signal for `full_experiment=0`.
- Checked raw Ramsey signal, `signal/reference`, and signal normalized by a fitted reference trend.
- Checked scan-order/per-average drift using per-average reference/signal/ratio means and first-vs-last acquired point differences under snake order.
- Ran detrended FFT checks and exact-frequency least-squares sinusoid fits at:
  - expected carrier: `1.000 MHz`
  - expected 13C sidebands: `0.615423 MHz` and `1.384577 MHz`
  - prior scout component: `0.884 MHz`
- Tried exploratory damped-cosine fits only as a diagnostic, not as claim support.

Key quantitative results:

- Run completed without abort; final counts `44.184 kcps`; `8 x 50000` shots; `tau = 0..8 us`, 41 points; `dt = 0.2 us`; Nyquist `2.5 MHz`; FFT bin spacing `~121.95 kHz`.
- Combined reference mean `49.31 kcps`, Ramsey signal mean `44.58 kcps`, mean ratio `0.9042`.
- Per-average reference and signal means span about `30-32%`, but the per-average ratio mean spans only about `3.9%`, indicating substantial common-mode count changes that ratio normalization partly suppresses.
- Combined `signal/reference` exact-frequency least-squares amplitudes:
  - `0.615423 MHz`: amplitude `0.0111`, `~1.67 sigma`
  - `1.000 MHz`: amplitude `0.00916`, `~1.39 sigma`
  - `1.384577 MHz`: amplitude `0.00843`, `~1.28 sigma`
  - `0.884 MHz`: amplitude `0.00742`, `~1.10 sigma`
- The strongest ratio FFT bins are around `1.2195 MHz`, `0.4878 MHz`, `1.0976 MHz`, and `0.9756 MHz`; they are not a clean carrier/sideband pattern.
- Per-average phase consistency is weak: ratio phase-coherence `R` is about `0.65` at `1.0 MHz`, `0.43` at the low sideband, `0.61` at the high sideband, and `0.42` at `0.884 MHz`.
- Exploratory damped-cosine fit to the ratio gives poor support (`R2 ~ 0.14`, fitted frequency `~0.95 MHz`, fitted T2star `~3.0 us`). Raw-signal damped fits prefer very short `~0.2 us` decay and high frequency, consistent with overfitting early-point/readout structure rather than a reliable T2star.

## Plausible interpretation

- The measurement is valid/analyzable as a completed Ramsey acquisition, but it does not provide claim-grade evidence for a coherent Ramsey carrier at the programmed `1.0 MHz` detuning.
- The det-shift diagnostic argues against the prior `~0.884 MHz` scout component being a robust physical Ramsey feature: it is weak here and not dominant in the normalized exact-frequency check.
- There may be weak oscillatory structure in the data, but it is comparable to residual scatter and common-mode/readout variation, and it does not have strong per-average coherence.

## Claims not yet supported

- Do not claim a measured T2star from this run.
- Do not claim 13C coupling or resolved 13C sidebands from this run.
- Do not claim that the programmed Ramsey carrier was cleanly observed at `1.0 MHz`.
- Do not use the exploratory damped-cosine fit values as physical parameters.

## Recommended next action

Do not blindly repeat the same Ramsey. First diagnose why the Ramsey contrast/carrier is weak despite the accepted pODMR resonance and good final counts: run a short, high-SNR Ramsey/phase diagnostic on r03 with a simpler frequency target or phase setting, or re-check the Ramsey pulse calibration/readout contrast near `mw_freq = 3.8759 GHz`. If the immediate goal is a defensible project conclusion rather than more troubleshooting, record this as a second non-claim-grade Ramsey result: r03 remains the aligned NV candidate, but T2star and 13C remain unsupported.
