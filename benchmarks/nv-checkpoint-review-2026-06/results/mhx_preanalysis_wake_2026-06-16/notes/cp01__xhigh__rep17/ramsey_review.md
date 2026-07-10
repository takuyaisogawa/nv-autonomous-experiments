# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- Local guidance: `md/knowledge.md` Ramsey repeat and FFT guardrail notes.
- Prior r03 context: `evidence/e003.json` weak-pi pODMR raw review and `evidence/e005.json` Ramsey design/model note.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` bridge job; `measurement/m003.json` terminal result; `measurement/m004.json` terminal status; `measurement/m005.json` run control.

## Calculations/scripts run

- Created and ran `analyze_ramsey.py`.
- Generated `ramsey_analysis_summary.json` and `ramsey_analysis.png`; PNG was checked as a nonempty `1280 x 1440` image.
- Parsed `measurement/m001.json` as `ramsey.xml`, `tau = 0..6 us`, 31 points, `dt = 0.2 us`, 4 averages x 50000 repetitions.
- Used the inspected `full_experiment=0` readout convention from the local Ramsey design note: readout1 is the 0-level reference and readout2 is the Ramsey signal.
- Computed raw readout summaries, signal/reference ratios, scan-order drift scores using the stored snake scan order, damped-cosine fits, Hann-window FFTs after linear detrending, and per-average sinusoid consistency checks.

Key numeric checks:

- Run completed without abort; status elapsed time `2124 s`; final counts `38.249 kcps`, down from the weak-pODMR `43.890 kcps` but above the run gate.
- Raw reference mean/min/max: `45.318 / 44.038 / 47.942 kcps`; raw Ramsey signal mean/min/max: `42.098 / 38.096 / 45.846 kcps`.
- Mean stored-average `signal/reference` ratio: `0.9306`; peak-to-peak range `0.1357`; median ratio SEM `0.0256`.
- Scan-order common-mode drop scores by average: `0.000`, `0.0346`, `0.0303`, `0.000`; none exceed the prior `0.15` drift flag threshold, though average-to-average brightness shifts remain visible.
- Normalized damped-cosine fit: `T2* = 2.11 +/- 0.97 us`, frequency `0.900 +/- 0.042 MHz`, amplitude `0.075 +/- 0.028` in ratio units, `R2 = 0.390`, and weak BIC improvement vs a linear baseline (`Delta BIC = -1.24`).
- Raw-signal damped-cosine fit: `T2* = 1.77 +/- 0.81 us`, frequency `0.966 +/- 0.047 MHz`, `R2 = 0.463`, `Delta BIC = -5.36`.
- FFT of normalized ratio: top bin `0.968 MHz`, only `1.48x` the median nonzero FFT amplitude. The programmed `det=1.5 MHz` bin at `1.452 MHz` is `0.76x` median. Expected 13C sideband bins from the project model are near `1.129 MHz` and `1.935 MHz`; the lower bin is `0.79x` median and the upper bin is `1.33x` median, not a resolved pair.
- Per-average best single-frequency fits are inconsistent: `0.925`, `1.650`, `1.300`, and `0.855 MHz`. At fixed `0.968 MHz`, average 2 has almost no support (`R2 vs linear = 0.011`).

## Plausible interpretation

The Ramsey scout is analyzable and not a hardware/count-gate failure. It shows a weak, short-lived oscillatory component in the averaged readouts, with a provisional decay scale around `T2* ~ 2 us`.

This is not yet claim-grade. The dominant averaged FFT/fit frequency is near `0.9-1.0 MHz`, not the programmed `1.5 MHz` Ramsey carrier, and the stored averages do not support one common frequency cleanly. That mismatch could reflect residual frequency error, low SNR, short-window fitting ambiguity, or drift/brightness changes that are not large enough to hard-flag the run.

The FFT does not support a nearby 13C assignment. A single upper-sideband-like bin is present, but it is comparable to other bins and is not accompanied by a clear lower sideband or carrier structure.

## Claims not yet supported

- Do not claim a final numeric T2star for r03 from this scout. `T2* ~ 2 us` is only a provisional fit scale.
- Do not claim resolved 13C coupling or absence of 13C coupling.
- Do not claim the Ramsey carrier behavior validates exact resonance at `3.876 GHz`; the measured oscillation frequency is not centered on the programmed `det=1.5 MHz` expectation.
- Do not abandon r03 from this measurement alone; the run completed and still contains plausible Ramsey contrast.

## Recommended next action

Run one bounded Ramsey repeat on r03 after a fresh track/count check, increasing stored averages rather than repetitions or tau points because the per-average window is already near the drift cap. Keep the same validated `auto__ramsey` path and a Nyquist-safe grid unless a fresh weak-pi/frequency diagnostic gives a provenance-backed reason to change `mw_freq` or `det`. The repeat should test whether the `~0.9-1.0 MHz`, `~2 us` component persists across averages; if it remains non-claim-grade, stop blind Ramsey repeats and switch to a targeted frequency diagnostic before pursuing a 13C conclusion.
