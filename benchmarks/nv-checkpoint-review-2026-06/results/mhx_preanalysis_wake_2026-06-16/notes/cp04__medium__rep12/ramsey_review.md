# Ramsey Review: det-shift short-tau run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- New measurement metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` bridge status, `measurement/m005.json` bridge control.
- Prior context used from project state: accepted r03, fine weak-pi center `mw_freq = 3.8759 GHz`; prior short-tau det=1.0 MHz Ramsey had strongest empirical component near `1.192 MHz`; det-shift hypothesis expected a physical carrier-like component to move toward about `1.692 MHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs: `ramsey_detshift_analysis.json`, `ramsey_detshift_review.png`, `analysis_stdout.txt`.
- Raw export checks:
  - `ExperimentData` shape `[1, 2, 41]`; `ExperimentDataEachAvg` shape `[1, 12, 2, 41]`.
  - Per-average mean reproduces combined data to numerical precision (`~1.4e-14 kcps` max difference for both readouts).
  - Sequence XML in the raw export indicates readout 1 is the 0-level reference and readout 2 is the Ramsey signal because `full_experiment = 0`.
- Acquisition summary:
  - `tau = 0.048..1.968 us`, `48 ns` spacing, 41 points.
  - `12 averages x 90000 repetitions`, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`.
  - Terminal bridge result completed normally, final count `44.796 kcps`, no stop request.
- Quantitative screens:
  - Median SEM across stored averages: signal `0.711 kcps`, point-wise ratio `0.0126`.
  - Signal range over tau: `6.46 kcps`; reference range: `2.40 kcps`; ratio range: `0.134`.
  - Broad LS screen with linear baseline over `0.2..4 MHz` is dominated by the search-floor/slow-transient component at `0.2 MHz`, not a clean Ramsey carrier.
  - Target-band LS screen over `0.8..2.5 MHz` peaks near `0.857..0.878 MHz`, depending on view, again not at the programmed carrier or expected sidebands.
  - Target fits in point-wise ratio:
    - `1.500 MHz` programmed carrier amplitude `0.0240`.
    - `1.692 MHz` det-tracking-from-prior hypothesis amplitude `0.0250`.
    - `1.192 MHz` prior artifact-control amplitude `0.0051`.
    - `1.307 MHz` lower 13C sideband amplitude `0.0095`.
    - `2.076 MHz` upper 13C sideband amplitude `0.0062`.
  - Similar target fits in reference-line-normalized view: `1.500 MHz` amplitude `0.0235`, `1.692 MHz` amplitude `0.0255`, sidebands `<=0.0057`.
  - Per-average phase coherence in ratio fits is high at the programmed/det-shift frequencies (`~0.95..0.96`) and low for the prior `1.192 MHz` control (`~0.39`), but the target amplitudes are close together and the `1.92 us` span gives only about `0.52 MHz` Fourier resolution.

## Plausible interpretation

- The run completed safely and produced analyzable Ramsey data on the accepted r03 target.
- The prior fixed `~1.192 MHz` component is not reproduced strongly in the det=1.5 MHz run; that argues against simply promoting the earlier `1.192 MHz` feature as a stable physical Ramsey carrier.
- There is a weak coherent component in the `1.5..1.7 MHz` neighborhood, compatible with the det-shift target band in a limited sense. However, it is not the dominant empirical component, is only about twice the median ratio SEM, and the short time span cannot cleanly separate `1.500 MHz` from `1.692 MHz`.
- The 13C sideband targets near `1.307 MHz` and `2.076 MHz` are weak in both point-wise and reference-line-normalized checks.
- Best current read: the det-shift result is suggestive that the previous artifact-control frequency did not stay fixed, but it is still not claim-grade evidence for a clean programmed-carrier/sideband Ramsey model.

## Claims not yet supported

- No well-supported numeric `T2*` should be claimed from this run.
- No well-supported nearby `13C` conclusion should be claimed from this run.
- Do not claim that the prior `~1.192 MHz` feature cleanly tracked to `~1.692 MHz`; the data are too bandwidth-limited and baseline/transient dominated for that.
- Do not claim resolved 13C sidebands; the planned sideband amplitudes are below the carrier-neighborhood amplitudes and not dominant.

## Recommended next action

- Stop blind Ramsey repeats on r03 under this same short-tau/readout configuration.
- Make the next step an explicit branch decision: either move to an alternate protocol better suited to establishing T2*/13C under these conditions, or close the Ramsey branch as unsupported/non-claim-grade under current conditions.
- If continuing hardware work, first do a fresh tracking/resonance sanity check, then use an alternate protocol rather than another same-family Ramsey accumulation.
