# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior design/readout context: `evidence/e007.json`, `evidence/e013.md`; readout convention used here is readout1 = reference and readout2 = Ramsey signal for `full_experiment=0`.
- New Ramsey run: `measurement/m001.json` raw savedexperiment export, plus `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Local outputs created: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the Ramsey export: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, 8 averages, 50000 reps, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Built signal metrics from readout2 and readout1:
  - combined reference mean `49.313 kcps`;
  - combined Ramsey signal mean `44.580 kcps`, range `39.308..47.029 kcps`;
  - per-average fitted-reference-line normalized signal mean `0.9034`, std over tau `0.0257`, range `0.8052..0.9575`.
- Ran linear-baseline plus sinusoid least-squares checks on the normalized trace:
  - expected lower 13C sideband `0.615 MHz`: amplitude `0.00966`, residual RMS `0.02477`, `R2 = 0.072`;
  - prior scout component `0.884 MHz`: amplitude `0.00611`, residual RMS `0.02529`, `R2 = 0.033`;
  - programmed carrier `1.000 MHz`: amplitude `0.00588`, residual RMS `0.02532`, `R2 = 0.030`;
  - expected upper 13C sideband `1.385 MHz`: amplitude `0.00528`, residual RMS `0.02538`, `R2 = 0.026`.
- Ran exploratory frequency checks:
  - free least-squares scan favored about `0.467 MHz` with only `R2 ~ 0.265`, not an expected carrier or 13C sideband;
  - Hann-window FFT top components were near `1.220`, `1.098`, and `0.488 MHz`, not cleanly centered on `1.000`, `0.615`, or `1.385 MHz`;
  - leave-one-average-out free-best frequencies moved among about `0.46`, `1.15..1.18`, and the lower search boundary, so the exploratory structure is not stable.
- Verified generated plot metadata with Python/PIL: `ramsey_review_plot.png` is a `1200 x 1275` RGBA PNG. Direct image viewer access failed with an access error, so interpretation above is based on numeric outputs.

## Plausible interpretation

The run completed and returned analyzable data, but it does not show a claim-grade Ramsey carrier at the programmed `1.0 MHz` detuning. The expected 13C sidebands near `0.615` and `1.385 MHz` are also weak relative to residual structure. Average-to-average raw counts vary substantially in common mode, but reference-line normalization keeps the mean ratio reasonably bounded; this looks like usable-but-noisy data rather than a failed export.

The det-shift diagnostic is unfavorable: the previous non-claim-grade `~0.884 MHz` component is not strongly reproduced, and the new scan does not produce a clean `1.0 MHz` carrier. The visible spectral structure is more plausibly residual drift/noise/sequence or detuning implementation behavior than a supported physical Ramsey/T2star or 13C signature.

## Claims not yet supported

- No supported T2star value from this run.
- No supported 13C coupling claim from this run.
- No supported no-13C/absence conclusion from this run alone.
- No supported physical assignment for the exploratory `~0.47`, `~1.10`, or `~1.22 MHz` components.
- No basis to fit and report a decay constant before a stable Ramsey carrier is established.

## Recommended next action

Do not spend another long scan on a T2star/13C claim attempt yet. First validate the Ramsey carrier path on r03: recheck the resonance if needed, then run a short two-detuning Ramsey diagnostic with enough sampling to confirm that the dominant spectral component follows programmed detuning. Only fit T2star or evaluate 13C sidebands after the carrier is reproducible and det-tracking is demonstrated.
