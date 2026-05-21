Sequence inspection:
- Active sequence name from the export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction flow performs adj_polarize, then detection, then waits. Because full_expt = 0, the optional 1-level reference branch is skipped. The sequence then applies rabi_pulse_mod_wait_time and performs a second detection.
- Therefore readout 1 is the bright/0-level reference after polarization, and readout 2 is the pODMR signal after the modulated Rabi microwave pulse.
- mod_depth is 1 in the recorded variable values.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MHz sample rate, giving a 52 ns active pulse duration.

Data assessment:
The absolute readouts contain substantial shot-to-shot and average-to-average baseline drift, so the relevant check is the contrast between the post-pulse signal readout and the preceding reference readout at the same scan point. The combined signal/reference ratio has its strongest localized dip at 3.855 GHz: readout 1 is high while readout 2 is low, giving a ratio near 0.913. This same scan point is also the deepest or near-deepest contrast dip in each individual average, which argues against a purely one-average fluctuation. Neighboring points are not uniformly low, so the feature is narrow and noisy, but the repeated contrast minimum is consistent with a pODMR resonance within this scan.

Decision: resonance_present.
