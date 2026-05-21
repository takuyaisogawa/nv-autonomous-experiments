Used inputs/sequence.xml and the raw export for this case only.

Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active branch polarizes the NV, takes a first detection, waits, applies one modulated Rabi microwave pulse, then takes a second detection. Because full_expt = 0, the optional 1-level reference branch is not active.

Readout roles: readout 1 is the true 0-level optical reference after polarization and before the swept microwave pulse. Readout 2 is the post-microwave signal after the swept modulated Rabi pulse.

Pulse settings from the provided XML: length_rabi_pulse = 5.2e-08 s, which is 52 ns and exactly 13 samples at the 250 MHz sample rate after rounding. mod_depth = 1. The final wait is 1 us, the pump is 1 us, and the detection timing offset is 0.2 us.

For this active sequence, a pODMR resonance should appear as a localized drop of the post-pulse signal relative to the 0-level reference, preferably consistent across the two averages. The combined normalized post/reference trace has several isolated low points, including at the low-frequency edge and near 3.890 GHz, and it also rises above the reference near 3.905-3.910 GHz. The individual averages show strong drift and only weak consistency: the positive 3.905-3.910 feature has the wrong sign for a dark-state pODMR dip, while the negative points are not uniquely localized or cleanly repeated.

Decision: no reliable pODMR resonance is present in this scan.
