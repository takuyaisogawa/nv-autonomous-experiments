Case podmr_030_2026-05-13-160024.

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the active instructions, full_expt = 0, so the optional 1-level reference block is skipped. The remaining readouts are therefore:

- readout 1: detection immediately after adj_polarize, acting as the bright/polarized 0-level reference.
- readout 2: detection after rabi_pulse_mod_wait_time, acting as the microwave-pulse signal readout.

The microwave pulse uses length_rabi_pulse = 52 ns, rounded at the 250 MHz sample rate to the same 52 ns duration. The sequence XML sets mod_depth = 1, and the raw export variable table also records mod_depth = 1.

For a pODMR resonance in this sequence, I would expect a frequency-localized, repeatable change in the post-pulse signal relative to the polarized reference, usually a dip in fluorescence/contrast at resonance. The combined readouts are noisy: readout 2 alternates between being above and below readout 1, with isolated low ratios near 3.860, 3.885, and 3.915 GHz but also strong high ratios nearby such as 3.870, 3.895, and 3.925 GHz. The per-average overlay does not show a consistent feature reinforced across averages; the apparent extrema are not stable and look comparable to point-to-point noise/drift.

Decision: resonance_absent.
