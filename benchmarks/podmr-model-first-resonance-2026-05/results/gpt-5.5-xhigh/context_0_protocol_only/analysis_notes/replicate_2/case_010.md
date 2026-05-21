Sequence context:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. The XML sets sample_rate to 250 MHz, length_rabi_pulse to 5.2e-08 s, mod_depth to 1, full_expt to 0, delay_wrt_1mus to 2e-07 s, and pumping_time to 1e-06 s.

Because full_expt is 0, the optional "Acquire 1 level reference" block is inactive. The active readouts are therefore:

1. Readout 1: detection immediately after adj_polarize, serving as the bright/0-state reference.
2. Readout 2: detection after rabi_pulse_mod_wait_time with the 52 ns microwave pulse at mod_depth 1, serving as the microwave-affected signal.

Decision:

For a pODMR resonance in this sequence, the post-pulse signal should drop relative to the 0 reference when the microwave frequency is resonant. The combined signal-reference contrast is most negative at 3.855 GHz, where readout 2 is about 2.10 counts below readout 1, and this dip is present in both averages. The neighboring points at 3.850 and 3.860 GHz have positive contrast, making the 3.855 GHz feature a localized contrast dip rather than only a slow drift. Other points are noisy, but this repeated local dip is consistent with a pODMR resonance.

Prediction: resonance_present.
