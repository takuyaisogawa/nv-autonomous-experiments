# Ramsey Det-Shift Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison data: `evidence/e006.json` terminal det=1.0 MHz short-tau raw export, `evidence/e007.json` prior scan-order drift review, `evidence/e008.json` prior terminal short-tau review.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Output artifacts: `ramsey_detshift_analysis.json` and `ramsey_detshift_review.png`.
- Checks performed:
  - Verified current raw axis contract: averaging `ExperimentDataEachAvg` over the average axis reconstructs `ExperimentData` with max absolute error `1.4e-14`.
  - Confirmed current run: tau `0.048..1.968 us`, `41` points, `48 ns` step, `12 x 90000` repetitions, `1.08e6` shots/tau, `mw_freq=3.8759 GHz`, `det=1.5 MHz`, final counts `44.796 kcps`.
  - Sampling limits: FFT bin spacing `0.508 MHz`, nominal resolution `1/span = 0.521 MHz`, Nyquist `10.42 MHz`.
  - Noise/drift: current median signal SEM `0.711 kcps`, median ratio SEM `0.0126`; Python scan-order common-mode drift check flagged no averages, max drop score `0.0397`.
  - Dense LS screens fitted a linear baseline plus sine/cosine at each frequency; FFT nearest-bin values were used only as coarse visual checks.

## Quantitative result

- Previous det=1.0 MHz short-tau terminal raw export had the combined ratio LS maximum at `1.192 MHz`, ratio amplitude `0.0363`, R2 improvement `0.656`.
- Current det=1.5 MHz run:
  - Ratio LS maximum is near `1.623 MHz`, amplitude `0.0255`, R2 improvement `0.430`.
  - Planned det-tracking target `1.692 MHz` has similar ratio amplitude `0.0250`, R2 improvement `0.411`.
  - Programmed `1.5 MHz` target has ratio amplitude `0.0240`, R2 improvement `0.359`.
  - Old fixed `1.192 MHz` artifact-control target is weak: ratio amplitude `0.00511`, R2 improvement `0.0167`.
  - Raw signal and signal-over-fitted-reference views are not led by the det-shifted component; both screen strongest near `0.882 MHz` with raw-signal amplitude `1.53 kcps` and R2 improvement `0.577`.
  - Current 13C sideband target checks are weak: det-tracking sidebands `1.307/2.077 MHz` have ratio amplitudes `0.0095/0.0061`; programmed-det sidebands `1.115/1.885 MHz` have ratio amplitudes `0.0108/0.0173`.
  - Per-average frequency screens are not coherent; target `1.692 MHz` has only `4/12` averages with R2 improvement above `0.2`, while old `1.192 MHz` has `0/12`.

## Plausible interpretation

The run completed cleanly and is analyzable. The old `~1.192 MHz` ratio component from the det=1.0 MHz short-tau run does not persist at the same frequency after changing det to 1.5 MHz, which argues against a simple fixed-frequency artifact. The current ratio view has power near the intended det-shift region (`1.623..1.692 MHz`), so the measurement is suggestive that some part of the earlier empirical component may be det-dependent.

However, the support is not strong enough for a physical Ramsey carrier model. The short tau span limits frequency discrimination to about `0.52 MHz`; the raw signal and fitted-reference-normalized signal prefer `~0.882 MHz` rather than the det-shift target; the per-average screens are inconsistent; and sideband targets are weak. Treat this as useful diagnostic evidence, not a parameter extraction.

## Claims not yet supported

- No supported numeric `T2star` from this run or from the r03 Ramsey series.
- No supported nearby `13C` coupling conclusion from this run.
- No supported claim that the Ramsey carrier has been confirmed at `1.5 MHz`, `1.623 MHz`, or `1.692 MHz`.
- No supported physical assignment of the `0.882 MHz` raw-signal component.
- No supported high-precision frequency claim from the short `1.92 us` span.

## Recommended next action

Do not run another blind same-style short-tau Ramsey repeat. Do a bridge-free branch synthesis and then pivot to a deliberately different protocol or diagnostic before more hardware time: either an alternate Ramsey/readout/phase-control test that can separate raw-signal and normalization artifacts, or a coherence/13C protocol such as Hahn/CPMG/XY-family after a fresh quantitative model and current advisory check.
