Sequence inspection:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first performs optical polarization and detection to acquire the true 0-level reference readout. The optional 1-level reference block is inactive because full_expt is 0, despite do_adiabatic_inversion being set. The experimental signal readout follows a rabi_pulse_mod_wait_time pulse and then detection.

Relevant pulse parameters:

- length_rabi_pulse: 5.2e-08 s, rounded at 250 MHz sample rate, so the active microwave pulse duration is 52 ns.
- mod_depth: 1 in the variable values used for this run.
- readout 1 role: 0-level reference / baseline fluorescence.
- readout 2 role: post-Rabi-pulse signal fluorescence.

Data assessment:

The raw readouts fluctuate at the level of roughly a few counts across the scan. The signal readout does not show a clean, localized and repeatable pODMR-like resonance feature relative to the reference. There are excursions near several scan points, but the per-average traces indicate these are not stable enough to identify a resonance: the apparent peaks and dips are inconsistent between the two averages and do not form a coherent single resonance shape. Since pODMR resonance should appear as a reproducible frequency-dependent fluorescence contrast feature in the signal readout, the evidence here is insufficient.

Decision: resonance_absent.
