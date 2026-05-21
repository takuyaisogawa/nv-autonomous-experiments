Active sequence inspection:

- SequenceName is Rabimodulated.xml.
- The active experiment has full_expt = 0, so the optional 1-level reference block is skipped.
- The acquisition order is: polarize, detection for the true 0-level/bright reference, wait, rabi_pulse_mod_wait_time, then detection for the microwave-pulse affected signal.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate; this is 52 ns.
- mod_depth is 1 in the variable values used for this run.

Readout roles:

- readout 1 is the pre-microwave true 0-level reference.
- readout 2 is the post-rabi-pulse detection and is the readout to inspect for pODMR contrast against the reference/noise behavior.

Data assessment:

The scan covers 3.825 to 3.925 GHz in 5 MHz steps with two averages. The combined readout 2 trace is noisy, with both upward and downward excursions. There are low points around 3.885-3.890 GHz, 3.910 GHz, and 3.925 GHz, but these do not form a clean, reproducible ODMR-like dip when viewed against readout 1 and the per-average overlays. The strongest structure in readout 2 is actually a local high region near 3.895-3.905 GHz rather than a fluorescence loss. The readout 2 standard deviation over frequency is comparable to stochastic point-to-point variation, and the difference readout2-readout1 alternates sign without a consistent resonance profile.

Decision:

No reliable pODMR resonance is present in this single-NV scan.
