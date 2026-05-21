Active sequence: Rabimodulated, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided XML sets full_expt = 0, so the optional 1-level reference block is inactive. The two active detections are therefore:
- readout 1: the initial true 0-level reference after adj_polarize.
- readout 2: the detection after rabi_pulse_mod_wait_time.

The active Rabi pulse uses length_rabi_pulse = 5.2e-08 s. At the 250 MHz sample rate this is 13 samples, so the rounded pulse duration remains 52 ns. The provided XML has mod_depth = 1 for this pulse.

The raw readouts have a shared upward drift and substantial point-to-point scatter. The readout2/readout1 contrast has an isolated negative point near 3.865 GHz, but the surrounding trace is not a coherent pODMR line shape and other smaller sign changes occur across the scan. With only two averages, the observed separation is not convincing evidence of a resonance.

Decision: resonance_absent.
