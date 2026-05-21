Active sequence and roles:

- The scan uses Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns after sample-rate rounding.
- mod_depth is 1.
- full_expt = 0, so the optional 1-level reference branch is disabled.
- The first detection after adj_polarize is the 0-level/reference readout without the Rabi pulse.
- The second detection follows the 52 ns Rabi-modulated microwave pulse and is the microwave-affected signal readout.

Resonance assessment:

The two combined readouts are noisy and mostly track broad/common fluctuations rather than showing a stable localized ODMR feature. The microwave-affected readout does not show a consistent, repeatable dip or peak relative to the reference across the frequency sweep; the sign and magnitude of signal-reference contrast fluctuate point to point, and the per-average traces show substantial average-to-average offset/drift. There are isolated excursions, but they are not coherent enough to identify a pODMR resonance.

Decision: resonance_absent.
