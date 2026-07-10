# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- New completed Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status/control snapshot, `measurement/m005.json`.
- Prior Ramsey context: `evidence/e008.json` terminal det=1.0 MHz short-tau review and `evidence/e005.md` 10-average autosave note.
- Created local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_det1p5_review.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Validated raw array contract: `ExperimentDataEachAvg` shape `(1, 12, 2, 41)` and per-average mean reproduces combined `ExperimentData` with max absolute difference `1.4e-14`.
- Confirmed acquisition settings: `tau = 0.048..1.968 us`, step `0.048 us`, 41 points, `12 x 90000 = 1.08e6` shots per tau point, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`.
- Computed raw reference/signal and signal/reference traces, per-point SEM, FFT bin spacing, LS sinusoid screens after linear baseline removal, target-frequency amplitudes, per-average frequency screens, and simple snake-order drift checks.
- Key noise/scale checks: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`; signal linear-residual peak-to-peak `6.29 kcps`; ratio linear-residual peak-to-peak `0.133`.
- Target LS checks:
  - Programmed `1.5 MHz` carrier: ratio amplitude `0.0240`, raw-signal amplitude `1.13 kcps`, ratio R2 improvement `0.359`.
  - Prior fixed-artifact control `1.192 MHz`: ratio amplitude `0.0051`, raw-signal amplitude `0.474 kcps`, ratio R2 improvement `0.0167`.
  - Det-tracking prior-component target `1.692 MHz`: ratio amplitude `0.0250`, raw-signal amplitude `1.22 kcps`, ratio R2 improvement `0.411`.
  - Programmed 13C sidebands `1.115/1.885 MHz`: ratio amplitudes `0.0108/0.0173`.
  - Det-tracking 13C sidebands `1.307/2.077 MHz`: ratio amplitudes `0.0095/0.0061`.
- Exploratory band screens disagree by view/preprocessing:
  - All-tau ratio screen peaks near `1.623 MHz`.
  - All-tau raw-signal and signal-over-refline screens peak near `0.882 MHz`.
  - Skipping `tau <= 0.2 us`, ratio screen peaks near `0.746 MHz`; raw-signal/refline screens peak near `0.805-0.806 MHz`.
  - Ratio FFT largest bins are `0.508`, `1.524`, and `2.033 MHz`; bin spacing is `0.508 MHz`, so FFT localization is coarse.
  - Per-average top frequencies are spread across `0.79..1.94 MHz`; they do not form one clean carrier/sideband pattern.
- Drift sanity checks: scan order is `snake`; within-average acquired-order end-to-end slopes have median absolute size `2.16 kcps` and max `3.29 kcps`; forward-vs-reverse average RMS delta is `1.10 kcps` with mean delta `0.175 kcps`. This is run-quality provenance, not by itself a hard anomaly.

## Plausible interpretation

- The det=1.5 MHz run is terminal, analyzable, and has structured short-tau contrast above point noise.
- The old `~1.19 MHz` feature is not preserved as a strong fixed-frequency component in this new run, so the fixed-artifact hypothesis is weakened.
- The result is still not a clean det-tracking Ramsey carrier: the ratio view prefers about `1.62 MHz`, the raw-signal/refline views prefer about `0.88 MHz` or `0.81 MHz` after skipping early points, and individual averages are inconsistent.
- The det-tracking target near `1.692 MHz` has nontrivial LS amplitude, but it is not uniquely dominant or robust across views. Treat it as suggestive diagnostic context, not a physical frequency claim.
- The 13C sideband targets are weak and not dominant. This measurement does not support a nearby 13C conclusion.

## Claims not yet supported

- No supported numerical `T2*` value for r03 from this Ramsey series.
- No supported nearby `13C` coupling or sideband assignment.
- No supported claim that `1.623`, `1.692`, `0.882`, or `0.805 MHz` is the physical Ramsey carrier.
- No supported claim that the r03 Ramsey problem is solved by simply changing detuning or accumulating another identical Ramsey repeat.

## Recommended next action

Stop blind Ramsey repeats on r03 under this protocol. Do a bridge-free synthesis of all four r03 Ramsey datasets and decide between:

1. a supported negative/unsupported conclusion for r03 Ramsey/T2*/13C under current conditions, or
2. one deliberately different protocol that tests a specific failure mode, preferably a Hahn-echo/CPMG-style baseline or another non-Ramsey control, rather than another short-tau Ramsey repeat.

If the project still needs a definitive T2-family number, the next experimental action should be an alternate protocol with an explicit success criterion, not another det-shift Ramsey.
