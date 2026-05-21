Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML has full_expt = 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is true. The executed readouts are therefore:

- readout 1: the initial "true 0 level reference" detection after adj_polarize and before the swept microwave pulse.
- readout 2: the signal detection after rabi_pulse_mod_wait_time.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate to 52 ns. The provided XML sets mod_depth = 1.

The combined readouts and the two per-average traces fluctuate around the same baseline without a reproducible dip or peak tied to the swept microwave frequency. Readout 2 does not show a clear, consistent pODMR contrast feature relative to the readout 1 reference; the apparent excursions are comparable to point-to-point and average-to-average noise. I therefore classify this scan as resonance_absent.
