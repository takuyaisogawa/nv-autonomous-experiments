Active sequence identified from inputs/sequence.xml and raw_export.json: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction path first polarizes and detects the true 0-level reference, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection. The full_expt variable is 0, so the optional 1-level reference block is not executed despite do_adiabatic_inversion being true.

Readout roles: readout 1 is the pre-microwave polarized/reference detection; readout 2 is the post-Rabi-pulse detection used to test microwave-frequency-dependent response. For a pODMR resonance I would expect a coherent frequency-localized contrast feature between these readouts, typically a dip or structured contrast around resonance rather than independent point-to-point scatter.

The combined readouts fluctuate over the scan without a stable, localized contrast signature. Readout 2 is often above readout 1 and has isolated high points near roughly 3.86 and 3.905 GHz, but these are peak-like and not consistently supported as a resonance dip by both averages. The per-average traces show broad scatter and average-dependent variation rather than a reproducible pODMR resonance feature.

Decision: resonance_absent.
