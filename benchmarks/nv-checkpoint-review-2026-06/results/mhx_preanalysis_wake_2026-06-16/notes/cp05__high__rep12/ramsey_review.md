# Ramsey Review

## Files/data used

- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted Ramsey job spec for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: completion/status/control metadata.
- `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`: project context and prior measurement interpretation.
- Generated scratch outputs: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed raw Ramsey arrays: 41 tau points from 48 ns to 8.048 us in 200 ns steps, 20 averages, 50000 repetitions per average, two readouts per tau.
- Checked completion metadata: run status `completed`, final counts `43.433 kcps`, no stop request, no bridge error, safe shutdown ok.
- Computed signal/reference ratio, per-point SEM from the 20 stored averages, readout common-mode drift, full-span and skip-first-4-point frequency screens, windowed FFT checks, and least-squares amplitudes at planned frequencies.
- Planned target frequencies from the run context: carrier `1.500 MHz`, lower 13C sideband `1.1152 MHz`, upper 13C sideband `1.8848 MHz`; prior artifact-control frequency `1.192 MHz`.

## Quantitative checks

- Combined readouts: reference mean `48.789 kcps`, signal mean `44.670 kcps`, ratio mean `0.9156`.
- Ratio peak-to-peak is `0.1206`; median per-point ratio SEM across averages is `0.0116`; linear-detrended ratio RMS is `0.0220`.
- Readout levels vary across stored averages: signal fractional span `29.1%`, reference fractional span `27.0%`, but ratio fractional span is smaller at `7.44%`; first-to-second half ratio mean changes only `-0.11%`. This looks mostly common-mode, not a hard count-failure signature.
- Full-span ratio LS screen top is near `2.270 MHz` with amplitude `0.01845` and residual-RMS ratio `0.01789` (`amp/resid ~1.03`).
- Planned carrier at `1.500 MHz`: ratio LS amplitude `0.01573`, residual RMS `0.01900` (`amp/resid ~0.83`); raw-signal amplitude `0.705 kcps`, residual RMS `0.861 kcps`.
- Planned sidebands are weaker: lower `1.1152 MHz` ratio amplitude `0.00277`; upper `1.8848 MHz` ratio amplitude `0.00962`.
- Skip-first-4 tau points does not rescue the target model: carrier ratio amplitude `0.01224`, lower sideband `0.00067`, upper sideband `0.00525`; top remains near `2.2665 MHz`.
- Windowed FFT ratio bins are mixed: `1.463 MHz`, `1.585 MHz`, `2.317 MHz`, and `2.195 MHz` are all comparable. FFT bin spacing is `121.95 kHz`, Nyquist `2.5 MHz`.
- Scan-order split is not fully stable: forward averages top near `2.281 MHz`, reverse averages top near `1.517 MHz`; carrier amplitude is `0.0132` forward and `0.0192` reverse.
- Per-average top frequencies are scattered (`~0.355` to `2.341 MHz`), with several averages near the carrier but no consistent carrier/sideband pattern.
- A constrained carrier+13C-sideband ratio model has sideband amplitudes too small to support a 13C claim and is not preferred by AIC over a simpler single-frequency descriptive model.

## Plausible interpretation

The measurement completed cleanly and contains analyzable Ramsey-like oscillatory structure. The refreshed pODMR center did improve the context for a detuned Ramsey follow-up, and the planned `1.5 MHz` carrier is present at a nonzero descriptive amplitude. However, it is not the dominant or stable component across the full quantitative checks. The strongest full-span screen is near `2.27 MHz`, close enough to the high-frequency side of the 2.5 MHz Nyquist limit to treat cautiously, and the FFT, skip-first-points, scan-order split, and per-average screens do not converge on the planned carrier plus 13C sidebands.

This is therefore useful negative/diagnostic evidence: the run does not support promoting a T2star or nearby 13C conclusion yet. It also argues that simply increasing shots at the same 8 us Ramsey settings may not solve the ambiguity without an additional control that separates true detuning response from scan-order/high-frequency artifacts.

## Claims not yet supported

- No supported T2star value from this dataset.
- No supported nearby 13C coupling claim from this dataset.
- No claim that the strongest `~2.27 MHz` screen component is physical; it is not a planned target and is near the high-frequency guardrail.
- No claim of a clean carrier-only Ramsey model; the `1.5 MHz` component is descriptive but not robust across views.
- No claim that the pODMR center is wrong; the current result is ambiguous Ramsey frequency content, not a refutation of the refreshed pODMR calibration.

## Recommended next action

Run a targeted short-span detuning-control Ramsey rather than another long 8 us repeat: keep the same accepted r03 target and refreshed pODMR basis, but use a shorter tau span with higher sampling density and two deliberate detunings in separate runs, e.g. `det=1.0 MHz` and `det=2.0 MHz` with otherwise matched settings and enough averages for scan-order split checks. A physical Ramsey carrier should move with the programmed detuning; a fixed high-frequency/scan-order artifact should not. Only attempt T2star/13C fitting after that detuning-tracking check produces a stable carrier in combined, skip-early, forward/reverse, and per-average views.
