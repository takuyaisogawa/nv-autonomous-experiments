# Ramsey review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, and `context.json` for objective, prior r03 status, Ramsey targets, and interpretation guardrails.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: executed job spec for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result, status, and run-control metadata.
- Scratch outputs created here: `ramsey_analysis.py`, `ramsey_analysis_results.json`, `ramsey_analysis_plot.png`.

## Calculations or scripts run

- Ran `python ramsey_analysis.py`.
- Confirmed from the embedded `ramsey.xml` text in `m001.json` that readout 1 is the true mS=0 reference and readout 2 is the Ramsey signal after `ramsey(...)`.
- Terminal health checks: job/result completed, final counts `43.433 kcps`, no stop request, empty monitor error, `aborted=false`, safe shutdown ok.
- Scan geometry: `tau=48 ns..8.048 us`, `41` points, `200 ns` step, `8.0 us` span, `2.5 MHz` Nyquist, about `125 kHz` nominal resolution, `20 x 50000 = 1.0e6` shots per tau.
- Data/noise checks: mean signal `44.67 kcps`, mean reference `48.79 kcps`, median signal SEM across averages `0.850 kcps`, median ratio SEM `0.01161`. Stored-average mean signal ranged `37.38..50.37 kcps`; reference ranged `41.74..54.90 kcps`, a common-mode drift/provenance issue but not a count-collapse anomaly.
- Least-squares sinusoid screens used a constant plus linear baseline. In `signal/reference`, full-span top was `2.270 MHz` with amplitude `0.01845`; skipping the first four tau points kept the top near `2.267 MHz` with amplitude `0.01418`.
- Target amplitudes in `signal/reference`: carrier `1.500 MHz` amplitude `0.01575` full / `0.01231` skip4; 13C lower `1.1152 MHz` `0.00278` / `0.00067`; 13C upper `1.8848 MHz` `0.00962` / `0.00527`; prior fixed `1.192 MHz` control `0.00194` / `0.00191`.
- Raw-signal target amplitudes: carrier `0.705 kcps` full / `0.512 kcps` skip4; lower 13C `0.145 kcps` / `0.012 kcps`; upper 13C `0.261 kcps` / `0.124 kcps`. The carrier raw amplitude is below the prior expected order-`2..6 kcps` Ramsey oscillation scale and near/below per-point SEM.
- FFT checks were mixed: carrier-adjacent bins near `1.463/1.585 MHz` full-span and `1.486 MHz` skip4 are visible, but high-frequency bins near `2.317/2.297 MHz` are also prominent.
- Per-average frequency screens were not coherent: ratio top frequencies were scattered; only `5/20` stored averages had their top screen within `0.125 MHz` of the carrier, `0/20` near lower 13C, `2/20` near upper 13C, and `0/20` near the old `1.192 MHz` control. Carrier phase/coefficient consistency was moderate, but sideband consistency was poor.

## Plausible interpretation

The measurement completed cleanly and is analyzable. It contains weak carrier-like power near the programmed `1.5 MHz` detuning in the raw, ratio, fitted-reference, and FFT views, but the carrier is not dominant, is small relative to the expected raw oscillation scale, and is only comparable to the measured uncertainty. The strongest continuous LS feature is instead near `2.27 MHz`, close to the high-frequency side of the sampled band and not one of the planned carrier/13C targets.

The refreshed pODMR center did not turn the high-shot, long-span Ramsey into a clean carrier-plus-sideband dataset. The most plausible project-level interpretation is still mixed/non-claim-grade Ramsey contrast on r03 under this protocol, with residual systematic/protocol or timing/phase effects more likely than a simple lack-of-shots problem.

## Claims not yet supported

- No well-supported numeric T2star should be claimed from this run.
- No supported nearby 13C coupling or sideband conclusion is established. The expected `1.115/1.885 MHz` sideband pattern is not coherent.
- Do not promote the descriptive high-frequency `~2.27 MHz` component or its damped-fit `T2star ~2.65 us` as a physical NV result.
- Do not claim a definitive absence of all nearby 13C spins; the supported statement is narrower: this Ramsey branch has not produced claim-grade 13C evidence under the tested conditions.

## Recommended next action

Do not run another blind repeat of the same refreshed-center `det=1.5 MHz`, `8 us`, 41-point Ramsey on r03. The next runnable project step should be an alternate Ramsey/control plan that tests the protocol and timing/phase path directly, or an alternate T2star route if one is available under the validated manifests. If no suitable alternate protocol is available, record a supported "unsupported/negative under current Ramsey conditions" conclusion for r03 T2star/13C and move project effort to the next candidate or protocol branch.
