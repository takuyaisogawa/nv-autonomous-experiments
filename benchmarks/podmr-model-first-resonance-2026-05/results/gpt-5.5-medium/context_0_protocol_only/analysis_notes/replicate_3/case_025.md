Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825e9 to 3.925e9 Hz in 5 MHz steps. The executed variables include length_rabi_pulse = 5.2e-08 s and mod_depth = 1. The full_expt variable is 0, so the conditional one-level reference block is skipped.

Readout roles:

Readout 1 is the detection immediately after adj_polarize, so it is the polarized/0-level reference for each frequency point. Readout 2 is the detection after the rabi_pulse_mod_wait_time call using length_rabi_pulse and mod_depth, so it is the microwave-driven pODMR signal readout.

Data assessment:

The signal readout has a clear localized dip near the middle of the mw_freq sweep, with combined readout 2 falling from about 39 before the feature to about 31.2 at the minimum and then recovering. Readout 1 does not show a matching sharp local dip at the same point, although both readouts have broader drift across the scan. The per-average overlay also shows the same frequency-localized depression in the post-pulse signal channel, especially around the central scan points.

Decision:

A pODMR resonance is present.
