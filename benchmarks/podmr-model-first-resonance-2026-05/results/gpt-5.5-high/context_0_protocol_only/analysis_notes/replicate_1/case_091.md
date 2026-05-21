The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect, then wait, then apply rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, then detect again. Since full_expt is 0, the optional 1-level reference branch is inactive. Therefore readout 1 is the polarized 0-level/pre-pulse reference, and readout 2 is the post-microwave-pulse signal readout.

The active microwave pulse duration is length_rabi_pulse = 52 ns, rounded at the 250 MHz sample rate to the same 52 ns duration, and mod_depth is 1. The post-pulse readout should show a frequency-localized contrast relative to the 0 reference if a pODMR resonance is present.

The combined readouts show only small, noisy differences between readout 2 and readout 1, with the signal-reference contrast changing sign repeatedly across the scan. The strongest deviations are isolated and are not reproduced consistently between the two averages at the same frequency. There is no stable dip, peak, or coherent resonance-shaped contrast feature across the swept microwave frequency range.

Decision: resonance_absent.
