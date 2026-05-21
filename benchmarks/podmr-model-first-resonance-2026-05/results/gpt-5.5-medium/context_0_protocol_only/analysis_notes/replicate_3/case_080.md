Case podmr_066_2026-05-17-072831.

The provided sequence XML is Rabimodulated.xml, varying mw_freq. The active instruction path has full_expt = 0, so the optional "1 level reference" block is skipped even though do_adiabatic_inversion is true. The two acquired readouts are therefore:

- readout 1: true 0 level/reference detection after optical polarization.
- readout 2: detection after the modulated Rabi microwave pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this rounds to 13 samples, still 52 ns. The provided sequence XML sets mod_depth = 1.

The scan covers 3.825 to 3.925 GHz in 5 MHz steps. The post-pulse readout relative to the reference has a broad negative contrast in the central/high-frequency part of the sweep: r2-r1 reaches about -2.73 at 3.880 GHz, -3.06 at 3.890 GHz, and -2.94 at 3.910 GHz, with r2/r1 minima around 0.936-0.943 in the same region. Both individual averages show negative contrast around 3.88-3.89 GHz, although the data are noisy and only two averages are available.

Decision: a pODMR resonance is present. The evidence is a broad, repeatable depression of the post-pulse readout relative to the reference near 3.88-3.91 GHz, consistent with resonance-induced population change under the active Rabimodulated sequence.
