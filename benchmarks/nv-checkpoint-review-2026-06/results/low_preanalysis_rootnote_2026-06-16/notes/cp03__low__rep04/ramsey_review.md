# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, and `evidence/e017.md`.
- New measurement/job files: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` run status, `measurement/m005.json` control state.
- Generated local analysis artifacts: `ramsey_shorttau_analysis_summary.json` and `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with local Python/NumPy.
- Confirmed scan settings from raw export: `tau = 0.048..1.968 us`, 41 points, 48 ns spacing, 12 averages, 90000 repetitions/point, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Computed combined signal/reference traces and per-average SEM.
- Ran least-squares screens with constant + linear trend + sinusoid at:
  - programmed Ramsey carrier: `1.000 MHz`
  - expected 13C sideband checks from project state: `0.615 MHz` and `1.385 MHz`
- Ran broad frequency screens over `0.2..5 MHz`.
- Made diagnostic plot `ramsey_shorttau_review.png` showing raw signal/reference, normalized traces, and per-average ratios.

Key numerical checks:

- Raw signal mean/std: `48.573 / 0.456 kcps`; median per-point SEM across averages: `1.120 kcps`.
- Reference mean/std: `44.655 / 1.574 kcps`, much more structured than the signal channel.
- Raw-signal LS amplitude at `1.000 MHz`: `0.213 kcps`, only about `0.19x` the median raw SEM; LS amplitudes at `0.615` and `1.385 MHz` are `0.175` and `0.149 kcps`.
- Signal/reference LS amplitude at `1.000 MHz`: `0.03275` ratio units, but the reference alone has a large `1.000 MHz` LS amplitude of `1.282 kcps` and a broad strongest structure near low frequency / about `1.18 MHz` in FFT-style checks.
- Reference-line normalization reduces the `1.000 MHz` amplitude to `0.00475` ratio units.
- Per-average mean counts drift downward late in the run: raw average means include `43.793`, `42.016`, and `45.918 kcps` for averages 10-12 versus `55.188 kcps` at average 2; reference means show the same late drop. This is common-mode-like and affects confidence in ratio-only structure.

## Plausible interpretation

The short-tau/high-SNR Ramsey diagnostic completed and is analyzable, but it does not provide claim-grade evidence for a Ramsey carrier. The raw signal channel has no resolved 1 MHz oscillation above measured per-point uncertainty. The stronger oscillatory appearance in the signal/reference ratio is plausibly driven in large part by reference-channel structure and common-mode count changes rather than by clean NV Ramsey contrast.

This result weakens the prior working hypothesis that the previous long-window Ramsey failures were only due to a tau-zero artifact or insufficient early-time SNR. If r03 has Ramsey contrast under these settings, it is below the present raw-signal sensitivity or is being masked by readout/reference/systematic effects.

## Claims not yet supported

- A numeric `T2*` for r03 is not supported by this dataset.
- A nearby `13C` conclusion is not supported. The target sidebands at `0.615` and `1.385 MHz` are not separated from artifacts or noise in raw-signal evidence.
- The ratio trace alone should not be used to claim a detuning-following Ramsey carrier, because the reference channel carries substantial frequency-dependent structure.
- The existing r03 pODMR alignment conclusion remains supported by prior project evidence, but this Ramsey run does not add a T2star/13C claim.

## Recommended next action

Do not run another blind Ramsey repeat on r03. First review the pulse/readout implementation and normalization route for reference-channel modulation or sequence/readout artifacts, using a control or alternate protocol that can separate readout/reference structure from true Ramsey contrast. If the goal is to close the current branch promptly, record r03 as aligned but with unsupported T2star and unsupported 13C under the tested Ramsey conditions.
