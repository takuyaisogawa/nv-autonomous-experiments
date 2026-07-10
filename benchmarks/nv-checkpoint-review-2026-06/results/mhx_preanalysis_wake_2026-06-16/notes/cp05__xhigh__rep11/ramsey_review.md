# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- Prior plan/targets: `evidence/e014.json`.
- New terminal Ramsey data and metadata: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` final status, `measurement/m005.json` control.
- Local outputs created: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` as two readouts over 41 tau points and `ExperimentDataEachAvg` as 20 averages x 2 readouts x 41 tau points.
- Checked run health: completed `2026-05-14T09:28:25`, final counts `43.433 kcps`, no abort, no stop request, monitor error empty, above the `20 kcps` minimum.
- Built raw signal, point-wise `signal/reference`, and fitted-reference-line normalized traces.
- Estimated SEM across the 20 stored averages: median signal SEM `0.850 kcps`; median ratio SEM `0.0116`.
- Ran least-squares frequency screens using `c + m*t + a*cos(2*pi*f*t) + b*sin(2*pi*f*t)` from `0.25..2.35 MHz`, plus Hann-window FFT checks.
- Repeated screens for full span and skip-first-4 tau points, and checked target amplitudes at carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior det-shift top `1.623 MHz`, and old fixed-control `1.192 MHz`.
- Checked per-average broad-top frequencies, target phase coherence, bootstrap amplitudes from resampled averages, and a simple snake-order drift/outlier summary.

## Plausible interpretation

- The measurement itself is usable; there is no hard bridge/count/stop anomaly.
- The strongest combined LS component is not the planned carrier or expected 13C sideband: `signal/reference` full-span top is `2.270 MHz` with amplitude `0.01845`, and skip4 top is `2.266 MHz` with amplitude `0.01418`.
- The programmed carrier is present but secondary: ratio amplitude `0.01575` full-span and `0.01231` skip4; raw-signal amplitude `0.705 kcps` full-span and `0.512 kcps` skip4. This is below the median per-point signal SEM and below the prior model-plan expected raw oscillation scale.
- Sideband evidence is weak/asymmetric: low-sideband ratio amplitude is `0.00278` full / `0.00067` skip4; high-sideband ratio amplitude is `0.00962` full / `0.00527` skip4. The low/high pair does not form a coherent 13C pattern.
- Per-average frequency content remains mixed. Only `6/20` ratio averages have broad-top frequencies inside the `1.2..1.8 MHz` carrier planning band; ratio broad tops range from about `0.357` to `2.340 MHz`.
- The old `1.192 MHz` fixed-control component remains weak (`0.00194` full / `0.00191` skip4 ratio amplitude), so this does not simply revive that artifact. However, the new dominant `~2.27 MHz` component is outside the planned carrier/sideband model and close enough to the high-frequency end to require caution.
- Larger post-hoc skips eventually move the top toward the carrier, but the planned full/skip4 review still fails the clean carrier/sideband consistency test. Treat this as another analyzable but non-claim-grade Ramsey result.

## Claims not yet supported

- No numeric T2star claim is supported from this run.
- No nearby 13C claim is supported from this run.
- The `~2.27 MHz` feature should not be promoted as the Ramsey carrier or a 13C sideband without an explicit follow-up that explains why it is outside the planned target model.
- The refreshed pODMR center is not proven to have solved the earlier weak/mixed Ramsey issue.
- The data do not support sub-grid precision for the microwave resonance center beyond the prior pODMR calibration note.

## Recommended next action

Do not run another blind long-span Ramsey repeat on r03. Close this refreshed-center Ramsey branch as non-claim-grade under current conditions, then choose a non-blind alternate path: either record a supported unsupported/negative r03 Ramsey/T2star/13C conclusion under the current Ramsey route, or run a targeted alternate protocol/diagnostic specifically designed to test the unexplained `~2.27 MHz` component before making any positive T2star or 13C claim.
