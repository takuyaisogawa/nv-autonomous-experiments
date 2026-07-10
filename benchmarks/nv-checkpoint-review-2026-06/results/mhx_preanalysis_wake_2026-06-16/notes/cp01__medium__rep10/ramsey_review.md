# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Ramsey terminal/export data: `measurement/m001.json` through `measurement/m005.json`.
  - `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
  - `measurement/m002.json`: submitted Ramsey job spec.
  - `measurement/m003.json`: terminal bridge result; completed normally, final counts `38.249 kcps`.
  - `measurement/m004.json`: final run status/control snapshot; completed after `2124 s`, live estimator reported `492.946 s` per average.
  - `measurement/m005.json`: stop control state; no stop requested.
- Prior context from project state: accepted aligned candidate is `image145844_reimage_r03`, tracked at `[117.314436, 117.761644, 115.141679] um`; weak-pi pODMR grid-supported resonance was `3.876 GHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Generated `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Confirmed from embedded `ramsey.xml` that `full_experiment=0`, so readout 1 is the initial `m_S=0` reference and readout 2 is the post-Ramsey signal.
- Parsed Ramsey scan: `tau = 0..6 us`, `31` points, `0.2 us` step, `4 x 50000` repetitions, snake order, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
- Computed reference-normalized contrast `(ref - signal) / ref`.
- Ran linear-detrended Hann FFT on contrast and raw signal.
- Ran descriptive decaying-cosine fits after signal review, plus fixed-frequency sinusoid fits at:
  - programmed Ramsey carrier: `1.5 MHz`;
  - approximate expected 13C sidebands using the project model: `1.115 MHz` and `1.885 MHz`;
  - best descriptive frequency near `0.941 MHz`.

## Quantitative checks

- Raw/readout summary:
  - mean reference: `45.318 kcps`;
  - mean signal: `42.098 kcps`;
  - mean normalized contrast: `7.08%`;
  - contrast range over tau: `0.54%..14.09%`;
  - contrast standard deviation over tau: `3.40%`;
  - median point SEM across four averages: `2.56%`.
- Per-average signal/reference ratio means: `0.9347`, `0.9298`, `0.9199`, `0.9377`; average-to-average baseline variation is comparable to weak spectral features.
- Scan-order drift check using first/last third in acquisition order:
  - signal changes per average: `+1.57%`, `-1.82%`, `-2.20%`, `-1.41%`;
  - reference changes per average: `-1.15%`, `-4.71%`, `-2.68%`, `+1.81%`.
- FFT sampling:
  - actual sample step: `0.2 us`;
  - unpadded DFT bin spacing: `161.3 kHz`;
  - highest positive bin for 31 odd samples: `2.419 MHz` (sampling Nyquist is `2.5 MHz`).
- Contrast FFT top bins:
  - largest: `0.968 MHz`;
  - other large bins: `0.323`, `0.806`, `1.935`, `0.161`, `1.774 MHz`.
  - nearest programmed carrier bin `1.452 MHz` is not dominant.
- Fixed-frequency contrast fits versus a linear baseline:
  - `1.5 MHz`: combined amplitude `0.58%`, R2 improvement `0.016`;
  - `1.115 MHz`: combined amplitude `0.79%`, R2 improvement `0.028`;
  - `1.885 MHz`: combined amplitude `1.18%`, R2 improvement `0.064`.
- Descriptive free-frequency decaying-cosine fit:
  - frequency `0.941 MHz`;
  - T2star-like time `2.39 +/- 1.19 us`;
  - R2 `0.446`;
  - residual RMSE `2.49%`.
  This fit is not strong enough to promote to a T2star claim.

## Plausible interpretation

- The Ramsey run completed and produced analyzable data, but the scout is not claim-grade.
- There is real contrast variation in the Ramsey signal, but it is weak relative to average-to-average baseline variation and point-level SEM.
- The programmed `1.5 MHz` carrier is not cleanly recovered. The strongest descriptive feature is nearer `0.94..0.97 MHz`, which could be compatible with resonance drift/detuning, an analysis/noise artifact, or an unresolved mixture of weak components.
- A bin near the high-side expected 13C sideband (`~1.885 MHz`, nearest FFT bin `1.935 MHz`) is visible in the FFT, but fixed-frequency fits and per-average behavior are too weak/inconsistent to assign it to 13C.
- If the `0.94 MHz` feature were physical, the decay scale would be on the order of a few microseconds, but this dataset does not support quoting T2star.

## Claims that are not yet supported

- No well-supported T2star value is established.
- No well-supported 13C coupling/nearby-13C conclusion is established.
- The descriptive `T2star ~2.4 us` fit should not be used downstream as a physical result.
- The FFT features near `0.968 MHz` or `1.935 MHz` should not be assigned to resonance detuning or 13C without follow-up.
- The run does not invalidate r03 as the aligned candidate; prior pODMR evidence still supports r03, and this Ramsey result mainly shows that the first T2star/13C scout was inconclusive.

## Recommended next action

Run a fresh weak-pi pODMR or equivalent narrow resonance check on r03 before another Ramsey. The Ramsey ended with lower final counts (`38.249 kcps` versus prior `43.890 kcps`) and did not recover the programmed `1.5 MHz` carrier, so first verify whether the resonance center shifted from `3.876 GHz`. Then repeat Ramsey with the updated center and a redesigned acquisition that keeps per-average drift within the active cap while increasing claim strength through more averages/SNR and preserving FFT coverage of the carrier and `+/- ~0.385 MHz` 13C sidebands.
