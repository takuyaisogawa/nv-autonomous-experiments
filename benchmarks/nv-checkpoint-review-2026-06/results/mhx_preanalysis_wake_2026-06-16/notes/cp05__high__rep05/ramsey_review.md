# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json`.
- Job/spec/status metadata: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Local analysis artifacts created here: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed the terminal run is `nv23_ramsey_20260514_055148_auto_ramsey`, completed 2026-05-14 09:28:25 with final counts `43.433 kcps`, no stop request, and no monitor error.
- Parsed embedded `ramsey.xml` readout contract: readout 1 is the true mS=0 reference; readout 2 is the Ramsey signal for `full_experiment=0`.
- Checked acquisition: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=0.048..8.048 us`, `0.2 us` step, 41 points, `20 x 50000` shots, `1.0e6` shots/tau, nominal frequency resolution `0.125 MHz`, Nyquist `2.5 MHz`.
- Local drift/common-mode check over stored averages found no robust-z outliers (`|z|>3`) in reference, signal, or ratio. Linear total-change estimates were about `-4.4%` reference, `-5.2%` signal, and `-0.8%` ratio across averages.
- Used across-average SEM rather than stored point errors for consistency checks: median SEM was `0.850 kcps` raw signal, `0.0116` pointwise ratio, and `0.0174` reference-line-normalized signal.
- Ran least-squares sinusoid screens with intercept and linear trend on raw signal, pointwise ratio, and reference-line-normalized signal, both full-span and after skipping the first 4 tau points. Also ran simple detrended/windowed FFT checks.
- Target checks used carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, and prior-control frequencies `1.192`, `1.623`, and `0.746 MHz`.

## Plausible interpretation

- The programmed `1.5 MHz` Ramsey carrier is now visible and phase-coherent, but not dominant. In reference-line normalization, the carrier LS amplitude is `0.01447` full-span (`R2=0.297`) and `0.01049` after skipping 4 points (`R2=0.272`); per-average carrier phase coherence is high (`0.85`).
- The largest full-span LS component is instead near `2.27 MHz` in raw and normalized views, and it persists after skipping the first 4 tau points. In reference-line normalization its amplitude is `0.01678` full-span and `0.01139` skip-4, larger than the carrier.
- FFT is consistent with ambiguity rather than a clean model: normalized FFT has strong bins near `2.317 MHz`, `1.463 MHz`, `1.585 MHz`, and `2.195 MHz`.
- Fixed-frequency decay fits are descriptive only and not stable. Carrier-only exponential-grid fits give about `0.97 us` using all points and about `2.95 us` after skipping 4 points; the unmatched `2.271 MHz` component fits at least as well (`R2=0.643` full-span vs carrier `R2=0.544`).
- Expected 13C sidebands are not supported. In reference-line normalization the full-span amplitudes are `0.00299` at `1.115 MHz` and `0.00536` at `1.885 MHz`, both below the carrier and unmatched component. Per-average phase coherence is weak, especially lower sideband (`0.27`; upper `0.45`).

## Claims not yet supported

- Do not claim a numeric T2star from this Ramsey. The decay estimate depends strongly on early-point handling and on whether the unmatched `2.27 MHz` component is included.
- Do not claim nearby 13C coupling or a resolved 13C sideband pair.
- Do not identify the `2.27 MHz` feature as physical without a detuning/control test; it could be a sampling/sequence/reference artifact or mixed transient structure.
- Do not treat this run as a clean carrier/sideband model even though the programmed carrier is more visible than in prior runs.

## Recommended next action

Do not run another blind accumulation of the same 8 us Ramsey. Either close r03 as aligned but still non-claim-grade for T2star/13C under the present Ramsey protocol, or run a targeted control that changes detuning and sampling enough to test whether the `1.5 MHz` carrier and `2.27 MHz` component track the programmed detuning. A useful next Ramsey control would keep the refreshed center but use finer tau sampling and a deliberate det shift; promote T2star only if a single carrier/decay model survives raw, normalized, skip-transient, FFT/LS, and per-average phase checks.
