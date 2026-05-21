Case podmr_046_2026-05-16-235726

The provided sequence is Rabimodulated.xml. The active instructions first polarize and detect, giving the true 0-level/reference readout. Because full_expt = 0, the optional 1-level reference block is skipped. The second active detection follows rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, so the microwave-affected signal readout is after a 52 ns modulated Rabi pulse. The provided XML variable list gives mod_depth = 1.

The scan varies mw_freq from 3.825 GHz to 3.925 GHz. The two combined raw readouts are both noisy at the few-count level. The microwave-affected readout does not show a clear, localized, reproducible ODMR-like dip or peak relative to the reference; apparent excursions are comparable to average-to-average scatter and are not consistently mirrored as a resonance feature. Readout 1 also has substantial structure, indicating baseline/noise variation rather than a clean frequency-dependent spin contrast.

Decision: resonance absent. The data do not support a confident pODMR resonance in this sweep.
