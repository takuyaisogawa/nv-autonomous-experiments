Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence enables channels 1:3, sets the microwave source, then performs a polarization/detection block before the microwave pulse. Because full_expt is 0, the optional 1-level reference block is inactive. The active readout roles are therefore:

- readout 1: pre-microwave bright-state / 0-level reference after adj_polarize
- readout 2: post-microwave signal after rabi_pulse_mod_wait_time

The active Rabi-modulated pulse uses length_rabi_pulse = 52 ns. At the 250 MHz sample rate this is 13 samples, so rounding does not change it. The provided sequence and exported variable values give mod_depth = 1.

The raw traces have a slow downward drift across the sweep, visible in both readouts, so I treated the resonance evidence as a localized suppression of the post-pulse signal relative to the pre-pulse reference rather than as an absolute raw count minimum. The post-pulse readout shows a pronounced dip around 3.875 GHz: the combined values are about 43.54 for the post-pulse signal and 45.37 for the reference, and both individual averages show negative signal-reference contrast at that frequency. Nearby points recover enough that this is more consistent with a microwave resonance than only common-mode drift.

Decision: pODMR resonance is present.
