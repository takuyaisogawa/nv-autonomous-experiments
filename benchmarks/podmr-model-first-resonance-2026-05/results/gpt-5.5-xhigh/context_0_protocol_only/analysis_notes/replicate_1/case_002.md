Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, full_expt = 0, so the optional 1-level reference block is inactive. The active readouts are:
- readout 1: true 0-level reference after optical polarization and detection, before the final microwave pulse.
- readout 2: signal readout after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.

The MW-applied signal readout drops well below the 0-level reference over a contiguous central region: at 3.870, 3.875, 3.880, and 3.885 GHz the signal-reference differences are about -5.08, -6.96, -6.96, and -5.62 counts, with ratios around 0.88, 0.84, 0.83, and 0.87. The feature is broader and stronger than the point-to-point fluctuations in the reference readout, and the per-average traces both contribute to a central trough near 3.875-3.880 GHz.

There is also a low endpoint at 3.925 GHz, but the contiguous central dip in the signal readout is the resonance-like feature expected for pODMR. I therefore classify this case as resonance_present.
