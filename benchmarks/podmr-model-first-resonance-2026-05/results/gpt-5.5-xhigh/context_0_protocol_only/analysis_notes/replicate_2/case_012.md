Sequence review:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional 1-level reference block is skipped.
- Readout 1 is the initial true 0-level reference after polarization and before the microwave pulse.
- Readout 2 is the signal readout after the modulated Rabi microwave pulse.
- mod_depth is 1 from the provided sequence variables.
- length_rabi_pulse is 52 ns; at 250 MS/s it remains 52 ns after sample-clock rounding.

Decision:

For a pulsed ODMR resonance in this active sequence, I would expect a reproducible frequency-localized change in the post-pulse signal readout relative to the 0-level reference, normally a dip in readout 2 relative to readout 1. The combined readouts show several isolated deviations, including negative contrast near about 3.860 GHz and 3.885 GHz, but the contrast changes sign across the scan and the per-average traces show substantial point-to-point scatter rather than a stable resonance-like feature. The raw readout 2 trace does not form a coherent line shape relative to readout 1.

Prediction: resonance_absent.
