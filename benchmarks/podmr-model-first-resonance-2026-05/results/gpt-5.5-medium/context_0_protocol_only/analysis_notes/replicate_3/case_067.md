Sequence inspection:

- The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The saved variable values give mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, which is 52 ns. The pulse length is rounded to the 250 MHz sample clock, still 52 ns.
- full_expt = 0, so the optional 1-level reference block is inactive despite do_adiabatic_inversion being true.
- The executed detection order is: laser polarization, detection before the microwave pulse, wait, modulated Rabi pulse, detection after the microwave pulse, final wait.
- Therefore readout 1 is the pre-pulse 0-level/reference readout, and readout 2 is the post-pulse signal readout after the modulated microwave pulse.

Data assessment:

The two combined readouts are noisy and there is scan-to-scan baseline variation, but the signal readout is locally suppressed relative to the reference at about 3.880 GHz and again near 3.890 GHz. The strongest signal-reference differences are around -3.29 counts at 3.880 GHz and -3.23 counts at 3.890 GHz, while many other points are closer to zero or positive. This creates a localized pODMR-like contrast dip in the post-pulse signal relative to the reference, rather than only a shared drift in both readouts.

Decision: resonance_present.
