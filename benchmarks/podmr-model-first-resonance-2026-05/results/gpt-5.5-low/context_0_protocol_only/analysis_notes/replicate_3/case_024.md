Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse before the signal detection is rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns, mw_ampl = -5 dBm, ampIQ = 5 dBm, and freqIQ = 50 MHz. full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true.

Readout roles:

Readout 1 is the initial detection after optical polarization, serving as the true 0-level/reference readout. Readout 2 is the detection after the modulated Rabi pulse and is the microwave-sensitive signal readout.

Data assessment:

Across the scan, readout 1 remains near roughly 28-31 counts without a comparable central dip. Readout 2 has a clear localized decrease from about 29 counts down to roughly 24 counts near 3.875-3.880 GHz, then recovers toward about 29 counts. The dip appears in the combined data and is consistent with microwave-frequency-dependent pODMR contrast rather than a shared optical/reference fluctuation.

Decision:

A pODMR resonance is present.
