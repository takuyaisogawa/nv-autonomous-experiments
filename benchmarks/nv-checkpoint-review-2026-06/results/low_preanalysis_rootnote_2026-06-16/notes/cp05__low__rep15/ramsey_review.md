# Ramsey Review

## Files/Data Used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json` for project objective, prior Ramsey history, and analysis criteria.
- `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted job/config metadata.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json` and `measurement/m005.json`: final runtime status/control provenance.
- Generated local artifacts: `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.

## Calculations/Scripts Run

- Ran local Python checks on the raw export:
  - Verified data axes: `ExperimentData` shape `[1, 2, 41]`, `ExperimentDataEachAvg` shape `[1, 20, 2, 41]`, and averaging over the 20 stored averages reproduces the combined data to `1.42e-14`.
  - Used readout 1 as reference and readout 2 as Ramsey signal.
  - Built raw-signal, point-wise ratio, and fitted-reference-line normalized views.
  - Computed SEM across stored averages, least-squares sinusoid screens from `0.1..2.45 MHz`, FFT checks after linear detrending, target amplitudes at `1.5 MHz`, `1.115 MHz`, `1.885 MHz`, prior `1.192 MHz`, and prior det-shift `1.623 MHz`.
  - Repeated frequency screen after skipping the first 4 tau points.
  - Checked per-average frequency-screen consistency and simple robust drift proxies.
- Plot generation initially hit a local Tk backend issue, then succeeded with Matplotlib `Agg`.

## Plausible Interpretation

- The run completed cleanly: `auto__ramsey`, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, tau `48 ns..8.048 us` in 41 points, `20 x 50000` shots, final counts `43.433 kcps`.
- Noise/effect scale: median raw-signal SEM is `0.850 kcps`; raw signal peak-to-peak is `6.27 kcps`; median ratio SEM is `0.0116`; ratio peak-to-peak is `0.1206`.
- The strongest combined LS screen is near `2.27 MHz` in all three combined views:
  - raw signal top near `2.272 MHz`, amplitude `0.818 kcps`;
  - point-wise ratio top near `2.270 MHz`, amplitude `0.01845`;
  - fitted-reference ratio top near `2.272 MHz`, amplitude `0.01678`.
- The programmed carrier is present but not dominant:
  - raw `1.5 MHz` amplitude `0.705 kcps`, below the `2.27 MHz` top and comparable to the median raw SEM;
  - point-wise ratio `1.5 MHz` amplitude `0.01575`, below the `2.27 MHz` top but above the median ratio SEM;
  - fitted-reference ratio `1.5 MHz` amplitude `0.01447`, also below the `2.27 MHz` top.
- Expected 13C sideband targets are weak/inconsistent:
  - lower `1.115 MHz`: raw `0.146 kcps`, ratio `0.00277`, fit-ref ratio `0.00299`;
  - upper `1.885 MHz`: raw `0.261 kcps`, ratio `0.00961`, fit-ref ratio `0.00536`.
- Skipping the first 4 tau points leaves the top still near `2.26..2.27 MHz`; the `1.5 MHz` carrier remains secondary, and the sideband targets remain weak.
- Per-average screens are not cleanly repeatable: coarse raw top-frequency bins scatter across low frequency, `~1.5 MHz`, `~2.1..2.4 MHz`, and other bins; ratio tops are likewise mixed. This argues against promoting the combined `2.27 MHz` or `1.5 MHz` component as a stable physical Ramsey carrier without additional support.
- Simple robust drift proxies did not flag any stored average at `|z| > 3.5`, but average means varied substantially (`signal 37.38..50.37 kcps`, reference `41.74..54.90 kcps`), so common-mode/baseline variation remains relevant provenance.
- A descriptive damped-sinusoid fit finds a combined component near `2.28 MHz` with fitted decay `~1.8 us` raw / `~2.6 us` ratio, but this follows the non-target dominant component and is not claim-grade.

## Claims Not Yet Supported

- No supported numeric `T2*` claim from this run. The fit-derived decay constants are descriptive only because the signal model is not established by raw/readout-aware carrier evidence.
- No supported nearby `13C` conclusion. The expected `1.115/1.885 MHz` sidebands are not consistently strong or repeatable across views and averages.
- No supported claim that the `2.27 MHz` feature is the physical Ramsey carrier. It is the strongest combined screen component, but it is not the programmed detuning and lacks per-average consistency.
- No supported claim that simply accumulating more identical Ramsey averages will resolve the issue; this run already used `1.0e6` shots per tau point and still produced a mixed frequency picture.

## Recommended Next Action

Do not run another blind Ramsey repeat under the same conditions. Treat the accepted r03 alignment and refreshed pODMR center as still valid, but close the current Ramsey branch as non-claim-grade under these conditions. The next useful action is a targeted alternate protocol or diagnostic that changes the information channel, preferably a Hahn/CPMG-style baseline (`auto__cpmg`, `N = 1`) to establish a robust coherence envelope before returning to 13C spectroscopy.
