# Ramsey review: r03 first T2star scout

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Ramsey run metadata/control/status: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Ramsey raw export: `measurement/m001.json`, exported from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Prior context from snapshot: `project/state.md` says r03 was the accepted aligned candidate, weak-pi pODMR grid resonance was `3.876 GHz`, and the Ramsey plan was `tau=0..6 us`, 31 points, `det=1.5 MHz`, 4 averages x 50000 repetitions.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Parsed `ExperimentData`, `ExperimentDataEachAvg`, `ExperimentDataError`, and `ScanOrderInfo` from `measurement/m001.json`.
- Confirmed run parameters: 31 tau points from `0.000..6.000 us`, `0.200 us` spacing, 4 averages, 50000 repetitions, saved in tau order with snake acquisition order recorded.
- Computed raw signal/reference medians and reference-normalized contrast.
- Fit the combined reference-normalized trace to a damped cosine with linear baseline.
- Ran an FFT on the windowed normalized contrast and checked peak locations against the programmed `1.5 MHz` detuning and the expected `~0.385 MHz` 13C separation scale recorded in project state.
- Generated `ramsey_review_plot.png` showing raw channels, normalized contrast with fit, per-average traces, and FFT.

Key numerical results:

- Terminal status: completed, no bridge error; final counts reported `38.249 kcps`.
- Counts drift relative to prior weak-pi terminal count `43.890 kcps`: about `-12.9%`.
- Raw signal median early/late: `44.538 -> 45.442 kcps` (`+2.0%`); reference median early/late: `42.308 -> 41.750 kcps` (`-1.3%`).
- Combined normalized ratio peak-to-peak: `14.7%`.
- Combined damped-cosine fit: `T2star = 2.30 +/- 1.14 us`, fitted oscillation `0.943 +/- 0.036 MHz`, `R2 = 0.446`, residual RMS `0.027` in fractional contrast units.
- Per-average fits are inconsistent:
  - avg 1: `T2star 4.94 us`, `f 0.927 MHz`, `R2 0.493`
  - avg 2: `T2star 2.86 us`, `f 1.682 MHz`, `R2 0.381`
  - avg 3: `T2star 0.19 us`, `f 0.690 MHz`, `R2 0.007`
  - avg 4: `T2star 0.21 us`, `f 0.089 MHz`, `R2 0.074`
- Strongest FFT bins in the combined normalized trace: `0.968 MHz`, `0.323 MHz`, `0.161 MHz`, `0.806 MHz`, `1.935 MHz`, `1.774 MHz`, `0.645 MHz`, `1.613 MHz`; FFT bin spacing is `0.161 MHz`.

## Plausible interpretation

- The Ramsey run completed and contains real tau-dependent contrast at the several-percent to ten-percent scale.
- The combined trace has a plausible oscillatory component, but it is not centered at the programmed `1.5 MHz` detuning; the strongest FFT bin and combined fit are near `0.94..0.97 MHz`.
- The per-average behavior is the main limitation. Averages 1 and 2 show some oscillatory structure, but averages 3 and 4 do not support the same model. This makes the combined `T2star ~2.3 us` fit descriptive only.
- The final count drop from the prior weak-pi run and the per-average disagreement suggest drift or changing readout conditions during the Ramsey acquisition may be contaminating the result.
- The FFT has bins near possible detuning/sideband scales, including `1.935 MHz`, but the dominant peak is not the programmed detuning and the 13C sideband pattern is not coherent enough to interpret.

## Claims that are not yet supported

- A well-supported T2star value is not established. The descriptive fit has broad uncertainty and poor per-average reproducibility.
- A 13C coupling conclusion is not established. The FFT does not show a stable, interpretable carrier-plus-sideband structure around `1.5 MHz` with `~0.385 MHz` separation.
- The observed `~0.94 MHz` oscillation should not yet be claimed as the true Ramsey detuning, because it may reflect drift, readout normalization artifacts, or fit/FFT instability on a short 6 us trace.
- This run does not invalidate r03 as the aligned NV; the prior pODMR evidence still supports using r03 for targeted follow-up.

## Recommended next action

Repeat a targeted Ramsey on r03 before making T2star or 13C claims, but adjust it based on this failure mode rather than blindly extending the same scan. Use a shorter, higher-SNR diagnostic Ramsey centered on the observed oscillation uncertainty: keep per-average tracking enabled, collect enough averages to check reproducibility, and choose tau spacing/span so both `~1 MHz` and the intended `1.5 MHz +/- 0.385 MHz` sideband scale are resolvable. If runtime limits allow, prefer more averages or repetitions over a much longer tau span until per-average stability is demonstrated.
