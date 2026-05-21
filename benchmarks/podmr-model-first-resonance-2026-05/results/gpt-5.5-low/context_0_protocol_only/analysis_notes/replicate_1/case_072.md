Sequence inspection:

The active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed path has full_expt = 0, so the optional 1-level reference block is skipped. The sequence first polarizes and detects the true 0-level reference, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection. Thus readout 1 is the no-microwave reference level and readout 2 is the readout after the 52 ns modulated microwave pulse.

Resonance assessment:

For pODMR I expect a frequency-localized contrast feature in the pulse readout relative to the reference, normally a reproducible dip or peak over a small frequency interval rather than broad run-to-run scatter. The combined traces are noisy and the two averages differ strongly. Readout 2 has a high excursion near 3.895-3.905 GHz and low points near the edges, but these are not a stable, isolated resonance-shaped feature in the per-average overlay. The contrast between readout 2 and the reference changes sign and is dominated by average-dependent fluctuations rather than a coherent pODMR line.

Decision: resonance_absent.
