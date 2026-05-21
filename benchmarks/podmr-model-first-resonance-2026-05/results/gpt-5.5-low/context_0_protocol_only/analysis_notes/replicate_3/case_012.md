Case podmr_030_2026-05-13-160024.

Sequence inspection:
- Active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The microwave frequency is set as mw_freq + detuning, with detuning = 0.
- The active microwave operation is rabi_pulse_mod_wait_time using length_rabi_pulse.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, so the pulse duration is 52 ns.
- mod_depth = 1 in the variable values used for this run.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped despite do_adiabatic_inversion being true.

Readout roles:
- readout 1 is the initial detection after adj_polarize, described in the XML as acquiring the true 0 level reference.
- readout 2 is the detection after the modulated 52 ns Rabi pulse and is the pODMR signal readout for the swept microwave frequency.

Data assessment:
The two averaged readouts fluctuate strongly across the scan. The post-pulse readout does not show a stable, localized dip or peak that is reproducible relative to the 0-level reference across the two averages. Several large excursions are present, but they are narrow/noisy and not supported consistently by both readout traces or by the per-average overlays. Because the apparent structure is comparable to point-to-point noise and average-to-average variation, I do not identify a reliable pODMR resonance in this scan.
