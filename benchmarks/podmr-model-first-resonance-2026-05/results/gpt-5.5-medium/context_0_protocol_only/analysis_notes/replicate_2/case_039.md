Case podmr_024_2026-05-16-175646.

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active microwave pulse: rabi_pulse_mod_wait_time after the first detection.
- full_expt = 0, so the optional 1-level reference block is skipped.
- Readout roles: readout 1 is the initial true 0-level reference detection after polarization; readout 2 is the detection after the modulated rabi pulse.
- mod_depth = 1 from Variable_values.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Assessment:
The combined raw traces are noisy and do not show a reproducible frequency-localized ODMR resonance. Readout 2 does not form a clear resonance-like dip relative to readout 1; its deviations alternate sign and include isolated high and low points. The per-average overlay indicates that the apparent variations are not stable between the two averages, especially around the lower point near 3.895 GHz and the higher points near 3.905-3.925 GHz. With only two averages and no consistent contrast feature across the scanned microwave frequency range, I judge the data as resonance absent.
