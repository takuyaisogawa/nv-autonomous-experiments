Sequence review:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout roles: readout 1 is the initial post-polarization detection, serving as the true 0-level/reference readout before the driven pulse. Readout 2 is the detection after the active rabi_pulse_mod_wait_time block.
- Active pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- Pulse duration: length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, i.e. 52 ns.
- mod_depth = 1.

Data assessment:

The combined signal readout (readout 2) shows a clear, localized dip centered around 3.875-3.880 GHz, falling from roughly 21-22 counts on the shoulders to about 17 counts at the minimum. The reference readout (readout 1) varies more weakly and does not explain the full contrast; comparing readout 2 against readout 1 leaves a strong central depression. The per-average traces have drift, but the resonance-like contrast remains in the combined readouts.

Decision: pODMR resonance present.
