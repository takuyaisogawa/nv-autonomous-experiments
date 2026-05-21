Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence, varying mw_freq from 3.825 GHz to 3.925 GHz.

Sequence interpretation from inputs/sequence.xml:
- sample_rate = 250 MHz, so the 52 ns Rabi pulse is exactly 13 samples after rounding.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1 in the provided XML/variable values.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true.
- Readout role 1: after adj_polarize and before the Rabi pulse, this is the true 0-level / bright reference.
- Readout role 2: after rabi_pulse_mod_wait_time, this is the microwave-pulse signal readout.

Resonance assessment:
The post-pulse signal readout does not show a clear, reproducible pODMR resonance dip relative to the pre-pulse reference across the microwave-frequency scan. Apparent excursions are comparable to average-to-average scatter, and the strongest visible structure around roughly 3.90 GHz is mainly in the reference readout rather than a coherent signal contrast feature. The two averages do not support a stable resonance-shaped response.

Decision: resonance_absent.
