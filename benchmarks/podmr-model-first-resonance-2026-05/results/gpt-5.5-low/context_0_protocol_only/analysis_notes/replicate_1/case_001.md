Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- The first detection after adj_polarize is the true 0-level/reference readout.
- The 1-level reference block is inactive because full_expt = 0.
- The final detection after rabi_pulse_mod_wait_time is the microwave-pulse signal readout.

Pulse settings used for the active signal block:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, so a 52 ns pulse.
- mod_depth = 1 in the variable values, so full modulation depth for the Rabi pulse.
- do_adiabatic_inversion is true, but the adiabatic inversion code is inside the inactive full_expt block and is not used.

Assessment:
The combined raw readouts vary only by a few counts with no clear, reproducible ODMR-like contrast feature between the reference and signal readouts across the microwave-frequency scan. Readout 2 has a high excursion near 3.91-3.915 GHz, but this is upward rather than a clean pODMR dip and the two averages shown in the overlay are separated by drift/noise, especially in the same region. Readout 1 also lacks a matching feature. With only two averages and substantial average-to-average variation, the apparent structure is not reliable evidence of a resonance.

Decision: resonance_absent.
