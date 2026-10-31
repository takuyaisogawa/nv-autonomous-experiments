# Experiment Intent Schema

Before requesting a measurement, the agent records its purpose, settings,
expected results, and stopping conditions in an `experiment_intent` record.

## Flow

```text
agent plans a measurement
        |
        v
agent writes experiment_intent
        |
        v
software checks request fields and safety constraints
        |
        v
accepted request is submitted to the MATLAB bridge
        |
        v
measurement results
        |
        v
agent updates the evidence log and project state
```

## Minimal Fields

These measurement requests are stored under:

```text
cases/<case>/project/experiment_intents/
```

The main fields are:

| Field | Purpose |
| --- | --- |
| `schema_version` | Version of the intent schema. |
| `kind` | Should be `experiment_intent`. |
| `intent_id` | Stable id used to link intent, submit spec, result, and evidence. |
| `project_id` | Project that owns the intent. |
| `status` | Planned, verified, submitted, done/completed, failed, canceled, or superseded. |
| `summary` | One-line measurement objective. |
| `scientific_rationale` | Why the agent thinks this measurement is worth doing. |
| `comparison_targets` | Prior state, evidence, or analysis artifacts this intent should test against. |
| `expected_evidence` | Artifacts expected after successful execution. |
| `success_criteria` | Conditions for interpreting the run as useful. |
| `stop_conditions` | Conditions that should prevent or halt the action. |
| `planned_measurement` | Measurement family, sequence, target, and planned parameters. |
| `submit_spec` or `submit_spec_path` | Measurement parameters submitted to the bridge, or the path to the file containing them. |
| `safety_contract` | Safety constraints and checks required before the measurement. |
| `safety_verification` | Results of the checks performed before submission. |

## Validation and Submission

The verification code checks the request fields, project state, measurement
queue, and safety constraints before a request can be submitted. Readers can
compare the planned measurement with the saved parameters and verification
records. Hardware execution is disabled in this release; see
[Public scope](public_scope.md).
