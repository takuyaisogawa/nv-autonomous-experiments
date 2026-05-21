Sequence review:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional "1 level reference" block is inactive.
- readout 1 is the true 0 level / polarized reference acquired after adj_polarize and detection, before the swept Rabi pulse.
- readout 2 is the signal readout acquired after rabi_pulse_mod_wait_time and detection.
- mod_depth is 1.
- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns; at 250 MS/s this is already aligned to a 4 ns sample grid.

Decision note:
Because readout 2 is the post-pulse signal, I looked for a frequency-localized depression of readout 2 relative to readout 1. The combined signal-reference contrast is near zero or positive at several off-feature points but becomes mostly negative across the central part of the sweep, especially around roughly 3.865-3.890 GHz, with additional negative contrast near 3.900-3.915 GHz. The individual averages are noisy and not perfectly repeatable point-by-point, but the broad negative contrast region is consistent with a pODMR response rather than only a single isolated outlier.

Prediction: resonance_present.
