Case podmr_014_2026-05-12-081841.

The provided sequence is Rabimodulated.xml. It sets up microwave excitation while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV and immediately performs detection, which is the true 0-level reference readout. The optional 1-level reference block is inactive because full_expt is 0, so the active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the experimental detection readout. Thus readout 1 is the reference after polarization, and readout 2 is the post-microwave-pulse pODMR signal readout.

The raw readouts do not show a stable, frequency-localized pODMR feature. Readout 2 fluctuates around the mid-40s with isolated excursions, including a low point near 3.91 GHz, but the per-average overlay shows that these excursions are not consistent between averages. Readout 1 also has comparable scatter and peaks/dips, indicating that the apparent features are dominated by noise or drift rather than microwave-frequency-dependent NV contrast.

Decision: resonance_absent.
