Case podmr_007_2026-05-11-064944.

I used the provided sequence XML and raw export rather than labels or external context. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variable values give length_rabi_pulse = 52 ns and mod_depth = 1. full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped. The active readouts are therefore the initial detection after adj_polarize, used as the true 0-level reference/readout 1, and the final detection after rabi_pulse_mod_wait_time with the swept microwave frequency, used as the driven readout/readout 2.

The readout levels are noisy at about 30 to 34.5 counts with only two averages. The final driven readout does not show a coherent pODMR resonance shape relative to the reference readout. Differences between readout 2 and readout 1 alternate in sign across the sweep, with isolated large negative points near 3.855 and 3.895 GHz and isolated positive points near 3.845, 3.915, and 3.925 GHz. The per-average overlay indicates that these features are not reproducible between averages and are consistent with shot/noise fluctuations rather than a stable resonance dip or peak.

Decision: resonance_absent.
