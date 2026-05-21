Case podmr_007_2026-05-16-013306

I used only inputs/sequence.xml, inputs/raw_export.json, and the provided raw readout plot for this decision.

The active scan sequence is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence polarizes and detects first, then because full_expt is 0 it skips the optional 1-level reference block, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the second detection. Thus readout 1 is the polarized reference/background readout and readout 2 is the MW-pulsed pODMR-sensitive readout. The active pulse duration is 52 ns after sample-rate rounding at 250 MHz.

The combined readout 1 trace is mostly flat around 35-37 counts with no comparable feature. Readout 2 shows a pronounced trough centered around roughly 3.875-3.880 GHz, dropping from mid-30s counts to about 28-29 counts, and the per-average overlay shows this dip in both averages despite baseline offsets. This frequency-localized contrast in the pulsed readout relative to the reference is consistent with a pODMR resonance.

Decision: resonance_present.
