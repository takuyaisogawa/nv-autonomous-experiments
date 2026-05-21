Case podmr_011_2026-05-16-120107.

The provided sequence is Rabimodulated.xml with mw_freq as the scanned variable. In the active instructions, full_expt is 0, so the optional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true. The sequence therefore performs an initial polarization and detection for the bright/reference readout, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection. The active pulse duration is rounded at 250 MS/s, remaining 52 ns.

Readout role interpretation: readout 1 is the pre-microwave reference/0-level detection; readout 2 is the post-microwave Rabi-modulated signal detection. The scan covers 3.825 to 3.925 GHz in 5 MHz steps with 2 averages.

The reference readout stays near 41-43 counts without a comparable central loss, while the post-pulse signal readout has a strong, localized dip from roughly 3.87 to 3.885 GHz, reaching about 33 counts near 3.88 GHz. This feature is present in both averages and is much larger than the reference drift/noise. Because the expected pODMR signature is a microwave-frequency-dependent loss in the post-pulse signal relative to the reference, this measurement contains a clear resonance.
