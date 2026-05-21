I used the provided sequence XML and raw export for this case only.

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence sets full_expt = 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is true. The active readouts are therefore:

1. A true 0-level reference after adj_polarize and detection, before the microwave rabi pulse.
2. A signal readout after rabi_pulse_mod_wait_time followed by detection.

The provided sequence XML has mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, which is rounded at 250 MS/s and remains a 52 ns pulse. The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).

The first readout is comparatively flat around the low 40s across the mw_freq sweep. The second readout shows a strong, localized fluorescence dip centered around approximately 3.875-3.880 GHz, falling from the low 40s to about 31-32 counts in the combined data. The same dip is visible in both individual averages, while the reference readout does not show a matching artifact of comparable size. Because the post-pulse signal readout has a reproducible, frequency-localized contrast dip against a stable reference, this is consistent with a pODMR resonance being present.
