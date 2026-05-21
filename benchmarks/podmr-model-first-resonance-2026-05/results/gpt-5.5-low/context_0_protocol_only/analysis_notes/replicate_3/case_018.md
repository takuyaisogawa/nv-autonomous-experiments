Active sequence identification:

The supplied sequence is Rabimodulated.xml. It polarizes the NV, performs a detection readout for the true 0-level reference, waits, skips the optional 1-level reference block because full_expt = 0, then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth before a final detection readout.

Readout roles:

Readout 1 is the initial reference detection after optical polarization, before the scanned microwave pulse. Readout 2 is the signal detection after the rabi_pulse_mod_wait_time microwave pulse.

Pulse settings:

The sequence variables give length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at the 250 MHz sample rate. The exported variable values give mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Decision:

Readout 1 remains comparatively flat across the scan, while readout 2 has a pronounced localized reduction around 3.875 to 3.880 GHz, dropping from the high-30-count baseline to about 29 and 28 counts. The dip is visible in both per-average traces, indicating it is not just a single-average artifact. Because the signal readout after the microwave pulse shows a frequency-localized contrast feature relative to the reference readout, this measurement contains a pODMR resonance.
