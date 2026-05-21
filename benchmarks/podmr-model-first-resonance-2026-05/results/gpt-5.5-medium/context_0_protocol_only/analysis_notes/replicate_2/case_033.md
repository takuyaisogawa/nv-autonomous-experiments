Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML sets length_rabi_pulse = 5.2e-08 s, which is 52 ns after sample-rate rounding at 250 MHz, and mod_depth = 1. full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. The active readouts are therefore the initial detection after polarization, serving as the true 0-level/reference readout, followed by the detection after rabi_pulse_mod_wait_time, serving as the driven signal readout.

The reference readout remains roughly flat near 47-50 counts across the sweep. The driven signal readout shows a clear, reproducible contrast dip centered near 3.875-3.880 GHz, dropping to about 39 counts while neighboring points recover toward the high-40s. Both averages show the same depression in the signal channel, while the reference channel does not show a matched drop. This frequency-localized dip in the driven readout relative to the reference is consistent with a pODMR resonance.

Decision: resonance_present.
