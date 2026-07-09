# Analysis Reports

Generated audit / comparison spreadsheets kept out of the main project tree.
These are **outputs** of the audits, not source — safe to delete and regenerate.

| File | What it is | How to regenerate |
|---|---|---|
| `FXR90_fix_backlog.xlsx` | Master fix backlog (prioritised issues, status dropdowns, missing-description worklist) | manual / audit scripts |
| `FXR90_fix_backlog_UPDATED.xlsx` | Newer copy of the backlog that also has the **Schema Lint** sheet (the original was locked in Excel when it was written) | — reconcile into the file above |
| `rest_vs_mqtt_field_report.xlsx` | REST spec vs MQTT schema field-by-field parity (type / enum / description) | `python RestAPI/scripts/compare_rest_mqtt_schemas.py` |
| `rest_vs_openapimd_report.xlsx` | `RestAPI/FXR90-rest-api.yaml` vs `docs/openapi_md.json` field parity | audit script |
| `schema_example_report.xlsx` | REST schema-vs-example validation (examples that contradict their schema) | audit script |
| `schema_example_report_both_sources.xlsx` | Schema-vs-example check run across both spec sources | audit script |
| `command_response_id_report.xlsx` | MQTT command id vs response id cross-check | audit script |

Note: `RestAPI/developer_feedback/endpoint_issues.xlsx` is intentionally **not** here — it is
developer-feedback source material, not a generated report.
