Case: podmr_009_2026-05-16-113112

I used inputs/sequence.xml to identify the active sequence before judging the data. The sequence is Rabimodulated.xml / Rabimodulated behavior. The active path first polarizes and detects the true 0-level reference, so readout 1 is the pre-microwave reference. Because full_expt = 0, the optional 1-level reference block is inactive, even though do_adiabatic_inversion is set. The active microwave operation is rabi_pulse_mod_wait_time followed by detection, so readout 2 is the signal readout after the microwave/Rabi-modulated pulse.

Relevant sequence parameters from the provided XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns
- sweep variable = mw_freq
- frequency range = 3.825 to 3.925 GHz in 5 MHz steps

Data assessment:
- Readout 1 stays mostly in the 28 to 31 count range and does not show a comparable central suppression.
- Readout 2 drops sharply around 3.875 to 3.885 GHz: 24.29, 24.15, and 25.00 counts at those points.
- The readout2 - readout1 contrast reaches about -7.14, -5.88, and -5.75 counts at 3.875, 3.880, and 3.885 GHz, with signal/reference ratios about 0.77 to 0.81.
- The same central suppression appears in both individual averages, so it is not only a single-average artifact.

Conclusion: a pODMR resonance is present.
