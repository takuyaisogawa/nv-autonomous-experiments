Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, the enabled path first polarizes the NV and records a detection window for the true 0-level / bright reference. Since full_expt = 0, the optional 1-level reference block is inactive. The sequence then applies one rabi_pulse_mod_wait_time pulse and records the second detection window. Thus readout 1 is the pre-pulse polarized reference and readout 2 is the post-Rabi-pulse signal readout.

The relevant pulse settings from the provided XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at the 250 MHz sample rate. The active microwave pulse therefore tests frequency-dependent response during a fixed 52 ns pulse.

The combined readouts are noisy, but the post-pulse signal is lower than the reference across a contiguous region from roughly 3.85 to 3.885 GHz, with the strongest normalized depression around 3.855 GHz. The two individual averages do not perfectly agree point by point, but both show a negative contrast at the strongest point and the combined trace has a broad dip-like feature rather than only one isolated excursion. I therefore classify the pODMR resonance as present, with limited confidence in the exact center or lineshape.
