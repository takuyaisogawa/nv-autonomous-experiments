Active sequence: Rabimodulated.xml / Rabimodulated pODMR scan with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From the provided sequence XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active microwave pulse duration is 52 ns.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive despite the adiabatic inversion boolean being set.
- Active readout roles are therefore the initial detection after adj_polarize as the true 0-level/reference readout, followed by the detection after rabi_pulse_mod_wait_time as the microwave-pulse signal readout.

Data assessment:
The two combined raw readouts fluctuate around roughly 50 counts with only two averages. The signal/readout after the modulated Rabi pulse does not show a clear, localized, reproducible pODMR resonance feature relative to the reference. Apparent excursions, such as the high point near 3.840 GHz and the low point near 3.920 GHz, are isolated and comparable to the average-to-average scatter visible in the per-average overlay. There is no consistent adjacent-point dip or peak across the scan that would support calling a resonance.

Decision: resonance_absent.
