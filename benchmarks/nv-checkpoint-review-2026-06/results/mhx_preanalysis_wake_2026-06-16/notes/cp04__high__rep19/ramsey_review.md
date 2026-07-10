# Ramsey Review: r03 det-shift short-tau run

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus relevant local memory in `md/memory.md` and `md/knowledge.md`.
- New measurement:
  - `measurement/m001.json`: raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`: terminal result.
  - `measurement/m004.json` and `measurement/m005.json`: terminal status/control.
- Prior comparison:
  - `evidence/e006.json`: prior det=1.0 MHz short-tau raw export.
  - `evidence/e008.json` and `evidence/e019.json`: prior short-tau review and det-shift plan/model.
- Generated local audit artifacts:
  - `analyze_ramsey_detshift.py`
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_review.png`

## Calculations or scripts run

Ran:

```powershell
python analyze_ramsey_detshift.py
```

Main checks:

- Verified raw average axis contract: `ExperimentDataEachAvg` is `[scan, avg, readout, point]`; averaging over `avg` reproduces `ExperimentData`.
- Interpreted `full_experiment=0` Ramsey readouts as readout 1 reference and readout 2 Ramsey signal from the saved sequence text and project context.
- Recomputed the prior det=1.0 MHz short-tau frequency screen from `evidence/e006.json`; strongest ratio component is `1.192 MHz`, matching the prior review.
- For the new det=1.5 MHz run, ran linear-baseline least-squares sinusoid screens over `0.25..2.5 MHz` on raw signal, reference, point-wise ratio, and signal divided by a fitted reference line.
- Checked target amplitudes at old artifact-control `1.192 MHz`, programmed carrier `1.500 MHz`, predicted det-tracking carrier `1.692 MHz`, and 13C sideband targets near `1.115`, `1.885`, `1.307`, and `2.077 MHz`.
- Computed FFT-bin checks, per-average top-frequency screens, a local scan-order drift proxy using `ScanOrderEachAvg`, and descriptive damped-sinusoid grid fits.

Quantitative highlights:

- Run completed cleanly: status `completed`, final counts `44.796 kcps`, `stop_requested=false`, monitor error empty, safe shutdown true.
- Grid: `tau=0.048..1.968 us`, `41` points, step `48 ns`, `12 x 90000 = 1.08e6` shots per tau point.
- Local drift proxy flagged no averages.
- Median per-point uncertainty: signal SEM `0.711 kcps`, ratio SEM `0.0126`.
- New ratio screen top: `1.623 MHz`, ratio LS amplitude `0.02547`.
- New raw-signal screen top: `0.882 MHz`, raw LS amplitude `1.533 kcps`.
- Target amplitudes in the new run:
  - Old `1.192 MHz`: ratio `0.00511`, raw signal `0.474 kcps`.
  - Programmed `1.500 MHz`: ratio `0.02399`, raw signal `1.128 kcps`.
  - Predicted det-tracking `1.692 MHz`: ratio `0.02505`, raw signal `1.225 kcps`.
  - 13C sideband targets are smaller or inconsistent; largest checked sideband-like ratio amplitude is programmed high sideband `1.885 MHz` at `0.01732`.
- Per-average top ratio frequencies are scattered: `[1.938, 1.543, 0.870, 0.886, 1.751, 0.792, 0.897, 1.201, 0.799, 1.662, 0.250, 1.712] MHz`.

## Plausible interpretation

The det-shift run is informative but mixed. It argues against simply treating the prior `~1.192 MHz` feature as a fixed artifact, because the `1.192 MHz` ratio amplitude is strongly suppressed in the new det=1.5 MHz run and the ratio view now has its largest component near `1.62 MHz`, close to the predicted det-tracking `~1.692 MHz` carrier.

However, the raw signal view is not clean: its strongest component is near `0.882 MHz`, a frequency already seen as a non-claim-grade feature in earlier project history. The reference readout also has its own low-frequency structure near `0.924 MHz`, so the ratio-view peak may be shaped by readout/reference dynamics rather than a clean Ramsey carrier alone.

Best current interpretation: there may be a weak det-dependent Ramsey response around `1.5..1.7 MHz`, but it is entangled with baseline/readout transients and is not yet strong or consistent enough to support a numeric T2star or 13C assignment.

## Claims not yet supported

- A well-supported numeric T2star for r03 is still not established.
- A nearby 13C conclusion is not supported; sideband targets are not dominant or consistent across raw/readout-aware views.
- The `1.623..1.692 MHz` normalized feature should not yet be claimed as the physical Ramsey carrier.
- The descriptive damped-sinusoid fit should not be promoted to a physical T2star; the raw/readout-aware signal model is not clean enough.
- Another blind same-style Ramsey repeat is not justified by this evidence.

## Recommended next action

Do a short bridge-free branch synthesis across all r03 Ramsey datasets, then choose an alternate targeted path rather than another blind Ramsey repeat. The strongest practical next experiment would be a protocol/control that separates Ramsey phase accumulation from readout/reference transients, or an alternate T2 baseline route, before attempting any T2star or 13C claim. If no such targeted control is available, close the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey conditions while preserving the aligned-NV conclusion.
