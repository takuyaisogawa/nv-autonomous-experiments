Sequence and roles:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns after sample-rate rounding, mod_depth = 1, switch_delay = 100 ns, mw_ampl = -5 dBm, ampIQ = 5 dBm, and freqIQ = 50 MHz.

The full_expt variable is 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true. The active readout roles are therefore:

- readout 1: initial polarized no-MW "true 0 level" reference detection after adj_polarize.
- readout 2: detection after the modulated 52 ns rabi pulse, which is the pODMR-sensitive readout.

Data assessment:

The two combined raw readouts are noisy over only two averages. Readout 2 relative to readout 1 has point-to-point excursions, but they do not form a coherent resonance-like feature. The strongest positive differences occur at isolated frequencies around 3.865, 3.880, and 3.900 GHz, while negative differences also occur at isolated frequencies such as 3.825, 3.840, and 3.895 GHz. The per-average overlays show substantial scatter and no reproducible narrow or broad dip/peak across averages.

Decision:

No reliable pODMR resonance is present in this scan. The observed variations are better explained by noise and average-to-average scatter than by a consistent microwave-frequency-dependent resonance.
