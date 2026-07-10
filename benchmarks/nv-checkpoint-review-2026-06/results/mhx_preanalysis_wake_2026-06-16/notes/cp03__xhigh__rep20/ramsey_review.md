# Ramsey review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior Ramsey/design context: `evidence/e003.json` (terminal det=1.0 MHz 8 us review), `evidence/e006.json` and `evidence/e009.json` (short-tau design/intent), `evidence/e017.md` (design/start note).
- New terminal measurement: `measurement/m001.json` raw export, `measurement/m002.json` executed job spec, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` control.

## Calculations or scripts run

- Created and ran `analyze_ramsey_shorttau.py`.
- Generated `ramsey_shorttau_analysis.json`, `ramsey_shorttau_traces.png`, and `ramsey_shorttau_fft.png`.
- Checks performed:
  - Loaded readout1 as the `full_experiment=0` reference and readout2 as Ramsey signal, following the prior protocol review.
  - Verified acquisition: `tau=0.048..1.968 us`, `41` points, `48 ns` step, `12 x 90000` repetitions (`1.08e6` shots/point), final counts `35.122 kcps`, completed safely, no stop request, no monitor error.
  - Calculated raw signal/reference means and per-point noise estimates: reference mean `48.573 kcps`, signal mean `44.655 kcps`, ratio mean `0.91946`, median signal SEM across averages `1.138 kcps`, median ratio SEM `0.0127`.
  - Scan-order/common-mode checks: average 11 has a >15% common-mode drop vs run median; no average had >15% first-half/second-half scan-order drift. Removing average 11 did not materially change the frequency conclusion.
  - Least-squares fixed-frequency screens with linear baseline:
    - `1.000 MHz` carrier: ratio amplitude `0.0274`, signal amplitude `1.282 kcps`, ratio R2 improvement `0.355`.
    - `0.615 MHz` expected low 13C sideband: ratio amplitude `0.0243`, signal amplitude `1.102 kcps`, ratio R2 improvement `0.312`.
    - `1.385 MHz` expected high 13C sideband: ratio amplitude `0.0271`, signal amplitude `1.222 kcps`, ratio R2 improvement `0.345`.
    - strongest 0.5-5 MHz component: near `1.206 MHz`, ratio amplitude `0.0364`, signal amplitude `1.686 kcps`, ratio R2 improvement `0.654`.
  - FFT sanity check: coarse short-window bins are `0.508 MHz` and `1.016 MHz`; their ratio amplitudes are comparable (`0.0300` and `0.0280`), so the FFT does not isolate a unique carrier or sideband.
  - Forced damped 1 MHz diagnostic fit prefers an apparent very short T2* (`~0.16-0.19 us`) but with a broad near-best range reaching the lower grid bound (`0.1..0.43 us`) and with an ambiguous carrier/sideband model; not claim-grade.

## Plausible interpretation

- The run completed and is analyzable. It is not a pure no-signal result: compared with the previous det=1.0 MHz 8 us run (`0.00916` ratio / `0.277 kcps` carrier LS amplitude), the short-tau data has a stronger early-time oscillatory residual (`0.0274` ratio / `1.282 kcps` at 1 MHz; first `0.768 us` signal residual peak-to-peak `5.09 kcps`).
- The result still does not support a clean Ramsey carrier/13C model. The expected carrier and both expected 13C sidebands have similar amplitudes, the strongest band-limited LS component is near `1.20 MHz` rather than exactly at the programmed carrier or a predicted sideband, and the short `1.92 us` span gives only about `0.52 MHz` nominal frequency resolution.
- The persistent `~1.18-1.21 MHz` feature is worth noting as a hypothesis, but current evidence cannot distinguish a physical component from short-window curvature/drift/model degeneracy.

## Claims not yet supported

- No supported numeric T2* claim from this dataset.
- No supported nearby 13C claim.
- No supported claim that the `1.0 MHz` programmed carrier is cleanly resolved.
- No supported claim that the `~1.2 MHz` component is physical.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Record this as non-claim-grade but informative early-time evidence, then decide between a deliberately discriminating follow-up protocol and branch closeout. If pursuing one more r03 attempt, predefine a protocol that can separate carrier/sideband physics from the broad `~1.2 MHz`/curvature ambiguity, such as a phase-cycled or detuning-pair short-tau Ramsey with explicit success criteria; otherwise close the r03 T2*/13C branch as unsupported under current conditions.
