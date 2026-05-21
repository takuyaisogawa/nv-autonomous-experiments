Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the "Acquire 1 level reference" branch is inactive. The active readout order is therefore:
1. adj_polarize followed by detection: readout 1 is the bright/0-level reference.
2. rabi_pulse_mod_wait_time followed by detection: readout 2 is the microwave-affected signal.

The active microwave pulse uses length_rabi_pulse = 5.2e-08 s, which is 52 ns, with mod_depth = 1. The sample-rate rounding keeps the pulse at 52 ns for the 250 MHz sample rate.

Decision basis: readout 2 drops below readout 1 over a contiguous middle section of the mw_freq sweep, with the strongest combined contrast near 3.855 GHz and a broader negative-contrast region extending roughly from 3.850 to 3.885 GHz. The per-average traces are noisy, but both averages contribute negative signal-reference contrast in this region. This is consistent with a pODMR resonance rather than an isolated single-point fluctuation.
