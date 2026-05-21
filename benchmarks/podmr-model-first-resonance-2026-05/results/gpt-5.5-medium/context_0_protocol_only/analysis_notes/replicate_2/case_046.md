Active pulse sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects a true 0-level reference, then because full_expt = 0 it skips the optional 1-level reference block. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the 0-reference detection and readout 2 is the post-Rabi-pulse signal detection.

The post-pulse signal readout has a distinct local maximum at 3.875 GHz: readout 2 is 58.06 there, versus neighboring values of about 56.48 and 55.79, and it is also well above readout 1 at the same frequency. The reference readout does not show the same sharp feature, so the structure is tied to the microwave pulse response rather than common count drift. The sign is positive in this readout convention, but the localized frequency-dependent contrast indicates a pODMR resonance.
