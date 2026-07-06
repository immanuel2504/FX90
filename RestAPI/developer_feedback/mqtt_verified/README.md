# Developer feedback — verified against the Zebra IoTC MQTT documentation

These commands were reviewed by comparing `openAPISpec.yaml` (REST) against the corresponding **MQTT command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal**, which is the complete reference. Each file lists where the REST specification is missing `enum`s, descriptions, required fields, or full definitions that the MQTT documentation already provides.

## Commands

| Tag | Method | Path | Operation ID | Feedback | Scenario |
|-----|--------|------|--------------|----------|----------|
| Certificate | PUT | `/cloud/certificates` | `setUpdateCertificate` | [feedback](set_updateCertificate_schema_feedback.md) | [scenario](scenarios/set_updateCertificate_scenario.md) |
| Firmware | PUT | `/cloud/os` | `setOS` | [feedback](set_os_schema_feedback.md) | [scenario](scenarios/set_os_scenario.md) |
| userapp | PUT | `/cloud/apps/install` | `setInstallUserApp` | [feedback](set_installUserapp_schema_feedback.md) | [scenario](scenarios/set_installUserapp_scenario.md) |
| Control | PUT | `/cloud/mode` | `setMode` | [feedback](set_mode_schema_feedback.md) | [scenario](scenarios/set_mode_scenario.md) |

## Folder layout

```text
mqtt_verified/
├── set_updateCertificate_schema_feedback.md
├── set_os_schema_feedback.md
├── set_installUserapp_schema_feedback.md
├── set_mode_schema_feedback.md
└── scenarios/
    ├── set_updateCertificate_scenario.md
    ├── set_os_scenario.md
    ├── set_installUserapp_scenario.md
    └── set_mode_scenario.md
```
