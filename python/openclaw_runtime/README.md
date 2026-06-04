# Runtime Helpers

Sanitized helper scripts retained because they are referenced by
the two public cases or required by retained case-referenced source files.

Included helper groups:

- Bridge and data parsing: `matlab_bridge_client.py`, `tools_mat_parse.py`
- Schema/spec support: `project_schema.py`, `submit_spec_utils.py`
- Sequence design: `design_nv_sequence.py`
- Report support: `latex_report_build.py`

The copied files preserve the production helper structure where possible. Local
defaults are exposed through environment variables such as `MATLAB_23C_ROOT`,
`NV_BRIDGE_ROOT`, `OPENCLAW_WORKSPACE_ROOT`, `OPENCLAW_MAT_CACHE_ROOT`,
`OPENCLAW_TOOLS_MAT_PARSE`, and `OPENCLAW_TECTONIC`, or represented by explicit
placeholders.

Live backend dispatch, daemon wiring, and direct live queue mutation are outside
this runtime-helper layer. The retained execution-path source is published
under `python/openclaw_nv_execution_source/` with direct execution disabled.
