Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout roles: the first detection after adj_polarize is the true 0-level/reference readout; the second detection follows the active microwave pulse and is the pODMR signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, rounded at 250 MS/s, mod_depth = 1, switch_delay = 100 ns.
- do_adiabatic_inversion is true as a variable, but the adiabatic inversion calls are inside the inactive full_expt block or commented out, so they are not part of the active measurement.

Data assessment:

The combined signal readout does not show a clear, localized ODMR resonance across the microwave-frequency sweep. Readout 2 is mildly structured and tends to be lower at higher frequency, but this appears as broad drift/noise rather than a distinct dip or peak at a consistent scan position. The per-average overlay shows strong opposite average-to-average baseline drift, so the combined traces are likely affected by drift cancellation and averaging artifacts. There is no robust resonance-shaped contrast between the reference and post-pulse readout.

Decision: resonance_absent.
