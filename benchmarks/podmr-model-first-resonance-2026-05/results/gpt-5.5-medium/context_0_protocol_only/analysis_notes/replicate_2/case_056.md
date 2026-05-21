Active sequence inspection:

The provided XML/raw export identifies the active sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The runtime variables list length_rabi_pulse = 5.2e-08 s, mod_depth = 1, full_expt = 0, and delay_wrt_1mus = 2e-07 s.

Because full_expt is zero, the conditional "Acquire 1 level reference" block is inactive. The active readouts are therefore:

1. Readout 1: after adj_polarize, before the Rabi pulse, serving as the bright/0-level reference.
2. Readout 2: after rabi_pulse_mod_wait_time using the 52 ns pulse and mod_depth 1, serving as the microwave-affected signal readout.

Decision:

The post-pulse readout shows a clear local minimum around the sweep center near 3.875 GHz, and both individual averages have negative signal-minus-reference contrast at that same point. Other points are noisy and there is some common drift in the reference channel, but the centered depletion in the microwave-affected readout is consistent with a pODMR resonance in this scan.
