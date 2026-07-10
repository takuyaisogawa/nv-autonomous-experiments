# Ramsey Review: r03 Short-Tau High-SNR Diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`, and `evidence/e017.md`.
- New measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job/spec metadata, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` run control.
- Scratch outputs created here: `analyze_shorttau_ramsey.py`, `ramsey_shorttau_analysis.json`, and `ramsey_shorttau_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_shorttau_ramsey.py`.
- Parsed the terminal raw export as combined data shape `1 x 2 x 41` and per-average data shape `1 x 12 x 2 x 41`.
- Confirmed scan settings from local metadata: `auto__ramsey`, tau `0.048..1.968 us` in 41 points, `48 ns` spacing, `mw_freq = 3.8759 GHz`, programmed `det = 1.0 MHz`, `12 x 90000` repetitions, terminal final counts `35.122 kcps`, no stop request.
- Checked raw signal, reference, signal/reference ratio, per-point SEM from stored averages, target least-squares components at `0.615`, `1.000`, `1.188`, and `1.385 MHz`, a frequency scan from `0.2..3.0 MHz`, forward/reverse snake-direction splits, per-average phase consistency, and simple decaying-cosine fits.

## Plausible interpretation

- Unlike the two prior long-window Ramsey reviews, this short-tau/high-SNR run shows a supported early-time Ramsey-like modulation in the signal readout.
- Combined raw signal has mean `44.65 kcps`, peak-to-peak `6.50 kcps`, and median per-point SEM `1.14 kcps`; the reference readout is much flatter over tau, with peak-to-peak `2.18 kcps`.
- The strongest combined sinusoidal screen is near `1.188 MHz`, not exactly the programmed `1.000 MHz` carrier. Raw-signal LS at `1.188 MHz` gives amplitude `1.79 +/- 0.24 kcps`, reduced chi2 `0.69`, and unweighted scan `R2 ~ 0.72`; signal/reference gives amplitude `0.0340 +/- 0.0027`, with best frequency `1.192 MHz`.
- The `1.188 MHz` component survives a scan-direction split: forward averages give raw amplitude `1.80 kcps`, phase `2.20 rad`, `R2 ~ 0.72`; reverse averages give raw amplitude `1.57 kcps`, phase `2.30 rad`, `R2 ~ 0.67`. That argues against a simple monotonic snake-scan drift artifact.
- Stored averages have large common-mode level drift: per-average reference means range about `42.0..55.2 kcps` and signal means `37.5..51.2 kcps`. This is important provenance and limits precision, but the fitted phase at `1.188 MHz` is fairly consistent across averages with circular resultant length `0.95`; median per-average raw amplitude is `1.78 kcps`.
- A free-frequency decaying cosine fit to raw signal returns frequency `1.183 +/- 0.046 MHz`, initial amplitude `2.88 +/- 0.66 kcps`, and `T2star = 1.78 +/- 0.90 us` with reduced chi2 `0.66`. This is a plausible working model, not a final T2star claim, because the tau window is only `1.92 us` long and the fit is model-dependent.
- The programmed `1.000 MHz` component is present but weaker than the `1.188 MHz` component: raw-signal amplitude `1.38 +/- 0.24 kcps`, reduced chi2 `1.28`, and lower `R2`. The repeated offset from the programmed carrier could reflect an effective resonance/microwave detuning near `0.18..0.19 MHz`, a sequence/phase artifact, or another systematic. It should be tested directly rather than absorbed into a T2star claim.

## Claims that are not yet supported

- Do not claim a final numeric T2star yet. The best free-frequency fit suggests a short-us scale decay, but the confidence interval is wide and the window is too short to establish the envelope robustly.
- Do not claim nearby `13C`. The expected sideband checks at about `0.615` and `1.385 MHz` are not the dominant spectral evidence, and this short window has poor sideband resolution by design.
- Do not claim the programmed `1.000 MHz` Ramsey carrier is the dominant component. The dominant component is consistently near `1.19 MHz`.
- Do not claim the modulation is free of drift/systematic concerns. Average-to-average common-mode drift is large, even though the direction split and reference behavior make a simple scan-order drift explanation unlikely.

## Recommended next action

Before another T2star/13C acquisition, run a targeted frequency-origin diagnostic rather than a blind Ramsey repeat. The most direct next step is an immediate fine weak-pi pODMR or equivalent resonance check around the current `3.8759 GHz` setting, wide enough to test a `~0.18..0.19 MHz` resonance shift, followed by a short-tau Ramsey with adjusted `mw_freq` only if the resonance check supports the shift. If the resonance has not shifted, use a deliberate det-shift short-tau Ramsey pair to see whether the `~1.19 MHz` component follows programmed detuning or stays fixed as a systematic.
