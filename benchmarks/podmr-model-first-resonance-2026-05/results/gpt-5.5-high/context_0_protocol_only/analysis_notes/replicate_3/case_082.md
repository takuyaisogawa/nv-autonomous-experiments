Case podmr_068_2026-05-17-075825.

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz in 5 MHz steps. The active pulse sequence first polarizes and detects a true 0-level/reference readout, then skips the optional 1-level reference because full_expt = 0. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Therefore readout 1 is the pre-pulse/reference PL channel and readout 2 is the post-modulated-Rabi-pulse signal channel.

The raw traces both fall strongly at the high-frequency end, especially around 3.920 to 3.925 GHz, which indicates a common-mode baseline or PL change rather than a pulse-specific pODMR resonance. Comparing readout 2 against readout 1 gives noisy point-to-point contrast with isolated deviations, but no reproducible localized dip or peak that is confined to the pulsed readout. The two averages also show substantial scatter, so the single-point contrast excursions are not enough evidence for a resonance.

Decision: resonance_absent.
