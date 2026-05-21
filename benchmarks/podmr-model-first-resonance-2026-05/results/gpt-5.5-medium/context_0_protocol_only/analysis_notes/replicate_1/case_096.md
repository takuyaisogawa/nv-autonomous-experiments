Case podmr_082_2026-05-17-111957.

The provided sequence XML is Rabimodulated.xml. It sweeps mw_freq over the scan while using a rabi_pulse_mod_wait_time block before the final detection. The active variables show length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, and mod_depth = 1. The full_expt variable is 0, so the conditional "1 level reference" block is not active. The two observed readouts therefore correspond to the initial true 0-level reference detection after optical polarization, followed by the measurement detection after the modulated 52 ns microwave pulse.

I treated readout 1 as the reference and readout 2 as the microwave-pulse signal. The raw traces are noisy with only two averages. The signal/reference contrast has both positive and negative excursions: prominent low points near 3.850 GHz and around 3.905-3.915 GHz, but also high points near 3.865 and 3.875 GHz. The per-average overlay does not show a stable common dip shape; the apparent features are comparable to average-to-average scatter and do not form a clear pODMR resonance.

Decision: resonance_absent.
