# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` run control.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified array contract before analysis: `ExperimentData` shape `[1,2,41]`; `ExperimentDataEachAvg` shape `[1,20,2,41]`; averaging over the stored-average axis reproduces `ExperimentData`.
- Used the sequence text in the raw export to assign readout roles: readout 1 is the true `mS=0` reference; with `full_experiment=0`, readout 2 is the Ramsey signal.
- Built the tau axis from metadata: `48 ns..8.048 us`, `41` points, `200 ns` step; Nyquist about `2.5 MHz`, FFT bin spacing about `122 kHz`.
- Checked terminal/run health: completed, final counts `43.433 kcps`, safe shutdown true, not aborted, no stop request, monitor `last_error` empty.
- Computed raw signal, point-wise signal/reference, and signal/reference-line views; SEM across `20` stored averages; FFT bins; dense least-squares frequency screens with intercept and linear baseline; target amplitudes at carrier and expected 13C sidebands.
- Used the project working model for target checks: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `B~359.46 G`, `13C Larmor~384.8 kHz`, expected sidebands near `1.115 MHz` and `1.885 MHz`.
- Ran stored-average bootstrap resampling (`n=1000`) and skip-transient checks after skipping `0,1,2,3,4,5,8` initial tau points.

## Plausible interpretation

- The run is technically usable: terminal metadata show no hard acquisition anomaly, and the tau/readout axes are internally consistent.
- There is carrier-region Ramsey-like power, but it is not clean claim-grade. In the raw signal, the dense LS screen found the top component near `2.269 MHz` with amplitude `0.827 kcps`; the programmed carrier region was second near `1.516 MHz` with amplitude `0.744 kcps`. The raw carrier target amplitude at exactly `1.5 MHz` was `0.729 kcps`, while the median per-point raw-signal SEM was `0.850 kcps`.
- The fitted-reference-line normalized view behaves similarly: top near `2.269 MHz` with amplitude `0.01697`; carrier-region near `1.516 MHz` with amplitude `0.01526`; exact `1.5 MHz` target amplitude `0.01494`, compared with median normalized SEM `0.01741`.
- Bootstrap over stored averages favored `2.27 MHz` as the top component more often than the carrier region: about `78%` of normalized resamples had top frequency within `+/-80 kHz` of `2.269 MHz`, versus about `22%` within `+/-80 kHz` of `1.5 MHz`. Raw bootstrap was similar (`75%` vs `24%`).
- Skip-transient checks did not remove the `2.27 MHz` feature; after skipping up to 8 early points, the top in all three combined views remained around `2.27 MHz`, with a weaker but persistent carrier target amplitude.
- The expected first 13C sidebands are weak and not symmetric: in the fitted-reference-line view, lower sideband amplitude near `1.115 MHz` was `0.00323`, upper sideband near `1.885 MHz` was `0.00572`, both far below the carrier-region/top amplitudes and with low LS `R2`.
- A descriptive fixed-carrier damped fit returns `T2star ~1.53 us` with raw amplitude `2.59 kcps` and `R2 ~0.47`, but this should be treated only as a descriptive shape check because the carrier/sideband model is not otherwise cleanly supported.

## Claims that are not yet supported

- No well-supported numeric `T2star` claim from this run. The fixed-carrier damped fit is not enough because signal presence/model assignment remains ambiguous.
- No supported nearby `13C` claim. The expected `det +/- f13C` sidebands are weak, not dominant, and not a consistent sideband pattern.
- Do not assign the `2.269 MHz` component to a physical 13C feature from this evidence alone. It is close to `det + 2*f13C` under the working model, but the project target model expected first sidebands at `1.115/1.885 MHz`; this requires an explicit follow-up model/control before interpretation.
- Do not claim that the old `~1.192 MHz` empirical feature is the Ramsey carrier or a 13C feature; it is weak in this long-span run.
- Do not claim sub-grid or sub-100-kHz precision for the pODMR-derived microwave center; the project already marked `3.8765 GHz` as grid-supported with several-100-kHz uncertainty.

## Recommended next action

Stop blind repeats of the same Ramsey branch. Record this refreshed-center 1e6-shot Ramsey as technically valid but still non-claim-grade for both `T2star` and `13C`. The next scientific action should be a deliberate branch decision: either move to an alternate protocol/control designed to separate carrier, artifacts, and 13C structure, or close the r03 Ramsey/13C objective under current conditions as unsupported/negative. If continuing experimentally, prioritize a model-driven control rather than more averaging of the same `det=1.5 MHz`, `8 us` Ramsey scan.
