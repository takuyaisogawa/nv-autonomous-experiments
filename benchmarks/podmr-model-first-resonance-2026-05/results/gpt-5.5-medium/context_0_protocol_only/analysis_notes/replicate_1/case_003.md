Case podmr_006_2026-05-11-020739.

The provided XML sequence is Rabimodulated with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active experiment uses sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, and full_expt = 0. The 52 ns pulse is unchanged by sample-rate rounding because it is 13 samples at 250 MHz.

Readout roles from the instructions:
- The first detection follows adj_polarize and is the true 0-level polarized reference.
- The optional 1-level reference branch is skipped because full_expt = 0.
- The second detection follows rabi_pulse_mod_wait_time using the swept microwave frequency, so it is the signal readout for the pODMR contrast.

The second readout has a clear localized drop around 3.875-3.885 GHz, reaching about 40.5 counts while nearby points are mostly in the mid-to-high 40s. This dip is present in the combined data and is supported by the per-average overlay, whereas the reference readout does not show the same sustained depression. This is consistent with a pODMR resonance.
