Case podmr_035_2026-05-16-210045.

Sequence inspection:
- Active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.
- sample_rate is 250 MHz.
- length_rabi_pulse is 5.2e-08 s, rounded to 52 ns at the sample rate.
- mod_depth is 1 in the provided sequence XML and variable values.
- full_expt is 0, so the optional "Acquire 1 level reference" block is not active even though do_adiabatic_inversion is true.

Readout roles:
- Readout 1 is acquired immediately after adj_polarize and is the true 0-level laser/reference readout.
- Readout 2 is acquired after the active rabi_pulse_mod_wait_time pulse using the swept microwave frequency, and is the signal readout for the pODMR contrast.

Data assessment:
Both readouts show a gradual upward drift across the frequency sweep. The signal readout is usually below the reference readout, but the separation is noisy and not localized to a clear frequency. There is no consistent narrow dip or reproducible contrast feature across the two averages that stands out from the readout scatter and common drift. The apparent point-to-point variations are comparable to the per-average fluctuations, including isolated excursions that do not form a coherent resonance line.

Decision: resonance_absent.
