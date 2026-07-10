# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey files: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior local context used for comparison: `evidence/e003.json` prior det=1.0 MHz 8 us Ramsey review, `evidence/e006.json` short-tau model/advisory plan, `evidence/e017.md` short-tau start note.

## Calculations/scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.
- Checks performed:
  - Parsed the raw export as 2 readouts x 41 tau points, with 12 stored averages.
  - Reconstructed tau grid: 0.048 to 1.968 us, 48 ns step.
  - Computed raw reference, raw signal, point-wise ratio, and signal/reference-line views.
  - Computed per-point SEM from stored averages.
  - Ran scan-order-aware drift screening using the recorded snake acquisition order.
  - Ran linear-baseline plus sinusoid least-squares screens at 1.0 MHz carrier, expected 13C sidebands 0.615/1.385 MHz, and a dense exploratory frequency grid.
  - Ran FFT checks on linearly detrended data.
  - Ran descriptive carrier-locked damped-cosine fits, but treated them as non-claim-grade.

## Quantitative findings

- Run completed safely: `auto__ramsey`, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000` repetitions, `1.08e6` shots/tau point, final counts `35.122 kcps`.
- Mean readouts: reference `48.57 kcps`, signal `44.65 kcps`, ratio `0.9195`.
- Median per-point SEM: signal `1.14 kcps`, ratio `0.0127`.
- Detrended peak-to-peak structure: signal `5.25 kcps`, ratio `0.1146`, signal/reference-line `0.1079`.
- Drift screen: no average exceeded a 15% end-to-start drop threshold. Stored-average means varied substantially, though: signal means `37.47..51.21 kcps`, reference means `42.02..55.19 kcps`.
- Programmed 1.0 MHz carrier is now visible but not dominant:
  - Signal LS amplitude `1.28 kcps`, ratio amplitude `0.0274`.
  - Baseline residual improvement: signal `0.377`, ratio `0.355`.
- Best exploratory component remains off-carrier near `1.19 MHz`:
  - Signal top near `1.187 MHz`, amplitude `1.68 kcps`, improvement `0.681`.
  - Ratio top near `1.192 MHz`, amplitude `0.0363`, improvement `0.656`.
- Expected 13C sideband checks are not discriminating in this short window:
  - Low sideband `0.615 MHz`: signal amplitude `1.10 kcps`, ratio `0.0243`.
  - High sideband `1.385 MHz`: signal amplitude `1.22 kcps`, ratio `0.0271`.
  - FFT bin spacing is about `0.508 MHz`, nominal span resolution about `0.521 MHz`, so the short-tau scan cannot separate carrier/sideband candidates well.
- Descriptive carrier-locked damped-cosine fits give very short apparent T2star values, but with large uncertainty:
  - Raw signal fit: `T2star ~0.186 us`, SEM `~0.112 us`.
  - Ratio fit: `T2star ~0.159 us`, SEM `~0.096 us`.

## Plausible interpretation

The short-tau/high-SNR change did reveal early-time Ramsey-like contrast that was not obvious in the prior 8 us scans. This supports the hypothesis that the previous long-window data were missing or diluting a short-lived early-time feature. However, the strongest component is again near `1.18..1.19 MHz`, not exactly the programmed `1.0 MHz` carrier, and the short span makes nearby frequency assignments highly covariant. A plausible physical explanation is a very short T2star with resonance drift or detuning offset of order `0.2 MHz`; a plausible nonphysical explanation is a fixed analysis/apparatus/baseline component in the same band. This dataset alone does not distinguish those.

## Claims not yet supported

- No claim-grade numeric T2star. The apparent `~0.16..0.19 us` fits are descriptive only.
- No supported nearby-13C conclusion. The sideband amplitudes are comparable to the carrier and best off-carrier component, and the short tau span lacks frequency resolution.
- No supported statement that the Ramsey phase follows the programmed detuning. The best exploratory component remains off the nominal carrier.
- No supported claim that r03 failed as a Ramsey target. The new data show usable early-time contrast, but its assignment is unresolved.

## Recommended next action

Do not run another blind long-window Ramsey repeat. First run a frequency/protocol discriminator: refresh the weak-pi pODMR center near `3.8759 GHz` or run a short-tau Ramsey detuning-dependence check on the same r03 to see whether the `~1.19 MHz` component follows programmed detuning or remains fixed. Only after that should a T2star fit be promoted or a longer/high-resolution 13C scan be planned.
