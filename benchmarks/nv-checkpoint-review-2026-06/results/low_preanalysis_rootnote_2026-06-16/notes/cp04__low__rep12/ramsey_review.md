# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New Ramsey terminal data:
  - `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: control file.
- Generated local artifacts: `analyze_ramsey_review.py`, `ramsey_review_analysis.json`, `ramsey_review_plot.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey_review.py`.
- Verified `ExperimentDataEachAvg` axis contract by averaging stored averages and comparing to `ExperimentData`; max absolute mismatch was `1.4e-14 kcps`.
- Confirmed run settings from local files: det-shift Ramsey on accepted r03, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 0.048..1.968 us`, 41 points, `12 x 90000` repetitions, final counts `44.796 kcps`.
- Computed raw readout, signal/reference ratio, linear-reference-normalized ratio, per-point SEM, least-squares sinusoid screens, and target-frequency amplitudes.
- Decision-frequency checks:
  - Programmed carrier `1.500 MHz`: ratio LS amplitude `0.0261`, raw-signal amplitude `1.13 kcps`, signal-fit `R2 = 0.345`.
  - Det-tracking prediction from prior `~1.192 MHz` feature, `1.692 MHz`: ratio LS amplitude `0.0272`, raw-signal amplitude `1.22 kcps`, signal-fit `R2 = 0.427`.
  - 13C sideband targets `1.307 MHz` and `2.076 MHz`: ratio amplitudes `0.0103` and `0.0067`, raw-signal amplitudes `0.266 kcps` and `0.251 kcps`.
  - Prior fixed-feature control `1.192 MHz`: ratio amplitude `0.0056`, raw-signal amplitude `0.474 kcps`.
- Noise/provenance checks: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`; simple mean-brightness drift span across averages `13.5%`. The full frequency screen is dominated by a slow/edge component at the lower scan bound (`0.2 MHz`), and the restricted/skip-transient screens still favor low-frequency residual structure near `0.5 MHz`.

## Plausible interpretation

- The run completed safely and is analyzable.
- Compared with the previous det=1.0 MHz short-tau run, the prior `~1.192 MHz` component does not remain strong at `1.192 MHz` in this det=1.5 MHz dataset.
- There is a weak component near the programmed/det-tracking region: `1.692 MHz` is slightly stronger than `1.500 MHz` in this simple LS screen, and both are above the median raw-signal SEM at about `1.0..1.2 kcps`.
- This is suggestive that some Ramsey-frequency content may move with det, but it is not clean claim-grade evidence because the trace remains dominated by slow baseline/transient structure and the target amplitudes are small compared with the full raw/ratio range.

## Claims that are not yet supported

- Do not claim a numeric T2star from this run. The carrier/decay shape is not clean enough to promote a damped-sinusoid fit.
- Do not claim nearby 13C coupling. The expected sideband targets are weak and below/near noise-scale in raw signal.
- Do not claim that `1.692 MHz` is a confirmed physical Ramsey carrier. It is a plausible weak det-tracking feature, not a decisive result.
- Do not claim that the low-frequency screen peak is physical; it is more consistent with baseline/transient contamination unless independently reproduced under a targeted protocol.

## Recommended next action

Stop blind Ramsey repeats on this branch. The next useful action is a protocol-change decision: either run a non-blind phase/control Ramsey diagnostic designed to suppress/remove the early-time baseline transient and directly test det-tracking carrier phase, or switch to an alternate T2*/coupling protocol such as Hahn/CPMG-style baseline before closing the r03 Ramsey/13C branch as unsupported under current Ramsey conditions.
