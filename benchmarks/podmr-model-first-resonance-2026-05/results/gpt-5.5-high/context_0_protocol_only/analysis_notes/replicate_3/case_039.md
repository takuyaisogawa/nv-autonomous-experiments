The provided sequence XML is Rabimodulated.xml. The active scan varies mw_freq from 3.825 GHz to 3.925 GHz. The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at the 250 MHz sample rate, and mod_depth = 1. The full_expt variable is 0, so the optional 1-level reference block is not executed despite do_adiabatic_inversion being true.

Readout role interpretation: the first detection after adj_polarize is the polarized/0-level reference readout. The second active detection follows the 52 ns modulated Rabi pulse and is the microwave-affected signal readout. Therefore the relevant pODMR contrast is the relation of the post-pulse readout to the reference across the microwave-frequency sweep.

The two combined raw readouts fluctuate at the few-count level without a stable, repeatable resonance-shaped feature. The signal-reference difference changes sign several times and includes isolated extrema, such as a low around 3.895 GHz followed immediately by a high around 3.905 GHz, rather than a coherent dip or peak over neighboring frequency points. With only two averages, the per-average overlays show comparable point-to-point scatter, so the visible structure is not convincing evidence of a pODMR resonance.

Decision: resonance absent.
