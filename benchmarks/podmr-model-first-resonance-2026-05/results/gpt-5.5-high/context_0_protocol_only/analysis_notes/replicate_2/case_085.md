Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The programmed microwave/Rabi pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- full_expt = 0, so the optional 1-level reference block is inactive.
- Readout 1 is the true 0-level reference acquired after optical polarization and before the microwave pulse.
- Readout 2 is the signal readout acquired after the 52 ns modulated microwave pulse.

Data assessment:
Both readouts show a broad upward baseline trend across the scan range. The difference between signal and reference changes sign several times and does not form a reproducible dip or peak at a consistent microwave frequency. The per-average overlay shows substantial average-to-average scatter, with individual averages not supporting a common resonance feature. There is no localized contrast feature that stands out from the baseline drift and noise.

Decision:
No pODMR resonance is evident in this measurement.
