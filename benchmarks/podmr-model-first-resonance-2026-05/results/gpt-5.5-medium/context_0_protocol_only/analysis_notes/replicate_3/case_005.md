Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout roles:
- The first detection occurs immediately after optical polarization and is the true 0 / bright reference readout.
- full_expt is 0, so the optional 1-level reference block is inactive.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection, which is the pulse-affected signal readout.

Decision basis:
The relevant pODMR observable is the signal readout relative to the pre-pulse reference. The combined contrast has some isolated positive excursions where the post-pulse signal is lower than the reference, notably near 3.840 GHz, 3.865 GHz, and toward the high-frequency edge. However, these features are point-like or edge-like rather than a coherent resonance dip, and the two per-average overlays are dominated by large opposite drifts with inconsistent feature strength. The raw signal trace itself does not show a clear reproducible ODMR line shape across the sweep.

Conclusion: resonance_absent.
