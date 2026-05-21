Active sequence and roles:

- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect a true 0-level reference, then wait.
- full_expt is 0, so the optional 1-level reference block is inactive.
- The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection.
- Therefore readout 1 is the 0-level/reference fluorescence and readout 2 is the post-microwave-pulse fluorescence.

Pulse parameters:

- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns.
- mod_depth is 1 in the exported Variable_values.

Resonance assessment:

The post-pulse readout does not show a distinct, reproducible ODMR-like contrast feature relative to the reference readout. Both channels vary at the few-count level, with a broad downward trend and average-to-average scatter. There are local changes around several frequencies, but they are not isolated in the microwave-affected readout and are comparable to drift/noise seen in the reference and individual averages. The strongest apparent structures are not consistent enough across averages to identify a pODMR resonance.

Decision: resonance_absent.
