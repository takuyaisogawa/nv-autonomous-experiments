# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus prior notes in `evidence/e004.json`, `evidence/e006.md`, `evidence/e007.json`, and `evidence/e013.md`.
- New Ramsey measurement files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final status, and `measurement/m005.json` control state.
- The run reviewed here is `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`, saved as `1DExp-seq-ramsey-vary-tau-2026-05-13-204940`.

## Calculations/scripts run

- Created and ran `ramsey_analysis.py`; it writes `ramsey_analysis_summary.json`, `ramsey_traces.png`, and `ramsey_spectra.png`.
- Confirmed terminal metadata: completed, not aborted, safe shutdown ok, final counts `44.184 kcps`.
- Confirmed scan: `ramsey.xml`, `tau = 0..8 us`, `41` points, `dt = 0.2 us`, `8 x 50000` shots, snake scan order. Nyquist is `2.5 MHz`; span resolution is `125 kHz` and FFT bin spacing is `121.95 kHz`.
- Readout statistics from the combined raw export:
  - Readout1/reference mean `49.31 kcps`, std `0.87 kcps`.
  - Readout2/Ramsey signal mean `44.58 kcps`, std `1.34 kcps`.
  - Point-wise signal/reference ratio mean `0.9042`, std `0.0294`.
  - The `tau=0` point is notably low: signal `39.31 kcps`, ratio `0.8025`.
- Ran linear-baseline least-squares sinusoid screens on raw signal, point-wise signal/reference, and signal/reference-line normalization at:
  - expected low 13C sideband `0.615423 MHz`,
  - prior exploratory feature `0.884 MHz`,
  - programmed carrier `1.000 MHz`,
  - expected high 13C sideband `1.384577 MHz`.
- For point-wise signal/reference, the targeted amplitudes are weak: `0.0111` at `0.615 MHz` (`1.67 sigma`, `R2=0.074`), `0.0092` at `1.000 MHz` (`1.39 sigma`, `R2=0.053`), `0.0084` at `1.385 MHz` (`1.28 sigma`, `R2=0.046`), and `0.0074` at `0.884 MHz` (`1.10 sigma`, `R2=0.035`).
- Free-frequency scans are not mutually consistent. The point-ratio trace fits best near `1.178 MHz` (`R2=0.308`), while raw signal and reference-line normalization fit best near `0.466 MHz`. Windowed FFT peaks for point-ratio are at `1.098` and `1.220 MHz`, not cleanly at the expected `1.000 MHz` carrier.
- Per-average point-ratio free-fit maxima scatter strongly: `[0.265, 1.635, 0.455, 0.420, 1.165, 0.635, 2.040, 1.415] MHz`.
- Simple scan-order end/start drift check flagged no averages at a 15% drop threshold, but per-average brightness varies substantially: reference means span `40.47..55.53 kcps`, signal means span `36.20..50.27 kcps`, and ratio means span `0.891..0.926`.

## Plausible interpretation

The measurement completed cleanly and is usable for analysis. The earlier pODMR context still supports r03 as the aligned candidate and `3.8759 GHz` as the working microwave frequency. This Ramsey dataset, however, does not show a reproducible detuned Ramsey carrier at the programmed `1.0 MHz`, nor a stable pair of 13C sidebands at `0.615/1.385 MHz`.

There is weak oscillatory structure, including a low `tau=0` point and a normalized free-fit feature around `1.18 MHz`, but the apparent frequency depends on normalization and is not reproduced across averages. The data therefore look more like non-claim-grade Ramsey contrast plus normalization/drift/sequence-response ambiguity than a supported T2star/13C result.

The prior non-claim-grade `~0.884 MHz` feature is not strongly reproduced here, but this run does not by itself prove that feature was an artifact.

## Claims not yet supported

- No supported T2star value: the carrier/envelope gate fails, so a damped-cosine fit would be fit-driven rather than evidence-driven.
- No supported 13C coupling conclusion: the expected sidebands are weak, not paired robustly, and not reproducible across averages.
- No claim that the Ramsey phase ramp is behaving exactly as modeled: the dominant normalized feature is offset from `1.0 MHz`, and raw/refline views prefer a different frequency.
- No sub-grid resonance precision beyond the prior grid-supported `3.8759 GHz` pODMR basis.

## Recommended next action

Do not blindly repeat the same long Ramsey. Run a short Ramsey phase-ramp/frequency-response control on r03 first, using the same `mw_freq = 3.8759 GHz` but two programmed detunings or opposite detuning signs if supported by the sequence. The pass criterion should be that the dominant normalized peak shifts by the programmed detuning difference and that per-average phases/frequencies are consistent. If that control passes, then rerun a longer T2star/13C Ramsey with the validated detuning response; if it fails, inspect the Ramsey/IQ det implementation or switch to an alternate validated Ramsey route before making T2star or 13C claims.
