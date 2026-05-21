Sequence review:

The provided XML is Rabimodulated.xml. The scan varies mw_freq across 3.825 to 3.925 GHz. The active sequence first polarizes and detects a true 0-level reference, waits, skips the 1-level reference block because full_expt = 0, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1 before the second detection. Thus readout 1 is the no-microwave 0-level reference and readout 2 is the signal after the 52 ns modulated microwave pulse.

Data assessment:

Readout 1 stays relatively flat around the mid to high 46-48 count range, with point-to-point noise but no matching broad dip. Readout 2 shows a pronounced, localized decrease around 3.870-3.880 GHz, falling to about 39 counts at the minimum while nearby off-resonance points return to about 46-48 counts. The same depression is visible in both per-average traces, so it is not just a single-average artifact. Because the contrast appears only in the pulse readout and is localized in frequency, this is consistent with a pODMR resonance.
