The provided sequence is Rabimodulated.xml. The active instructions set the microwave frequency from the swept mw_freq plus detuning, enable channels 1-3, then acquire a polarized reference readout before any swept microwave pulse. Because full_expt is 0, the optional 1-level reference block is not active, even though do_adiabatic_inversion is true. The active swept operation is therefore a single rabi_pulse_mod_wait_time followed by detection.

Readout role interpretation: readout 1 is the initial post-polarization reference detection, and readout 2 is the detection after the swept microwave Rabi-modulated pulse. The active mod_depth from the provided XML is 1, and length_rabi_pulse is 5.2e-08 s, rounded at 250 MHz sample rate, so the pulse duration remains 52 ns. The scan sweeps mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Both readouts have a shared upward drift across the scan, so the resonance decision should come from the post-pulse readout relative to the reference, not from the absolute level alone. The combined readout 2 trace shows localized suppression relative to readout 1, most clearly near 3.865 GHz, with another low point near 3.830 GHz. The per-average traces are noisy, but the post-pulse/reference contrast still shows localized negative excursions rather than only smooth drift.

Decision: resonance_present.
