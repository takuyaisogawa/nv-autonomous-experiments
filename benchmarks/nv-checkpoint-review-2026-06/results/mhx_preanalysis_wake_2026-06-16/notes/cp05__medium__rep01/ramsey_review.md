# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective, accepted r03 context, prior Ramsey outcomes, and required terminal review checks.
- `evidence/e014.json`: model/design note for the refreshed-center Ramsey; target frequencies were carrier `1.5 MHz`, expected 13C sidebands `1.115193 MHz` and `1.884807 MHz`, with prior controls near `1.623 MHz`, `0.746 MHz`, and `1.192 MHz`.
- `evidence/e001.json`: weak-pi pODMR refresh supporting `mw_freq = 3.8765 GHz` and expected 13C Larmor `384.8065 kHz`.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: job spec/result/status/control for `nv23_ramsey_20260514_055148_auto_ramsey`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`; outputs are `ramsey_analysis.json` and `ramsey_analysis.png`.
- Confirmed array contract: `ExperimentDataEachAvg` shape is `[scan, avg, readout, point]`; averaging the 20 per-average traces reproduces `ExperimentData` with max absolute difference `1.42e-14`.
- Run summary: completed normally, no stop request, final counts `43.433 kcps`, `tau = 48 ns..8.048 us`, `41` points, `20 x 50000` shots, `det = 1.5 MHz`, `mw_freq = 3.8765 GHz`.
- Noise check: median signal SEM across averages `0.850 kcps` per tau point; median raw signal `44.804 kcps`, median reference `48.881 kcps`.
- Drift check from local scan-order reconstruction: no averages exceeded a `15%` common-mode drop flag.
- Frequency screens used linear-baseline plus sinusoid least-squares over `0.25..2.40 MHz`, full span and skip-first-4-tau views, for raw signal, point-wise ratio, and reference-line-normalized signal.
- Main raw-signal results:
  - full-span LS top: `2.271 MHz`, amplitude `0.818 kcps`;
  - skip-first-4 LS top: `2.271 MHz`, amplitude `0.555 kcps`;
  - carrier `1.5 MHz`: `0.705 kcps` full span, `0.512 kcps` skip-first-4;
  - expected low 13C sideband `1.115 MHz`: `0.145 kcps` full, `0.012 kcps` skip-first-4;
  - expected high 13C sideband `1.885 MHz`: `0.261 kcps` full, `0.124 kcps` skip-first-4.
- Normalized views tell the same qualitative story:
  - point-wise ratio carrier amplitude `0.0157` full, `0.0123` skip-first-4; top near `2.27 MHz`;
  - reference-line-normalized carrier amplitude `0.0145` full, `0.0105` skip-first-4; top near `2.27 MHz`.
- FFT check after linear detrending:
  - raw full-span top in the searched band was near `2.317 MHz`;
  - raw skip-first-4 top was near `1.486 MHz`, close to the programmed carrier, but this was not the dominant LS result.
- Per-average LS tops were mixed rather than locked to one frequency; full-span per-average tops ranged across about `0.34..2.40 MHz`, with only a few near the carrier.
- A descriptive carrier-locked damped-sinusoid grid fit preferred `T2star ~1.02 us`, but this is not promoted because signal presence/shape is not clean enough.

## Plausible interpretation

- The new high-shot refreshed-center Ramsey is analyzable and healthy as an acquisition.
- There is weak carrier-like evidence at the programmed `1.5 MHz`: it appears in raw and both normalized views, remains after skipping the first four points, and is near the FFT top in the skip-transient raw view.
- The carrier is still small relative to the measurement context: raw carrier amplitude is `0.51..0.71 kcps`, below the median per-point SEM (`0.85 kcps`) and below the model-plan expected raw scale of roughly `1..1.7 kcps` from earlier det-shift/short-tau evidence.
- The strongest exploratory LS feature is instead near `2.27 MHz`, which is not the programmed carrier or the expected 13C sideband pair. Because this feature is also stronger in normalized views, it should be treated as an empirical component or possible artifact/control target, not a physical assignment.
- Expected 13C sidebands at `1.115` and `1.885 MHz` are weak and degrade strongly in skip-transient views. This does not support a nearby-13C claim.
- The result slightly improves confidence that the refreshed center can produce a weak det-tracking Ramsey component, but it does not produce a clean decay envelope or consistent carrier/sideband model.

## Claims that are not yet supported

- No numeric T2star claim is supported from this dataset. The descriptive `~1 us` carrier-locked fit is a fit result only, not a reliable physical T2star.
- No nearby 13C claim is supported. The expected sidebands are not stable or strong enough across raw/normalized, full/skip, and per-average checks.
- The `2.27 MHz` component should not be assigned to NV physics or 13C coupling from the current evidence.
- The refreshed pODMR center `3.8765 GHz` remains a frequency-calibration result only; it does not by itself establish Ramsey coherence or 13C coupling.

## Recommended next action

Do not run another blind long-span Ramsey repeat on r03 under the same conditions. Treat the r03 Ramsey/T2star/13C branch as still non-claim-grade after the refreshed-center high-shot test. The next action should be an alternate, targeted control/protocol decision: either run a phase/control Ramsey variant designed to separate real det-tracking carrier response from empirical high-frequency artifacts, or close this r03 branch with a supported "T2star and 13C unsupported under current Ramsey conditions" conclusion and move to a different protocol/candidate.
