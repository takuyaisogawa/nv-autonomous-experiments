# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Target Ramsey run metadata/control/status: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Raw savedexperiment export: `measurement/m001.json`.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_stdout.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py > ramsey_analysis_stdout.json`.
- Parsed `measurement/m001.json` raw arrays:
  - `tau = 0..8 us`, 41 points, `dt = 0.2 us`.
  - Nyquist `2.5 MHz`; FFT bin spacing from the 41-point record is about `0.122 MHz` (`1/8 us = 0.125 MHz` nominal design resolution).
  - `8` averages x `50000` repetitions; run completed with final counts `44.184 kcps`.
- Checked combined raw channels and point-wise normalized trace `ch1/ch0`.
- Computed Hann-window FFTs for raw `ch1` and normalized `ch1/ch0`.
- Ran least-squares sinusoid checks at diagnostic frequencies:
  - prior component: `0.884 MHz`
  - programmed detuning: `1.000 MHz`
  - expected det-13C sideband: `0.615 MHz`
  - expected det+13C sideband: `1.385 MHz`
- Fit a descriptive damped cosine with linear baseline to combined `ch1/ch0` and per-average `ch1/ch0`.

## Plausible interpretation

- The run completed and is analyzable; the counts are healthy and the scan is in tau order with snake acquisition recorded.
- The combined normalized trace has some oscillatory structure, but it is not a clean programmed-det Ramsey carrier:
  - Largest normalized FFT bins are near `1.098 MHz` and `1.220 MHz`; the `0.976 MHz` bin near the programmed `1.000 MHz` detuning is smaller.
  - Descriptive combined normalized damped-cosine fit gives `f = 1.187 +/- 0.027 MHz`, `T2star = 2.27 +/- 0.81 us`, `R2 = 0.486`.
  - This is a possible order-of-magnitude T2star indicator, not a final result.
- Fixed-frequency normalized least-squares checks are weak:
  - `0.884 MHz`: amplitude `0.0074`, `R2 = 0.035`
  - `1.000 MHz`: amplitude `0.0092`, `R2 = 0.053`
  - `0.615 MHz`: amplitude `0.0111`, `R2 = 0.074`
  - `1.385 MHz`: amplitude `0.0084`, `R2 = 0.046`
- Per-average normalized fits are inconsistent: fitted frequencies scatter across about `0.27, 1.10, 0.46, 1.22, 1.17, 0.62, 0.53, 1.36 MHz`, with low-to-moderate `R2`. This argues against treating the combined fit as claim-grade.
- The prior `~0.884 MHz` component from the first Ramsey scout is not reinforced here. That supports treating it as non-claim-grade and not yet physical.
- There is no clear, reproducible pair of sidebands at `det +/- f13C`; the weak bins near `0.615 MHz` and `1.385 MHz` do not survive per-average consistency checks.

## Claims not yet supported

- No well-supported final `T2star` value is established from this run.
- No supported 13C coupling conclusion is established.
- The combined fitted `T2star ~2.3 us` should not be reported as a project claim without caveats.
- The strongest combined spectral content near `1.1..1.2 MHz` should not be claimed as a calibrated Ramsey carrier without resolving the per-average inconsistency.
- The earlier `~0.884 MHz` feature should not be interpreted as a stable physical component.

## Recommended next action

Record this det-shifted Ramsey as analyzable but non-claim-grade. Do not claim T2star or 13C yet.

For the next experimental step, avoid a blind repeat. Use the diagnostic result to design a cleaner confirmation run: same accepted r03 and fine-pODMR center, but with acquisition split into shorter per-average jobs or otherwise improved drift/readout control, and predefine pass criteria requiring a reproducible carrier in individual averages plus sideband checks. If the goal is first to secure T2star, use a denser/shorter tau window around the observed decay scale before extending again for 13C FFT evidence.
