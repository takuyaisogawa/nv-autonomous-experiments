Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The active microwave pulse is rabi_pulse_mod_wait_time after the initial polarization/reference detection. The sequence has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. That leaves readout 1 as the true 0-level reference immediately after adj_polarize and readout 2 as the signal detection after the Rabi-modulated microwave pulse.

From the provided sequence XML, mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, i.e. 52 ns. At the 250 MHz sample rate this pulse length is already an integer 13 samples after rounding.

The post-pulse signal readout has a strong localized dip centered near 3.875-3.880 GHz, falling from roughly the low 42-count baseline to about 34.7-35.7 counts. This dip appears in both individual averages at the same frequency range, while the reference readout is comparatively not dominated by the same deep feature. That is consistent with a pODMR resonance being present.
