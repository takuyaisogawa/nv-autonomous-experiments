Sequence and role check:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- XML variables: sample_rate = 250 MHz, full_expt = 0, mod_depth = 1, length_rabi_pulse = 5.2e-08 s.
- The 52 ns rabi pulse is already on the 4 ns sample grid, so the active pulse duration remains 52 ns.
- Because full_expt = 0, the optional 1-level reference block is skipped.
- The active detections are therefore:
  - readout 1: initial polarized 0-level reference, before the microwave pulse.
  - readout 2: post-rabi-pulse signal readout.

Data assessment:

The relevant pODMR contrast is the post-pulse signal relative to the pre-pulse 0-level reference. The combined signal/reference contrast fluctuates around zero with point-scale excursions of roughly a few percent. There is a small dip-like patch near 3.845-3.860 GHz, but it is not smooth or distinct relative to the surrounding scatter, and there are also comparable non-resonant excursions including a positive feature near 3.88 GHz. The two averages show strong baseline differences and do not support a clear, reproducible resonance feature.

Decision:

No reliable pODMR resonance is present in this scan.
