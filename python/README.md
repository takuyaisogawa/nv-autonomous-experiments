# Python

Python source for the public case-study release.

- `openclaw_runtime/`: case-referenced runtime and analysis helpers copied
  from the live NV automation workspace: MATLAB parsing, MATLAB wrapper support,
  project schema / submit-spec support, sequence design, and report building.
- `openclaw_nv_execution_source/`: sanitized case-referenced execution-path
  source for project management, batch execution, bridge runtime watch, and
  direct enqueue helpers.

Direct execution of the execution-source files is disabled in this public
release.
