Active sequence assessment:

The scan uses the Rabimodulated sequence. The executable path polarizes the NV, performs a first detection, waits, skips the optional 1-level reference block because full_expt is 0, applies rabi_pulse_mod_wait_time, then performs a second detection. Therefore readout 1 is the post-polarization 0-state/reference readout, and readout 2 is the readout after the microwave Rabi pulse. The active microwave pulse is length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so it remains 52 ns. The XML sets mod_depth = 1 for the active pulse.

Data assessment:

The reference readout stays near the high-30s to low-40s across the scan and does not show a matching central suppression. The post-pulse readout develops a clear dip centered at about 3.875 to 3.880 GHz, dropping to about 31.9 and 30.8 in the combined data while neighboring/off-resonant points are mostly around 38 to 40. The same minimum occurs in both averages at 3.880 GHz, with the post-pulse readout about 8 to 11 counts below the reference there.

Decision:

This is consistent with a pODMR resonance being present.
