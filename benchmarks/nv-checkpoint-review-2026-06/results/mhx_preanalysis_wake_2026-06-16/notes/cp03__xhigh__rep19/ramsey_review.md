# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- New short-tau Ramsey terminal data: `measurement/m001.json` raw export, `measurement/m002.json` job settings, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison/design context: `evidence/e003.json` terminal review of the det=1.0 MHz 8 us Ramsey, `evidence/e006.json` short-tau model/advisory, `evidence/e017.md` design/start note.
- Generated locally: `scratch_ramsey_analysis.py`, `ramsey_analysis_summary.json`, `ramsey_shorttau_review.png`.

## Calculations/scripts run

- Ran `python scratch_ramsey_analysis.py`.
- The script extracted the 2-readout, 41-point, 12-average Ramsey data; built tau from 48 ns to 1.968 us; computed raw signal/reference, point-wise ratio, and signal normalized to a fitted reference line.
- It ran scan-order-aware common-mode drift checks using the stored snake order, target LS fits at 1.0 MHz, 0.615 MHz, 1.385 MHz, the previous 8 us top component near 1.178 MHz, and the first-scout 0.884 MHz component.
- It ran frequency screens, FFT summaries, odd/even and first/last average consistency checks, leave-one-average checks, and constant-amplitude vs exponential-decay sinusoid fits.
- Plot file was mechanically verified as nonblank: `2160 x 1440`, nonwhite pixel fraction about `0.073`.

## Quantitative result

- Run completed: `nv23_ramsey_20260513_230331_auto_ramsey`, `auto__ramsey`, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000` repetitions, `1.08e6` shots per tau point, final counts `35.122 kcps`. Status/control show no stop request and empty monitor error.
- No drift flags from the local scan-order-aware check. Common-mode end-minus-start fractions ranged from about `-0.060` to `+0.117`, below the `0.15` drop flag threshold.
- New data show a much stronger recurring oscillatory component than the previous 8 us run:
  - Raw signal top LS screen: `1.187 MHz`, amplitude `1.68 kcps`, baseline-residual R2 improvement `0.681`.
  - Point-wise ratio top LS screen: `1.192 MHz`, amplitude `0.0363`, R2 improvement `0.656`.
  - Signal/reference-line top LS screen: `1.187 MHz`, amplitude `0.0346`, R2 improvement `0.681`.
  - Raw signal detrended peak-to-peak is `5.25 kcps` vs median per-point signal SEM `1.14 kcps`; ratio detrended peak-to-peak is `0.115` vs median ratio SEM `0.0127`.
- The programmed `1.0 MHz` carrier is not the top component:
  - At `1.0 MHz`: raw signal amplitude `1.28 kcps`, ratio amplitude `0.0274`, R2 improvement about `0.35-0.38`.
  - At expected 13C sidebands `0.615/1.385 MHz`: ratio amplitudes `0.0243/0.0271`; neither is dominant or resolved.
- Consistency checks support the `~1.19 MHz` neighborhood as a real feature candidate: odd/even averages top near `1.174/1.233 MHz`, first/last halves near `1.188/1.209 MHz`, and leave-one-average constant-amplitude ratio fits span only `1.187-1.201 MHz`.
- The short tau span gives coarse FFT resolution. FFT power appears mainly in broad bins near `0.508` and `1.016 MHz`; it is useful as a sanity check but not for a fine 13C sideband claim.
- Decay is not constrained. Equal-weight decay fits are not favored over constant-amplitude sinusoid fits: delta AIC(decay - constant) is `+1.75` for ratio, `+0.81` for signal/reference-line, and `+0.76` for raw signal. The SEM-weighted raw fit weakly prefers a decayed model near `T2* ~1.8 us`, but that is not robust across views, and leave-one fits can push T2* to the upper bound.

## Plausible interpretation

The short-tau/high-SNR diagnostic succeeded at its main diagnostic purpose: it makes an early-time Ramsey-like oscillatory response visible. The recurring component near `1.18-1.20 MHz` is stronger and more consistent than the previous det=1.0 MHz 8 us dataset, whose top screen was also near `1.178 MHz` but weaker.

The result does not cleanly validate the programmed-carrier model. A `~1.19 MHz` Ramsey feature with a `1.0 MHz` phase ramp could plausibly indicate a microwave frequency/resonance detuning of order `0.19 MHz`, a timing/phase-path artifact, or another systematic feature. The current files do not distinguish those possibilities.

## Claims not yet supported

- No numeric T2* claim is supported from this measurement. The oscillation is visible, but the decay envelope is not robustly constrained over this short span.
- No nearby 13C claim is supported. The short span was not designed for high-resolution 13C spectroscopy, and the expected sideband fits are not dominant.
- No claim that the NV resonance has shifted by `~0.19 MHz` is supported yet; that is only a plausible explanation for the `~1.19 MHz` feature.
- No claim that r03 is invalid is supported. Existing pODMR evidence still supports r03 as the aligned candidate; the unsupported part remains T2*/13C interpretation.

## Recommended next action

Do not run another blind Ramsey repeat. First run a targeted frequency-basis diagnostic on r03, preferably a fresh fine weak-pi pODMR around `3.8759 GHz` wide enough to test a `~0.2 MHz` shift, or an equivalent Ramsey det/mw-frequency diagnostic. If that verifies the frequency basis, then design a follow-up Ramsey with the corrected carrier condition and a longer/high-quality span for T2* and 13C sideband resolution. If the `~1.19 MHz` feature cannot be tied to the carrier/frequency basis, switch to an alternate T2 protocol or close the r03 Ramsey/13C branch as unsupported under current conditions.
