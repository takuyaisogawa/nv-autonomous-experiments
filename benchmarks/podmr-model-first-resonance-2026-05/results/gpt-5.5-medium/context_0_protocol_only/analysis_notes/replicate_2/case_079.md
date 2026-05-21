Case podmr_065_2026-05-17-071421

I used the provided sequence.xml as the sequence source. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The pulse program first polarizes the NV and performs a detection readout for the true 0-level reference, then waits, applies rabi_pulse_mod_wait_time with length_rabi_pulse, and performs a second detection readout. Because full_expt is 0, the optional 1-level reference branch is inactive even though do_adiabatic_inversion is true.

Readout roles:
- readout 1: polarized true 0-level reference detection before the Rabi pulse.
- readout 2: detection after the Rabi pulse, which is the pODMR signal readout.

Sequence parameters relevant to the decision:
- mod_depth = 1 from sequence.xml.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- mw_freq is the scanned variable; detuning is 0.

The combined readouts show a broad upward drift across the frequency sweep in both channels rather than a localized resonance-shaped dip or peak in the signal channel relative to the reference. The per-average traces are noisy and the apparent structure is not reproducible as a clear pODMR feature: readout 2 does not show a consistent frequency-localized contrast change against readout 1, and both averages mainly follow baseline variation. I therefore classify this scan as not containing a convincing pODMR resonance.
