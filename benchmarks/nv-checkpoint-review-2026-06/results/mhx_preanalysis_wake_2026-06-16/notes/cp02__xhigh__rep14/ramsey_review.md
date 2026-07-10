# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior context/evidence: `evidence/e006.md` and `evidence/e004.json` for the fine weak-pi pODMR center at 3.8759 GHz; `evidence/e007.json` and `evidence/e013.md` for the second Ramsey model/advisory and expected checks.
- New Ramsey terminal data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` run status, and `measurement/m005.json` control state.
- Generated local artifacts: `scratch_ramsey_analysis.py`, `ramsey_analysis_summary.json`, and `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python scratch_ramsey_analysis.py`.
- Parsed `measurement/m001.json`: Ramsey scan was `tau = 0..8 us`, 41 points, 0.2 us step, 8 averages x 50000 repetitions, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`; terminal result reports final counts `44.184 kcps`.
- Used the protocol context from `evidence/e007.json`: readout 1 is reference and readout 2 is Ramsey signal for `full_experiment=0`.
- Checked exact-frequency least-squares amplitudes after a linear baseline at:
  - expected low 13C sideband: `0.615423 MHz`
  - prior unexplained component: `0.884 MHz`
  - programmed carrier: `1.000 MHz`
  - expected high 13C sideband: `1.384577 MHz`
- Checked ordinary FFT/Hann FFT peaks, per-average complex amplitude coherence, average-to-average count variation, and a simple scan-order common-mode edge drift check.

## Quantitative findings

- The programmed `1.0 MHz` carrier is weak in the combined raw signal: exact fit amplitude `0.277 kcps`, explaining only `2.45%` of linearly detrended signal variance. Excluding the high-leverage `tau=0` point reduces this to `0.152 kcps` and `1.10%`.
- The expected low sideband at `0.615423 MHz` is the strongest target-frequency fit, especially excluding `tau=0`: amplitude `0.522 kcps`, explaining `13.0%` of linearly detrended raw-signal variance. This is still small relative to the reported signal error scale in the raw export (`~1.87 kcps`) and far below the pre-measurement expected raw oscillation scale of order `2-6 kcps`.
- The high sideband at `1.384577 MHz` is not supported: excluding `tau=0`, exact fit amplitude is `0.098 kcps` and explains `0.47%` of variance.
- The prior `~0.884 MHz` feature does not persist as a coherent combined raw-signal feature: excluding `tau=0`, exact fit amplitude is `0.055 kcps` and explains `0.15%` of variance.
- FFT peaks are broad/inconsistent with a clean target assignment. Combined raw signal with Hann window peaks at about `1.220`, `1.098`, `0.488`, `0.122`, and `0.610 MHz`; the target carrier and sideband checks are not an isolated, symmetric Ramsey/13C pattern.
- Stored averages disagree in baseline/count level: average signal means span `36.20..50.27 kcps` and reference means span `40.47..55.53 kcps`. The simple scan-order common-mode edge check ranges from `-5.4%` to `+10.1%`, below a 15% drift flag threshold but large enough to make sub-kcps spectral features fragile.

## Plausible interpretation

The second Ramsey completed cleanly and is analyzable, but it still does not provide claim-grade Ramsey evidence. The det-shift diagnostic weakens the idea that the first scout's `~0.884 MHz` feature was a stable physical carrier, because that component is nearly absent after excluding `tau=0`. However, the new run also does not show a clean carrier following the programmed `1.0 MHz` detuning. The only moderately suggestive feature is near the expected lower 13C sideband, but without a supported carrier, without the high sideband, and with average/baseline instability, it is not enough to claim a nearby 13C.

## Claims not yet supported

- No supported numeric `T2*` value from this run.
- No supported nearby `13C` conclusion from this run.
- No supported assignment of the observed FFT structure to a physical Ramsey carrier or hyperfine sideband pattern.
- No support for treating the earlier `~0.884 MHz` scout component as a stable physical feature.

## Recommended next action

Do not blindly repeat the same Ramsey. First run a focused Ramsey-frequency/control diagnostic on the same accepted r03 branch: use the fine-pODMR center, keep the same tau span/shot budget if counts remain healthy, but compare at least two programmed detunings or a near-zero-detuning control so the Ramsey phase response can be tested directly in time domain. If a carrier that tracks the programmed detuning is recovered, then take a higher-SNR T2* run and only then fit T2* / revisit 13C sideband claims. If the carrier still fails to track detuning, return to calibration/sequence-readout validation before more T2* acquisition.
