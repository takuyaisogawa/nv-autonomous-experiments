Sequence metadata and roles:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, after rounding to the 250 MHz sample grid.
- full_expt = 0, so the optional 1-level reference branch is skipped despite do_adiabatic_inversion being true.
- Readout 1 is the 0-level/reference detection immediately after optical polarization and before the microwave pulse.
- Readout 2 is the signal detection after the modulated Rabi pulse.

Resonance assessment:
The relevant pODMR contrast is readout 1 minus readout 2, since the reference is acquired before the microwave pulse and the signal after it. The largest combined contrast occurs at 3.860 GHz, where readout 1 is 53.44 and readout 2 is 48.85, giving about 4.60 counts of contrast. This feature is also present in both individual averages: the same frequency has high contrast in each average, and readout 2 reaches a clear local/global low while readout 1 is elevated. Neighboring points are much lower in contrast, so the feature is narrow and noisy, but it is consistent enough across the two averages to call a pODMR resonance present.
