Case podmr_005_2026-05-10-173726.

The provided XML is Rabimodulated.xml with mw_freq as the scanned variable. The active sequence first polarizes and detects a true 0-level reference, waits, skips the optional 1-level reference block because full_expt = 0, then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth before a second detection. Therefore readout 1 is the 0/reference readout and readout 2 is the post-microwave-pulse signal readout.

Relevant pulse settings from the provided sequence are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At sample_rate = 250000000 Hz this is 13 samples, so the rounded pulse duration remains 52 ns.

The combined post-pulse readout shows a clear multi-point dip across the central part of the scan, falling from roughly 42 counts to about 35 counts near 3.88 GHz, while the reference readout remains comparatively flat and does not contain the same broad trough. The per-average traces show that the post-pulse dip around the same region is present in both averages, so it is not just a single-average spike. There is also an edge drop at the high-frequency end, but the central repeated trough is the stronger pODMR-like feature.

Decision: resonance_present.
