# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, with targeted Ramsey/13C guidance cross-checked against `md/knowledge.md`.
- New terminal Ramsey measurement:
  - `measurement/m001.json`: raw export from `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: execute request/manifest for `nv23_ramsey_20260513_230331_auto_ramsey`.
  - `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: completed result/status/control records.
- Scratch outputs created here:
  - `analyze_ramsey.py`
  - `ramsey_shorttau_review.png`

## Calculations/Scripts Run

- Ran `python analyze_ramsey.py`.
- Parsed the Ramsey raw export as two readout channels over 41 tau points, using channel 0 as signal and channel 1 as reference.
- Measurement settings confirmed from JSON:
  - `tau = 0.048..1.968 us`, 41 points, `dt = 48 ns`.
  - `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
  - `12 averages x 90000 repetitions = 1.08e6 shots/tau`.
- Computed combined raw signal, raw reference, signal/reference ratio, per-point SEM across stored averages, FFT screen, and least-squares sinusoid amplitudes with offset + linear baseline at:
  - `0.615 MHz` expected lower 13C sideband position.
  - `1.000 MHz` programmed Ramsey carrier.
  - `1.385 MHz` expected upper 13C sideband position.
- Key quantitative results:
  - Raw signal mean/min/max: `48.573 / 47.568 / 49.744 kcps`.
  - Reference mean/min/max: `44.655 / 40.698 / 47.197 kcps`.
  - Ratio mean/min/max: `1.0892 / 1.0174 / 1.1910`.
  - Median point SEM: ratio `0.0151`, raw signal `1.12 kcps`, raw reference `1.14 kcps`.
  - Combined ratio LS amplitudes:
    - `0.615 MHz`: `0.0292` ratio units, `1.94 x` median ratio SEM.
    - `1.000 MHz`: `0.0327` ratio units, `2.17 x` median ratio SEM.
    - `1.385 MHz`: `0.0317` ratio units, `2.10 x` median ratio SEM.
  - Combined raw-signal LS amplitudes:
    - `0.615 MHz`: `0.175 kcps`.
    - `1.000 MHz`: `0.213 kcps`.
    - `1.385 MHz`: `0.149 kcps`.
    - These are far below the median raw-signal SEM of `1.12 kcps`.
  - Combined ratio FFT top bins:
    - `1.524 MHz` amplitude `0.0324`.
    - `0.508 MHz` amplitude `0.0279`.
    - `1.016 MHz` amplitude `0.0278`.
  - Per-average best FFT frequencies are inconsistent: examples include `0.508`, `1.016`, `1.524`, `2.033`, `3.049`, and `8.130 MHz`.

## Plausible Interpretation

- The measurement completed and is analyzable, but it does not provide claim-grade Ramsey/T2star evidence.
- The short-tau/high-SNR change did not reveal a robust raw-signal carrier. At the programmed `1.0 MHz`, raw signal amplitude is only `0.213 kcps`, well below the measured per-point raw SEM (`~1.12 kcps`).
- Ratio-space structure exists at about the `2 x` median ratio SEM level, but it is not specific: the programmed carrier and both expected 13C sideband test frequencies have similar amplitudes, and the strongest FFT bins do not form a stable carrier/sideband pattern.
- The ratio is strongly affected by the reference channel behavior; the reference has much larger fitted amplitudes than the raw signal at the tested frequencies. That makes the ratio oscillation insufficient by itself as NV Ramsey evidence.
- Per-average spectral inconsistency argues against promoting any one frequency component as a supported physical Ramsey fringe.

## Claims Not Yet Supported

- A numeric `T2*` for r03 is not supported by this dataset.
- Nearby 13C coupling is not supported. The expected `0.615/1.385 MHz` sideband positions are not distinguished from the carrier or from unrelated FFT bins.
- The prior weak spectral features from earlier Ramsey scans are still not promoted; this short-tau diagnostic did not establish a det-following, reproducible carrier/sideband model.
- A statement that r03 has no Ramsey contrast at all is also too strong. The supported conclusion is narrower: under this protocol and analysis, no claim-grade Ramsey/T2star/13C signature is resolved.

## Recommended Next Action

- Do not run another blind Ramsey repeat on r03.
- Treat the r03 Ramsey/13C branch as unsupported under the current Ramsey protocol unless a deliberately different protocol is chosen.
- Recommended branch decision: either move to an alternate coherence protocol designed to separate reference/readout artifacts from NV phase evolution, or close r03 with aligned pODMR supported but T2star/13C not supported.
