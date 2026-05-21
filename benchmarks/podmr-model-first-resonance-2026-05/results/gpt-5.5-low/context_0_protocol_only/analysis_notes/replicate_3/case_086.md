Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Pulse flow: adj_polarize followed by detection for the true 0-level reference, then wait. The 1-level reference block is skipped because full_expt = 0. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection.
- Readout roles: readout 1 is the no-microwave true 0-level reference. readout 2 is the post-modulated-Rabi-pulse signal readout.
- mod_depth: 1.
- Pulse duration: length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Resonance assessment:

The signal readout is generally offset below the reference by about 0.63 counts on average, but the contrast fluctuates irregularly across the scan. The largest negative differences occur at several separated points, including the low-frequency side and the high-frequency endpoint, while nearby points often recover or change sign. Per-average overlays show substantial average-to-average scatter, and the combined traces do not show a reproducible frequency-localized ODMR dip or coherent resonance shape around the scanned range. Therefore I classify this case as resonance_absent.
