Sequence/readout interpretation:

The provided sequence is Rabimodulated.xml. The active microwave pulse is
rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at
250 MHz to 52 ns. The provided sequence XML sets mod_depth = 1. The
full_expt variable is 0, so the optional 1-level reference block is skipped.

This leaves two active detection roles in each scan point:

1. Readout 1 is the true 0-level reference acquired after optical
   polarization, before the swept microwave Rabi pulse.
2. Readout 2 is the signal acquired after the 52 ns modulated Rabi pulse.

The scan sweeps mw_freq from 3.825 GHz to 3.925 GHz. A pODMR resonance would
normally appear as a localized and reproducible fluorescence contrast feature
in the post-pulse signal relative to the 0-reference. The combined traces are
noisy and show several alternating deviations, while the per-average overlay
shows substantial baseline offsets between averages. The low and high points
in the post-pulse readout are not consistent across averages and do not form a
clear, isolated resonance dip or peak over the sweep.

Decision: resonance_absent.
