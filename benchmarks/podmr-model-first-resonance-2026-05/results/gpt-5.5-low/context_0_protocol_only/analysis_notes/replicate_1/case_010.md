Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first performs adj_polarize followed by detection, which is the true 0-level reference readout. The optional 1-level reference block is skipped because full_expt = 0. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the reference and readout 2 is the microwave-pulse-affected pODMR signal.

The combined readouts are noisy and do not show a coherent, localized resonance contrast. The signal/reference ratio fluctuates above and below 1 across the scan, with isolated negative points near several unrelated frequencies rather than a consistent dip. The two per-average traces show large opposing baseline drift, so apparent features in the combined data are not reproducible enough to identify a resonance.

Decision: resonance_absent.
