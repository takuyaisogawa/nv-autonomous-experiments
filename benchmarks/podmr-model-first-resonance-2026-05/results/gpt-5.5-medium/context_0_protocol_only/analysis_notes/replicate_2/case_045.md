Active sequence: Rabimodulated pODMR with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML enables channels 1-3, sets the microwave source, then acquires a polarized reference detection before the microwave pulse. Because full_expt is 0, the optional 1-level reference block is skipped. The final detection is taken after rabi_pulse_mod_wait_time, so readout 1 is the polarized reference and readout 2 is the microwave-pulse readout.

The active pulse uses length_rabi_pulse = 52 ns, rounded at the 250 MHz sample rate, and mod_depth = 1 according to the provided sequence variable values. The scan therefore tests whether this fixed 52 ns, fully modulated pulse produces a frequency-dependent fluorescence change.

The averaged raw traces do not show a stable resonance-like contrast. Readout 1 and readout 2 have nearly identical means, and the pointwise difference has mean about 0.007 counts with scatter about 1.39 counts. The largest apparent changes are isolated points, especially near the high-frequency end, and are not reproduced as a coherent dip across neighboring frequencies or consistently in both averages. The per-average overlays show broad offset/noise differences but no common resonance feature centered within the sweep.

Decision: resonance_absent.
