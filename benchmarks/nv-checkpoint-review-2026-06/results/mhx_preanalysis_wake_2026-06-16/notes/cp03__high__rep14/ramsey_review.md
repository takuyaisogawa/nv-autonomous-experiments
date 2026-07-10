# Ramsey review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey terminal data and metadata: `measurement/m001.json` through `measurement/m005.json`.
- Prior comparison/design context: `evidence/e003.json` for the previous det=1.0 MHz 8 us Ramsey terminal review, `evidence/e006.json`/`evidence/e009.json` for the short-tau model/advisory and target frequencies, and `evidence/e017.md` for the short-tau start note.

## Calculations/scripts run

- Added and ran `analyze_shorttau_ramsey.py`.
- Outputs:
  - `ramsey_shorttau_analysis.json`
  - `ramsey_shorttau_diagnostic.png`
- Checks performed:
  - Raw reference/signal statistics, ratio, and signal normalized to a fitted reference line.
  - SEM estimates from exported errors and from 12 stored averages.
  - Fixed-frequency least-squares screens at 1.0 MHz carrier, 0.615422875 MHz and 1.384577125 MHz expected 13C sidebands, prior 0.884361482 MHz scout feature, and previous 1.178 MHz screen feature.
  - Exploratory LS frequency scan from 0.1 to 5 MHz.
  - FFT amplitude sanity check, noting the short-window bin spacing.
  - Forward-vs-reverse snake average and first-vs-second-half consistency checks.

## Quantitative review

- Run completed cleanly: `auto__ramsey` / `ramsey.xml`, `tau = 0.048..1.968 us` in 41 points, `48 ns` step, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000 = 1.08e6` shots per tau point. Terminal final count was `35.122 kcps`, above the 20 kcps gate; stop request was false and safe shutdown was reported.
- Sampling is intentionally short: span `1.92 us`, about `1.92` cycles at 1 MHz. FFT bin spacing is coarse at `0.508 MHz`, so FFT cannot cleanly separate 1.0 MHz from nearby sidebands; LS checks are more informative.
- Combined readouts: reference mean `48.573 kcps`, signal mean `44.655 kcps`, ratio mean `0.91946`.
- Noise scale: exported signal error median `1.397 kcps`; stored-average signal SEM median `1.138 kcps`; ratio SEM median `0.0127`.
- The short-window signal is not flat: signal linear-residual peak-to-peak `5.25 kcps`, ratio residual peak-to-peak `0.1146`, and first-0.75-us raw signal peak-to-peak `5.69 kcps`.
- Fixed-frequency LS on the ratio gives:
  - 1.0 MHz carrier: amplitude `0.0274`, baseline-residual gain `0.355`; raw-signal amplitude `1.28 kcps`.
  - Low 13C sideband at 0.615 MHz: ratio amplitude `0.0243`, gain `0.311`; raw amplitude `1.10 kcps`.
  - High 13C sideband at 1.385 MHz: ratio amplitude `0.0271`, gain `0.345`; raw amplitude `1.22 kcps`.
  - Prior 0.884 MHz scout feature: ratio amplitude `0.0126`, gain `0.071`.
- The strongest combined LS component is not exactly the programmed carrier: top ratio screen is near `1.192 MHz` with amplitude `0.0363` and gain `0.656`; raw signal and signal/reference-line screens peak near `1.187-1.188 MHz` with raw amplitude about `1.68 kcps`.
- Direction/time checks argue against a simple snake-direction artifact:
  - Forward averages top near `1.17 MHz`, reverse averages top near `1.23 MHz`.
  - First-half averages top near `1.185 MHz`, second-half averages top near `1.205 MHz`.
  - Detrended subset correlations with the combined ratio trace are high: `0.90-0.94`.
- There is still sizable common-mode count variation between stored averages: average signal means span `13.74 kcps`, reference means span `13.17 kcps`. Ratio means are more stable but still span about `0.063`.

## Plausible interpretation

The short-tau/high-SNR diagnostic did what it was designed to test: it reveals a repeatable early-time Ramsey-like oscillatory structure that was weak or washed out in the earlier 8 us datasets. The component is stronger than the per-point SEM scale and appears in forward/reverse and early/late subsets, so it should not be dismissed as pure noise or a trivial scan-order artifact.

The frequency content is still not claim-grade for final physics. The strongest LS component is around `1.19 MHz`, close to the previous 8 us top screen near `1.178 MHz`, rather than a clean programmed `1.0 MHz` carrier. A plausible explanation is a residual resonance-frequency offset after the fine pODMR, so the Ramsey beat is det plus an uncorrected offset. Another plausible explanation is a timing/baseline response that projects strongly into the short-window sinusoid basis. This run supports "early-time oscillation exists on r03 under this protocol"; it does not yet support a calibrated T2star or 13C assignment.

## Claims not yet supported

- A numeric T2star is not supported. The short window contains less than 2 us and does not constrain a decay envelope well enough; frequency, baseline, and envelope are still confounded.
- A nearby 13C claim is not supported. The expected sideband fixed-frequency amplitudes are comparable to the carrier and to the broad top component, not a resolved sideband pair.
- A no-13C conclusion is also not fully supported; the present data mainly say no resolved 13C signature has been demonstrated under the current Ramsey analyses.
- The `~1.19 MHz` component should not yet be claimed as the true detuning or resonance shift without a detuning/frequency-control check.
- The previous non-claim-grade Ramsey datasets should not be reinterpreted as T2star evidence just because this short-tau run shows structure.

## Recommended next action

Do not run another blind Ramsey repeat. The next useful step is a targeted detuning/frequency diagnostic: refresh the weak-pi pODMR center if needed, then run a short Ramsey check with deliberately shifted `det` or `mw_freq` to test whether the `~1.19 MHz` component follows the programmed detuning as a true Ramsey carrier. If it follows detuning, use that calibrated carrier to plan a longer high-SNR Ramsey window for T2star and sideband sensitivity. If it does not follow detuning, treat the feature as protocol/baseline artifact and switch to an alternate T2/13C protocol rather than accumulating more Ramsey repeats.
