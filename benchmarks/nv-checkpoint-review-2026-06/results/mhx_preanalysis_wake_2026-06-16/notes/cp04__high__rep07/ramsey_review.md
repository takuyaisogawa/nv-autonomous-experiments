# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `context.json`.
- New measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` status; `measurement/m005.json` control.
- Prior comparison: `evidence/e006.json` terminal det=1.0 MHz short-tau raw export; `evidence/e008.json` prior terminal det=1.0 MHz review.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Wrote `ramsey_analysis.json` and `ramsey_detshift_review.png`.
- Verified raw-export axis contract by averaging `ExperimentDataEachAvg` back to `ExperimentData`.
- Used readout1 as reference and readout2 as Ramsey signal, following the prior terminal review/protocol context.
- Checked raw signal, point-wise `signal/reference`, and `signal/fitted-reference-line`.
- Computed per-point SEM from 12 stored averages, scan-order-aware common-mode drift scores using `ScanOrderEachAvg`, FFT bins after linear detrending, least-squares sinusoid screens from 0.25 to 2.5 MHz, target amplitudes, and a descriptive damped-sinusoid grid fit.

## Quantitative checks

- New run: `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 0.048..1.968 us` in 41 points, `12 x 90000` repetitions, final counts `44.796 kcps`, completed with no monitor error and no stop request.
- Drift: no flagged averages with a 15% common-mode drop threshold; snake scan order from `Scan.ScanOrderEachAvg`.
- Noise/effect size: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`. Early `tau <= 0.75 us` peak-to-peak variation is `6.46 kcps` in raw signal and `0.134` in ratio, so there is real structure above point SEM.
- Frequency resolution is limited by the short span: FFT bin spacing `0.508 MHz`, nominal `1/span = 0.521 MHz`; LS frequency peaks should be treated as broad diagnostics.
- Point-wise ratio all-tau LS screen: strongest component at `1.623 MHz`, amplitude `0.02547`, R2 improvement `0.430`.
- Target checks in point-wise ratio:
  - programmed `1.5 MHz`: amplitude `0.02399`, R2 improvement `0.359`;
  - prior `1.192 MHz` if det-tracking by +0.5 MHz -> `1.692 MHz`: amplitude `0.02505`, R2 improvement `0.411`;
  - fixed prior `1.192 MHz` artifact control: amplitude `0.00511`, R2 improvement `0.0167`.
- 13C sideband checks were not dominant:
  - programmed det +/- 13C Larmor targets `1.115/1.885 MHz`: ratio amplitudes `0.01076/0.01732`;
  - shifted empirical-carrier +/- 13C Larmor targets `1.307/2.077 MHz`: ratio amplitudes `0.00953/0.00614`.
- View consistency is weak: raw signal and `signal/fitted-reference-line` screens both peak near `0.882 MHz`, while point-wise ratio peaks near `1.623 MHz`; skipping `tau <= 0.2 us` moves the ratio screen top to about `0.746 MHz`. Per-average top frequencies are scattered.
- Descriptive damped-grid fits prefer `0.674 MHz, T2* ~0.461 us` in ratio and `0.820 MHz, T2* ~0.739 us` in raw signal. These are diagnostics only and are not promoted.

## Plausible interpretation

The det-shift run is terminal and analyzable. It argues against simply treating the old `~1.192 MHz` point-wise ratio feature as a fixed-frequency artifact, because that fixed target is weak in the new ratio data. The all-tau point-wise ratio has a broad component in the det-shifted region expected from the prior feature moving toward `~1.692 MHz`.

That said, the evidence is not claim-grade for a physical Ramsey carrier. The programmed `1.5 MHz` and det-tracked `1.692 MHz` amplitudes are comparable, the raw/readout-aware views disagree on the dominant frequency, the skip-early-tau screen changes the preferred frequency, and individual averages are inconsistent. The safest interpretation is a real short-tau transient or analysis-sensitive oscillatory structure, not a supported carrier/sideband model.

## Claims not yet supported

- No numeric T2star is supported from this run.
- No nearby 13C coupling/conclusion is supported.
- Do not claim a clean Ramsey carrier at `1.5 MHz` or `1.692 MHz`.
- Do not promote the descriptive `T2* ~0.46..0.74 us` fits.
- Do not claim the `0.882 MHz` raw/signal-over-refline feature is physical.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Do a bridge-free synthesis of all r03 Ramsey results and then either switch to an alternate protocol that can test the Ramsey contrast/sequence-artifact failure mode directly, or close the r03 Ramsey/T2star/13C branch as unsupported under current conditions while preserving the prior aligned-NV claim.
