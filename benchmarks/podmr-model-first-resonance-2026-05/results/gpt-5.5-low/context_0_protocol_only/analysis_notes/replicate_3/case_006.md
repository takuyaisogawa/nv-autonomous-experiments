Sequence inspection:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825e9 to 3.925e9 Hz in 5 MHz steps.
- Executed pulse path: polarize, detect the true 0-level reference, wait, then apply rabi_pulse_mod_wait_time with length_rabi_pulse, mod_depth, and switch_delay, then detect the signal readout.
- full_expt is 0, so the optional 1-level reference branch is inactive.
- Readout roles: readout 1 is the pre-microwave 0-level/reference detection; readout 2 is the detection after the modulated Rabi microwave pulse.
- Pulse duration: length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- mod_depth: variable/exported active value is 1.

Data assessment:
The post-pulse readout is lower than the reference near the center of the scan, most notably around 3.87-3.875 GHz, where the reference is high and the signal readout is suppressed. This creates a localized negative contrast consistent with a pODMR resonance under the active Rabimodulated sequence. The two averages show substantial baseline drift, so confidence is not maximal, but the combined readout contrast has a plausible resonance feature rather than only featureless noise.
