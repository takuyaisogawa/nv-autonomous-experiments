Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active microwave pulse: rabi_pulse_mod_wait_time after the initial reference readout.
- Pulse duration: length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- mod_depth: 1 from Variable_values.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true.

Readout roles:
- readout 1 is the initial detection after adj_polarize, serving as the true 0-level/reference readout.
- readout 2 is the detection after the 52 ns modulated Rabi pulse, serving as the signal readout for the pODMR scan.

Resonance decision:
The combined traces and the per-average overlay do not show a stable, reproducible ODMR-like contrast feature across the frequency sweep. Apparent excursions such as the readout 2 high point near 3.84 GHz and the low point near 3.92 GHz are not supported by both averages and are comparable to the scatter between averages. The two readout channels also do not show a coherent differential dip or peak at a consistent frequency. I therefore classify this case as resonance_absent.
