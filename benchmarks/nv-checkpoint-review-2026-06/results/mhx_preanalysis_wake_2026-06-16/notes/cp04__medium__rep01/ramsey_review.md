# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus relevant prior Ramsey summaries in `evidence/`.
- New completed Ramsey: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison run: `evidence/e006.json`, the terminal det=1.0 MHz short-tau Ramsey raw export.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed readout 1 as reference and readout 2 as Ramsey signal, matching the existing `ramsey.xml full_experiment=0` context.
- Checked the new run parameters: `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 0.048..1.968 us`, `41` points, `12 x 90000` shots, final count `44.796 kcps`.
- Computed raw signal/reference means, per-point SEM from the 12 averages, signal/reference ratios, linear-detrended residuals, FFT peaks, and least-squares sinusoid screens.
- Compared target amplitudes at `1.5 MHz`, prior empirical `1.192 MHz`, det-tracking prediction near `1.692 MHz`, and contextual 13C sideband checks near `1.307` and `2.076 MHz`.

## Plausible interpretation

- The new data are analyzable and terminal, with no stop request and no bridge hard failure. Mean reference is `48.08 kcps`, mean Ramsey signal is `44.27 kcps`, and mean signal/reference ratio is `0.9207`.
- A blind LS screen down to `0.3 MHz` is dominated by a slow/baseline-like component at the lower search edge, so the most conservative reading is still baseline/transient sensitivity.
- When restricted above the slow component, the new combined ratio screen peaks at `0.857 MHz` for `>0.7 MHz`, and at `1.616 MHz` for `>1.0 MHz`. The `1.616 MHz` component is qualitatively near the det-tracking expectation from the previous `~1.192 MHz` feature, but it is not clean or robust.
- Target amplitudes are weak: at `1.5 MHz`, signal amplitude is `1.13 kcps` (`1.59x` median signal SEM) and ratio amplitude is `0.0240` (`1.90x` median ratio SEM); at `1.692 MHz`, signal amplitude is `1.23 kcps` (`1.72x` SEM) and ratio amplitude is `0.0250` (`1.98x` SEM).
- The prior `~1.192 MHz` component does not remain strong in the new det=1.5 MHz run: ratio amplitude at `1.192 MHz` is only `0.0051` (`0.40x` median ratio SEM), versus `0.0363` in the previous det=1.0 MHz run.
- The 13C contextual sidebands are not supported: ratio amplitudes are only `0.0095` at `1.307 MHz` and `0.0062` at `2.076 MHz`, both below one median ratio SEM.

## Claims that are not yet supported

- Do not claim a numeric T2star from this run. The carrier/decay model is not sufficiently established.
- Do not claim nearby 13C coupling. The expected sideband checks are weak and not dominant.
- Do not claim clean det-following Ramsey behavior. There is weak det-shift-ish content near `1.6..1.7 MHz`, but the all-tau/band-limited/per-average checks are inconsistent.
- Do not promote the earlier `~1.192 MHz` feature as a stable physical Ramsey component; this run argues against that simple fixed-frequency interpretation.

## Recommended next action

Avoid another blind Ramsey repeat on r03. Treat the r03 Ramsey/T2star/13C result under the current Ramsey protocol as unsupported/non-claim-grade, and choose deliberately between closing this branch with that conclusion or switching to a different protocol/control designed to separate early-time baseline artifacts from a real Ramsey carrier.
