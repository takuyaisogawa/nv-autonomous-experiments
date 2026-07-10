# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- New Ramsey det-shift data:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`, `measurement/m005.json`: terminal status/control snapshots.
- Prior comparison data:
  - `evidence/e008.json`: terminal det=1.0 MHz short-tau review.
  - `evidence/e019.json`: det-shift model plan and target frequencies.
- Generated local analysis artifacts:
  - `analyze_ramsey_detshift.py`
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_analysis.png`

## Calculations/scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified `ExperimentDataEachAvg` axis contract as `[slice, avg, readout, point]` by averaging over the average axis back to `ExperimentData`; max absolute mismatch was `1.4e-14`.
- Confirmed run parameters from local files: `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 0.048..1.968 us`, `41` points, `12 x 90000` repetitions, terminal final counts `44.796 kcps`, snake scan order, no stop request, completed status.
- Computed raw reference/signal, point-wise signal/reference ratio, signal normalized by a fitted reference line, per-point SEM across stored averages, FFT bins, and continuous least-squares sinusoid screens with a linear baseline.
- Compared targeted frequencies:
  - Programmed carrier `1.500 MHz`.
  - Programmed 13C sidebands `1.115/1.885 MHz`.
  - Predicted det-tracking carrier if the prior `1.192 MHz` component were physical: `1.692 MHz`.
  - Predicted det-tracking sidebands `1.307/2.077 MHz`.
  - Prior fixed-artifact control `1.192 MHz`.

## Plausible interpretation

- The new run completed cleanly and is analyzable. Median SEM is `0.711 kcps` for raw signal and `0.0126` in ratio; raw signal residual peak-to-peak after linear detrending is `6.29 kcps`, and ratio residual peak-to-peak is `0.133`.
- The prior fixed `1.192 MHz` control is weak in the new det=1.5 MHz data: ratio LS amplitude `0.0051`, raw-signal LS amplitude `0.474 kcps`.
- Carrier-region content is now stronger: programmed `1.500 MHz` gives ratio amplitude `0.0240` and raw-signal amplitude `1.13 kcps`; the det-tracking target `1.692 MHz` gives ratio amplitude `0.0250` and raw-signal amplitude `1.22 kcps`. The strongest FFT ratio bin is `1.524 MHz` with amplitude `0.0246`.
- The continuous LS screen ranked by R2 improvement peaks near `1.62 MHz`, between the programmed carrier and the predicted det-tracking carrier. Given the short `1.92 us` span and FFT bin spacing near `0.508 MHz`, this is compatible with a carrier-region Ramsey response shifting upward relative to the prior `1.192 MHz` run, but it does not precisely distinguish `1.5` from `1.692 MHz`.
- A large low-frequency/trend-like component remains in amplitude-ranked screens near the lower search boundary (`~0.35 MHz`), and per-average top frequencies are inconsistent. This keeps the result below claim-grade for physical parameter extraction.
- The det-shift result argues against simply treating the prior `~1.192 MHz` component as a fixed analysis artifact. It is more consistent with some det-dependent Ramsey response being present, but the shape is still contaminated by baseline/transient structure.

## Claims not yet supported

- A numeric `T2star` is still not supported. The available short-tau data show carrier-region oscillatory content, but the envelope is not cleanly constrained over this window and is mixed with low-frequency/transient structure.
- A nearby `13C` conclusion is not supported. Programmed sideband checks are weaker than the carrier-region response: ratio amplitudes are `0.0108` at `1.115 MHz` and `0.0173` at `1.885 MHz`; det-tracking sideband checks are also weak (`0.0095` at `1.307 MHz`, `0.0061` at `2.077 MHz`).
- The exact Ramsey carrier frequency is not supported beyond a broad carrier-region statement. Current data cannot cleanly separate the programmed `1.500 MHz` carrier from the predicted `1.692 MHz` det-tracking target.
- No separate MATLAB scan-order drift-analysis JSON for this new terminal run was present in the local snapshot. Local per-average means show common-mode variation but no bridge stop/error; this is not identical to the prior project's scan-order-aware drift tool.

## Recommended next action

- Do not run another blind Ramsey repeat.
- Treat r03 as still aligned and the new det-shift as evidence for det-dependent Ramsey content, but keep `T2star` and `13C` open/unsupported.
- Next, use an alternate protocol or deliberately redesigned Ramsey measurement that resolves the ambiguity: either improve carrier/phase discrimination over a longer or better-conditioned tau window after checking drift/tracking limits, or switch to a protocol less sensitive to the observed short-tau transient/baseline structure before making a T2star or 13C claim.
