# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior plan/model context: `evidence/e014.json` for the refreshed-center Ramsey design and required post-run checks.
- New terminal measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Local analysis artifacts created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_plot.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Reconstructed tau from raw scan metadata: 0.048 to 8.048 us, 41 points, 0.2 us step; Nyquist 2.5 MHz, nominal resolution 125 kHz.
- Verified readout/average axis contract: `ExperimentDataEachAvg` averages reproduce combined `ExperimentData` to floating precision.
- Checked run health: job/status completed, final counts 43.433 kcps, no stop request, no monitor error, safety shutdown ok.
- Local drift/count check using stored `ScanOrderInfo` (`snake`, data saved in tau order): no robust outlier averages; common-mode average level ranged 39.56 to 52.64 kcps (CV 6.8%), so there is drift/provenance but no count-collapse flag.
- Compared raw signal, signal/reference, and signal/fitted-reference-line views with full-span and skip-first-4 LS frequency screens.
- Target checks used the planned det=1.5 MHz carrier, expected 13C sidebands at 1.115 and 1.885 MHz, prior empirical 1.192 MHz control, and prior det=1.623 MHz top.
- Key ratio-view LS results:
  - full-span top is 2.270 MHz, amplitude 0.01845;
  - programmed 1.500 MHz carrier amplitude is 0.01575;
  - 1.115 MHz low sideband amplitude is 0.00278;
  - 1.885 MHz high sideband amplitude is 0.00962;
  - median point-wise ratio SEM is 0.01161.
- Simultaneous ratio fit keeps both off-target and carrier components: 2.270 MHz amplitude 0.01792 plus 1.500 MHz amplitude 0.01513, residual RMS 0.01440. Planned carrier+first-sideband model alone has weak/one-sided sideband support and residual RMS 0.01783.
- Per-average frequency screens are mixed. In the ratio view, only 6/20 full-span averages and 5/20 skip-first-4 averages have their top frequency within +/-0.2 MHz of the carrier; sideband counts are not convincing.
- Descriptive damped-cosine fits are not claim-grade: the ratio full-span fit at the observed 2.27 MHz component gives T2star about 2.36 us, while skip-first-4 gives about 7.83 us with large uncertainty and different stability.

## Plausible interpretation

The run is analyzable and healthy enough to use as evidence. It shows a weak but coherent Ramsey-like response, including a planned-carrier component near 1.5 MHz. However, the dominant full-span feature is consistently off-target near 2.27 MHz in raw, point-wise ratio, and fitted-reference-line views. That frequency is not the planned carrier or the planned first-order 13C sidebands. It is numerically close to `det + 2*f_13C` using the project model, but the expected first-order sideband pair is not clean or symmetric, so this is an observation, not a 13C assignment.

Compared with the project goal, the refreshed-center high-shot Ramsey improved evidence that there is some coherent oscillatory structure, but it still does not produce a clean carrier/decay/sideband model suitable for promoting a T2star or nearby-13C conclusion.

## Claims not yet supported

- No supported numeric T2star. Damped fits are sensitive to frequency choice and skipped early points.
- No supported nearby 13C conclusion. The planned low sideband is weak, the high sideband is not paired cleanly, and the strongest 2.27 MHz feature is outside the preplanned first-order sideband model.
- No claim that the microwave center is definitively wrong by about 0.77 MHz; that is only one possible explanation for the off-target beat.
- No claim that the previous 1.192 MHz empirical component is physical; it remains weak in this long-span run.

## Recommended next action

Do not run another blind accumulation on the same Ramsey settings. First, run a targeted detuning/frequency-control diagnostic after a quick pODMR center sanity check: choose two or three programmed detunings around the current center and require the dominant Ramsey component to track detuning one-for-one, with sidebands maintaining the expected +/-384.8 kHz separation, before any T2star or 13C fit is promoted. If that control remains mixed, close the r03 Ramsey branch as unsupported under this protocol and switch to an alternate coherence/coupling protocol rather than repeating this scan.
