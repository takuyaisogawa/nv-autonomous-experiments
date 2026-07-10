# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior local context for this run: `evidence/e006.json` short-tau model/advisory, `evidence/e009.json` verified intent, `evidence/e017.md` design/start note, plus the prior det=1.0 MHz Ramsey review summarized in `project/state.md` / `evidence/e003.json`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`, producing `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Checks included raw reference/signal statistics, per-point SEM from the 12 stored averages, pointwise ratio, signal over fitted reference line, linear-baseline least-squares amplitudes at 1.000 MHz and expected 13C sidebands, a 0.2-3.0 MHz frequency screen, FFT sanity bins, per-average frequency screens, and forward/reverse snake-order comparison.
- Ran a SciPy damped-cosine fit and 120-resample average-bootstrap check, producing `ramsey_fit_bootstrap.json`.

Key quantitative results:

- Run completed: `nv23_ramsey_20260513_230331_auto_ramsey`, `tau=0.048..1.968 us` in 41 points, 48 ns step, `det=1.0 MHz`, `12 x 90000` shots per tau point, final counts `35.122 kcps`, no stop request.
- Raw signal mean `44.655 kcps`, reference mean `48.573 kcps`. Raw signal peak-to-peak is `6.50 kcps`; linear-detrended peak-to-peak is `5.25 kcps`; first `0.75 us` peak-to-peak is `5.69 kcps`. Median signal SEM is `1.14 kcps`; median ratio SEM is `0.0127`.
- Programmed 1.0 MHz carrier is present at a useful but not dominant level: raw LS amplitude `1.28 kcps` and ratio LS amplitude `0.0274`, with ratio fit improvement `R2=0.355`.
- The strongest exploratory component is higher, near `1.19 MHz`: top ratio screen `1.192 MHz`, amplitude `0.0363`, fit improvement `R2=0.656`; top raw screen near `1.187 MHz`, amplitude `1.68 kcps`.
- Expected sideband-target fits are also non-negligible but not separable here: `0.615 MHz` ratio amplitude `0.0243`, `1.385 MHz` ratio amplitude `0.0271`. The short span gives only about `0.52 MHz` nominal resolution / `0.508 MHz` FFT bin spacing, so this dataset is not a clean 13C sideband measurement.
- Free-frequency damped-cosine fits prefer roughly `1.18-1.21 MHz`. Ratio fit: `f=1.209 MHz`, `T2*=2.15 us`; raw fit: `f=1.183 MHz`, `T2*=1.78 us`. Bootstrap median `T2*=2.21 us`, but the 16-84% range is broad (`1.38..7.41 us`) and 13% of resamples ran beyond `10 us`, so the decay time is not tightly constrained.

## Plausible interpretation

- This short-tau/high-SNR run does support an early-time Ramsey oscillation on accepted r03. That is stronger than the two prior long-window Ramsey datasets, which were non-claim-grade.
- The oscillation is most naturally described as an empirical carrier near `1.2 MHz`, not as a clean programmed `1.0 MHz` carrier. A plausible explanation is a residual resonance detuning or drift of order `0.2 MHz`, but this is not proven from this dataset alone.
- The T2* scale is plausibly around a few microseconds, but the scan ends at `1.968 us`, so it constrains signal presence better than it constrains the envelope.

## Claims not yet supported

- Do not claim a final numeric T2* from this run. The fit is model-dependent and upper-tail-limited by the short span.
- Do not claim nearby 13C coupling. The expected 13C sideband spacing is smaller than the useful frequency resolution of this short scan, and the sideband-target amplitudes are not uniquely separated from the empirical carrier fit.
- Do not claim the `1.19-1.21 MHz` component is definitively a physical resonance offset without a fresh frequency check.
- Do not use this run to close the project objective as complete.

## Recommended next action

Run a fresh r03 track/fine weak-pi pODMR recenter check, because the final count is lower than the prior `44.184 kcps` state and the Ramsey carrier appears offset from the programmed detuning. If the resonance remains usable, run one non-blind longer high-SNR Ramsey that still starts after tau=0 but spans at least about `6 us` with enough points for sub-13C-splitting frequency resolution and even-average drift balancing. Use that longer trace, not this short diagnostic alone, for the final T2* fit and any 13C Fourier claim. If the longer/recentered run fails to reproduce a carrier, stop blind Ramsey repeats on r03 and move to an alternate protocol or branch closeout as unsupported under current conditions.
