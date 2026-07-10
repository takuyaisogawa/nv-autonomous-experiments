# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`, and relevant Ramsey/readout guidance from `md/knowledge.md`.
- Prior r03 evidence: `evidence/e003.json` for weak-pi pODMR support of `mw_freq = 3.876 GHz`; `evidence/e005.json` for the Ramsey protocol/model; `evidence/e008.json` for the submitted Ramsey intent.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` submitted job spec; `measurement/m003.json` terminal result; `measurement/m004.json` terminal status; `measurement/m005.json` control state.
- Generated local artifacts: `ramsey_analysis.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python ramsey_analysis.py`.
- Parsed readout1 as reference and readout2 as Ramsey signal, following the project protocol inspection for `full_experiment=0`.
- Computed raw readout means, pointwise `signal/reference`, per-average summaries, acquisition-order drift checks, fixed-frequency sinusoid fits at the programmed `det = 1.5 MHz`, free sinusoid scans from `0.2..2.45 MHz`, FFT amplitudes, and a 500-resample bootstrap over the four stored averages.

Key numbers:

- Ramsey completed: run `1DExp-seq-ramsey-vary-tau-2026-05-13-185521`, `tau = 0..6 us`, `31` points, `0.2 us` step, `4 x 50000` repetitions.
- Final count was `38.249 kcps`, down from the recent `43.5..43.9 kcps` context by about `12..13%`, but not a count-collapse failure.
- Mean readouts: reference `45.318 kcps`, signal `42.098 kcps`; mean normalized ratio `0.93055`. Median SEM was `1.015 kcps` for signal and `0.02557` for normalized ratio.
- Programmed-carrier check on normalized ratio at `1.5 MHz`: amplitude `0.00568`, `R2 = 0.026`, delta AIC `+3.53` versus a linear baseline. The raw-signal fixed-det amplitude was only `0.133 kcps`, far below the signal SEM scale.
- Free sinusoid scan on normalized ratio prefers about `0.95 MHz`: amplitude `0.0241`, `R2 = 0.269`, delta AIC `-5.36`; bootstrap over averages gives best-frequency 5/50/95% quantiles `0.86/0.94/1.68 MHz`, so the frequency is not stable.
- Per-average normalized best frequencies disagree: about `0.92`, `1.66`, `1.30`, and `0.86 MHz`.
- From the project model, `B ~ 359.3 G` gives `13C Larmor ~0.3846 MHz`; expected sidebands for actual `det = 1.5 MHz` are near `1.115` and `1.885 MHz`. The high-sideband FFT bin is visible in the normalized trace, but the programmed carrier is weak and the reference readout has a strong feature near the same high-sideband bin, so this is not assignable to 13C.

## Plausible interpretation

This is a completed, valid, analyzable Ramsey scout on accepted r03, but it is non-claim-grade. There is some oscillatory structure in the signal/reference trace near `0.9..1.0 MHz`, comparable to the ratio SEM scale, and it may reflect a Ramsey-like component with residual frequency offset or imperfect centering. However, the designed `1.5 MHz` Ramsey carrier is not supported, the individual averages do not share a stable frequency/phase, and reference/readout drift is non-negligible.

The r03 pODMR-based alignment/resonance evidence remains usable project context. This Ramsey result does not by itself invalidate r03, but it also does not provide a reliable T2* or 13C conclusion.

## Claims not yet supported

- No numeric T2* value is supported from this scout.
- No 13C coupling or 13C absence claim is supported.
- The apparent `~0.95 MHz` structure is not yet a confirmed physical Ramsey frequency.
- A resonance shift, detuning-sign issue, or sequence phase-convention issue is plausible but not established by this data alone.
- A hardware/count failure claim is not supported; the run completed and final counts stayed well above the configured `20 kcps` minimum.

## Recommended next action

Do not run a blind same-parameter T2* repeat or record a T2*/13C result from this scout. First perform a bounded frequency-centering follow-up on r03, preferably a fine weak-pi pODMR around the `3.876 GHz` grid minimum or an equivalent short Ramsey carrier-centering diagnostic. If that supports an adjusted center, repeat Ramsey with the corrected frequency and more stored averages rather than longer per-average repetitions, while preserving FFT coverage for `det +/- ~0.385 MHz` sidebands under the tracking-window cap.
