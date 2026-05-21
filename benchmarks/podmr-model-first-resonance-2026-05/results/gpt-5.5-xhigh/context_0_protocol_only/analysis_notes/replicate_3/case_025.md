Active sequence: Rabimodulated, scanned over mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The provided sequence has full_expt = 0, so the optional 1-level reference block is not active. The active readouts are therefore:

- readout 1: initial polarized "true 0 level" reference detection before the microwave pulse
- readout 2: detection after a rabi_pulse_mod_wait_time microwave pulse

Pulse settings from the provided sequence are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With the 250 MHz sample rate this remains a 52 ns pulse.

The post-pulse readout shows a strong local loss relative to the reference around 3.870-3.880 GHz, centered near 3.875 GHz. In the combined data, readout 2 falls from near parity with readout 1 to a ratio of about 0.824 at 3.870 GHz, 0.763 at 3.875 GHz, and 0.843 at 3.880 GHz, while neighboring off-resonant points are much closer to the reference. Both individual averages show the same dip in this frequency region, so the feature is not just a single-average fluctuation or simple baseline drift.

Decision: a pODMR resonance is present.
