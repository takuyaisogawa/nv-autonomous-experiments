The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence polarizes the NV, takes a detection readout as the true 0-level reference, waits, applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then takes the signal detection readout. full_expt = 0, so the optional 1-level reference block is skipped despite do_adiabatic_inversion being true.

Readout role interpretation:
- readout 1: pre-pulse true 0-level reference after optical polarization
- readout 2: post-modulated-Rabi-pulse signal readout

The combined readouts show only small, irregular contrast changes across the scanned microwave frequency range. Candidate excursions in readout2 relative to readout1 are not stable in the two per-average overlays; several large point-to-point changes are caused by only one average and do not form a reproducible dip or peak with a resonance-like line shape. There is no convincing frequency-localized pODMR feature.

Decision: resonance absent.
