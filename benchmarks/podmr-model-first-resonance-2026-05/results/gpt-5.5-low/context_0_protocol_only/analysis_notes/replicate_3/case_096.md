Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active channels: ch_on = [1 1 1 0 0 0].
- The sequence first performs adj_polarize, then detection: this is the true 0-level reference readout.
- full_expt = 0, so the optional 1-level reference block is inactive.
- The active microwave manipulation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. This second readout is the pODMR signal readout after the MW pulse.

Data assessment:

The signal readout is noisy, but it shows a localized depression relative to the 0-reference in the high-frequency part of the scan. The strongest and most repeated contrast occurs around 3.895-3.915 GHz, especially near 3.905 GHz where the combined signal is about 2.44 counts below the reference. Both individual averages also show low signal readout at 3.905 GHz. This is consistent with a pODMR resonance rather than only unstructured readout scatter.

Decision: resonance_present.
