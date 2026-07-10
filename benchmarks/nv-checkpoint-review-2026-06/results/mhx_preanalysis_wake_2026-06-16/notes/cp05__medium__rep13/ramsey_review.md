# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/state.md`, `project/advice.md` for objective, current r03 status, and required claim posture.
- `md/memory.md`, `md/knowledge.md` for local NV/Ramsey review rules.
- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted Ramsey job spec.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result, status, and control metadata.
- Prior project context in `project/state.md` for earlier non-claim-grade Ramsey results and expected targets.

## Calculations/Scripts Run

- Created and ran `analyze_ramsey.py`; output is `ramsey_analysis_summary.json`.
- Verified `ExperimentDataEachAvg` axis contract as `[avg, readout, point]`; averaging per-average readouts reproduced `ExperimentData` for both readouts.
- Reviewed terminal health: job completed, final counts `43.433 kcps`, `stop_requested=false`, monitor `last_error=""`, saved scan `20 x 50000` shots.
- Confirmed scan: `tau = 0.048..8.048 us`, `41` points, `0.200 us` step, `1.0e6` shots per tau point, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
- Target frequencies from the project model: carrier `1.500 MHz`; 13C sidebands near `1.115 MHz` and `1.885 MHz` using `f13C ~384.8 kHz`. Nominal FFT resolution is `125 kHz`; Nyquist is `2.5 MHz`.
- Ran linear detrending, FFT screens, least-squares sinusoid amplitude screens, and per-average frequency screens for raw signal, point-wise signal/reference, and signal/reference-linear-fit views. Repeated screens after skipping the first 4 tau points.

## Plausible Interpretation

- The measurement is technically analyzable and has no hard terminal anomaly in the provided metadata.
- The refreshed-center Ramsey still does not give claim-grade Ramsey evidence. In all three combined views, the strongest full-span LS screen is near `2.27 MHz`, not the programmed `1.5 MHz` carrier or the expected `1.115/1.885 MHz` 13C sidebands.
- Full-span target amplitudes:
  - Raw signal: top `2.271 MHz` amplitude `0.818 kcps`; carrier `1.500 MHz` amplitude `0.705 kcps`; median per-point SEM `0.850 kcps`.
  - Point-wise ratio: top `2.270 MHz` amplitude `0.01845`; carrier amplitude `0.01573`; median SEM `0.01161`.
  - Reference-line-normalized signal: top `2.271 MHz` amplitude `0.01677`; carrier amplitude `0.01445`; median SEM `0.01741`.
- Skip-first-4-points screens remain non-claim-grade: the top stays near `2.266..2.271 MHz`, and carrier amplitudes drop to `0.509 kcps`, `0.01224`, and `0.01043` in raw, point-wise ratio, and ref-line-normalized views.
- Per-average frequency support is mixed. Only `5/20` raw-signal averages and `6/20` point-wise-ratio averages have their strongest LS component within `0.25 MHz` of the `1.5 MHz` carrier in the full-span screen; skip-first-4 gives `4/20`, `6/20`, and `4/20` for raw, point-wise ratio, and ref-line-normalized views.
- The simple per-average common-mode brightness check shows substantial average-to-average scatter (`~28%` peak-to-peak) but only a modest net linear trend (`-4.8%` end-minus-start). That supports caution about per-average spectral consistency, not a hard rejection of the terminal run.
- The `2.27 MHz` feature is an empirical component in this run. It is not yet physically assigned; it is close to the Nyquist guardrail and not one of the planned carrier/13C targets.

## Claims Not Yet Supported

- No numeric `T2*` claim is supported from this run. The programmed carrier/decay shape is not established above SEM with consistent per-average support, so a damped-sinusoid T2* fit would be descriptive only.
- No nearby `13C` claim is supported. The expected sidebands near `1.115 MHz` and `1.885 MHz` are not dominant or consistent across raw and normalized views.
- The `2.27 MHz` component should not be promoted to a physical coupling, true detuning, or stable apparatus artifact without a targeted check.
- This run does not overturn the established r03 alignment/pODMR conclusion; it only says the Ramsey/T2*/13C branch remains unsupported under this protocol.

## Recommended Next Action

Avoid another blind Ramsey repeat on r03. Since this high-shot refreshed-center long-span run remains non-claim-grade after multiple prior Ramsey attempts, choose a different diagnostic path: either run a targeted protocol/route check that can test the `2.27 MHz` component and pulse-phase/timing behavior, or move to an alternate coherence protocol such as Hahn/CPMG-style T2-family measurement before making the supported project conclusion that r03 Ramsey/T2*/13C is unresolved under current Ramsey conditions.
