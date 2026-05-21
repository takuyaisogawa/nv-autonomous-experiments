The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets length_rabi_pulse to 52 ns and mod_depth to 1, with full_expt = 0, so the optional 1-level reference block is not active.

The executed detection order is therefore: optical polarization followed by a true 0-level reference detection, then a modulated Rabi pulse followed by the signal detection. Thus readout 1 is the 0-reference and readout 2 is the post-pulse pODMR signal.

Comparing the post-pulse readout against the reference, the strongest ODMR-like contrast appears near 3.920 GHz, where readout 2 drops well below readout 1. The same high-frequency local dip is visible in the per-average signal traces, though the scan is noisy and the feature is close to the scan edge. I interpret this as evidence that a pODMR resonance is present.
