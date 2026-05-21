Case podmr_008_2026-05-11-131831.

The provided sequence XML is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The active sequence has full_expt = 0, so the intermediate "1 level reference" branch is skipped. The active readouts are therefore:

1. After adj_polarize and before the microwave pulse: true 0 / bright reference.
2. After rabi_pulse_mod_wait_time and before the final wait: post-microwave signal readout.

The rabi pulse duration is length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, which remains 52 ns. The provided sequence XML sets mod_depth = 1. The microwave pulse is a modulated rabi pulse using that duration and modulation depth.

The combined raw readouts are noisy and show drift between averages. The post-pulse signal readout ranges roughly from 18.6 to 21.2 counts, but it does not show a coherent ODMR-like resonance dip across the scan. The apparent low point near 3.840 GHz is isolated, while nearby points recover immediately and the per-average overlay shows strong average-dependent drift rather than a repeated spectral feature. The reference readout also varies substantially, so isolated signal/reference excursions are not reliable evidence of a resonance.

Decision: resonance_absent.
