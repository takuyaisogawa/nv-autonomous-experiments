Case podmr_036_2026-05-16-211536.

The provided XML and raw export identify the active sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence polarizes, performs an initial detection, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by a second detection and final wait. Because full_expt = 0, the conditional 1-level reference block is skipped despite do_adiabatic_inversion being true. Thus readout 1 is the true 0-level polarized reference and readout 2 is the post-pulse signal readout.

The raw readouts fluctuate around roughly 50 counts with only two averages. The readout-2/readout-1 contrast has isolated excursions, including a positive spike near 3.840 GHz and negative points near 3.920-3.925 GHz, but these are not a coherent resonance dip or peak and are not consistently supported by the per-average traces. The variations look comparable to measurement scatter rather than a frequency-localized pODMR response from a single NV center.

Decision: resonance_absent.
