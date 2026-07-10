# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`.
- New measurement bundle: `measurement/m001.json` raw export, `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison/planning evidence: `evidence/e008.json` terminal det=1.0 MHz short-tau review, `evidence/e019.json` det-shift model/start note, `evidence/e021.json` verified intent, `evidence/e023.json` det-shift job contract.

## Calculations or scripts run

- Ran inline Python analysis over `measurement/m001.json`.
- Saved quantitative output to `analysis/ramsey_detshift_analysis.json`.
- Saved diagnostic plot to `analysis/ramsey_detshift_review.png`.
- Checks performed:
  - Parsed terminal det-shift Ramsey metadata: `nv23_ramsey_20260514_015423_auto_ramsey`, completed `2026-05-14T04:15:00`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - Verified scan shape: `tau = 0.048..1.968 us`, 41 points, `12 x 90000` repetitions, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`.
  - Computed raw signal/reference means, reference-line-normalized ratio, per-point SEM, common-mode per-average drift, broad least-squares frequency screens, FFT sanity screen, and direct LS amplitudes at the planned comparison frequencies.

## Quantitative results

- Mean readouts: signal `48.08 kcps`, reference `44.27 kcps`.
- Median across-average SEM: signal `0.745 kcps`; reference-line-normalized ratio equivalent `0.712 kcps`.
- Common-mode average-to-average drift stayed within about `-9.5%..+4.0%`; no average exceeded the `15%` drift flag threshold.
- Broad LS screen on both raw signal and reference-line-normalized ratio is dominated by the low-frequency boundary near `0.2 MHz`, consistent with slow baseline/shape content rather than a clean Ramsey carrier.
- Direct target-frequency LS amplitudes on the combined trace:
  - Programmed `1.5 MHz` carrier: ratio amplitude `0.037`, raw-signal amplitude `0.037 kcps`, weak versus SEM.
  - Det-tracking prediction from prior `1.192 + 0.5 = 1.692 MHz`: ratio amplitude `0.098`, raw-signal amplitude `0.099 kcps`, weak versus SEM.
  - Expected lower 13C sideband `1.116 MHz`: ratio amplitude `0.324`, raw-signal amplitude `0.325 kcps`, still below SEM and not dominant in the broad screen.
  - Expected upper 13C sideband `1.884 MHz`: ratio amplitude `0.143`, raw-signal amplitude `0.144 kcps`, below SEM.
  - Prior empirical `1.192 MHz`: ratio amplitude `0.293`, raw-signal amplitude `0.294 kcps`, below SEM.
- FFT sanity check has coarse-bin peaks near `1.016`, `0.508`, `1.524`, and `2.033 MHz`; the LS target check does not support a robust programmed `1.5 MHz` carrier despite the FFT bin near `1.524 MHz`.
- Per-average frequency screens are not coherent: 11 of 12 averages peak at the low-frequency boundary `0.2 MHz`; one peaks near `1.111 MHz`.

## Plausible interpretation

The det-shift diagnostic did not make the prior `~1.19 MHz` component track upward by `+0.5 MHz`, and it did not reveal a strong programmed `1.5 MHz` Ramsey carrier. The combined direct amplitudes at the programmed carrier, det-tracking prediction, expected 13C sidebands, and prior empirical frequency are all below the measured per-point SEM. The data are analyzable and not obviously failed, but the dominant content looks more like slow baseline/early-time shape or analysis-window leakage than a claim-grade Ramsey oscillation.

This result strengthens the earlier caution: r03 remains an aligned NV candidate by pODMR evidence, but the Ramsey datasets so far do not support a clean carrier/decay model or a nearby 13C sideband interpretation under the current Ramsey protocol.

## Claims that are not yet supported

- No supported numerical T2star claim from the new det=1.5 MHz Ramsey data.
- No supported nearby 13C claim from the new data.
- No supported claim that the prior `~1.19 MHz` feature was the physical Ramsey carrier.
- No supported claim that changing det from `1.0 MHz` to `1.5 MHz` produced a det-following Ramsey oscillation.
- No supported claim that the weak lower-sideband-sized content near `1.116 MHz` is a 13C sideband; its amplitude is below SEM and the per-average screens are incoherent.

## Recommended next action

Do not run another blind Ramsey repeat on r03 with this same protocol. The next decision should be a branch-level one: either switch to an alternate T2star/13C protocol or close the current Ramsey branch with a supported negative/unsupported conclusion under these conditions. If continuing experimentally, first design a non-blind protocol-change test aimed at separating pulse/timing/readout artifacts from true free precession, rather than only increasing averages.
