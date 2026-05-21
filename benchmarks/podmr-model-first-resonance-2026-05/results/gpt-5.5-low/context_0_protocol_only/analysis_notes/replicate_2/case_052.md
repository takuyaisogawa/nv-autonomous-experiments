Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML sets length_rabi_pulse to 52 ns and mod_depth to 1. full_expt is 0, so the optional 1-level reference block is inactive. The executed readout roles are therefore: first detection after optical polarization as the true 0-level/reference readout, then a modulated Rabi pulse, then the second detection as the pulse-affected signal readout.

The combined readouts and per-average overlays show fluctuations of a few counts, but there is no consistent, repeatable dip or peak in the signal relative to the reference at the same microwave frequency. Features near the low-frequency side and around 3.88-3.91 GHz are not stable across averages and are comparable to baseline scatter. I therefore do not identify a reliable pODMR resonance in this scan.
