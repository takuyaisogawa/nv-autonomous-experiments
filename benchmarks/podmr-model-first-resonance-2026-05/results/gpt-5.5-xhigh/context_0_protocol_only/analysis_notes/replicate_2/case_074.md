Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional 1-level reference block is not active. The readout roles are therefore:
- readout 1: true 0-level reference after optical polarization, before the microwave pulse.
- readout 2: signal readout after the modulated Rabi microwave pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounded duration is 13 samples, i.e. 52 ns. The mod_depth used by the active pulse is 1.

For the combined data, readout 2 relative to readout 1 has its lowest normalized point near 3.875 GHz, with ratio about 0.931 and difference about -3.64 counts. However, this feature is not stable across the two averages: the large dip at 3.875 GHz is mainly from one average, while the other average is near baseline there. Similar negative excursions appear at other frequencies such as 3.83, 3.86-3.865, 3.91, and 3.92 GHz. The raw traces look dominated by point-to-point noise and reference variation rather than a reproducible localized ODMR dip.

Decision: resonance_absent.
