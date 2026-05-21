Sequence inspection:

- Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is not executed.
- The executed readouts are the initial detection after optical polarization, which acts as the bright/0 reference, followed by a detection after a modulated Rabi pulse, which is the microwave-addressed signal readout.
- mod_depth is 1 from the active variable values.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MS/s to 52 ns.

Data assessment:

The combined readouts fluctuate point-to-point with no narrow, repeatable ODMR-like dip or peak across the mw_freq sweep. The two averages show large opposing drift/trend structure, and the averaged traces do not reveal a consistent resonance feature shared between readout roles. The signal readout does not show a coherent contrast feature relative to the 0-reference readout that would support calling a pODMR resonance.

Decision: resonance absent.
