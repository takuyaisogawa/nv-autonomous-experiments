Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, length_rabi_pulse is 5.2e-08 s, rounded at 250 MS/s to 52 ns. mod_depth is 1. full_expt is 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is true; no adiabatic inversion is executed in the active path.

Readout roles in the active path:
- readout 1 is the initial detection after optical polarization, before the microwave Rabi pulse, serving as the 0-level / baseline reference.
- readout 2 is the detection after the modulated 52 ns microwave pulse, serving as the microwave-affected signal readout.

The baseline readout remains fairly flat around the mid-30s across the sweep, while the signal readout shows a pronounced, localized dip near 3.875-3.880 GHz, dropping to roughly 26 counts and recovering on both sides. The dip appears in both averages, though with noise, and is selective to the post-pulse readout rather than a shared baseline fluctuation.

Decision: resonance_present.
