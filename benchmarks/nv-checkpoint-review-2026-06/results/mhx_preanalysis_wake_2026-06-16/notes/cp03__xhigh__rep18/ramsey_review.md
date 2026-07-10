# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` bridge result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior context for comparison: `evidence/e003.json` terminal review of the previous det=1.0 MHz, 0..8 us Ramsey; `evidence/e006.json` short-tau diagnostic design/model; `evidence/e017.md` start note.

## Calculations or scripts run

- Added and ran `python analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis_plot.png` (PNG verified as 1760 x 1280 RGBA; direct viewer access failed locally).
- Checks performed:
  - Parsed raw readouts as project-established Ramsey roles: readout 1 reference, readout 2 signal.
  - Verified acquisition shape: tau = 0.048..1.968 us, 41 points, 48 ns step, 12 averages x 90000 repetitions = 1.08e6 shots/tau.
  - Checked bridge metadata: job completed, no stop request, monitor last_error empty, final count text `Final = 35.122 kcps`.
  - Computed combined raw signal/reference, point-wise ratio, signal/reference-line normalization, per-point SEM across averages, and per-average means.
  - Ran corrected scan-order-aware within-average drift check using `ScanOrderInfo.order_each_avg`; flagged averages = [].
  - Ran least-squares sinusoid screens with linear baseline at the programmed carrier, expected 13C sidebands, prior scout component, and the prior 8 us top component.
  - Ran per-average vector/phase checks for target components.
  - Tried diagnostic Ramsey decay fits under multiple baseline and tau-window choices; fit results were used only to test robustness, not promoted.

## Plausible interpretation

- This short-tau/high-SNR run changes the evidence state: it shows a reproducible early-time Ramsey-like oscillatory component in the signal/ratio views, not just reference noise.
- The programmed 1.0 MHz carrier is visible but not dominant: raw-signal LS amplitude `1.282 kcps`, ratio amplitude `0.0274`, signal/reference-line amplitude `0.0264`; median point SEM is `1.138 kcps` raw signal and `0.0127` ratio. Per-average vector averaging is phase-coherent at 1.0 MHz (raw vector amplitude `1.282 kcps`; ratio vector amplitude `0.0272`).
- The strongest combined screen is still near the earlier det=1.0 MHz top feature, not exactly at the programmed carrier: ratio top `1.192 MHz` with amplitude `0.0363`, raw-signal top `1.187 MHz` with amplitude `1.68 kcps`. This is stronger than the prior 8 us run (`1.178 MHz`, ratio amplitude `0.0225`; 1.0 MHz carrier only `0.00916` ratio / `0.277 kcps` raw).
- The reference channel alone has much smaller target-frequency amplitudes (for 1.0 MHz, `0.213 kcps` raw reference), so the main feature is not explained as a reference-only artifact.
- Average-to-average brightness moves substantially, including lower late averages, but signal/reference ratio means are tighter and the corrected within-average scan-order drift screen flags no averages. Treat common-mode brightness drift as provenance, not a hard invalidation.
- A reasonable working hypothesis is: r03 has an early-time Ramsey response under this protocol, with an apparent carrier-like component around 1.0..1.2 MHz. The offset of the strongest component from 1.0 MHz could reflect small resonance detuning, baseline/window effects, or protocol/systematic phase behavior; the current data do not distinguish these cleanly.

## Claims not yet supported

- No numeric T2star is supported. Diagnostic fits are model-dependent: all-tau raw signal gives T2* about `0.19 us` with fixed 1 MHz + linear baseline, about `2.31 us` with fixed 1 MHz + quadratic baseline, and about `1.78 us` with free frequency + linear baseline; dropping the first four points drives some fits to the `20 us` upper bound while another gives about `0.97 us`.
- Do not claim the precise carrier frequency is `1.192 MHz`; the tau span is only `1.92 us`, baseline choice matters, and the strongest component does not by itself establish the physical detuning.
- Do not claim nearby 13C coupling. The expected sidebands (`0.615 MHz`, `1.385 MHz`) are present only at amplitudes comparable to other components (`0.0243` and `0.0271` ratio) and are not a resolved sideband pattern around a supported carrier.
- Do not claim absence of nearby 13C. The carrier/baseline model is still unsettled, so this Ramsey evidence only says a nearby-13C signature is not supported under the present analysis.
- Do not use this run to revise the fine-pODMR resonance center or assert microwave-frequency drift without a direct recalibration/check.

## Recommended next action

Do not run another blind Ramsey repeat or promote a T2star fit from this dataset. The next useful action is a targeted frequency/calibration follow-up: first re-check the r03 weak-pi/fine-pODMR center near `3.8759 GHz`, then, only if the center and counts remain usable, run a matched short-tau det-following Ramsey diagnostic with changed programmed det to test whether the `~1.19 MHz` feature moves as a Ramsey carrier. If it does not move with det or the recalibration does not explain the offset, stop Ramsey repeats on r03 and switch to an alternate T2/13C protocol or close the r03 Ramsey/13C branch as unsupported under current conditions.
