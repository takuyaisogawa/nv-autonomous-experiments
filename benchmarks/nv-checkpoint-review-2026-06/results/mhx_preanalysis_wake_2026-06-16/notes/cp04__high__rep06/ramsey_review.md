# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey run:
  - Raw export: `measurement/m001.json`.
  - Job spec/result/status/control: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Comparison Ramsey run from project evidence:
  - Prior terminal short-tau det=1.0 MHz raw export: `evidence/e006.json`.
  - Prior scan-order drift review: `evidence/e007.json`.
  - Det-shift model/start context: `evidence/e019.json`, `evidence/e023.json`, `evidence/e024.json`, `evidence/e028.json`, `evidence/e029.json`.
- Created local scratch outputs: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, `ramsey_detshift_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified `ExperimentDataEachAvg` axis order as `[slice, average, readout, tau]`: averaging over the 12-average axis reproduces combined `ExperimentData` with max absolute mismatch `1.42e-14`.
- Used readout 1 as reference and readout 2 as Ramsey signal, consistent with the project protocol note for `auto__ramsey` / `full_experiment=0`.
- Computed raw signal, signal/reference ratio, and signal over a linear fitted reference line.
- Computed per-point SEM from 12 stored averages, scan-order-aware common-mode drift scores using snake acquisition order, least-squares sinusoid screens, and detrended Hann-window FFT screens.
- Least-squares model was `y = c0 + c1*tau + A*cos(2*pi*f*tau) + B*sin(2*pi*f*tau)`; reported amplitude is `sqrt(A^2+B^2)` and improvement is relative to a linear baseline.

## Key quantitative checks

- New det=1.5 MHz run completed cleanly: `12 x 90000`, tau `0.048..1.968 us` in 41 points, final counts `44.796 kcps`, no stop request, no bridge error.
- New run local drift check: no flagged averages; max common-mode drift score `0.0397`, below the `0.15` flag threshold.
- New run noise/variation:
  - Median signal SEM `0.711 kcps`; median ratio SEM `0.0126`.
  - Signal residual peak-to-peak after linear baseline `6.29 kcps`; ratio residual peak-to-peak `0.133`.
- Prior det=1.0 MHz terminal comparison:
  - Ratio LS top component near `1.192 MHz`, amplitude `0.0363`, R2 improvement `0.656`.
  - Raw-signal LS top near `1.187 MHz`, amplitude `1.682 kcps`, R2 improvement `0.681`.
- New det=1.5 MHz run:
  - Ratio LS top is broad near `1.623 MHz`, amplitude `0.0255`, R2 improvement `0.430`.
  - Raw-signal LS top is near `0.882 MHz`, amplitude `1.533 kcps`, R2 improvement `0.577`.
  - Reference channel has structured variation, top near `0.924 MHz`, amplitude `0.405 kcps`, R2 improvement `0.292`.
  - At the planned det-tracking frequency `1.692 MHz`, ratio amplitude is `0.0250` with R2 improvement `0.411`; raw-signal amplitude is `1.225 kcps` with R2 improvement `0.427`.
  - At the programmed carrier `1.500 MHz`, ratio amplitude is `0.0240` with R2 improvement `0.359`; raw-signal amplitude is `1.128 kcps` with R2 improvement `0.345`.
  - The old `1.192 MHz` control is weak in the new ratio view: amplitude `0.00511`, R2 improvement `0.017`; raw-signal amplitude `0.474 kcps`, R2 improvement `0.064`.
  - Expected 13C sideband targets are not compelling: ratio amplitudes are `0.0108` at `1.115 MHz`, `0.0173` at `1.885 MHz`, `0.00953` at `1.307 MHz`, and `0.00614` at `2.077 MHz`.
  - FFT is not decisive over this short window; current ratio FFT top bins are `0.508`, `1.524`, and `2.033 MHz`.

## Plausible interpretation

- The new det=1.5 MHz run does not simply preserve the prior `~1.192 MHz` component. That argues against treating the prior feature as a fixed-frequency analysis artifact.
- There is partial det-tracking-looking content: the ratio view is strongest near `1.62 MHz`, and the explicit `1.692 MHz` det-tracking target has nearly the same ratio amplitude as the screen maximum.
- The evidence is still not claim-grade. Raw signal and signal-over-reference-line are dominated near `0.88 MHz`, while the ratio view emphasizes `~1.62 MHz`; the reference channel itself has structured low-MHz variation. The result therefore looks like mixed Ramsey signal plus baseline/reference/transient structure, not a clean physical carrier with robust sidebands.
- Under the project rule to establish raw/readout-aware signal presence before fitting T2star, this run should not be used to promote a numeric T2star.

## Claims not yet supported

- No well-supported T2star value for r03.
- No well-supported nearby 13C conclusion.
- No supported assignment of the new `~1.62/1.69 MHz` ratio component as the Ramsey carrier.
- No supported 13C sideband model at `1.115/1.885 MHz` or `1.307/2.077 MHz`.
- No claim that the prior `~1.192 MHz` feature was purely a fixed artifact; the det-shift run argues against that simple explanation but does not establish the physical alternative.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the Ramsey branch under current conditions as non-claim-grade after multiple analyzable attempts. The next project decision should be explicit: either close the r03 Ramsey/T2star/13C result as unsupported under these conditions, or switch to a different, model-driven protocol for the 13C question after a fresh resonance/count check. If another experiment is chosen, it should be an alternate protocol or a targeted control with a precomputed expected signal and a clear pass/fail criterion, not another same-style Ramsey accumulation.
