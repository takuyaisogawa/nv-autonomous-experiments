# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used
- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior Ramsey context: `evidence/e003.json` for the completed det=1.0 MHz, 0..8 us Ramsey review; `evidence/e006.json`, `evidence/e007.json`, and `evidence/e017.md` for the short-tau diagnostic design/start rationale.
- New terminal measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job/spec, `measurement/m003.json` result, `measurement/m004.json` status, and `measurement/m005.json` control.

## Calculations or scripts run
- Inspected local schemas with PowerShell/Python and searched project context with `rg`.
- Wrote and ran `python scratch_ramsey_analysis.py`.
- Script outputs: `ramsey_shorttau_analysis.json` and `ramsey_shorttau_analysis.png` (PNG header/dimensions verified with PIL: 1200 x 1200).
- Analysis used the project/prior-review channel convention for `ramsey.xml` with `full_experiment=0`: trace 1 is the mS=0 reference and trace 2 is the Ramsey signal.
- Quantitative checks included raw signal/reference summaries, per-average SEM, common-mode drift flags, forward/reverse scan-order splits, FFT bin spacing, and least-squares tone screens after a linear baseline at 1.000 MHz, 0.615423 MHz, 1.384577 MHz, and the prior long-window top component near 1.178 MHz.

## Plausible interpretation
- The run completed safely: `nv23_ramsey_20260513_230331_auto_ramsey`, final counts `35.122 kcps`, no stop request, empty monitor error, `12 x 90000` repetitions, `41` tau points from `0.048` to `1.968 us` at `48 ns` spacing, `mw_freq=3.8759 GHz`, `det=1.0 MHz`.
- Raw reference was relatively flat over tau (`48.573 kcps` mean, `0.456 kcps` std over tau). Raw Ramsey signal had a strong baseline/trend component (`44.655 kcps` mean, start `40.698 kcps`, end `43.501 kcps`, linear slope `0.966 kcps/us`) and median per-point SEM across averages of `1.138 kcps`.
- A residual oscillatory component near `1.18-1.19 MHz` is present in the short-tau data after linear-baseline removal: combined raw-signal top screen `1.187 MHz`, amplitude `1.682 kcps`, residual-R2 improvement `0.681`; ratio top screen `1.192 MHz`, amplitude `0.0363`.
- The `~1.18 MHz` component is not only due to the one low-brightness average: excluding average 11 still gives a top near `1.184-1.186 MHz` with `1.73 kcps` raw-signal amplitude. It also appears in scan-direction splits: forward averages top near `1.190 MHz`, reverse averages top near `1.185 MHz`.
- The programmed `1.0 MHz` carrier is present but weaker/less explanatory than the `~1.18 MHz` component: raw-signal amplitude `1.282 kcps`, residual-R2 improvement `0.377`. This is only about `1.1x` the median per-point SEM and is not a clean carrier basis for a T2* fit.
- Common-mode brightness drift is non-negligible: per-average common mean ranged from `39.745` to `53.200 kcps` around median `46.857 kcps`; average 11 exceeded a `15%` common-mode deviation flag. The feature survives removing that average, but this remains important provenance.
- The most plausible read is: the short-tau/high-SNR run reveals a reproducible early-time Ramsey-like residual near `1.18 MHz`, consistent with either an unresolved frequency/detuning mismatch or a stable sequence/readout artifact. It does not yet establish the physical carrier frequency or decay envelope.

## Claims not yet supported
- No numeric T2* is supported from this dataset. The window spans only `1.92 us`, has only about two cycles near 1 MHz, has a strong baseline/trend, and the dominant residual is offset from the programmed carrier.
- No nearby-13C conclusion is supported. The expected det +/- 13C sideband targets (`0.615423` and `1.384577 MHz`) are not a dominant or paired sideband pattern; their raw-signal amplitudes (`1.102` and `1.222 kcps`) are comparable to the programmed-carrier screen and below the `~1.18 MHz` component. FFT resolution is coarse (`0.508 MHz` bin spacing; `0.521 MHz` nominal 1/span), so the short window is not a claim-grade sideband measurement.
- The data do not support a precise resonance offset or sign. The `~1.18 MHz` residual may imply a detuning mismatch, but this has not been tested by changing programmed detuning or mw frequency under the same short-tau/high-SNR conditions.
- The run does not challenge the earlier pODMR-supported r03 alignment conclusion; it only updates the Ramsey/T2*/13C branch.

## Recommended next action
- Do not fit/promote T2* or claim 13C from this run.
- Run one targeted detuning/frequency-discrimination Ramsey check under the same short-tau/high-SNR conditions, not a blind repeat. The check should determine whether the `~1.18 MHz` residual follows the programmed Ramsey detuning or a small mw-frequency shift. If it follows predictably, use that calibrated carrier in a later envelope-quality T2* measurement; if it does not, close the r03 Ramsey/13C branch as unsupported under current conditions or switch protocols.
