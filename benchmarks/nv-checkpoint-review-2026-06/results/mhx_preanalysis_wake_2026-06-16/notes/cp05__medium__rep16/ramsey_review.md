# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`.
- New Ramsey data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Run provenance: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Planning/context evidence: `evidence/e014.json` and `evidence/e022.json` for refreshed-center det=1.5 MHz, expected sidebands, and shot plan.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` as readout1 reference and readout2 Ramsey signal, with `ExperimentDataEachAvg` shape `[20, 2, 41]`.
- Confirmed scan: tau `0.048..8.048 us`, step `0.2 us`, span `8.0 us`, 41 points, 20 averages x 50000 repetitions = `1.0e6` shots/tau, Nyquist `2.5 MHz`, nominal resolution `0.125 MHz`.
- Checked terminal health: result/status completed, final counts `43.433 kcps`, `stop_requested=false`, monitor `last_error=""`, safety not aborted.
- Built raw-signal, point-wise ratio, and fitted-reference-line ratio views.
- Ran least-squares sinusoid screens over `0.2..2.4 MHz`, both full span and skipping first 4 tau points.
- Checked target amplitudes at carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior artifact-control `1.192 MHz`, and prior det-shift top `1.623 MHz`.
- Ran a discrete FFT check after linear detrending. Leading bins in the normalized views were around `1.463/1.585 MHz` and `2.195/2.317 MHz`; the target carrier is visible but not uniquely dominant.
- Estimated per-point SEM across stored averages: raw signal median `0.850 kcps`, point-wise ratio median `0.0116`, fitted-reference-line ratio median `0.0174`.
- Scan-order-aware drift proxy using snake acquisition order found no hard drift anomaly: median ratio second-half minus first-half `0.0011`, max absolute `0.0281`.

## Plausible interpretation

- This is a usable completed Ramsey dataset, but it is still non-claim-grade for T2star and 13C.
- The refreshed pODMR center did improve the appearance of a carrier-like component near the programmed detuning: fitted-reference-line ratio LS amplitude at `1.5 MHz` is `0.0145` full span and `0.0105` after skipping the first four tau points; raw-signal amplitude is `0.705 kcps` full span and `0.512 kcps` after skip4.
- Those carrier amplitudes are at or below the per-point SEM scale and far below the earlier expected order-`2..6 kcps` raw oscillation scale, so they are not strong enough to promote a quantitative T2star fit.
- The largest dense LS component is near `2.27 MHz` in raw and fitted-reference-line views, not at the carrier or either expected 13C sideband. FFT bins also show comparable power near `2.2..2.3 MHz`.
- Expected 13C sidebands are weak/inconsistent: fitted-reference-line amplitudes are `0.0030` at `1.115 MHz` and `0.0054` at `1.885 MHz` full span, falling to `0.00024` and `0.00255` after skip4.
- Stored-average screens remain mixed; per-average top frequencies span most of the search band rather than clustering at the programmed carrier or sidebands.
- The most plausible reading is that r03 has weak carrier-like Ramsey structure under the refreshed-center det=1.5 MHz condition, but the dominant spectral content is still a mixture of noise, readout/baseline structure, and/or sequence/transient artifacts. The refreshed-center long-span run does not rescue the Ramsey/T2star/13C claim.

## Claims not yet supported

- No numeric T2star is supported from this dataset.
- No nearby 13C coupling or resolved 13C sideband conclusion is supported.
- The `~2.27 MHz` feature should not be claimed as physical without a targeted detuning/control test.
- The visible `1.5 MHz` carrier-like component should not be promoted to a fitted decay parameter because amplitude and per-average consistency are insufficient.
- The prior accepted alignment of r03 remains supported by pODMR context, but this Ramsey dataset alone does not strengthen the alignment claim.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the refreshed-center long-span Ramsey branch as still unsupported for T2star/13C under the current route. The next project action should be a decision point: either switch to a targeted control/alternate protocol that tests the Ramsey sequence and the recurring off-target spectral content, or close this r03 Ramsey branch with a supported "no well-supported T2star or 13C conclusion under current conditions" result.
