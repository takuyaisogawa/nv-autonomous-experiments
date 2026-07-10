# Ramsey Review: det=1.5 MHz Short-Tau Shift Check

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective and prior decision state.
- `measurement/m001.json`: raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: submitted Ramsey contract, accepted r03 target metadata, and analysis intent.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal run/status/control records.
- Scratch outputs created here: `scratch/ramsey_detshift_analysis.json` and `scratch/ramsey_detshift_review.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python/numpy/scipy.
- Confirmed run geometry: `tau = 0.048..1.968 us`, 41 points, 48 ns spacing, 12 averages, 90000 repetitions per point.
- Treated readout channel 0 as signal and channel 1 as reference, consistent with prior raw-review convention; reviewed raw signal, reference, and signal/reference ratio.
- Computed per-point SEM from the 12 stored averages: median signal SEM `0.745 kcps`; median ratio SEM `0.0146`.
- Ran a simple common-mode drift check using average-wise `(signal_mean + reference_mean)/2`; deviations from median ranged from `-9.45%` to `+4.00%`, so no average crossed a broad `15%` flag threshold.
- Ran least-squares sinusoid screens with offset and linear baseline terms, plus an FFT check on detrended ratio data.
- Checked target frequencies:
  - Programmed det carrier `1.500 MHz`: ratio amplitude `0.0286`, raw-signal amplitude `0.037 kcps`, LS `R2 = 0.360`.
  - Det-tracking prediction from prior `~1.192 MHz` component: `1.692 MHz`, ratio amplitude `0.0298`, raw-signal amplitude `0.099 kcps`, LS `R2 = 0.409`.
  - Prior fixed component `1.192 MHz`: ratio amplitude `0.00594`, LS `R2 = 0.0207`.
  - Programmed 13C sideband positions `1.116/1.884 MHz`: ratio amplitudes `0.0128/0.0203`, LS `R2 = 0.080/0.182`.
  - Det-tracking sideband positions `1.307/2.076 MHz`: ratio amplitudes `0.0113/0.00681`, LS `R2 = 0.0596/0.0243`.
- Ramsey-band screen results:
  - Full low-frequency screen was dominated by a boundary/slow component near `0.2 MHz`, so it should not be interpreted as a Ramsey carrier.
  - Restricting to `0.8..2.5 MHz`, the combined-ratio maximum was near `0.858 MHz`.
  - Restricting to `1.0..2.3 MHz`, the combined-ratio maximum was near `1.614 MHz`, between the programmed `1.5 MHz` and det-tracking `1.692 MHz` expectations.
  - Per-average best frequencies over `0.8..2.5 MHz` were scattered (`~0.81, 0.87, 0.89, 1.17, 1.51, 1.66, 1.74, 1.77, 1.85, 1.96 MHz`), not a stable single component.
- Tried descriptive damped-sinusoid fits over `0.8..2.5 MHz`; fits were start-condition sensitive and sometimes stuck at the lower frequency bound, so they are not claim-grade. Starts near `1.5..1.692 MHz` gave descriptive frequencies `~1.62..1.65 MHz` and `T2star ~0.76..1.18 us`, but this is not robust enough to promote.

## Plausible interpretation

- The run completed cleanly: terminal status is `completed`, `incomplete=false`, final counts `44.796 kcps`, no stop request, and safe shutdown was reported.
- The det-shift diagnostic argues against the prior `~1.192 MHz` feature being a fixed artifact, because the fixed `1.192 MHz` target is weak in this run.
- There is some combined-data support for power in the `1.5..1.7 MHz` region after changing det to `1.5 MHz`, which is qualitatively more consistent with det-sensitive Ramsey content than with a fixed `1.192 MHz` component.
- However, the evidence is still weak: target raw-signal amplitudes are much smaller than the per-point signal SEM, the broad screen is contaminated by slow/boundary structure, and per-average best frequencies are inconsistent.

## Claims that are not yet supported

- No supported numerical T2star claim from this measurement. The descriptive `~0.8..1.2 us` fit scale is not robust enough because fit results depend on frequency window/start condition and the per-average frequency content is scattered.
- No supported nearby 13C claim. Neither programmed-det sidebands (`1.116/1.884 MHz`) nor det-tracking sidebands (`1.307/2.076 MHz`) form a clear, stable sideband pair.
- Do not claim that the r03 Ramsey carrier is definitively `1.5 MHz`, `1.61 MHz`, or `1.69 MHz`; the run only suggests possible det-sensitive content in that band.
- Do not close the broader project with a well-supported T2star/13C conclusion based on this dataset alone.

## Recommended next action

Stop blind Ramsey repeats on r03. Use this det-shift result as evidence that the prior fixed `1.192 MHz` artifact hypothesis is weakened, but the Ramsey/T2star/13C result remains non-claim-grade. The next action should be a deliberate branch decision: either switch to an alternate coherence/readout protocol designed to produce a cleaner short-time envelope, or document a supported negative/unsupported conclusion for r03 under the current Ramsey conditions and move to another candidate only if the project requires a claim-grade T2star/13C outcome.
