Active sequence:
- SequenceName is Rabimodulated.xml and the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, and mod_depth = 1. The 52 ns pulse is unchanged by the sample-rate rounding because it is 13 samples at 250 MHz.
- full_expt = 0, so the optional 1-level reference block is skipped. do_adiabatic_inversion is set true, but the active instructions do not run adiabatic inversion in this case.

Readout roles:
- Readout 1 is the first detection after adj_polarize, before the swept microwave Rabi pulse. This is the true 0-level/reference readout.
- Readout 2 is the detection after rabi_pulse_mod_wait_time using the 52 ns pulse and mod_depth = 1. This is the swept microwave signal readout.

Resonance assessment:
The raw readouts are noisy and there are only two averages, but the role-aware contrast between the post-pulse signal and the reference has a localized feature near 3.875 GHz. At that point readout 2 is 58.06 while readout 1 is 54.12, a difference of about 3.94 counts. The same positive contrast appears in both individual averages at the same frequency, so it is not only a single-average fluctuation. This frequency-localized response after the active microwave pulse is consistent with a pODMR resonance being present.
