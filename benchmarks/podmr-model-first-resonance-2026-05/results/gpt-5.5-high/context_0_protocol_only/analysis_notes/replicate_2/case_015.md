Sequence inspection:

The active sequence is Rabimodulated.xml. It sets the microwave frequency, polarizes the NV, detects once immediately, waits, then applies a modulated Rabi pulse and detects again. Because full_expt is 0, the optional 1-level reference block is skipped.

Readout roles:

Readout 1 is the true 0-level optical reference acquired after polarization and before the microwave pulse. Readout 2 is the signal readout acquired after the Rabi pulse.

Pulse settings from inputs/sequence.xml:

length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Resonance assessment:

Readout 1 stays near the mid-30 count level across the sweep and does not show a matching deep feature. Readout 2 shows a clear, localized drop from the mid-30s to about 26-27 counts around 3.875-3.880 GHz, and the same dip is visible in the per-average overlay. Since the signal readout after the microwave pulse changes strongly and locally while the reference remains comparatively stable, this is consistent with a pODMR resonance.
