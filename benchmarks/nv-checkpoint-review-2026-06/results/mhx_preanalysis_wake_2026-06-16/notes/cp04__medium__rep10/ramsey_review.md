# Ramsey Review: r03 det-shift short-tau run

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json` for project context and the intended det-shift test.
- `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: bridge job/submit spec.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json`: terminal bridge status.
- `measurement/m005.json`: bridge control state.
- Generated local analysis products: `ramsey_review_analysis.json`, `ramsey_review_timeseries.png`, and `ramsey_review_spectrum.png`.

## Calculations or scripts run

- Used inline Python/NumPy to load the raw export and verify the raw cube orientation. `ExperimentDataEachAvg` has shape `[12, 2, 41]`, and averaging over the 12 stored averages reproduces `ExperimentData` with max absolute mismatch about `7e-15 kcps`.
- Confirmed run metadata: completed run, final counts `44.796 kcps`, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 48 ns..1.968 us`, `41` points, `48 ns` step, `12 x 90000` repetitions. Nyquist is `10.417 MHz`; FFT bin spacing is `0.508 MHz`.
- Computed raw signal, reference, point-wise `signal/reference`, and signal divided by a fitted linear reference baseline.
- Computed across-average SEM estimates: median signal SEM `0.711 kcps`, median ratio SEM `0.0126`, median reference-line-normalized SEM `0.00978`.
- Ran least-squares sinusoid screens with a constant plus linear baseline over full data and with the first 3 tau points skipped. Checked target frequencies from the project plan: programmed `1.5 MHz`, prior-plus-det-shift `1.692 MHz`, prior artifact-control `1.192 MHz`, and expected 13C sidebands `1.307/2.076 MHz`.
- Ran Hann-window FFT checks after linear detrending.
- Ran simple average-to-average common-mode and snake direction checks. Mean reference varied by `6.01 kcps`, mean signal by `7.28 kcps`, mean ratio by `0.0639`; odd/even snake-direction mean ratio differed by `0.00613`, below the median ratio SEM scale.

## Plausible interpretation

- The run completed cleanly and is analyzable. There is no stop request, bridge error, zero-average failure, or count collapse in the terminal metadata.
- The prior short-tau empirical component near `1.192 MHz` is not supported in this det-shift run: skip-first-3 target amplitudes are only `0.376 kcps` in raw signal and `0.0058` in ratio, about `0.53x` and `0.46x` the corresponding median SEM estimates.
- A component in the expected det-shift neighborhood is present but weak. In the skip-first-3 view, the best target-band frequency is near `1.647-1.649 MHz`; the planned `1.692 MHz` check gives amplitudes of `1.016 kcps` raw signal, `0.0207` ratio, and `0.0211` reference-line-normalized, or about `1.43x`, `1.64x`, and `2.16x` the median SEM estimates.
- FFT is consistent with a weak target-band feature but not decisive: in the skip-first-3 ratio FFT, the `1.645 MHz` bin is comparable to the low-frequency `0.548 MHz` bin.
- The data therefore weakly favors "the prior 1.19 MHz feature does not stay fixed" over a simple fixed-artifact explanation, but it does not establish a clean det-following Ramsey carrier. Low-frequency/baseline structure remains competitive, and per-average frequency screens are inconsistent.
- The expected 13C sideband positions are not supported: skip-first-3 ratio amplitudes at `1.307 MHz` and `2.076 MHz` are only about `0.67x` and `0.73x` median ratio SEM.

## Claims that are not yet supported

- No well-supported numeric T2star should be claimed from this run. A target-band sinusoid can be fit descriptively, but raw/readout-aware signal presence is not strong enough to promote a decay fit.
- No nearby 13C coupling should be claimed. The expected sidebands are not resolved above uncertainty or competing baseline/FFT structure.
- Do not claim that the `1.692 MHz` component is a confirmed physical Ramsey carrier. It is a plausible weak det-shift hint, not a claim-grade signal.
- Do not claim that r03 failed as an aligned NV. The pODMR evidence for r03 alignment remains the supported alignment result; the unresolved part is Ramsey/T2star/13C under these conditions.

## Recommended next action

Avoid another blind Ramsey repeat. Treat the completed det-shift run as non-claim-grade but informative: it suppresses the fixed `~1.192 MHz` artifact-control and gives only weak evidence near the predicted shifted carrier. The next decision should be a branch-level choice between an alternate protocol that can establish T2star/13C more robustly under short-coherence/weak-contrast conditions, or a supported project conclusion that Ramsey on this r03 under the tested conditions does not yield a well-supported T2star or nearby-13C result.
