# Ramsey review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, and `md/knowledge.md`.
- New terminal Ramsey data: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Prior comparison/model context: `evidence/e008.json` for the terminal det=1.0 MHz short-tau review, `evidence/e019.json` for the det-shift hypothesis/target frequencies, and `evidence/e009.py` for prior local review conventions.
- Generated local artifacts: `ramsey_detshift_analysis.py`, `ramsey_detshift_analysis.json`, and `ramsey_detshift_diagnostics.png`.

## Calculations or scripts run

- Ran `python ramsey_detshift_analysis.py`.
- The script verified the raw-export axis contract by averaging `ExperimentDataEachAvg[:, readout, point]` back to `ExperimentData`.
- It treated readout 1 as reference and readout 2 as Ramsey signal, following the inspected project convention for `ramsey.xml` with `full_experiment=0`.
- It computed scan-order-aware drift scores from `Scan.ScanOrderEachAvg`, raw signal/reference/ratio statistics, per-point SEM over 12 stored averages, least-squares sinusoid screens, detrended FFT amplitudes, per-average frequency screens, and descriptive damped-sinusoid grid fits.
- The diagnostic PNG was written and programmatically checked as a nonempty 1600 x 2080 PNG.

## Quantitative checks

- Run status: `nv23_ramsey_20260514_015423_auto_ramsey` completed, `12 x 90000` repetitions, final count `44.796 kcps`, safe shutdown true, no stop request, and no monitor error.
- Scan grid: `tau = 0.048..1.968 us`, 41 points, 48 ns step, FFT bin spacing about `0.508 MHz`, nominal `1/span` resolution about `0.521 MHz`, Nyquist about `10.42 MHz`.
- Drift: no flagged averages; maximum scan-order drift score was `0.0397`, below the local `0.15` flag threshold.
- Noise/transient: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`. The first `0.75 us` still has a large transient: signal peak-to-peak `6.46 kcps`, ratio peak-to-peak `0.134`.
- Prior det=1.0 top control: the old `1.192 MHz` component is strongly reduced in this det=1.5 run: ratio LS amplitude `0.00511` and raw-signal amplitude `0.474 kcps`, versus prior `0.0363` and `1.684 kcps`.
- Det-shift targets:
  - programmed `1.500 MHz`: ratio amplitude `0.02399`, raw-signal amplitude `1.128 kcps`;
  - predicted tracking carrier `1.692 MHz`: ratio amplitude `0.02505`, raw-signal amplitude `1.225 kcps`;
  - combined ratio-screen top `1.623 MHz`: ratio amplitude `0.02547`, raw-signal amplitude `1.252 kcps`;
  - raw-signal and fitted-reference-line views instead peak near `0.882 MHz`, with raw-signal amplitude `1.533 kcps`.
- 13C sideband checks are not dominant. Programmed sidebands at `1.115/1.885 MHz` have ratio amplitudes `0.0108/0.0173`; predicted tracking sidebands at `1.307/2.077 MHz` have ratio amplitudes `0.00953/0.00614`.
- Descriptive damped fits are not claim-grade: ratio view prefers about `0.678 MHz`, `T2star = 0.469 us`; raw-signal view prefers about `0.818 MHz`, `T2star = 0.717 us`. These fits follow the early transient rather than a supported Ramsey carrier/sideband model.

## Plausible interpretation

- The new run is terminal, analyzable, and has no hard drift or execution anomaly.
- The det shift argues against simply promoting the previous `1.192 MHz` component as a fixed, repeatable physical feature, because that component is not retained as the dominant feature.
- The result still does not cleanly support a det-following Ramsey carrier. The ratio view has a broad strongest component near `1.62 MHz`, close to but not uniquely proving the `1.692 MHz` tracking expectation within the short time window. The raw-signal and fitted-reference-line views remain dominated by a lower-frequency/early-transient feature near `0.88 MHz`.
- The most plausible project-level reading is that `auto__ramsey` on r03 is still dominated by transient/baseline/readout/protocol effects under these conditions. The aligned-NV finding remains supported by prior pODMR, but the Ramsey branch remains non-claim-grade.

## Claims not yet supported

- A numeric physical `T2star` for r03.
- A nearby `13C` conclusion or resolved sideband structure.
- Assignment of the `1.623/1.692 MHz` ratio component as a real Ramsey carrier.
- Assignment of the `0.882 MHz` raw-signal component as physical rather than transient/protocol structure.
- A claim that the r03 NV lacks nearby 13C in general; only the present Ramsey evidence is unsupported.

## Recommended next action

Do not run another blind `auto__ramsey` repeat on this branch. Synthesize or close the r03 `auto__ramsey` Ramsey/T2star/13C evidence as non-claim-grade under current conditions. If the project continues on r03, switch to a deliberately different and validated path: first inspect/control the Ramsey phase/readout behavior, then use an alternate T2star/13C protocol or control measurement rather than accumulating another same-style Ramsey scan.
