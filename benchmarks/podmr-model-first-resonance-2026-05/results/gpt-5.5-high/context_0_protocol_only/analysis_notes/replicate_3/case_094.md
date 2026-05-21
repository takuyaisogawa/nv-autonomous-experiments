Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is inactive.
- The active readouts are the initial polarized/detection reference before the Rabi pulse, followed by the detection after the modulated Rabi pulse.
- mod_depth is 1 in the provided sequence XML and variable values.
- The Rabi pulse duration is length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, rounded to the 250 MHz sample clock.

Resonance decision:
The microwave-dependent readout does not show a reproducible ODMR-like resonance. The combined post-pulse readout has point-to-point fluctuations and a few isolated low points, but these are comparable to the scatter in the reference readout and are not consistently reproduced between the two averages. The readout-2 minus readout-1 contrast changes sign across the sweep, with the strongest negative point near 3.895 GHz not supported as a coherent dip by neighboring points or by both averages. Therefore I classify this case as resonance absent.
