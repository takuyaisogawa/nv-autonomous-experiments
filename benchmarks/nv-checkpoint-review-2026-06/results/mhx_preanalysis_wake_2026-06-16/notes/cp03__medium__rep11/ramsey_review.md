# Ramsey Review

## Files/Data Used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json` for project objective, prior decisions, and analysis posture.
- `evidence/e017.md` for the short-tau Ramsey design/start note.
- `measurement/m001.json` terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- `measurement/m002.json` bridge job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` run control.
- Generated scratch artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_shorttau_review.png`.

## Calculations Or Scripts Run

- Ran `python analyze_ramsey.py`.
- Parsed two readouts as reference/readout 1 and signal/readout 2.
- Reconstructed `tau = 48 ns..1.968 us`, 41 points, 48 ns spacing, `12 x 90000` repetitions, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Computed raw signal, point-wise signal/reference ratio, and signal normalized to a linear fit of the reference channel.
- Computed per-point SEM across 12 stored averages: median raw-signal SEM `1.138 kcps`, ratio SEM `0.0127`, reference-line-normalized SEM `0.0108`.
- Ran least-squares sinusoid screens with intercept and linear baseline at expected frequencies:
  - Raw signal amplitudes: `0.615 MHz = 1.252 +/- 0.232 kcps`, `1.000 MHz = 1.375 +/- 0.240 kcps`, `1.385 MHz = 1.127 +/- 0.261 kcps`.
  - Ratio amplitudes: `0.0236`, `0.0234`, `0.0247` respectively.
  - Reference-line-normalized amplitudes: `0.0235`, `0.0231`, `0.0246` respectively.
- Ran dense Lomb-Scargle screens from `0.2..5.0 MHz` after linear detrending:
  - Raw signal maximum near `1.184 MHz`.
  - Ratio maximum near `1.192 MHz`.
  - Reference-line-normalized maximum near `1.186 MHz`.
- Checked stored-average phase coherence for raw target fits:
  - Phase resultant `R = 0.881` at `0.615 MHz`, `0.933` at `1.000 MHz`, `0.925` at `1.385 MHz`.
- Ran a constrained 1 MHz decayed-cosine fit on raw signal as a diagnostic only: `T2star = 0.192 +/- 0.135 us`, amplitude `-9.96 +/- 8.29 kcps`, reduced chi2 `0.827`; this is not claim-grade because the amplitude/T2star are poorly constrained.
- Drift proxy from stored-average means shows large common-mode variation: signal average mean range `30.8%`, reference average mean range `27.1%`, with negative average-index slopes in both channels.

## Plausible Interpretation

- The short-tau/high-SNR data is not blank. It contains a coherent oscillatory component visible in raw signal and in both normalized views, with per-average phases broadly aligned.
- The strongest blind frequency screen is consistently near `1.18..1.19 MHz`, matching the earlier second-Ramsey terminal screen near `1.178 MHz` more than the programmed `1.000 MHz` carrier or the expected `0.615/1.385 MHz` 13C sidebands.
- Because the short scan spans only `1.92 us`, frequency discrimination is intrinsically coarse. Target fits at `0.615`, `1.000`, and `1.385 MHz` are not independent enough to assign the feature cleanly.
- The recurring `~1.18 MHz` feature could reflect a Ramsey detuning/frequency-calibration offset, an analysis/protocol artifact, or a real NV response under these conditions. The current data support further targeted diagnosis, not a final assignment.
- The final count `35.122 kcps` is lower than recent r03 runs but above the configured minimum; the reference and signal channels move together strongly across averages, so common-mode drift/provenance is important even though it does not by itself invalidate the oscillatory evidence.

## Claims Not Yet Supported

- No claim-grade numeric `T2star` is supported. The diagnostic decayed-cosine fit gives a very short value but is poorly constrained and frequency-assignment-dependent.
- No nearby `13C` conclusion is supported. The data do not isolate symmetric sidebands at the expected `0.615/1.385 MHz` positions.
- A clean programmed-carrier Ramsey model at exactly `1.000 MHz` is not supported; the blind maximum remains displaced near `1.18..1.19 MHz`.
- The data do not support treating the fine pODMR grid center as sub-grid-accurate.
- The large stored-average common-mode variation means normalized-view amplitudes should not be promoted without raw-readout agreement and follow-up.

## Recommended Next Action

Do not run another blind Ramsey repeat. Run a targeted detuning/frequency diagnostic: either refresh the weak-pi pODMR center around `3.8759 GHz` with enough resolution to test a `~0.18 MHz` offset, or run a small Ramsey det-scan / mw-frequency-offset check to see whether the observed `~1.18 MHz` component follows programmed detuning as ordinary Ramsey physics predicts. Use that result to decide whether a claim-grade T2star scan is warranted; defer 13C work until the carrier model is clean.
