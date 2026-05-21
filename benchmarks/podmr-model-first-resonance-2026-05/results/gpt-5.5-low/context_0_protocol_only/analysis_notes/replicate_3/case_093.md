Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, the active readout structure is:
- Readout 1 is acquired immediately after adj_polarize and is the true 0-level/reference fluorescence readout.
- full_expt is 0, so the optional 1-level reference branch is skipped.
- Readout 2 is acquired after rabi_pulse_mod_wait_time with length_rabi_pulse.

Sequence parameters used for interpretation:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, corresponding to 52 ns
- mw_freq is the swept parameter, with detuning 0

The relevant pODMR contrast is the post-microwave readout relative to the preceding 0-level reference. The combined traces show multiple point-to-point fluctuations, with isolated negative contrast near several frequencies and positive excursions elsewhere. There is no single reproducible dip or peak with a coherent line shape across the sweep. The per-average overlay shows substantial average-to-average scatter, and the apparent dips are not stable enough to identify a pODMR resonance.

Decision: resonance absent.
