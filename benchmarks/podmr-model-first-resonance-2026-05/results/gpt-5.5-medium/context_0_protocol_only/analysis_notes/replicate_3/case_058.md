Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. The active detections are therefore:

1. A true 0-level / polarized reference detection immediately after adj_polarize.
2. A signal detection after rabi_pulse_mod_wait_time.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate to 52 ns. mod_depth is 1 in the provided sequence/variable values. The sweep is therefore a pODMR-like microwave-frequency scan of the post-pulse readout against a reference readout.

The raw readouts do not show a clear localized resonance feature. The post-pulse signal varies by about the same scale as point-to-point noise and shows a broad upward drift toward the high-frequency edge rather than a distinct dip or peak. The two averages are not strongly consistent in producing a narrow resonance-like contrast feature at a common frequency. The endpoint rise in readout 2 is not enough by itself to identify a resonance because it sits at the scan boundary and is not supported by a resolved lineshape.

Decision: resonance absent.
