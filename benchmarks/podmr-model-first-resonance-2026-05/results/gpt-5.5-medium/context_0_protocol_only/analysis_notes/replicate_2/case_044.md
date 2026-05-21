Active sequence review:

The scan uses Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets length_rabi_pulse to 52 ns, mod_depth to 1, full_expt to 0, and do_adiabatic_inversion to true, but the adiabatic inversion code path is inside the skipped full_expt block. The active sequence therefore polarizes and detects a true 0-level reference, waits, applies rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth 1, then detects the post-pulse signal. The optional 1-level reference readout is not active because full_expt is zero.

Readout interpretation:

Readout 1 is the pre-microwave true 0-level reference. Readout 2 is the post-modulated-Rabi-pulse signal. A pODMR resonance should appear as a frequency-localized reduction of readout 2 relative to readout 1, or a corresponding dip in the post-pulse readout/contrast, rather than a label-dependent feature.

Decision:

The combined data show the clearest contrast dip at 3.895 GHz, where readout 2 is 49.81 versus readout 1 at 52.58, giving the lowest readout2/readout1 ratio in the scan, about 0.947. The neighboring point at 3.900 GHz recovers strongly. The per-average traces are noisy, but both readout-2 averages are low at this frequency compared with nearby high points, and the feature is consistent with the active pODMR readout role. I therefore classify this case as resonance present, with the caveat that the data are noisy and the feature is modest.
