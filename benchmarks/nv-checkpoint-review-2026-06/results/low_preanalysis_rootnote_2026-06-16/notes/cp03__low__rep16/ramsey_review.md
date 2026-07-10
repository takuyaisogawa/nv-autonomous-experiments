# Ramsey review: short-tau r03 diagnostic

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective and prior status.
- `evidence/e017.md`: design/start note for the short-tau/high-SNR Ramsey diagnostic.
- `measurement/m002.json`: executed job spec for `nv23_ramsey_20260513_230331_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- `measurement/m001.json`: terminal savedexperiment raw export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_results.json`, `ramsey_analysis_stdout.txt`, `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData`, `ExperimentDataEachAvg`, errors, scan order, and sequence variables from `measurement/m001.json`.
- Confirmed scan settings: `tau = 48 ns..1.968 us`, 41 points at 48 ns spacing, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, 12 averages x 90000 repetitions.
- Terminal metadata check: job completed, elapsed `8402 s`, no bridge error message.
- Raw/readout checks:
  - Mean signal `48.57 kcps`, mean reference `44.65 kcps`.
  - Median signal SEM `1.46 kcps`; empirical median ratio SEM across averages `0.0151`.
  - Signal/reference ratio peak-to-peak over the short window: `0.174`.
- Scan-order drift check using snake acquisition order:
  - No average exceeded 10% first-half/second-half signal contrast.
  - Maximum absolute half-contrast was `4.27%`.
- Least-squares sinusoid screens:
  - At programmed `1.000 MHz`: ratio amplitude `0.0271`, raw signal amplitude `0.214 kcps`.
  - At expected 13C sideband checks from prior model, `0.615 MHz` and `1.385 MHz`: ratio amplitudes `0.0282` and `0.0299`, raw amplitudes `0.176 kcps` and `0.149 kcps`.
  - Dense LS screen from `0.2..2.6 MHz` was dominated by low-frequency curvature at the lower bound (`0.200 MHz`, ratio amplitude `0.143`), not by a clean carrier/sideband peak.
- FFT check after linear detrending:
  - Top coarse bins in the analysis band: `1.524 MHz`, `1.016 MHz`, `0.508 MHz`, `2.033 MHz`, `2.541 MHz`.
  - The `1.016 MHz` bin is near the programmed carrier, but it is not the strongest FFT component.
- Fixed-carrier damped-cosine fit to the ratio at exactly 1.0 MHz:
  - Model: offset + slope + `A exp(-(tau/T2*)^2) cos(2*pi*1MHz*tau + phi)`.
  - Fit returned `T2* = 0.330 us`, uncertainty `0.076 us`, amplitude `0.154 +/- 0.035`, `R2 = 0.61`.

## Plausible interpretation

- The short-tau/high-SNR dataset is analyzable and does not show a hard acquisition anomaly.
- Unlike the prior longer Ramsey scans, this dataset shows a substantial early-time ratio excursion and a fixed-carrier damped-cosine fit gives a plausible very-short `T2*` near `0.33 us`.
- This supports the hypothesis that earlier long-window Ramsey attempts may have missed or diluted a very rapidly decaying Ramsey contrast.
- Treat the `0.33 us` value as a provisional, model-dependent estimate, not yet a final project claim. The carrier is not cleanly isolated by independent frequency screens: the LS scan is dominated by low-frequency curvature, and the FFT has a near-carrier bin but a stronger non-target bin.
- This scan was intentionally short and is poorly suited to a high-confidence 13C sideband conclusion.

## Claims that are not yet supported

- A final T2star claim for r03 is not yet fully supported. The fixed-carrier fit is encouraging, but needs a confirmatory protocol or fit robustness checks because spectral evidence is mixed and the model is constrained to the programmed carrier.
- A nearby 13C claim is not supported. The sideband target amplitudes at `0.615 MHz` and `1.385 MHz` are comparable to the programmed-carrier amplitude and are not cleanly distinguished from other spectral content.
- A clean det-following carrier/sideband model across the Ramsey runs is still not established.
- Do not claim sub-grid precision for the fine pODMR center beyond the prior `3.8759 GHz` grid-supported setting.

## Recommended next action

Run one confirmatory short-window Ramsey designed specifically to validate the very-short-`T2*` interpretation, not to search blindly:

- Keep r03 and `mw_freq = 3.8759 GHz`.
- Use a short tau window concentrated around early decay, preferably with phase/quadrature or a second detuning setting if the available protocol supports it, so a true Ramsey carrier can be separated from baseline curvature.
- Include enough points below `0.8 us` and enough repeats to test whether the `~0.33 us` decay and 1 MHz phase evolution reproduce.
- If this confirmation again shows only constrained-fit evidence without clean carrier behavior, stop blind Ramsey repeats on r03 and report T2star/13C as unsupported under the current Ramsey protocol, or switch to an alternate coherence/spectroscopy protocol.
