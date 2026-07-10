# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- Local guidance/context: `md/memory.md`, `md/knowledge.md`.
- Prior Ramsey plan/model: `evidence/e005.json`.
- New completed Ramsey artifacts:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
  - `measurement/m002.json`: submitted Ramsey job.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`, `measurement/m005.json`: final status/control provenance.
- Scratch outputs created here: `ramsey_analysis.py`, `ramsey_analysis_summary.json`, `ramsey_trace.png`, `ramsey_fft.png`.

## Calculations or scripts run

- Ran `python ramsey_analysis.py`.
- Confirmed the raw export is complete: Ramsey run `nv23_ramsey_20260513_185505_auto_ramsey` completed from `2026-05-13T18:55:17` to `2026-05-13T19:30:40`; terminal result reports `incomplete = false` and final counts `38.249 kcps`.
- Confirmed measurement settings from saved `Variable_values` and job metadata: `tau = 0..6 us`, 31 points, `0.2 us` step, `4 x 50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `full_experiment = 0`.
- Used the locally recorded readout-role basis: readout 1 is reference, readout 2 is Ramsey signal for this `full_experiment=0` path.
- Checked count/tracking provenance:
  - Aggregate reference mean `45.318 kcps`; aggregate Ramsey signal mean `42.098 kcps`.
  - Median aggregate per-point error scale is `1.88 kcps` reference and `1.82 kcps` signal.
  - Per-average common brightness varies about `-4.1%` to `+2.3%` around the median.
  - Saved scan position `[117.279, 117.294, 115.535] um` is about `0.612 um` from the earlier fresh tracked coordinate in the job metadata.
  - Final counts are about `12%` below the earlier `43.535 kcps` fresh-track value.
- Computed reference-normalized traces using both point-wise `signal/reference` and `signal/fitted-reference-line`.
- Ran line-detrended Hann FFT checks. With 31 inclusive points at `0.2 us`, `np.rfft` bin spacing is `161.3 kHz`; span-based resolution is `166.7 kHz`; Nyquist is `2.5 MHz`.
- Checked expected FFT features from the project model:
  - Programmed carrier: `1.500 MHz`.
  - Expected 13C sidebands for the project model: `1.115 MHz` and `1.885 MHz`.
  - The nearest carrier bin (`1.452 MHz`) is weaker than the median FFT amplitude in raw signal and normalized traces.
  - The lower expected sideband bin near `1.129 MHz` is only a modest peak; the upper sideband near `1.935 MHz` is not comparably supported. The sideband pattern is not symmetric or dominant.
- Ran diagnostic linear baseline plus sinusoid fits:
  - Fixed `1.5 MHz` sinusoid worsens BIC versus a linear baseline by about `+6.7` for raw signal and reference-line-normalized signal.
  - A free-frequency sinusoid gives a modest best component near `0.96 MHz`, with amplitude about `1.08 kcps` raw or `0.0238` normalized, and BIC improvement about `-3.7` versus a linear baseline.
  - Leave-one-out aggregate checks keep a best free frequency around `0.94..1.05 MHz`, but per-average fits are not uniformly supportive. Average 1 carries the strongest support; other averages are weak or conflicting.
- Ran diagnostic decaying-cosine fits on the reference-line-normalized trace. They returned about `2.1 us` exponential-envelope T2 and `3.2 us` Gaussian-envelope T2 at about `0.96 MHz`, but these fits are not claim-grade because the underlying Ramsey component is weak and not consistently supported.

## Plausible interpretation

- The Ramsey measurement completed successfully and is analyzable; it is not a hardware/no-data failure.
- The dataset is non-claim-grade for T2star and 13C. The programmed `1.5 MHz` Ramsey carrier is not supported by the aggregate fit or FFT. A weak Ramsey-like feature near `0.96 MHz` is plausible, and could reflect residual resonance offset/drift relative to the weak-pODMR grid center, but it is small compared with the pointwise noise scale and not cleanly repeated across all stored averages.
- The final-count drop, sub-micron saved-position shift, and per-average brightness changes are drift/focus provenance. They do not invalidate the run, but they make over-interpreting a weak fit especially risky.
- The FFT does not support a nearby 13C assignment. Peaks near expected sideband locations are comparable to other FFT features and do not form a consistent carrier-plus-sidebands pattern.

## Claims that are not yet supported

- A numeric T2star for r03 is not supported by this Ramsey scout.
- A nearby 13C conclusion is not supported.
- The diagnostic `~2-3 us` decay-fit values should not be promoted to project findings.
- The `~0.96 MHz` feature should not yet be treated as a confirmed Ramsey carrier or precise resonance offset.
- The data also do not support a strong negative claim that r03 has no 13C coupling; the scout is limited by SNR/drift and carrier uncertainty.

## Recommended next action

Fresh-track r03, verify counts, then do a targeted frequency/Ramsey follow-up rather than a blind repeat. A good next step is a finer weak-pi pODMR or short Ramsey frequency diagnostic around the current `3.876 GHz` basis to determine whether the resonance has shifted enough to explain the provisional `~0.96 MHz` Ramsey component. After that, repeat Ramsey with the same or slightly longer tau span only if the advisory tracking window is acceptable; preserve or increase total shots by using more tracked averages and/or split acquisitions rather than extending the untracked per-average window. Keep the FFT sideband check in the plan, but do not claim T2star or 13C until a clean carrier and reproducible decay are present.
