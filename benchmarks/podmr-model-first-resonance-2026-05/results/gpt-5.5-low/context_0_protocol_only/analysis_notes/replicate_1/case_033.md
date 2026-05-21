Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Relevant sequence settings from the provided XML/raw exported sequence values:
- full_expt = 0, so the optional "1 level reference" block is inactive.
- Readout 1 role: true 0-level/reference readout after adj_polarize and detection, before the microwave test pulse.
- Readout 2 role: signal readout after rabi_pulse_mod_wait_time followed by detection.
- mod_depth = 1 from the provided sequence XML variable values.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, equivalent to a 52 ns pulse.

Data assessment:
Readout 1 is relatively flat across the sweep, fluctuating around the high-40-count level without a narrow correlated dip. Readout 2 has a pronounced localized reduction centered near 3.875-3.880 GHz, dropping from the usual mid/high-40-count level to about 39 counts. The same dip is visible in the per-average overlay, so it is not just a single averaged trace artifact. Since the contrast appears in the post-pulse readout while the reference channel remains comparatively stable, this is consistent with a pODMR resonance.

Decision: resonance_present.
