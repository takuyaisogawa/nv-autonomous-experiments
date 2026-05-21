Sequence review:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is inactive despite do_adiabatic_inversion being true.
- Active readout roles: readout 1 is the initial polarized true-0 reference detection after adj_polarize; readout 2 is the detection after the modulated Rabi pulse.
- mod_depth is 1 from the provided sequence XML and variable values.
- Active pulse duration is length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate.

Data assessment:
The two combined raw readouts fluctuate around roughly 49-51 counts without a stable frequency-localized dip or peak. The readout2-readout1 difference is centered near zero and alternates sign across the sweep; the largest excursions occur as isolated noisy points rather than a coherent resonance shape. The per-average overlay shows substantial scatter and does not support a reproducible feature at any frequency.

Decision:
No convincing pODMR resonance is present in this scan.
