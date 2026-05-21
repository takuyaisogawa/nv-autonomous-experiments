Sequence inspection:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- Pulse sequence flow: adjusted optical polarization, detection for the 0-level/reference readout, wait, optional 1-level reference block skipped because full_expt = 0, then a modulated Rabi microwave pulse followed by detection for the signal readout.
- Readout roles: readout 1 is the polarized/reference readout before the swept Rabi pulse; readout 2 is the readout after the swept microwave Rabi pulse.
- mod_depth is 1 from Variable_values in the provided export, and length_rabi_pulse is 5.2e-08 s, rounded at the 250 MHz sample rate to 52 ns.

Resonance assessment:

Both raw readouts show a broad downward drift over the frequency sweep, so the shared baseline is not by itself evidence of pODMR. The signal-reference contrast has a few point-to-point excursions, including negative excursions near 3.880 and 3.890 GHz, but these do not form a clean, reproducible ODMR dip or peak across neighboring frequencies or across the two averages. The per-average traces are noisy and differ strongly in their baseline trends, which makes the apparent isolated dips more consistent with noise/drift than with a single NV pODMR resonance.

Decision: resonance_absent.
