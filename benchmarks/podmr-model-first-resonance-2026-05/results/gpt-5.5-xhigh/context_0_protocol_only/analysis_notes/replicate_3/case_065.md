Active sequence: Rabimodulated.xml.

The provided sequence XML sets up a microwave-frequency scan with a modulated Rabi pulse. The active path is:

1. Polarize the NV.
2. Detect the true 0-level reference.
3. Wait.
4. Skip the 1-level reference block because full_expt = 0.
5. Apply rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1.
6. Detect the post-pulse signal.

Readout roles:
- readout 1 is the 0-level/reference detection before the microwave pulse.
- readout 2 is the post-modulated-Rabi-pulse signal detection.

The pulse duration is 52 ns. With the 250 MHz sample rate, this is exactly 13 samples after rounding. The active modulation depth is 1.

The signal readout shows a clear local dip relative to the reference near 3.895 GHz. At that point readout 2 is about 45.38 while readout 1 is about 50.00, giving a signal-reference difference near -4.62 counts and a ratio near 0.908. The same dip is present in both averages, so it is not just a one-average outlier. Neighboring points recover substantially, making the feature frequency-local.

Decision: a pODMR resonance is present.
