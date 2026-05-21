Sequence inspection:
- The active scan sequence is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In sequence.xml, full_expt is 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true.
- The active readouts are therefore: readout 1 after polarization as the true 0-level / pre-microwave reference, then readout 2 after the microwave pulse as the pODMR signal.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- mod_depth is 1. The pulse duration length_rabi_pulse is 5.2e-08 s, and at 250 MHz sample rate it rounds to 13 samples, still 52 ns.

Data assessment:
The two averages have a strong brightness offset between averages, so the raw combined traces contain drift/noise comparable to or larger than small spectral features. The post-pulse readout does not show a clean frequency-localized dip or peak that is reproduced as a coherent pODMR line. The largest normalized contrast occurs at about 3.920 GHz, but it is an isolated single-point feature and is strongly influenced by a high excursion of the reference readout rather than a broad or stable decrease in the post-pulse signal. Neighboring points do not support a resonant lineshape expected for a 52 ns microwave pulse.

Decision: resonance_absent.
