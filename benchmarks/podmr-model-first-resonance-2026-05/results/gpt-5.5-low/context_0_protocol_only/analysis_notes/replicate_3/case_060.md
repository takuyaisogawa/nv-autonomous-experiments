Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML sequence first performs adj_polarize followed by detection, giving the true 0-level reference readout. The optional 1-level reference block is inactive because full_expt = 0, so the active measurement then applies rabi_pulse_mod_wait_time and performs a second detection. Thus readout 1 is the reference/background fluorescence and readout 2 is the post-microwave signal readout for the pODMR sweep.

Sequence parameters used for the decision: length_rabi_pulse is 5.2e-08 s, i.e. 52 ns before and after sample-rate rounding; mod_depth is 1 in the provided sequence XML and exported variable values; microwave amplitude is -5 dBm with IQ amplitude 5 dBm and freqIQ 50 MHz.

The raw readouts show strong point-to-point noise and drift. Normalizing the signal readout against the reference gives some isolated low points, for example near 3.860, 3.875, 3.885, 3.900, 3.915, and 3.925 GHz, but these are scattered rather than forming a single coherent pODMR dip or line shape. The two per-average traces also do not show a stable common resonance feature at the same frequency. Given the active readout roles and the lack of a reproducible, localized contrast feature, I decide that a pODMR resonance is absent.
