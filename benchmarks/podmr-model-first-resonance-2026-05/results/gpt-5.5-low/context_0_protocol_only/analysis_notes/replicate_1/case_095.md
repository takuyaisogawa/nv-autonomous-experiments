Sequence inspection:

- Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout roles: the first detection is the true 0-level/reference readout after optical polarization. The full_expt variable is 0, so the optional 1-level reference block is not active. The second detection is the measurement after the modulated Rabi pulse.
- Pulse settings used for the active measurement: length_rabi_pulse = 52 ns after sample-rate rounding, mod_depth = 1, switch_delay = 100 ns, delay_wrt_1mus = 200 ns.

Data assessment:

The two combined readouts both show a broad downward drift with frequency. The signal-minus-reference contrast is small, changes sign repeatedly, and its most negative points are isolated rather than forming a consistent dip or line shape. The per-average traces show substantial average-to-average offset and noise compared with any candidate pODMR contrast feature. There is no reproducible localized resonance feature supported by adjacent frequency points.

Decision: resonance_absent.
