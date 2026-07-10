# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`, and `evidence/e017.md`.
- New measurement: `measurement/m001.json` raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- New bridge context: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior Ramsey context: `evidence/e001.json` through `evidence/e003.json` for the previous det=1.0 MHz, 0..8 us terminal review; `evidence/e009.json` and `evidence/e017.md` for this short-tau diagnostic design.

## Calculations/scripts run

- Created and ran `analyze_ramsey_shorttau.py`.
- Outputs written under `analysis_outputs/`:
  - `ramsey_shorttau_summary.json`
  - `ramsey_shorttau_stdout.json`
  - `ramsey_shorttau_traces.png`
  - `ramsey_shorttau_frequency_screen.png`
- Checks performed:
  - Parsed tau scan and readout channels. The sequence context says readout 1 is the mS=0 reference and readout 2 is the Ramsey signal with `full_experiment=0`.
  - Verified new run metadata: completed, `tau=48 ns..1.968 us`, 41 points, 48 ns spacing, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000` shots per point.
  - Computed signal/reference/ratio traces and per-point SEM across 12 averages.
  - Checked run and within-average drift using saved snake scan order.
  - Ran linear-trend-plus-sinusoid least-squares screens at the programmed carrier `1.000 MHz` and expected 13C sidebands `0.615423 MHz` and `1.384577 MHz`.
  - Ran an exploratory frequency screen and an exponential-envelope grid fit at the carrier as a descriptive check only.

## Quantitative results

- Combined raw signal mean `44.655 kcps`, reference mean `48.573 kcps`, signal/reference ratio mean `0.9195`.
- Median per-point SEM across averages: signal `1.14 kcps`, reference `1.12 kcps`, ratio `0.0127`.
- There is substantial average-to-average brightness drift: signal average means span `37.47..51.21 kcps` (`30.8%` of mean), reference means span `27.1%` of mean. The ratio is much more stable but still spans `6.8%`.
- Maximum within-average first-half/second-half change: signal `8.4%`, reference `4.4%`.
- Programmed-carrier LS amplitude:
  - raw signal: `1.28 +/- 0.27 kcps`, SNR `4.73`, `R2=0.455`
  - ratio: `0.0274 +/- 0.0061`, SNR `4.50`, `R2=0.447`
- Nominal sideband LS amplitudes are comparable, not cleanly separated:
  - `0.615423 MHz`: signal `1.10 kcps`, ratio `0.0243`
  - `1.384577 MHz`: signal `1.22 kcps`, ratio `0.0271`
- Above `0.5 MHz`, the exploratory screen peaks are near `1.205 MHz`, `1.084 MHz`, and `1.326 MHz` in raw signal; ratio peaks are near `1.207 MHz`, `1.086 MHz`, and `1.328 MHz`. The exact target carrier is not the dominant screened frequency.
- Early/late carrier split is suggestive of fast decay: early-window signal carrier amplitude `1.07 +/- 0.26 kcps`, late-window `0.63 +/- 0.38 kcps`; ratio early `0.0309 +/- 0.0084`, late `0.0121 +/- 0.0100`.
- A descriptive carrier-envelope grid fit prefers very short `T2* ~0.16..0.19 us`, but this is not claim-grade because the frequency discrimination is weak and drift/baseline terms are significant.

## Plausible interpretation

This short-tau/high-SNR diagnostic is more informative than the two earlier long-window Ramsey datasets. It does show weak early-time Ramsey-like contrast near the programmed `1.0 MHz` detuning, and the reduced late-window amplitude is qualitatively consistent with a very short dephasing time.

However, the evidence is still not specific enough to support a numeric T2star or a nearby-13C conclusion. The nominal carrier and both expected 13C sideband frequencies fit with similar small amplitudes, and the exploratory screen prefers nearby frequencies around `1.1..1.3 MHz` rather than a clean carrier/sideband pattern. Average-to-average brightness drift is large in raw channels, although partially common-mode in the ratio.

## Claims not yet supported

- A well-supported T2star value for r03.
- A nearby 13C coupling claim from Ramsey FFT/sidebands.
- A precise Ramsey carrier frequency from this short time window.
- Promoting the descriptive `T2* ~0.16..0.19 us` fit to a project result.
- Treating the short-tau result as a clean detuning-following carrier confirmation without a targeted confirmation measurement.

## Recommended next action

Do not run another blind long-window Ramsey repeat on r03. If continuing r03, run a targeted confirmation that tests carrier specificity before attempting a 13C conclusion: a short-window, phase-cycled or otherwise differential Ramsey confirmation over the first `~0.8..1.2 us`, preferably with at least two deliberate detunings so the feature must move with the programmed detuning. If that confirmation fails, close the r03 Ramsey/T2star/13C branch as unsupported under current conditions and consider an alternate protocol rather than more Ramsey accumulation.
