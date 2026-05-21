Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect the true 0-level reference, skip the optional 1-level reference because full_expt = 0, then apply rabi_pulse_mod_wait_time followed by the signal detection. Thus readout 1 is the pre-microwave polarized reference and readout 2 is the post-rabi-pulse signal readout. The provided sequence has mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate, so the pulse duration is 52 ns.

The post-pulse readout does not show a stable ODMR-like dip or peak against the reference over the frequency sweep. The largest excursions are point-to-point fluctuations and differ between averages, with substantial per-average baseline offsets. The combined readouts cross and vary irregularly rather than showing a reproducible resonance-shaped contrast feature near a single frequency.

Decision: resonance_absent.
