Sequence inspection:
- Active sequence: Rabimodulated.xml.
- The sequence first polarizes and detects, labelled in the XML as the true 0 level reference.
- full_expt is 0, so the optional 1 level reference block is skipped.
- The second active readout is after rabi_pulse_mod_wait_time, so it is the pODMR signal after the microwave pulse.
- mod_depth is 1 in the provided sequence XML.
- length_rabi_pulse is 5.2e-08 s, and at 250 MHz this remains a 52 ns pulse after sample rounding.

Readout assessment:
The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. Both readouts show a broad upward drift with point-to-point scatter. The signal/reference contrast has several isolated negative excursions, including around 3.830 GHz, 3.865 GHz, and the high-frequency end, but no single localized dip is cleanly reproduced as a resonance feature across the averages. The apparent dips are comparable to the per-average scatter and baseline drift rather than a coherent pODMR line.

Decision: resonance_absent.
