# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus Ramsey/interpretation guardrails from `md/memory.md` and `md/knowledge.md`.
- New measurement: `measurement/m001.json` raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Run provenance: `measurement/m002.json` requested `auto__ramsey`, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 48 ns..8.048 us`, 41 points, 20 x 50000 shots; `measurement/m003.json` completed result; `measurement/m004.json` terminal status; `measurement/m005.json` control state.
- Generated local artifacts: `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.

## Calculations/scripts run

- Used Python/NumPy to inspect raw array shapes and metadata. `ExperimentDataEachAvg` is `[scan, avg, readout, point]`; the combined data are `[scan, readout, point]`.
- Treated readout 0 as raw Ramsey signal and readout 1 as reference. Checked raw signal, signal/reference ratio, and signal normalized by a fitted reference line.
- Ran least-squares sinusoid screens versus frequency, explicit target fits at 1.5 MHz carrier, expected 13C sidebands 1.115/1.885 MHz, old 1.192 MHz control, and prior det-shift 1.623 MHz feature.
- Ran guardrail checks excluding the 2.5 MHz Nyquist edge and skipping early tau points; also computed Hann-window FFT top bins.
- Saved a diagnostic plot of raw channels, fitted-reference normalization, and LS amplitude spectrum.

## Quantitative checks

- Measurement shape: 41 tau points from 0.048 to 8.048 us with 0.2 us spacing, Nyquist frequency about 2.5 MHz, 20 averages, 50000 reps/average.
- Terminal/run health: job completed, `stop_requested = false`, no bridge error message; status monitor reported empty `last_error`.
- Raw signal mean is 48.79 kcps; reference mean is 44.67 kcps. Raw signal peak-to-peak across tau is 2.07 kcps; median per-point signal SEM across averages is 0.87 kcps.
- The unconstrained LS screen peaks at 2.4995 MHz in normalized and raw views. Because this is at the Nyquist edge, it is not good physical evidence.
- With the Nyquist edge excluded, the strongest full-span exploratory component is near 0.807 MHz with normalized amplitude 0.00686 and raw-signal amplitude 0.307 kcps. Skipping 4 or 8 early tau points keeps the top near 0.8 MHz, not near the programmed carrier.
- Programmed 1.5 MHz carrier is weak: normalized LS amplitude 0.00220; raw-signal amplitude 0.099 kcps, well below the median raw signal SEM.
- Expected 13C sidebands are not a clean pair. The 1.115 MHz lower sideband is very weak: normalized amplitude 0.00038, raw 0.018 kcps. The 1.885 MHz upper target is larger but still modest: normalized amplitude 0.00520, raw 0.232 kcps, and it is not accompanied by a matching lower sideband or clear carrier.
- The previous 1.192 MHz control feature remains weak in this run: normalized amplitude 0.00196, raw 0.087 kcps.
- Descriptive damped-sinusoid fits can return finite T2star-like numbers, but the results depend on seed/target frequency and the carrier is not established, so these fits should not be promoted.

## Plausible interpretation

- The refreshed-center long-span Ramsey completed cleanly and is analyzable, but it does not provide claim-grade Ramsey evidence.
- The result argues against a simple, stable programmed-carrier Ramsey oscillation at 1.5 MHz under these conditions. Accumulating to 20 averages did not make the intended carrier dominant.
- The exploratory spectral content is dominated either by a Nyquist-edge artifact candidate or, after excluding that edge, by a broad/weak component near 0.8 MHz. That behavior is not aligned with the programmed 1.5 MHz carrier or the expected 13C sideband pattern at 1.115/1.885 MHz.
- The single larger upper-sideband-region response near 1.885 MHz is insufficient by itself because the carrier and lower sideband are weak and the FFT/LS views are not mutually clean.

## Claims not yet supported

- No supported numeric T2star for r03 from this run.
- No supported nearby 13C conclusion from this run.
- No supported claim that the 2.5 MHz edge peak is a physical Ramsey frequency.
- No supported claim that the weak 1.885 MHz response is a 13C sideband.
- No supported claim that more identical long-span Ramsey averaging will solve the issue.

## Recommended next action

Stop doing blind repeats of the same Ramsey branch. Use this as a supported non-claim-grade/negative Ramsey result under the current r03 conditions, then choose a targeted alternate protocol or diagnostic before spending more hardware time. The next best experimental action is a protocol change that directly tests whether the problem is Ramsey contrast/initial transient/readout normalization rather than averaging: for example a short calibrated Ramsey phase/carrier diagnostic or an echo-based T2 / decoupling route after confirming the current weak-pi pODMR center and tracking.
