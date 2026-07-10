# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior/follow-up context: `evidence/e004.json`, `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New Ramsey terminal data and bridge metadata: `measurement/m001.json` through `measurement/m005.json`.
- Generated local analysis artifacts: `ramsey_analysis.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations Or Scripts Run

- Ran `python ramsey_analysis.py`.
- Parsed `measurement/m001.json` raw savedexperiment export. The scan is `tau = 0..8 us`, 41 points, 0.2 us step, `8 x 50000` shots, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, snake order. From `evidence/e007.json`, readout1 is the `m_S=0` reference and readout2 is the Ramsey signal for `full_experiment=0`.
- Checked terminal metadata: job completed safely, final counts `44.184 kcps`, no stop request. Materialized status estimated `629.8 s` per average, above the earlier `600 s` planning cap; treat as runtime provenance for next planning, not a reason to reject the completed data.
- Computed raw/reference stats, per-average `signal/reference`, SEM across averages, and a simple scan-order common-mode drift score. No average exceeded the 0.15 drop flag; max drop score was `0.0386`.
- Performed weighted sinusoid-plus-slope least-squares checks on the mean per-average ratio at the planned frequencies:
  - `0.615423 MHz` low 13C sideband: amplitude `0.0133 +/- 0.0066`, `z = 2.02`.
  - `0.884 MHz` prior scout component: amplitude `0.00945 +/- 0.00613`, `z = 1.54`.
  - `1.000 MHz` programmed carrier: amplitude `0.00958 +/- 0.00650`, `z = 1.47`.
  - `1.384577 MHz` high 13C sideband: amplitude `0.01047 +/- 0.00665`, `z = 1.57`.
- Ran an exploratory free-frequency scan on the normalized ratio. Best component was near `1.177 MHz`, amplitude `0.0223` in ratio units, partial `R2 = 0.301`, with modest BIC improvement over slope-only (`-286.6` vs `-283.1`). Bootstrap over stored averages gave median `1.176 MHz` and 16-84% range `1.155..1.199 MHz`; `84.8%` of resamples landed within 125 kHz of `1.1775 MHz`, `0%` near `1.0 MHz` or `0.884 MHz`, `12%` near the low sideband, and `3.2%` near the high sideband.
- Tried decay-envelope fits on the normalized ratio. Exponential fits gave `T2* = 2.28 +/- 0.83 us` unweighted and `1.16 +/- 0.38 us` weighted; Gaussian fits gave `4.76 +/- 1.40 us` unweighted and `1.46 +/- 0.36 us` weighted. This spread is model-dependent.

## Plausible Interpretation

- The measurement is valid terminal Ramsey data on accepted r03 with healthy final counts and no scan-order drift flag at the simple 0.15 threshold.
- The planned `1.0 MHz` carrier is not supported at claim strength in the normalized trace. The prior non-claim-grade `~0.884 MHz` component also does not repeat.
- There is a plausible Ramsey-like normalized component near `1.18 MHz`. It is more coherent across stored-average bootstraps than the planned frequencies, but it was found exploratorily and is offset from the programmed carrier by about `0.18 MHz`. A residual microwave-frequency offset, sequence phase convention/calibration issue, or analysis/noise artifact remain plausible.
- The expected 13C sidebands near `0.615` and `1.385 MHz` are not supported. The low-sideband check is the largest planned-frequency amplitude, but it is only about `2 sigma`, not paired with the high sideband, and bootstrap support is weak.
- The data may indicate a few-microsecond dephasing scale, but the fitted `T2*` depends strongly on whether the envelope is exponential/Gaussian and on weighting. Treat this as diagnostic, not a final T2* value.

## Claims Not Yet Supported

- No well-supported numeric `T2*` claim from this run.
- No supported 13C coupling/sideband claim.
- No supported claim that the programmed `1.0 MHz` carrier is present.
- No definitive physical assignment of the exploratory `1.18 MHz` component.
- No proof that the prior `~0.884 MHz` scout component was physical or an artifact; it simply did not repeat here at useful strength.

## Recommended Next Action

Do not launch a blind higher-SNR repeat or report final T2*/13C conclusions yet. Run a cap-compliant Ramsey detuning diagnostic on the same accepted r03 branch after freshness/track checks: use a second programmed detuning separated from `1.0 MHz` (for example `det = 1.25 MHz`) with the same 8 us span but fewer points if needed to keep the per-average advisory under the active cap. Review whether the `~1.18 MHz` component shifts with the programmed detuning before fitting a T2* claim scan. If it tracks, use that result to choose the final T2* measurement conditions; if it does not, inspect sequence/readout/normalization artifacts before further Ramsey repeats.
