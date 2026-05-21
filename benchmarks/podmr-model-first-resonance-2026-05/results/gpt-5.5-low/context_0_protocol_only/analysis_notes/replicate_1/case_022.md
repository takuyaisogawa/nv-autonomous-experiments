Active sequence and roles:

The sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first performs adj_polarize followed by detection, so readout 1 is the true 0-level reference. The optional 1-level reference block is disabled because full_expt = 0, despite do_adiabatic_inversion being true. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, followed by detection, so readout 2 is the microwave-pulse signal readout.

Signal assessment:

Readout 1 remains relatively stable around the mid-30s across the scan, with no comparable broad feature. Readout 2 shows a strong localized reduction centered around the 3.875-3.880 GHz region, dropping from the mid-30s to roughly 29 and 28.2 counts before recovering on both sides. The same dip is visible in the per-average traces, so it is not just a single averaged artifact. Because the pulse-on signal readout changes strongly while the reference readout does not, this is consistent with a pODMR resonance.

Decision: resonance_present.
