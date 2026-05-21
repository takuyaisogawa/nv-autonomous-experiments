Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The XML shows full_expt = 0, so the optional "1 level reference" block is skipped. The active readouts are therefore:
- readout 1: detection immediately after optical polarization, used as the true 0-level/reference readout.
- readout 2: detection after rabi_pulse_mod_wait_time, used as the microwave-affected signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The sampled pulse duration remains 52 ns at the 250 MHz sample rate because it is already an integer number of 4 ns samples.

The raw readouts have a slow baseline drift, so I judged resonance from the signal readout relative to the reference readout. The combined signal-reference contrast has its strongest localized negative feature near 3.865 GHz, and the two per-average traces both show signal suppression relative to reference around 3.865-3.870 GHz. This looks like a weak but coherent pODMR resonance rather than random isolated readout scatter.
