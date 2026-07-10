# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey data and metadata: `measurement/m001.json` through `measurement/m005.json`.
- Planning/prior context used from local evidence only: especially `evidence/e014.json` for the refreshed-center Ramsey design and target frequencies, plus the prior conclusions summarized in `project/state.md`.
- Generated scratch outputs: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations Or Scripts Run

- Ran `python analyze_ramsey.py`.
- Verified raw export axis contract: `ExperimentData` shape `[2,41]`, `ExperimentDataEachAvg` shape `[20,2,41]`, and the mean over stored averages exactly reproduces the combined readouts.
- Confirmed acquisition settings: `tau = 0.048..8.048 us`, `0.200 us` step, 41 points, `20 x 50000` shots (`1.0e6` shots/tau), `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, Nyquist `2.5 MHz`, nominal resolution `125 kHz`.
- Terminal health check: completed, final counts `43.433 kcps`, no stop request, no monitor error, no safety abort.
- Computed per-point SEM over 20 stored averages: median signal SEM `0.850 kcps`, median reference SEM `0.867 kcps`, median point-wise ratio SEM `0.0116`, median fitted-reference-line-normalized SEM `0.0174`.
- Performed linear-baseline detrending and least-squares sinusoid screens from `0.25..2.35 MHz` for raw signal, point-wise ratio, and signal normalized by a fitted reference line. Also repeated the LS screen after skipping the first 4 tau points.
- Checked target fits at the programmed carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior short-tau component `1.192 MHz`, and prior det-shift top `1.623 MHz`.
- Ran FFT checks on the same views and screened per-average ratio traces for frequency consistency.
- Ran descriptive carrier-only damped-sinusoid grid fits, but did not promote them because signal presence was not supported.

## Plausible Interpretation

- The run itself is usable and has no hard anomaly. There is meaningful oscillatory structure in the data, but it is not a clean Ramsey carrier/sideband result.
- Full-span LS screens in all three views are dominated near `2.268 MHz` (`0.821 kcps` raw amplitude, `0.0168` ratio amplitude), not at the programmed `1.5 MHz` carrier or either expected 13C sideband. FFT checks similarly include strong high-frequency power (`2.317 MHz`) and split carrier-adjacent bins (`1.463/1.585 MHz`).
- The programmed carrier is present only weakly/mixed: full-span carrier amplitude is `0.713 kcps` raw, below the median signal SEM of `0.850 kcps`; point-wise ratio carrier amplitude is `0.0148`, only modestly above median ratio SEM; reference-line-normalized carrier amplitude is `0.0146`, below its median SEM.
- Skipping the first 4 tau points moves the raw and fitted-reference-line-normalized top screen near `1.52 MHz`, but the point-wise ratio top remains near `2.263 MHz`. This suggests a carrier-like component may be present after early-time structure, but it is not consistent enough across normalization views.
- Per-average frequency support is weak: only `5/20` stored-average ratio screens have their top frequency within one nominal resolution bin of the `1.5 MHz` carrier. Per-average mean signal/reference levels vary by about `7%` CV, while mean ratio is more stable, consistent with substantial common-mode drift or count variation.
- The expected sidebands are not supported. The lower sideband is near noise in all views; the upper sideband has a modest ratio amplitude but is not dominant, not raw-supported, and not consistent enough to claim 13C coupling.

## Claims Not Yet Supported

- No well-supported numeric `T2*` claim from this Ramsey data. Descriptive carrier-grid fits gave view-dependent values (`~1.4 us` raw/refline, `~3.1 us` ratio), but those fits depend on a carrier that failed the signal-presence checks.
- No supported nearby-13C conclusion from this data. The expected `1.115/1.885 MHz` sidebands are not consistently resolved above SEM or across views.
- Do not claim that the `2.268 MHz` feature is physical; it is only the strongest empirical screen component in this analysis.
- Do not claim that the refreshed pODMR center solved the previous Ramsey ambiguity. It improved a specific calibration hypothesis but did not produce claim-grade Ramsey evidence.
- Do not claim a hard negative absence of T2* or nearby 13C in the NV system; the supported statement is that the current auto-Ramsey evidence remains non-claim-grade under these conditions.

## Recommended Next Action

Stop doing blind repeats of this same long-span Ramsey branch. Treat r03 as an aligned NV with repeated non-claim-grade auto-Ramsey/T2*/13C evidence under the tested conditions, and move to a targeted diagnostic before spending more long acquisitions: either an alternate protocol/control that verifies coherent phase readout without the early-time/transient ambiguity, or a supported "T2*/13C not resolved under current Ramsey conditions" project conclusion if the objective allows closing that branch.
