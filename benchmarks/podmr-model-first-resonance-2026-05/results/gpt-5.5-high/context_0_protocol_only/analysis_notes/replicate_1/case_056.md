I used the supplied sequence XML and raw export only.

Active sequence:
- SequenceName/Rabimodulated.xml, swept parameter mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional 1-level reference block is skipped.
- The active measurement cycle is polarization, detection, wait, rabi_pulse_mod_wait_time, detection, final wait.
- do_adiabatic_inversion is true as a variable, but it is only inside the skipped full_expt block and is not active here.

Readout roles:
- Readout 1 is the initial post-polarization detection, acting as the bright/0-level reference.
- Readout 2 is the detection after the modulated Rabi microwave pulse, acting as the frequency-dependent signal readout.

Pulse settings:
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is 13 samples, so rounding leaves it at 52 ns.
- mod_depth = 1.
- switch_delay = 100 ns, freqIQ = 50 MHz.

Data assessment:
The raw readouts both show a broad downward drift over the scan, so I compare the post-pulse signal against the reference readout rather than using absolute fluorescence alone. The strongest local negative signal-reference contrast occurs near 3.875 GHz, where readout 2 is about 1.83 counts below readout 1, and this negative contrast is present in both averages. Neighboring points recover by 3.885 GHz, making this look like a localized ODMR-like dip on top of the drifting baseline. There are other noisy negative contrast points, especially earlier in the scan, so the evidence is not clean, but the feature near the center of the scan is consistent enough with a pODMR resonance to call resonance present.
