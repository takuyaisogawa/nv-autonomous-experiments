Sequence inspection:

- Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed instruction order first performs adj_polarize followed by detection, producing the true 0-level reference readout.
- full_expt is 0, so the optional 1-level reference block is inactive and does not contribute a readout.
- The active pODMR measurement is then a rabi_pulse_mod_wait_time call followed by detection, producing the second readout.
- The pulse duration is length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- The exported variable values give mod_depth = 1 for the executed run.

Data assessment:

Readout 1 is the reference and remains in the mid-to-high 30s with no comparable narrow contrast feature. Readout 2 is the signal readout and shows a strong, localized fluorescence dip centered around 3.875-3.880 GHz, falling from the nearby mid/high 30s to about 27 counts in the combined data. The same dip appears in both per-average traces, so it is repeatable rather than a single-average fluctuation. This is consistent with a pODMR resonance.
