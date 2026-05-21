Active sequence: Rabimodulated.xml, swept by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML shows a polarization/detection block first, labeled as the true 0-level reference. The optional 1-level reference block is inactive because full_expt = 0. The remaining active driven measurement is a rabi_pulse_mod_wait_time followed by detection. The pulse duration is length_rabi_pulse = 52 ns, with mod_depth = 1 in the provided sequence variable values.

Thus readout 1 is the bright/0 reference and readout 2 is the microwave-driven signal after the 52 ns modulated pulse. The driven readout shows a pronounced localized contrast loss relative to the reference near 3.895 GHz: combined readout 2 falls to about 45.38 while readout 1 is about 50.0, and this dip is visible in both per-average traces. Other fluctuations are noisy, but this repeated, frequency-localized drop is consistent with a pODMR resonance.

Decision: resonance_present.
