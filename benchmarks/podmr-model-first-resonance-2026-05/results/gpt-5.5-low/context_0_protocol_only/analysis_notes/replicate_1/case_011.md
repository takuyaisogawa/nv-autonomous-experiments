Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence XML sets length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at the 250 MHz sample rate, and mod_depth = 1. The sequence first polarizes and detects a true 0-level reference. Because full_expt = 0, the optional 1-level reference block is inactive. It then applies rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth, followed by the second detection. Thus readout 1 is the no-microwave reference and readout 2 is the microwave-pulse signal readout.

The reference readout is comparatively flat/noisy without a coherent dip. The signal readout shows a reproducible-looking depression around 3.900-3.905 GHz, reaching its lowest values near 3.905 GHz and recovering on the high-frequency side. With only two averages the trace is noisy, but the contrast appears primarily in the signal readout rather than both readouts, consistent with a pODMR resonance.

Decision: resonance_present.
