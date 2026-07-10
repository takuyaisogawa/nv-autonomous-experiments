# Ramsey review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior Ramsey/design context: `evidence/e003.json` for the terminal 8 us det=1.0 MHz Ramsey review, `evidence/e006.json` / `evidence/e009.json` for the short-tau design/model, and `evidence/e017.md` for the short-tau start note.
- New completed measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.
- Generated local artifacts: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis.json`, `ramsey_shorttau_analysis.png`, and `analysis_run_output.txt`.

## Calculations/scripts run

- Ran `python analyze_ramsey_shorttau.py`.
- The script reads only `measurement/m001.json` and computes raw/reference statistics, per-point SEM from 12 stored averages, scan-order drift scores from `ScanOrderInfo`, linear-baseline least-squares sinusoid screens at 1.0 MHz, 0.615 MHz, 1.385 MHz, and the prior 0.884 MHz component, a dense 0.1-3.0 MHz frequency scan, FFT bins, 1000 bootstrap resamples over stored averages, and simple decaying-cosine fits.
- Readout role check came from the saved `ramsey.xml` text in `measurement/m001.json`: with `full_experiment=0`, readout 1 is the true `mS=0` reference and readout 2 is the Ramsey signal.

## Quantitative checks

- Bridge/run health: terminal result is `completed`, no stop request, no error code, safe shutdown true. Final count text was `Final = 35.122 kcps`, above the 20 kcps gate but lower than the prior 44 kcps level.
- Scan: `tau = 0.048..1.968 us`, 41 points, 48 ns step, `det=1.0 MHz`, `mw_freq=3.8759 GHz`, `12 x 90000` repetitions, `1.08e6` shots per tau point. Nyquist is 10.42 MHz; nominal span resolution is 0.521 MHz.
- Raw signal presence: reference mean/std over tau `48.573/0.456 kcps`; Ramsey signal mean/std `44.655/1.574 kcps`; signal peak-to-peak `6.50 kcps`. Median signal SEM across tau points is `1.14 kcps`; median ratio SEM is `0.0127`.
- Normalized signal: signal/reference peak-to-peak is `0.143`, well above the median ratio SEM. This is not a normalization-only feature, because the raw signal channel carries the main tau dependence.
- Drift proxy: using the snake scan order, no averages exceed the 15% drop threshold. Common-mode end-minus-start drops are about 4.5-10.8%, so drift is provenance but not a hard anomaly.
- Target-frequency screens: at the programmed 1.0 MHz carrier, LS amplitude is `1.28 kcps` raw / `0.0274` ratio with ratio residual improvement `0.355`. The largest combined frequency-screen component is near `1.19 MHz` (`0.0363` ratio amplitude, residual improvement `0.656`), not exactly the programmed carrier.
- Sideband discrimination is weak: the expected 13C-sideband targets at `0.615` and `1.385 MHz` have ratio amplitudes `0.0243` and `0.0271`, comparable to the 1.0 MHz target. The short span's `0.521 MHz` nominal resolution is larger than the expected 13C separation from the carrier (~0.385 MHz).
- Bootstrap over stored averages: top frequency in the 0.5-2.0 MHz band has median `1.195 MHz` with 16-84% range `1.181..1.213 MHz`; the programmed-carrier amplitude has median `0.0272` ratio. The top frequency falls in 0.8-1.2 MHz in only 60.2% of resamples and in 1.1-1.5 MHz in 98.6%.
- Decaying-cosine fits are not claim-grade. A fixed-1.0 MHz ratio fit gives `T2* = 0.158 us` with `0.095 us` standard error and model dependence; the free-frequency fit has a frequency uncertainty larger than the fitted frequency.

## Plausible interpretation

The new short-tau/high-SNR Ramsey run finally shows a real early-time Ramsey-like modulation on accepted r03. This is consistent with the prior failure mode that the earlier 0..8 us scans diluted or obscured short-lived early-time contrast. It supports continuing with a targeted, non-blind Ramsey diagnostic rather than abandoning r03 immediately.

The data do not yet support a precise Ramsey carrier assignment. The 1.0 MHz component is now visible, but the best empirical frequency is closer to 1.19 MHz and the short window makes the carrier and expected 13C sidebands poorly separable.

## Claims not yet supported

- No numeric `T2*` claim is supported from this measurement.
- No nearby `13C` claim is supported.
- Do not claim that the observed component follows the programmed detuning yet.
- Do not claim a refined microwave resonance from this Ramsey data; the supported frequency basis remains the prior fine weak-pi pODMR grid center at `3.8759 GHz`.

## Recommended next action

Do not run another blind long-window Ramsey repeat. Run a targeted detuning-following short-tau confirmation on the same r03, keeping the short high-SNR style but deliberately changing the programmed detuning, then check whether the early-time component moves with detuning in raw and reference-corrected views. If it follows detuning, fit a short-T2* model and then design a longer/resolution-appropriate 13C measurement. If it does not follow detuning, close the r03 Ramsey/T2*/13C branch as unsupported under this protocol or switch to an alternate protocol.
