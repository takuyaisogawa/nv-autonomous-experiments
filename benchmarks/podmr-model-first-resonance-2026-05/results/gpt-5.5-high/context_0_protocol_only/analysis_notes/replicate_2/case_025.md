Active sequence: Rabimodulated.xml / Rabimodulated sequence while sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation:
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The first active detection occurs immediately after adj_polarize and is the true 0-level / polarized fluorescence reference.
- The second active detection occurs after rabi_pulse_mod_wait_time and is the microwave-driven pODMR signal readout.
- Variable values indicate length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence XML / exported variable values. The rabi pulse is rounded to the 250 MHz sample clock, still 52 ns.

Readout behavior:
The reference readout has a broad drift over the scan but no sharp dip around the central feature. The post-pulse signal readout shows a clear localized depression near 3.870-3.875 GHz, dropping from roughly 39-40 counts to about 31-33 counts in the combined data. The per-average overlay shows the same feature in the signal channel in both averages, while the reference channel mainly follows slow brightness drift.

Decision:
This is consistent with a pODMR resonance being present: the microwave-dependent post-pulse readout has a localized contrast feature relative to the polarized reference.
