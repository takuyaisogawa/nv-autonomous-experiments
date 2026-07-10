# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: objective and current project state.
- `context.json`: checkpoint context and recent evidence summaries.
- `evidence/e014.json`: planned refreshed-center Ramsey targets: carrier `1.500 MHz`, expected 13C sidebands `1.115 MHz` and `1.885 MHz`.
- `measurement/m001.json`: terminal raw export for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m002.json`: submitted recipe/metadata.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: completion/status/control provenance.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_review_plot.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `measurement/m001.json` as a 41-point tau scan from `0.048..8.048 us` with `dt=0.200 us`, `20` averages x `50000` repetitions, `mw_freq=3.8765 GHz`, `det=1.5 MHz`.
- Treated readout channel 0 as reference and channel 1 as Ramsey signal, consistent with the local plan.
- Checked raw signal, point-wise `signal/reference`, and `signal/fitted_reference_line`.
- Computed median point SEM across averages, per-average top frequency consistency, linear-baseline sinusoid least-squares frequency screens from `0.1..2.45 MHz`, FFT-bin peaks after linear detrending, and target amplitudes at `1.115`, `1.500`, `1.885`, and `1.192 MHz`.
- Rechecked target amplitudes after skipping the first 4 tau points.

Key numbers:

- Completion: job completed without bridge error; final-count text in `m003` is `43.433 kcps`; stop was not requested.
- Means: reference `48.789 kcps`, Ramsey signal `44.670 kcps`, point ratio `0.915627`.
- Signal range: `40.569..46.838 kcps`; median raw point SEM `0.850 kcps`.
- Per-average signal means are broad: median `44.588 kcps`, MAD `2.134 kcps`, range `37.377..50.371 kcps`.
- Raw LS screen: top `2.271 MHz` at `0.818 kcps`; carrier-near top `1.515 MHz` at `0.723 kcps`; programmed `1.500 MHz` amplitude `0.705 kcps`, only `0.83x` median raw point SEM.
- Point-ratio LS screen: top `2.270 MHz` at `0.01845`; `1.516 MHz` at `0.01623`; programmed carrier amplitude `0.01575`, `1.36x` median point-ratio SEM.
- Fitted-reference-line normalization: top `2.271 MHz` at `0.01678`; `1.515 MHz` at `0.01482`; programmed carrier amplitude `0.01447`, only `0.83x` median line-normalized SEM.
- 13C target amplitudes are not a coherent pair: line-normalized low/high sidebands are `0.00299` and `0.00536`, both below the carrier and not consistently dominant.
- Prior `1.192 MHz` feature is weak in this run: line-normalized amplitude `0.00226`.
- Per-average top frequencies are mixed: near `1.5 MHz` in only `1/20` raw or line-normalized averages and `4/20` point-ratio averages.
- Skipping the first 4 tau points reduces the line-normalized carrier amplitude to `0.01049` and the 13C sidebands to `0.00024` / `0.00255`.

## Plausible interpretation

This run is analyzable and adds useful evidence that the old fixed `~1.192 MHz` feature should not be promoted: the `1.192 MHz` target is weak here, while the combined average has a weak carrier-like component near the programmed `1.5 MHz` detuning.

However, the carrier-like response is small relative to measured point scatter, is not the strongest spectral component, weakens when early tau points are skipped, and is not reproduced consistently across stored averages. The 13C sideband targets are weaker and not a matched, repeatable carrier-plus-sideband pattern. The data therefore support only a weak/non-claim-grade Ramsey response at the refreshed center, not a reliable T2star or nearby-13C conclusion.

## Claims not yet supported

- A numerical T2star for r03 is not supported by this dataset.
- A nearby 13C coupling/sideband claim is not supported.
- The `2.27 MHz` screen maximum is not supported as a physical feature without additional controls.
- The refreshed pODMR center alone did not produce a claim-grade long-span Ramsey decay.
- More averaging of the same protocol is not justified as the next default step; this run already used `1.0e6` shots per tau point and the limiting issue is consistency/model support, not just total counts.

## Recommended next action

Do not promote T2star or 13C claims from this run. If continuing r03, change protocol rather than repeating the same long Ramsey: run a carrier-validation Ramsey control with phase cycling/quadrature readout if available, preceded by a brief pi/2/Rabi sanity check, and require per-average carrier consistency before fitting T2star or searching sidebands. If that control is not available or also fails, close r03 under current conditions with a supported "T2star/13C not established" conclusion.
