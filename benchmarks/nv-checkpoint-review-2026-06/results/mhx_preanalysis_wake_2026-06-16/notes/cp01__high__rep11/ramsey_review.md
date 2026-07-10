# Ramsey review: r03 T2star/13C scout

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior support for the target and frequency: `evidence/e003.json` weak-pi pODMR raw review supporting the 3.876 GHz grid minimum; `evidence/e005.json` Ramsey model/protocol/advisory; `evidence/e006.json` rejected 8 us/51 point advisory; `evidence/e007.json` accepted 6 us/31 point advisory; `evidence/e008.json` submit spec.
- New Ramsey data and terminal metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` after switching Matplotlib to the non-interactive `Agg` backend.
- Parsed `measurement/m001.json` as `ramsey.xml`, `full_experiment=0`: readout 1 is the initial mS=0 reference, readout 2 is the Ramsey signal.
- Confirmed scan/acquisition: tau 0..6 us, 31 points, 0.2 us step, 4 averages x 50000 repetitions, `mw_freq=3.876 GHz`, `det=1.5 MHz`.
- Model check from the existing working approximation: `B ~ 359.29 G`, expected 13C Larmor `~0.3846 MHz`; expected Ramsey features are carrier near `1.5 MHz` and possible 13C sidebands near `1.115 MHz` and `1.885 MHz`.
- Sampling check: DFT bin spacing from 31 samples is `161.3 kHz` while the scan-span resolution is `166.7 kHz`; Nyquist is `2.5 MHz`.
- Raw/readout checks:
  - Ramsey signal mean `42.10 kcps`, peak-to-peak `7.75 kcps`, median across-average SEM `1.01 kcps`.
  - Reference mean `45.32 kcps`, peak-to-peak `3.90 kcps`.
  - Final bridge counts dropped to `38.249 kcps` from the preceding weak-pODMR final `43.890 kcps`, about a `12.9%` drop.
  - Simple scan-order common-mode drift scores by average were `0%`, `3.5%`, `3.0%`, `0%`; none crossed a 15% flag threshold.
- Frequency checks:
  - Fixed-frequency regression at programmed `1.5 MHz`: raw amplitude `0.29 +/- 0.36 kcps` (`z ~0.8`, `R2 ~0`); ratio amplitude `0.0094 +/- 0.0075` (`z ~1.25`).
  - Detrended FFT top peak in both raw signal and ratio is near `0.968 MHz`; the nearest bin to `1.5 MHz` ranks only 13th in raw signal and 12th in ratio.
  - A post-hoc fixed regression at `0.968 MHz` gives raw amplitude `0.80 +/- 0.28 kcps` (`z ~2.9`) and ratio amplitude `0.0198 +/- 0.0079` (`z ~2.5`), but this is empirical and not the planned carrier.
- Fit checks:
  - Free damped-cosine fit to all raw signal gives `freq ~0.944 MHz`, `T2star ~1.31 +/- 0.49 us`, `R2 ~0.44`.
  - Free damped-cosine fit to all ratio data gives `freq ~0.882 MHz`, `T2star ~1.96 +/- 0.68 us`, `R2 ~0.38`.
  - Excluding the tau=0 point makes the raw decay fit non-informative: `R2 ~0.034` and `T2star` hits the 30 us upper bound.

## Plausible interpretation

The run completed and produced analyzable raw data, but it is not claim-grade for T2star or 13C. The strongest reproducible-looking structure is a weak, post-hoc component around `0.9-1.0 MHz`, not the programmed `1.5 MHz` Ramsey carrier. The tau=0 signal point is low across averages and strongly influences the free damped-cosine fit; once that point is removed, the T2star fit loses constraint.

This could be a weak Ramsey response with an effective carrier shifted away from the programmed detuning, a first-point/pulse artifact plus noise, or residual frequency/resonance drift during the 35 minute run. The final count drop and runtime advisory excursion support treating drift as relevant provenance, even though the within-average scan-order drift score did not hard-flag.

## Claims not yet supported

- A numeric T2star for r03 is not yet supported. The apparent `~1-2 us` fit is model/post-hoc dependent and collapses when tau=0 is excluded.
- A 13C conclusion is not supported. Expected sideband frequencies are within the sampled band, but there is no supported carrier at `1.5 MHz` and no defensible symmetric sideband assignment.
- The `0.9-1.0 MHz` feature is not yet a confirmed physical Ramsey frequency. It is a useful hypothesis for follow-up, not a result.
- The Ramsey data do not invalidate the prior pODMR alignment/frequency evidence by themselves; they only fail to deliver a supported T2star/13C conclusion.

## Recommended next action

Do not claim T2star or 13C from this scout. Re-check the r03 resonance/frequency under fresh tracking, then run a drift-safer Ramsey diagnostic designed around the observed failure mode: shorter untracked windows, enough points to resolve `~1.0-1.5 MHz`, and explicit comparison of `det=1.5 MHz` versus a lower carrier near the empirical `~1 MHz` feature. Only fit T2star after the repeated raw/normalized Ramsey trace shows a stable carrier across averages.
