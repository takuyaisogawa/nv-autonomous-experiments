I used inputs/sequence.xml to identify the active sequence path before deciding.

The active sequence is Rabimodulated.xml. The sequence first acquires a true 0-level reference by polarizing and detecting. Because full_expt is 0, the optional 1-level reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, followed by detection. At the 250 MHz sample rate, the 52 ns pulse is 13 samples and does not change after rounding.

Readout 1 is therefore the polarized reference readout without the final microwave pulse. Readout 2 is the post-pulse signal readout after the 52 ns modulated Rabi microwave pulse.

The microwave frequency scan runs from 3.825 GHz to 3.925 GHz in 5 MHz steps. Readout 2 shows a strong localized reduction centered at 3.875 GHz: the combined readout falls to about 28.83 there, compared with neighboring and off-resonance values mostly in the mid-to-high 30s. The same dip is visible in both individual averages, while readout 1 stays comparatively flat and does not show a matching collapse. This frequency-localized contrast in the signal readout is consistent with a pODMR resonance.
