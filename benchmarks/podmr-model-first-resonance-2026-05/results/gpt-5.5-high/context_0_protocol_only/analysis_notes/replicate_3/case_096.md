Sequence XML review:

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided XML, length_rabi_pulse is 5.2e-08 s and is rounded at the 250 MHz sample rate, so the active microwave pulse duration remains 52 ns. mod_depth is 1. full_expt is 0, so the conditional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true.

Readout roles:

Readout 1 is the true 0-level optical reference: adj_polarize followed by detection, with no preceding microwave pulse. Readout 2 is the pODMR signal readout after rabi_pulse_mod_wait_time using the 52 ns pulse and mod_depth 1, followed by detection. Therefore the relevant resonance signature is a frequency-localized change in readout 2 relative to readout 1, especially a lower pulsed readout from microwave-driven population transfer out of the bright state.

Data assessment:

The raw traces are noisy with only two averages, and there are isolated positive excursions in readout 2 near 3.865 GHz and 3.875 GHz. However, the pulsed readout shows a localized negative contrast relative to the optical reference in the upper part of the scan, especially around 3.895 GHz to 3.915 GHz, with combined differences of roughly -1.8, -2.4, and -2.3 counts at 3.895, 3.905, and 3.915 GHz. This contrast is larger than the small point-to-point offsets over much of the scan and has the expected sign for an ODMR-like dip in the microwave-pulsed signal.

Decision:

A pODMR resonance is present, though the data quality is noisy and the feature is not cleanly isolated.
