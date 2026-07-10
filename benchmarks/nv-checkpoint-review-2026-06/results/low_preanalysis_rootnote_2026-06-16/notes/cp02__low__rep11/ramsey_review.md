# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective and current context.
- `evidence/e006.md`, `evidence/e013.md`: fine weak-pi pODMR review and second Ramsey start note.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940`.
- `measurement/m003.json`: terminal bridge result for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- `measurement/m004.json`, `measurement/m005.json`: terminal status/control for the same run.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`; output written to `ramsey_analysis_summary.json`.
- Parsed raw export arrays directly:
  - `tau = 0..8 us`, 41 points, `dt = 0.2 us`.
  - FFT Nyquist `2.5 MHz`; bin spacing `0.12195 MHz`.
  - 8 averages x 50000 repetitions; terminal final counts `44.184 kcps`.
  - Trace 0 treated as the 0-level reference and trace 1 as the Ramsey readout, consistent with `ramsey.xml` and `full_experiment=0`.
- Checked raw signal and signal/reference normalization:
  - mean signal `44.580 kcps`, mean reference `49.313 kcps`.
  - combined signal/reference mean `0.9042`, range `0.8025..0.9721`, peak-to-peak `0.1696`.
  - normalized linear slope only `7.24e-4 per us` on the combined trace, but individual averages have noticeable mean/slope variation.
- FFT and least-squares frequency checks on detrended signal/reference:
  - strongest combined normalized FFT bins: `1.098 MHz` amplitude `0.0211`, `1.220 MHz` amplitude `0.0188`, `0.976 MHz` amplitude `0.0133`.
  - planned carrier check at `1.0 MHz`: nearest FFT bin `0.976 MHz`, FFT amplitude `0.0133`, LS amplitude `0.00913`, residual RMS `0.0282`.
  - expected 13C sideband checks: `0.615 MHz` bin amplitude `0.00759`, LS amplitude `0.0108`; `1.385 MHz` bin amplitude `0.00660`, LS amplitude `0.00842`.
  - prior scout component check at `0.884 MHz`: nearest bin `0.854 MHz`, FFT amplitude `0.00660`, LS amplitude `0.00738`.
  - exploratory damped-cosine fit on normalized combined trace: frequency `1.187 MHz`, T2* `2.27 us`, fit amplitude `0.071`, RMS residual `0.0208`, but this is not claim-grade because per-average spectral peaks disagree.
- Per-average consistency check:
  - per-average top normalized FFT peaks are split across `2.317, 2.317, 1.098, 0.488, 1.220, 0.610, 1.463, 0.488 MHz`.
  - per-average 1 MHz LS amplitudes vary from `0.00338` to `0.02297` ratio units.
  - per-average ratio means span `0.8909..0.9258`, indicating average-to-average baseline/contrast variation.

## Plausible interpretation

- The completed Ramsey run is analyzable and likely contains some oscillatory content near the intended detuned Ramsey carrier region: the combined normalized spectrum clusters near `~1.1-1.2 MHz`, and the exploratory fit returns `~1.19 MHz` with a few-us envelope.
- The earlier non-claim-grade `~0.884 MHz` component did not remain dominant after changing the programmed detuning to `1.0 MHz`; it is weaker than the main combined bins in this run. That argues against treating the previous `0.884 MHz` peak as a stable physical feature.
- The data do not cleanly support the exact programmed `1.0 MHz` carrier: the strongest combined FFT bin is `1.098 MHz`, not the `0.976 MHz` bin nearest 1.0 MHz, and the fitted frequency is higher still.
- The expected 13C sideband positions near `0.615/1.385 MHz` are present only as weak components comparable to other non-target bins and are not consistently recovered across averages.

## Claims that are not yet supported

- Do not claim a final T2*. The exploratory `T2* ~2.3 us` fit is useful for planning, but average-to-average inconsistency and carrier mismatch make it insufficient as a project conclusion.
- Do not claim resolved nearby 13C coupling. The target sidebands are weak and not uniquely distinguished from noise/baseline structure.
- Do not claim that the microwave center is wrong based only on this Ramsey fit. The fine pODMR still supports `3.8759 GHz` as the grid-supported resonance; this Ramsey run shows detuned-fringe ambiguity, not an independent resonance calibration.
- Do not claim the prior `~0.884 MHz` feature as physical. It did not persist as the dominant feature under the detuning-shift test.

## Recommended next action

- Do not proceed to a T2*/13C claim from this dataset alone. Run one targeted validation measurement before deciding whether to close the branch:
  - repeat Ramsey at the same `mw_freq = 3.8759 GHz` with a deliberately different detuning, preferably `0.7 MHz` or `1.3 MHz`, over `0..8 us` with the same or higher shots, so the carrier-shift test can distinguish true programmed-detuning response from fixed artifacts/baseline structure;
  - after acquisition, require per-average agreement of the dominant normalized FFT/LS component before fitting T2* or assessing 13C sidebands.
- If a repeat remains inconsistent across averages, pivot away from longer Ramsey repeats and treat r03 as aligned but not yet supporting a T2*/13C conclusion under this route.
