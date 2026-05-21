Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation from inputs/sequence.xml:
- sample_rate = 250 MHz, so length_rabi_pulse = 52 ns is already sample-aligned.
- mod_depth = 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is not active.
- The active readouts are therefore:
  1. Readout 1: true 0-level optical reference after adj_polarize and detection, before the swept microwave Rabi pulse.
  2. Readout 2: signal detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay).

Decision:
Readout 1 has a mostly smooth upward drift across the scan, while readout 2 shows a localized suppression relative to the reference near 3.865 GHz: the combined values are about 50.85 for the reference and 48.08 for the post-pulse signal, with adjacent signal points recovering toward about 50.4 and 50.8. The per-average overlay is noisy, but this frequency-localized contrast is consistent with a pODMR fluorescence dip after the microwave pulse rather than only a shared readout drift.

Prediction: resonance_present.
