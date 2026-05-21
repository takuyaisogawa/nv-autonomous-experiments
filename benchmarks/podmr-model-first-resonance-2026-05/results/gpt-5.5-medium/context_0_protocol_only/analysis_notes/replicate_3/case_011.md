Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first performs adj_polarize followed by detection, which is the true 0-level/reference readout. Because full_expt = 0, the optional 1-level reference block is inactive. The active microwave-dependent measurement is then a rabi_pulse_mod_wait_time pulse followed by detection, so the second acquired readout is the modulated signal readout after the pulse.

Relevant active parameters from the exported variable values are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, i.e. 52 ns. The plotted/ exported readout 2 signal has a pronounced local depression around 3.90 to 3.905 GHz, reaching about 24.1 counts, with recovery on the high-frequency side. This feature is stronger than the nearby reference fluctuations in readout 1 and is also visible in the per-average overlay, though the two averages are noisy.

Decision: resonance_present, with moderate confidence because the dip is localized and consistent with a pODMR contrast feature, but the data are noisy and only two averages are available.
