Sequence assessment:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant variables are length_rabi_pulse = 52 ns and mod_depth = 1 in the provided XML / variable values. full_expt = 0, so the optional 1-level reference block is inactive.

Readout roles:

The first detection occurs immediately after optical polarization and is the true 0-level / polarized reference. The second detection occurs after rabi_pulse_mod_wait_time using the swept microwave frequency, 52 ns pulse duration, and mod_depth = 1, so it is the pODMR signal readout.

Data interpretation:

The signal readout shows its strongest negative contrast relative to the reference near 3.895 GHz: readout 2 is about 49.81 while readout 1 is about 52.58, giving a signal/reference ratio near 0.947. Neighboring points are closer to baseline, and the feature appears as a narrow dip in the post-pulse signal rather than a matching dip in the reference channel. With only two averages the data are noisy, but the readout-role-aware contrast is consistent with a pODMR resonance.
