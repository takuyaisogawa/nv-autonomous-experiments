Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is inactive despite do_adiabatic_inversion being set.
- Readout 1 is the initial true 0-level reference after polarization and before the microwave pulse.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time.
- mod_depth is 1.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Data assessment:

For this sequence, a pODMR resonance should appear as a coherent frequency-dependent contrast change in the post-pulse signal relative to the 0-level reference, typically a reproducible dip in readout 2/reference near resonance. The combined readout ratio has several isolated excursions, but they are not a stable single feature. The per-average contrasts are not reproducible: candidate dips such as near 3.885 GHz appear strongly in one average but not in the other, while other negative points occur elsewhere. The raw readouts are dominated by point-to-point scatter and average-to-average drift rather than a consistent resonance-shaped response.

Decision: resonance_absent.
