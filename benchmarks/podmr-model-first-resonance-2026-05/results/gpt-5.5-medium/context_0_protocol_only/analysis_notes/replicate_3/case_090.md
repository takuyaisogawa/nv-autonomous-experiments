Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes and detects a true 0-level reference, then skips the optional 1-level reference because full_expt = 0. The active experiment readout after that is a Rabi-modulated microwave pulse followed by detection. Readout 1 is therefore the reference detection, and readout 2 is the MW-modulated detection. The sequence values show length_rabi_pulse = 52 ns and mod_depth = 1, with the pulse length rounded to the 250 MHz sample clock.

The combined readouts fluctuate around roughly the same count level. The largest readout2-readout1 differences are isolated single points, including a large negative point at the first scan point and a positive point near the third scan point, rather than a consistent resonance-shaped dip across neighboring frequencies. The per-average traces show substantial scatter and do not reproduce a stable contrast feature. There is a lower orange point near 3.905 GHz, but it is not supported by a corresponding repeated structure in both averages or by a clean local feature relative to the reference.

Decision: resonance_absent.
