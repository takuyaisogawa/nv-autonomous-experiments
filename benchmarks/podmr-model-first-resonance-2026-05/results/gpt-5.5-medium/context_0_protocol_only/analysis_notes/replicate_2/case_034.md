Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML enables channels [1 1 1 0 0 0], sets the microwave source, polarizes, detects a true 0-level reference, waits, then applies a modulated Rabi pulse and detects again. Because full_expt is 0, the optional 1-level reference block is skipped.

Readout roles:

Readout 1 is the true 0-level reference acquired immediately after optical polarization and before the microwave pulse. Readout 2 is the measurement after the active rabi_pulse_mod_wait_time call. The active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1, with switch_delay = 100 ns.

Resonance assessment:

For a pODMR resonance in this sequence, I would expect the post-pulse readout to show a coherent dip or contrast feature relative to the reference at the resonant microwave frequency. The two raw readouts fluctuate over the scan, but the contrast between readout 2 and readout 1 does not form a consistent resonance-shaped feature. The largest deviations are point-like or broad/noisy and are mixed with reference drift between the two averages. The per-average overlay also shows large average-to-average offsets, so the apparent combined features are not reliable evidence of a single NV pODMR resonance.

Decision: resonance_absent.
