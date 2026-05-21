Case podmr_023_2026-05-16-174219.

The provided sequence XML is Rabimodulated.xml. The active path first polarizes the NV and performs a detection before any microwave pulse; this readout is the true 0-level reference. The "Acquire 1 level reference" block is guarded by full_expt = 0, so it is inactive. The measured pODMR readout is the later detection following rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, and mod_depth = 1. The microwave frequency is the scanned variable from 3.825 GHz to 3.925 GHz.

Given those roles, a pODMR resonance should appear as a reproducible frequency-localized change in the post-pulse readout relative to the 0-reference, typically a dip for resonant transfer out of the bright state. The combined raw traces and the two per-average overlays show substantial drift and several isolated excursions. The post-pulse/reference contrast changes sign repeatedly, with candidate dips at different frequencies and comparable positive excursions nearby. These features are not consistent enough across the scan to identify a robust resonance.

Decision: resonance_absent.
