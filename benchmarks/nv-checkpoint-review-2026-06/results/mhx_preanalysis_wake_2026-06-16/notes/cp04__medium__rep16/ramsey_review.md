# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` terminal control.
- Prior-run context from `project/state.md`: accepted r03 at `mw_freq = 3.8759 GHz`; prior short-tau `det = 1.0 MHz` run had a non-claim-grade empirical component near `1.192 MHz`; this run tested whether it moved toward `~1.692 MHz` after changing `det` to `1.5 MHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Output files: `ramsey_analysis_summary.json` and `ramsey_detshift_review.png`.
- Raw array contract check: `ExperimentData` shape `[1,2,41]`; `ExperimentDataEachAvg` shape `[1,12,2,41]`; averaging over the stored-average axis reproduces `ExperimentData`. Readout 0 is the 0-level reference and readout 1 is the Ramsey signal for this `full_experiment = 0` sequence.
- Run parameters verified: job `nv23_ramsey_20260514_015423_auto_ramsey`, run `1DExp-seq-ramsey-vary-tau-2026-05-14-015440`, completed, final counts `44.796 kcps`, `tau = 48 ns..1.968 us`, `41` points, `12 x 90000 = 1.08e6` shots per tau, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, snake order.
- Noise/effect checks:
  - Median signal SEM across stored averages: `0.711 kcps`.
  - Median point-wise ratio SEM: `0.0126`.
  - Signal peak-to-peak over tau: `6.46 kcps`; ratio peak-to-peak: `0.134`.
  - Stored-average common-mode variation is visible: combined mean span `13.5%`; signal/reference average means are strongly correlated (`r ~ 0.90`), consistent with shared brightness drift/provenance.
- Least-squares sinusoid screens used constant+slope baseline terms. Full-window target amplitudes:
  - `1.5 MHz` programmed det: `1.13 kcps`, ratio `0.0240`.
  - `1.692 MHz` det-tracking prediction: `1.22 kcps`, ratio `0.0250`.
  - `1.192 MHz` prior-component control: `0.474 kcps`, ratio `0.0051`.
  - Predicted 13C sidebands: `1.307 MHz` ratio `0.0095`; `2.076 MHz` ratio `0.0062`.
  - In the restricted `1.0..2.4 MHz` ratio screen, the maximum is near `1.616 MHz` with ratio amplitude `0.0255`; this is close to both the `1.5 MHz` and `1.692 MHz` target amplitudes.
  - FFT after linear detrending is coarse for this short span; strongest nonzero ratio bins are `0.508 MHz`, `1.524 MHz`, `2.033 MHz`, and `1.016 MHz`.

## Plausible interpretation

- The measurement completed as intended and is analyzable; there is no terminal abort/control-stop evidence.
- The prior `~1.192 MHz` component is not reproduced as the dominant target-frequency component in the det-shift run. The normalized LS screen has its strongest relevant-band power near `1.6 MHz`, and the `1.5 MHz`/`1.692 MHz` target amplitudes are much larger than the old `1.192 MHz` control. This is qualitatively more compatible with a det-dependent Ramsey feature than with a perfectly fixed `1.192 MHz` artifact.
- However, the result is still not claim-grade. The strongest restricted-band ratio maximum is near `1.616 MHz`, not cleanly at the programmed `1.5 MHz` or the prior-plus-det-shift `1.692 MHz`; FFT bins are broad/coarse; raw signal screens are strongly affected by slow baseline structure; and the relevant amplitudes are only about one to two times the measured point-wise SEM/residual scale.
- The expected 13C sideband positions around `1.307 MHz` and `2.076 MHz` are weaker than the carrier-region candidates and are not independently supported.

## Claims that are not yet supported

- No supported numeric `T2star` from this run.
- No supported nearby `13C` claim from this run.
- No supported exact Ramsey carrier frequency. The data are consistent with weak det-dependent structure but do not isolate whether the carrier is `1.5 MHz`, `~1.6 MHz`, or `~1.692 MHz`.
- No supported claim that the remaining structure is purely physical or purely instrumental; the data show both a weak det-shift-compatible component and substantial baseline/common-mode provenance.

## Recommended next action

- Do not run another blind Ramsey repeat on r03 under the same conditions.
- Treat the Ramsey/T2star/13C state as unresolved/non-claim-grade under the current Ramsey protocol. The next useful step is a deliberate branch decision: either switch to an alternate coherence protocol that is less sensitive to this Ramsey carrier ambiguity, such as a Hahn/CPMG baseline before any 13C spectroscopy, or close the r03 Ramsey branch with a supported "no T2star/13C conclusion from current Ramsey data" statement.
