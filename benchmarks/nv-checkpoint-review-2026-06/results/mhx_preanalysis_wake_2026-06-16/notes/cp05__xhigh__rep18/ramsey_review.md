# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior local evidence used for context: `evidence/e001.json`/`e003.json` for the refreshed pODMR center and drift-style conventions, and `evidence/e014.json` for the planned Ramsey targets.
- New measurement files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submit spec, `measurement/m003.json` bridge result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis.json`, and `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` and `python -m py_compile analyze_ramsey.py`.
- Verified the raw array contract: `ExperimentData` shape `(2, 41)`, `ExperimentDataEachAvg` shape `(20, 2, 41)`, and averaging the per-average axis reproduces the combined reference and signal traces.
- Verified readout roles from the embedded `ramsey.xml`: readout 1 is the true 0-level reference; `full_experiment=0` skips the optional 1-level reference; readout 2 is the Ramsey signal.
- Terminal health: job completed, final counts `43.433 kcps`, safe shutdown true, stop request false, no hard anomaly.
- Scan: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=0.048..8.048 us`, `41` points, `0.2 us` step, `20 x 50000 = 1.0e6` shots per tau, Nyquist `2.5 MHz`, span resolution `125 kHz`.
- Local snake-order drift approximation found no flagged averages. This is a local approximation, not the MATLAB drift helper.
- Readout uncertainty: median signal SEM `0.850 kcps`; median point-wise ratio SEM `0.0116`; median fitted-reference-line ratio SEM `0.0174`.
- Full-span LS screen: strongest combined component is near `2.268 MHz` in raw, point-wise ratio, and fitted-reference-line views. The programmed `1.5 MHz` carrier is present but not the top screen: raw amplitude `0.713 kcps` with LS SNR `3.52`; point-wise ratio amplitude `0.0148` with SNR `3.53`; refline ratio amplitude `0.0146` with SNR `3.51`.
- Skip-first-4-tau LS screen: raw and fitted-reference-line views peak near `1.520 MHz`; carrier amplitudes are raw `0.520 kcps` with SNR `3.51` and refline ratio `0.0107` with SNR `3.51`. Point-wise ratio still peaks near `2.263 MHz`, with carrier amplitude `0.0117` and SNR `3.01`.
- Target sidebands are not persuasive. At `1.115 MHz`, amplitudes are small in all views. At `1.885 MHz`, the largest full-span value is point-wise-ratio-only and not reproduced in raw/refline or skip-first-4 views.
- Damped-sinusoid T2star fits are unstable: full-span fits collapse to short `~0.39..0.84 us` values with stretch power at the lower bound; skip-first-4 and skip-first-8 fits move by several-fold and sometimes shift free frequency away from the target. These are descriptive diagnostics only.

## Plausible interpretation

The run is technically usable and improves the carrier situation relative to the earlier ambiguous Ramsey branch. There is a weak, coherent carrier-like response near the programmed `1.5 MHz`, especially after excluding the first four tau points, and the first few points likely include transient/baseline structure.

The evidence is still not claim-grade for a physical Ramsey parameter extraction. The full-span top component near `2.27 MHz`, the point-wise ratio sensitivity, the inconsistent per-average top frequencies, and the unstable T2star fits all argue against promoting a numeric T2star. The carrier-like feature is useful evidence that the refreshed center did not simply fail, but it is too weak and model-dependent to close the T2star objective.

## Claims not yet supported

- A numeric T2star for r03.
- Nearby 13C coupling or a resolved 13C sideband pair at `1.115/1.885 MHz`.
- Physical assignment of the `~2.27 MHz` component.
- A broad negative claim that no 13C coupling exists under all protocols.
- Sub-grid microwave-center precision beyond the prior pODMR-supported `3.8765 GHz` grid center and several-100-kHz uncertainty.

## Recommended next action

Do not run another blind repeat of this Ramsey scan. Record this terminal run as weak carrier evidence with no supported T2star/13C conclusion. For the next project decision, either move to a targeted alternate protocol for nuclear-spin/coherence evidence after normal gates, or close r03 as unsupported for T2star/13C under the current Ramsey conditions. If the next action must stay Ramsey-specific, redesign around a specific failure mode such as early-time transient/phase-readout rather than repeating the same `8 us`, `det=1.5 MHz` scan.
