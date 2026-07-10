# Ramsey review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`, and prior short-tau design note `evidence/e017.md`.
- New Ramsey terminal data/metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: bridge job contract.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: final runtime status.
  - `measurement/m005.json`: run control.
- Generated local analysis artifacts:
  - `analyze_ramsey.py`
  - `ramsey_shorttau_metrics.txt`
  - `ramsey_shorttau_review.png`

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` with shape `1 x 2 x 41` and `ExperimentDataEachAvg` with shape `1 x 12 x 2 x 41`.
- Used the terminal scan metadata: `tau = 0.048..1.968 us`, `41` points, `48 ns` spacing, `12` averages, `90000` repetitions per average, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Treated readout 1 as reference and readout 2 as Ramsey signal, consistent with the current project convention for `ramsey.xml` when no additional spin-state reference is present.
- Checked raw signal, raw reference, point-wise `signal/reference`, and signal normalized by a fitted linear reference baseline.
- Computed per-point SEM across the 12 stored averages.
- Ran least-squares sinusoid screens with constant + linear trend terms at:
  - programmed carrier: `1.000 MHz`
  - expected 13C sidebands from the project model: `0.615 MHz` and `1.385 MHz`
  - dense exploratory screens over frequency.
- Ran an FFT check after linear detrending and Hann windowing.

Key quantitative results:

- Mean reference/signal: `48.573 kcps` / `44.655 kcps`.
- Median signal SEM across averages: `1.138 kcps`; median ratio SEM: `0.01271`.
- Raw signal peak-to-peak over the short window: `6.499 kcps`; ratio peak-to-peak: `0.14327`.
- LS amplitude at `1.000 MHz`: raw signal `1.282 kcps` (`1.13 x` median raw SEM), ratio `0.02741` (`2.16 x` median ratio SEM), reference-line-normalized `0.02639`.
- LS amplitude at `0.615 MHz`: raw signal `1.103 kcps` (`0.97 x` median raw SEM), ratio `0.02430` (`1.91 x` median ratio SEM).
- LS amplitude at `1.385 MHz`: raw signal `1.220 kcps` (`1.07 x` median raw SEM), ratio `0.02710` (`2.13 x` median ratio SEM).
- Dense LS screen excluding very low frequency is largest near `1.20 MHz`: raw signal amplitude about `1.686 kcps`, ratio amplitude about `0.03635`.
- Detrended FFT has broad-bin maxima at `1.524 MHz` and `1.016 MHz`; frequency resolution is coarse because the window is only `1.92 us`.
- Per-average mean counts vary substantially and mostly common-mode: signal average means `37.47..51.21 kcps`, reference average means `42.02..55.19 kcps`. Final bridge text was `35.122 kcps`, lower than the recent pre-run count history.

## Plausible interpretation

- The short-tau/high-SNR diagnostic is analyzable and completed safely. The raw export contains enough structure to see weak early-time oscillatory content in raw and normalized views.
- The short-tau redesign did improve the early-time diagnostic compared with a blind long-window repeat: there is now weak-to-moderate normalized spectral weight near the intended `1 MHz` scale, and the FFT has nearby broad content.
- The strongest non-low-frequency LS feature is around `1.20 MHz`, not exactly the programmed `1.00 MHz` carrier and not the expected `0.615/1.385 MHz` 13C sideband pair. This is qualitatively similar to the previous det=1.0 MHz run's largest component near `1.178 MHz`.
- A cautious physical reading is that r03 may have a weak, short-lived Ramsey response with effective detuning near `1.0..1.2 MHz`, but the current evidence does not isolate whether this is true Ramsey precession, residual baseline/count drift, imperfect reference correction, pulse/sequence artifact, or noise-shaped structure.
- The common-mode average-to-average count variation and lower terminal final count weaken any claim based only on small normalized amplitudes.

## Claims not yet supported

- No claim-grade `T2*` value is supported. A fit would be model-dependent because the signal presence/frequency basis is still not clean enough.
- No supported nearby-13C conclusion is available from this dataset. The short window has poor sideband resolution, and the target `0.615/1.385 MHz` amplitudes are comparable to the carrier-scale weak features rather than a clean sideband pattern.
- Do not claim that the programmed `1.0 MHz` carrier was cleanly observed. It is present as a weak LS component, but the largest exploratory component is offset near `1.20 MHz`.
- Do not claim that the previous non-claim-grade `~1.18 MHz` feature is physical. This dataset makes it more interesting, but still not decisive.
- Do not claim that r03 is unsuitable as an aligned NV; prior pODMR evidence still supports r03 as aligned. The unsupported part is the Ramsey/T2star/13C conclusion under current conditions.

## Recommended next action

- Avoid another blind Ramsey repeat on r03.
- Run a bridge-free synthesis/design step before any more hardware: compare all three Ramsey datasets quantitatively on the same raw/readout-aware pipeline, especially whether the `~1.18..1.20 MHz` feature persists with consistent phase/shape after controlling for reference drift and scan order.
- If hardware follow-up remains justified after that synthesis, use a discriminating protocol rather than accumulating another similar Ramsey trace. The most useful next measurement would either:
  - recalibrate the microwave resonance with weak-pi pODMR after the final-count drop, then run a phase-controlled/detuning-shift Ramsey pair designed to test whether the `~1.2 MHz` feature follows programmed detuning, or
  - switch to an alternate coherence/spectroscopy protocol suitable for weak/short-lived Ramsey contrast.
- Until that check is done, keep the project conclusion as: aligned r03 supported; `T2*` unsupported; nearby `13C` unsupported.
