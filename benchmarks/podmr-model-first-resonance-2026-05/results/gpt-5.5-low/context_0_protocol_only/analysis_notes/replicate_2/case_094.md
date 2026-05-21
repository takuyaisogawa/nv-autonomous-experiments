Case podmr_080_2026-05-17-105113.

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect a true 0-level reference, then skip the 1-level reference because full_expt is 0. The active measurement pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns after sample-rate rounding, mod_depth = 1, switch_delay = 100 ns, followed by detection. Thus the two readouts are the reference detection and the post-microwave-pulse detection roles from the active pODMR sequence, not a full 0/1 reference pair.

The combined raw readouts are noisy and only two averages are available. A clear pODMR resonance would normally appear as a reproducible microwave-frequency-dependent fluorescence dip or contrast feature in the readout associated with the microwave pulse, ideally aligned between readouts/averages. Here the most prominent common feature is a positive excursion near 3.870 GHz rather than a dip. The lower points occur at different nearby frequencies and are comparable to the per-average scatter, with no convincing broad or repeatable resonance-shaped depression across the sweep.

Decision: resonance_absent. Confidence is low because the data are noisy and sparse, but the observed structure is not a reliable pODMR resonance.
