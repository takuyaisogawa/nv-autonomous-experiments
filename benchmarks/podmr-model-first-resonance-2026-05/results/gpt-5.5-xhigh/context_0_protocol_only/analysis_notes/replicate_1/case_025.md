Case podmr_010_2026-05-16-114624

I used the provided sequence XML before deciding. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables show sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, mod_depth = 1, switch_delay = 1e-07 s, and full_expt = 0. The 52 ns pulse is already aligned to the 4 ns sample period. Although do_adiabatic_inversion is true, the adiabatic inversion calls are commented and the 1-level reference branch is skipped because full_expt is zero.

The readout roles from the instruction order are:

1. First detection after adj_polarize: true 0-level reference, no microwave pulse immediately before it.
2. Second detection after rabi_pulse_mod_wait_time: microwave-pulse readout using the 52 ns modulated Rabi pulse with mod_depth = 1.

There is no active 1-level reference readout in this run.

The microwave-pulse readout has a clear localized drop near 3.870-3.880 GHz, reaching about 31.19 at 3.875 GHz after being near 39-40 on the lower-frequency side and then recovering toward about 37.9 by 3.890 GHz. The 0-reference readout does not show the same narrow minimum at the center; at 3.875 GHz it is about 40.90. The per-average traces also show the signal-readout dip at the same frequency region in both averages, even though the absolute baselines differ.

The scan has background drift, especially at higher frequency, but the role-consistent, localized reduction in the post-pulse readout relative to the 0-reference is stronger than the drift. I classify this as a pODMR resonance present.
