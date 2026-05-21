Case podmr_008_2026-05-16-014743.

The provided sequence XML is Rabimodulated.xml. The active instructions first polarize and detect a true 0-level/reference readout, then wait. The optional 1-level reference branch is inactive because full_expt is set to 0, so the second acquired readout is the measurement after a rabi_pulse_mod_wait_time pulse. The microwave frequency is scanned by mw_freq. The modulated pulse uses length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, i.e. 52 ns, with mod_depth = 1 from the provided XML. Other relevant settings are freqIQ = 50 MHz, mw_ampl = -5 dBm, ampIQ = 5 dBm, delay_wrt_1mus = 0.2 us, and length_last_wait = 1 us.

Readout role interpretation: readout 1 is the true 0/reference fluorescence readout before the microwave pulse; readout 2 is the post-pulse signal readout. Because full_expt is inactive, there is no separate active 1-level calibration readout in this run.

The scan shows readout 1 remaining near roughly 40-43 counts across the frequency range, while readout 2 has a pronounced, localized dip near the middle of the scan around 3.875-3.880 GHz. The dip is much larger than the point-to-point variation elsewhere and appears in both averages, dropping from the surrounding low-40-count baseline to about 31-32 counts. This is the expected ODMR contrast signature for resonance in the pulse-modulated readout.

Decision: pODMR resonance is present.
