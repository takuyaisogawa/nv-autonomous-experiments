Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML executes an initial polarization and detection as the true 0-level reference, then waits. The optional 1-level reference block is disabled because full_expt is 0, so it does not contribute an active readout. The active microwave operation before the final detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, mod_depth = 1, switch_delay = 1e-07 s, mw_ampl = -5 dBm, ampIQ = 5 dBm, and freqIQ = 50 MHz.

Readout roles:

Readout 1 is the initial post-polarization 0-level reference detection. Readout 2 is the detection after the 52 ns modulated Rabi pulse. There is no active 1-level reference readout in this scan.

Resonance assessment:

The post-pulse readout does not show a clear, repeatable ODMR-like dip or peak relative to the reference over the microwave-frequency sweep. Both combined traces fluctuate at roughly the same scale, with only two averages and substantial point-to-point variation. Apparent extrema are not consistently supported by the per-average overlays, and there is no localized contrast feature that stands out from noise across neighboring frequency points.

Decision: resonance_absent.
