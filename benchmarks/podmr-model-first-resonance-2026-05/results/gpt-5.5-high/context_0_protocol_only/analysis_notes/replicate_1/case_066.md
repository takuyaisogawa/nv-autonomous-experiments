Sequence and readout interpretation:

The active sequence is Rabimodulated.xml. In the provided sequence XML, full_expt is 0, so the optional 1-level reference block is inactive. The executed measurement pattern is:

1. adj_polarize
2. detection
3. wait_for_awg
4. rabi_pulse_mod_wait_time
5. detection
6. wait_for_awg

Thus readout 1 is the pre-microwave true-0/reference readout, and readout 2 is the post-microwave readout after the modulated Rabi pulse. The active pulse uses length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate, so the pulse duration remains 52 ns. The provided sequence XML sets mod_depth = 1.

Resonance assessment:

The combined raw traces show fluctuations and a broad drift-like change, but the reference readout also varies substantially over the sweep. A pODMR resonance should appear as a localized, reproducible change in the post-pulse readout relative to the reference. The readout2-readout1 contrast is noisy, with isolated low points and an endpoint excursion, and the per-average overlays show large opposing drift rather than a consistent resonance-shaped feature. Because the apparent dips are not cleanly separated from reference drift or repeated across averages, I do not identify a reliable pODMR resonance in this scan.
