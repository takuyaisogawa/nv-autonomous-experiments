# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final run status, `measurement/m005.json` control state.
- Supporting prior context: `evidence/e001.json` through `evidence/e011.json`, especially the weak-pi pODMR review/model/advisory and Ramsey job planning/status records.
- Scratch outputs created in this directory: `ramsey_analysis_metrics.json` and `ramsey_review_plot.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python.
- Confirmed Ramsey scan settings: `tau = 0..6 us`, 31 points, `dt = 0.2 us`, 4 stored averages, 50000 repetitions per average, snake order with data saved in tau order.
- Checked readout traces as raw `readout1`/`readout2`, pointwise `readout2/readout1`, and `readout2` normalized by a fitted line to `readout1`.
- Computed per-average means, peak-to-peak variation, SEM across averages, correlations between each average and the aggregate trace, detrended Hann FFTs, and simple cosine/decaying-cosine fits.
- Sampling check: FFT bin spacing is `0.1613 MHz`, Nyquist is `2.5 MHz`. The programmed detuning is `1.5 MHz`; expected 13C sideband scale from the project model is about `0.385 MHz`, so sideband markers are near `1.115 MHz` and `1.885 MHz`.

## Plausible interpretation

- The run completed and produced analyzable data, but it is not claim-grade for T2star or 13C.
- Operationally, the run was drift-risky: the job completed without abort, but final count text was `38.249 kcps`, below the fresh r03 track/weak-pODMR level near `43-44 kcps`; the live per-average runtime estimate was `492.946 s`, above the original `450 s` planning cap.
- The expected Ramsey carrier is not cleanly supported. In the aggregate signal, the nearest FFT bin to `1.5 MHz` is `1.4516 MHz`, but it is not a dominant peak:
  - raw signal FFT: dominant bins include `0.9677 MHz`, `0.1613 MHz`, and `0.3226 MHz`; the `1.4516 MHz` bin is weaker.
  - pointwise ratio FFT: dominant bins include `0.9677 MHz`, `0.8065 MHz`, `0.3226 MHz`, and `1.9355 MHz`; the `1.4516 MHz` bin is weaker.
  - reference-line-normalized FFT: dominant bins include `0.9677 MHz`, `0.1613 MHz`, and `0.3226 MHz`; the `1.4516 MHz` bin is weaker.
- The per-average frequency content is not stable enough to assign a physical peak. Some averages show a strong `~0.968 MHz` component, while others favor low-frequency bins or sideband-adjacent bins.
- Fits do not support a robust T2star. A fixed `1.5 MHz` no-decay cosine explains very little variance (`R2` about `0.01-0.03` depending on view). Fixed-`1.5 MHz` decaying fits return short apparent T2star values around `0.25-0.38 us`, but these are not reliable because the expected carrier itself is not cleanly present. Free-frequency decaying fits prefer about `0.94-0.96 MHz` with T2star about `2.1-2.4 us`, but that frequency is not stable across averages and should be treated as a descriptive artifact/hypothesis, not a result.

## Claims not yet supported

- No supported numerical T2star claim from this Ramsey scout.
- No supported 13C coupling or nearby-13C conclusion from this FFT.
- No supported claim that the `~0.97 MHz` FFT/fitted feature is a real Ramsey carrier, resonance shift, or hyperfine sideband.
- No supported claim that the absence of a clean `1.5 MHz` carrier proves no Ramsey coherence; the acquisition had drift/count provenance and only 31 points over 6 us.

## Recommended next action

Do not make a T2star or 13C claim from this run. Before spending a longer Ramsey acquisition, refresh the r03 frequency/current condition with a short weak-pi pODMR or equivalent resonance check under current tracking/counts, then repeat Ramsey only if the resonance check is clean. For the repeat, keep the per-average tracking window inside the current advisory cap; if drift is still high, reduce repetitions/points rather than extending the untracked window, and use the refreshed resonance to set the programmed detuning so the Ramsey carrier should land cleanly inside the FFT band.
