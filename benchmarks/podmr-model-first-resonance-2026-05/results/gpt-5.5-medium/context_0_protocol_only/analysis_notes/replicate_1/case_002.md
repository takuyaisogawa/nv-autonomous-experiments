Active sequence and roles:

The provided sequence XML is Rabimodulated.xml with mw_freq as the swept variable. The pulse program first polarizes the NV and performs detection to acquire the true 0-level reference. Since full_expt is 0, the optional 1-level reference block is inactive. The active experimental signal is then produced by rabi_pulse_mod_wait_time using length_rabi_pulse = 5.2e-08 s, mod_depth = 1, and switch_delay = 1e-07 s, followed by detection. Thus readout 1 is the no-microwave initialized reference and readout 2 is the microwave-pulse readout.

Data assessment:

Readout 1 stays comparatively flat with no matching central feature, while readout 2 shows a clear localized fluorescence decrease from about 42 counts down to about 34.7 counts near 3.88 GHz, then recovers toward the surrounding baseline. The dip is visible in the combined trace and is also supported by the per-average overlay, although individual averages differ in amplitude. Because the sequence readout role makes readout 2 the relevant microwave-affected signal and the feature is localized in the frequency sweep rather than common-mode with the reference, this is consistent with a pODMR resonance.
