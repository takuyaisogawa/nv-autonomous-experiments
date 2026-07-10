# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior Ramsey/design context: `evidence/e003.json` (terminal det=1.0 MHz, 8 us Ramsey review), `evidence/e006.json` and `evidence/e009.json` (short-tau/high-SNR model and intent), `evidence/e017.md` (design/start note).
- New terminal measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` bridge result, `measurement/m004.json` final status, `measurement/m005.json` control.
- Scratch artifacts created here: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis.json`, `ramsey_shorttau_trace.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey_shorttau.py`.
- The script parsed the terminal raw export; used readout1 as the `m_S=0` reference and readout2 as Ramsey signal per the project protocol note for `ramsey.xml` with `full_experiment=0`.
- It computed raw/ratio statistics, per-point SEM across 12 stored averages, fixed-frequency least-squares screens at 0.615422875 MHz, 1.0 MHz, 1.178 MHz, and 1.384577125 MHz, a 0.2-3.0 MHz grid screen, linear-detrended FFT bins, per-average shape correlations, and a scan-order residual drift check.
- Verified the PNG artifact programmatically because the local image viewer hit an access error: `1280x1440` RGBA, nonblank pixel std `39.82`.

Key quantitative results:

- Run completed as `nv23_ramsey_20260513_230331_auto_ramsey`, final status `completed`, no stop request, monitor `last_error=""`, final count `35.122 kcps`.
- Measurement settings: `tau=0.048..1.968 us`, `41` points, `48 ns` step, `det=1.0 MHz`, `mw_freq=3.8759 GHz`, `12 x 90000 = 1.08e6` shots per tau point.
- Sampling limits: nominal resolution about `0.521 MHz`, Nyquist about `10.42 MHz`; this is an early-time diagnostic, not a high-resolution 13C spectrum.
- Raw signal readout: mean `44.655 kcps`, peak-to-peak `6.499 kcps`, median per-point SEM `1.138 kcps`.
- Pointwise ratio: mean `0.91946`, peak-to-peak `0.14327`, median per-point SEM `0.01271`.
- The average-to-average common-mode level moved substantially: reference mean range `42.02..55.19 kcps`, signal mean range `37.47..51.21 kcps`, ratio mean range `0.8935..0.9561`.
- All 12 stored-average detrended ratio traces positively correlated with the combined detrended shape; median correlation `0.627`.
- Scan-order residual drift scratch check: max absolute residual end-start fraction was about `11.0%` for signal, `9.2%` for reference, and `3.6%` for ratio. This is drift provenance, not a count-collapse or abort.
- Fixed-frequency ratio least squares with linear baseline:
  - low 13C target `0.615 MHz`: amplitude `0.02428`, R2 improvement `0.311`.
  - programmed carrier `1.000 MHz`: amplitude `0.02741`, R2 improvement `0.355`.
  - prior 8 us top component `1.178 MHz`: amplitude `0.03617`, R2 improvement `0.654`.
  - high 13C target `1.385 MHz`: amplitude `0.02715`, R2 improvement `0.345`.
- Best ratio grid component was near `1.192 MHz` with amplitude `0.03631` and R2 improvement `0.656`; this is close to the prior 8 us screen's `~1.178 MHz` component but should not be quoted as a precision frequency because the span is short and baseline covariance is significant.

## Plausible interpretation

- The short-tau/high-SNR run likely did reveal a real early-time Ramsey-like oscillatory signal on r03. The effect is larger than the per-point SEM in both raw signal and ratio, and the combined shape is not carried by a single stored average.
- The signal is not yet a clean programmed-carrier result. The `1.0 MHz` component is now visible, unlike the prior 8 us run, but the strongest least-squares component remains closer to `~1.18-1.19 MHz`, similar to the previous long-window screen.
- A plausible working hypothesis is that the effective Ramsey phase/frequency basis is offset from the fine-pODMR basis by roughly the observed excess frequency, or that the baseline/short-window shape is biasing the frequency screen. The sign and physical cause are not determined from this data alone.
- The short span explains why sideband assignment is weak: the `0.615`, `1.0`, and `1.385 MHz` target fits are not well separated at `~0.52 MHz` nominal resolution.

## Claims not yet supported

- No numeric T2star is supported. The short window tests early-time signal visibility but does not constrain a decay envelope well enough to promote a T2star fit.
- No nearby-13C conclusion is supported. The sideband targets are not uniquely resolved or dominant.
- Do not claim the precise oscillation frequency is `1.192 MHz`; treat it as an exploratory short-window component near `1.18-1.19 MHz`.
- Do not claim the fine pODMR center is wrong, or assign the offset sign, without a targeted frequency-basis check.
- Do not treat the run as hardware-failed: it completed with usable data and counts above the configured gate, though common-mode drift/count motion should be recorded as provenance.

## Recommended next action

Do not run another blind long-window Ramsey repeat. First reconcile the Ramsey frequency basis on r03 with a targeted diagnostic, such as a short-tau/high-SNR Ramsey at one or two altered programmed detunings or microwave-frequency offsets, chosen so that a real det-following carrier can be distinguished from a fixed artifact/baseline component. After the carrier basis is established, run a longer high-quality Ramsey only if it is needed to extract T2star and 13C sidebands; otherwise close the r03 Ramsey/13C branch as unsupported under current conditions.
