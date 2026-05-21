Sequence inspection:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference branch is not active.
- Readout 1 is the initial fluorescence detection after polarization, serving as the 0-level/reference readout.
- Readout 2 is the fluorescence detection after the active microwave Rabi pulse.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns.

Data assessment:

The microwave-affected readout shows its strongest low point near 3.860 GHz, and the readout-1 minus readout-2 contrast is largest at that same scan point. This feature is narrow and the scan is noisy with only two averages, but the post-pulse readout depression is visible in the averaged trace and is compatible with a pODMR response for this sequence. I therefore classify this case as resonance present, with low practical confidence despite the required confidence field value.
