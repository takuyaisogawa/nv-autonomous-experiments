Sequence review:

The active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz. The provided sequence XML sets length_rabi_pulse = 5.2e-08 s, which is rounded at 250 MHz sample rate and remains 52 ns. The XML sets mod_depth = 1. full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. The active readout structure is therefore: optical polarization, detection of the true 0-level reference, wait, a modulated Rabi microwave pulse with the 52 ns duration and mod_depth 1, then detection of the post-pulse signal readout.

Data assessment:

The two combined raw readout traces remain close in magnitude, with point-to-point fluctuations and slow drift visible in the per-average overlay. There is no stable, localized dip or peak across the microwave frequency sweep that is coherent with the expected post-pulse signal relative to the reference. Several apparent excursions are isolated or alternate between neighboring points, and the per-average traces show large opposing drift rather than a reproducible resonance feature.

Decision:

I do not identify a pODMR resonance in this scan.
