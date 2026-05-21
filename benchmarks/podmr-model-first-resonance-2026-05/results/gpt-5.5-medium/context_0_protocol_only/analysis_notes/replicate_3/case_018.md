Case podmr_003_2026-05-16-003531.

The provided sequence is Rabimodulated.xml with mw_freq as the scanned variable. The active instructions first acquire a true 0-level reference after polarization and detection, then skip the 1-level reference block because full_expt = 0, then apply rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1 before the final detection. Thus readout 1 is the initial reference readout and readout 2 is the microwave-pulse signal readout.

The signal readout shows a pronounced, localized fluorescence dip centered around the 3.875-3.880 GHz region, dropping from the surrounding high-30s level to about 28-29, while the reference readout remains comparatively smooth and does not show a matching dip. This frequency-localized contrast in the post-pulse readout is consistent with a pODMR resonance being present.
