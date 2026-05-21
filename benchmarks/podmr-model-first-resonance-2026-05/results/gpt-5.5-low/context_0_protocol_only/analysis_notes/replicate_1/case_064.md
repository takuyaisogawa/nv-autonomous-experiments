Sequence inspection:

- Active sequence: Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active readout roles: readout 1 is the true 0-level reference immediately after optical polarization; readout 2 is the detection after the modulated Rabi microwave pulse. The optional 1-level reference block is inactive because full_expt = 0.
- Pulse parameters used for the decision: mod_depth = 1, length_rabi_pulse = 52 ns, switch_delay = 100 ns, delay_wrt_1mus = 200 ns.

Data assessment:

The combined readouts are noisy and do not show a clear ODMR-like resonance feature. Readout 2 has one pronounced low point near the high-frequency side, while readout 1 has a separate high point near the middle of the scan; these features do not form a consistent paired contrast signature. The per-average overlay indicates substantial average-to-average scatter, with excursions that are not reproducibly localized at one frequency. Because the active measurement compares a 0-reference readout against a post-pulse readout, I would expect a resonance to appear as a stable frequency-dependent change in the post-pulse readout relative to the reference. That pattern is not convincing here.

Decision: resonance_absent.
