Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, full_expt is 0, so the active readouts are:
- readout 1: true 0-level reference after optical polarization and before the swept microwave pulse.
- readout 2: signal readout after rabi_pulse_mod_wait_time.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already an integer 13 samples after rounding. The provided XML gives mod_depth = 1.

The raw traces are noisy, but the signal/reference contrast is not random across the full sweep. The combined readout2/readout1 ratio has a sustained low region at the high-frequency side of the scan: about 0.947 at 3.905 GHz, 0.976 at 3.910 GHz, 0.972 at 3.915 GHz, and 0.954 at 3.920 GHz, followed by recovery to about 1.051 at 3.925 GHz. The same negative-contrast region appears in both per-average traces, whereas many other excursions are isolated single-point fluctuations.

Decision: resonance_present. The evidence is a reproducible normalized PL dip near 3.905-3.920 GHz in the readout taken after the active microwave pulse relative to the reference readout.
