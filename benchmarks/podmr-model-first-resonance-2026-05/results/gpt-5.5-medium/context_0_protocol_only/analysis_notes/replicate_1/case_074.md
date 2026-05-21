Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence XML has mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at the 250 MHz sample rate. Because full_expt = 0, the optional 1-level reference branch is skipped.

Readout roles: readout 1 is the detection immediately after optical polarization, serving as the true 0-level reference. Readout 2 is the detection after the rabi_pulse_mod_wait_time call, serving as the microwave-pulse signal readout.

The combined readouts show noisy point-to-point variation with readout 2 often below readout 1, but the contrast does not form a clear, reproducible pODMR resonance. The deepest combined relative dip occurs around 3.875 GHz, yet the per-average overlay indicates that this feature is not stable across averages and comparable fluctuations appear elsewhere in the scan. I therefore classify this case as resonance absent.
