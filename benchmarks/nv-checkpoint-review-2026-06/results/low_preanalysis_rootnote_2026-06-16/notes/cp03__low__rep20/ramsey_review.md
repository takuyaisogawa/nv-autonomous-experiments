# Ramsey Review

## Files/Data Used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective and prior decision state.
- `md/memory.md`, `md/knowledge.md`: local NV/Ramsey review rules and interpretation cautions.
- `evidence/e017.md`: short-tau Ramsey design/start note.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: bridge job/spec/result/status/control metadata for the completed short-tau run.
- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.

## Calculations/Scripts Run

- Created and ran `scratch_ramsey_review.py`.
- Outputs:
  - `scratch_ramsey_review_summary.json`
  - `scratch_ramsey_review.png`
- Data shape check: combined data `[2, 41]`; per-average data `[12, 2, 41]`.
- Confirmed scan: `tau = 48 ns..1.968 us`, 41 points, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` repetitions, final counts `35.122 kcps`.
- Computed raw signal/reference traces, signal/reference ratio, stored-average SEM, least-squares sinusoid components with a linear baseline, and frequency screens from `0.3..3.0 MHz`.

## Plausible Interpretation

- The run completed and is analyzable, with no stop request or aborted execution in the provided metadata.
- The signal readout has a large slow early-time shape: readout 2 rises from about `40.7 kcps` at `48 ns` to about `47.2 kcps` near `1.34 us`, then falls toward `43.5 kcps` by `1.968 us`. The reference readout is comparatively flatter around `48.6 kcps`.
- The programmed `1.0 MHz` component is present only at marginal scale:
  - raw-signal LS amplitude at `1.0 MHz`: `1.28 kcps`
  - median per-tau stored-average SEM in raw signal: `1.14 kcps`
  - ratio LS amplitude at `1.0 MHz`: `0.0274`, with median ratio SEM `0.0127`
- The target 13C sideband checks are not distinctive:
  - raw-signal amplitudes: `0.615 MHz = 1.10 kcps`, `1.385 MHz = 1.22 kcps`
  - these are comparable to the `1.0 MHz` carrier and SEM scale, not a clean sideband pair.
- The largest prior-relevant non-target component remains stronger than the programmed carrier:
  - `1.178 MHz` raw-signal LS amplitude `1.68 kcps`, ratio amplitude `0.0362`
  - this resembles the earlier long-window issue where the largest screen was not at the programmed carrier or expected sidebands.
- Stored-average means show substantial common-mode changes across averages. Signal mean ranges from `37.47` to `51.21 kcps`; reference mean ranges from `42.02` to `55.19 kcps`. This is provenance for drift/brightness variation and makes small normalized spectral features less compelling.
- A very-short-T2star/early-time failure mode remains plausible because the short-tau trace has real early-time structure, but the structure is not yet separable into a robust Ramsey carrier with a defensible decay envelope.

## Claims Not Yet Supported

- No well-supported numeric T2star claim from this dataset.
- No well-supported nearby 13C claim from this dataset.
- Do not claim that the `1.0 MHz` programmed carrier is cleanly resolved; its amplitude is only near the raw SEM scale and is not the dominant frequency screen.
- Do not claim the `0.615/1.385 MHz` sidebands; they are not stronger or more coherent than nearby/competing components.
- Do not fit and promote a T2star value from the slow early-time shape alone; it could include baseline/readout/transient or drift contributions rather than only Ramsey dephasing.

## Recommended Next Action

Stop blind Ramsey repeats on r03 under the current Ramsey settings. The short-tau/high-SNR diagnostic did not produce a claim-grade carrier/sideband model. The next useful action is to switch protocol or run a targeted control that tests whether the slow early-time shape is sequence/readout/baseline artifact versus real spin coherence, for example a same-grid microwave-off or detuning/phase control if available in the local bridge workflow. If no such control is feasible, close the r03 Ramsey/T2star/13C branch as unsupported under current conditions while preserving the supported alignment/pODMR finding.
