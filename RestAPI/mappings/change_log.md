# FXR90 API Docs — Change Log

Running record of edits to the FXR90 API documentation, so anyone can see what changed, why, and which files/commands were affected.

**Last updated:** 2026-07-05

---

## 1. `preSelection` documentation fix

**What:** The response field name in the `get_preSelection` docs was wrong (`rxSawFilter` → should be `preSelection`).

**Files changed:**
- `operation_descriptions/get_preSelection.md` — response table field `rxSawFilter` → `preSelection`
- `RestAPI/operation_descriptions/getPreSelection.md` — same fix

**Note:** `rxSawFilter` is kept in prose (it is the feature name); only the JSON **field name** was corrected.

**Rebuilt:** `RestAPI/FXR90-rest-api.yaml`, `docs/openapi_md.json`

---

## 2. Developer feedback for `openAPISpec.yaml` schema gaps

**What:** Reviewed every command against `openAPISpec.yaml` and created a `developer_feedback` area documenting schema-metadata gaps (missing `enum`, missing descriptions, undocumented responses, naming inconsistencies). The API contract itself is consistent; these are documentation/schema-quality issues to send to the developer.

**New folders/files:**
- `RestAPI/developer_feedback/` — 23 concise `*_schema_feedback.md` files (one per command / group) + `README.md` index
- `RestAPI/developer_feedback/scenarios/` — 23 scenario-style `*_scenario.md` files (each shows a concrete request/response example of the gap) + `README.md` index

**Commands with feedback files (gaps found):**

| Command(s) | Endpoint | Main gap(s) |
|------------|----------|-------------|
| `get_preSelection` / `set_preSelection` | `/cloud/preSelection` | GET value no `enum`; missing descriptions; PUT response no description |
| `get_mode` / `set_mode` | `/cloud/mode` | `type` no `enum`; `environment` missing; complex fields undocumented |
| `get_appled` / `set_appled` | `/cloud/app-led` | `color`/`status` no `enum` (differs from `set_stackled`) |
| `set_gpo` | `/cloud/gpo` | `port` range; descriptions |
| `set_region` | `/cloud/region` | `country`/`standardname` no `enum`/reference |
| `get_SupportedStandardList` | `/cloud/supportedStandardList` | `channeldata` vs `channelData`; boolean-as-string |
| `set_passthru` | `/cloud/pass-through` | `operationId` is `status`; `component` no `enum` |
| `set_cableLossCompensation` | `/cloud/cableLossCompensation` | units/ranges; numbered keys |
| `reboot` | `/cloud/reboot` | device ID mentioned but not in schema |
| `set_password` | `/cloud/updatePassword` | no `required`; password rules |
| `set_logs` | `/cloud/logs` | `level`/`componentName` no `enum` |
| `set_timeZone` | `/cloud/timeZone` | response has no schema; `timeZone` format |
| `set_updateCertificate` | `/cloud/certificates` | `type` enum, `required`, response schema |
| `set_refreshCertificate` | `/cloud/certificates/{certname}` | `type` no `enum`; response no schema |
| `del_certificate` | `/cloud/certificates/{certname}` | `type` body vs query; response no schema |
| `set_eSimConfig` | `/cloud/eSimConfig` | `operation` no `enum`; boolean-as-string |
| `set_hostName` | `/cloud/hostName` | `hostname` vs `hostName` |
| `set_os` | `/cloud/os` | example `authenticationOptions` vs schema `options` |
| `set_revertbackOS` | `/cloud/revertbackOS` | response no schema |
| `set_installUserapp` | `/cloud/apps/install` | `authenticationOptions` vs `options`; missing fields; no `required` |
| `set_dataToRG` | `/cloud/setdataToRG` | no request body defined |
| `set_reqToUserapp` | `/cloud/apps/{appname}/pass-through` | response object untyped |
| `set_startUserapp` / `set_stopUserapp` / `set_autostartUserapp` / `set_uninstallUserapp` | `/cloud/apps/{appname}/...` | responses have no schema; `autostart` no description |

**Commands reviewed — no gaps (no file created):**
`set_impinjGen2X`, `set_config`, `set_importCloudConfig`, `updateNetwork`, `set_bleConfig`, `set_ntpServer` (minor only).

---

## 3. Cross-check against `Command Schemas.json`

**What:** Verified 4 commands against `Command Schemas.json` (the richer, authoritative MQTT source). It resolves several open questions and revealed one real conflict.

| Command | Finding | Action |
|---------|---------|--------|
| `set_updateCertificate` | `Command Schemas.json` defines `type` `enum: [client, server, app]` and `required: [name, type, url]` | Feedback updated with exact values to port into `openAPISpec.yaml` |
| `set_os` | Correct credentials field is `options` (schema right, **example** wrong `authenticationOptions`); extra fields missing (`verifyPeer`, `verifyHost`, `CACertificate*`, `headers`, `retry`) | Feedback updated |
| `set_installUserapp` | Real conflict: `openAPISpec.yaml` uses `authenticationOptions`, `Command Schemas.json` uses `options`; extra fields missing | Feedback updated to flag mismatch |
| `set_mode` | `Command Schemas.json` has `type` enum, `environment` enum, and full definitions; `openAPISpec.yaml` is much thinner | New `set_mode` feedback + scenario files created |

**Files changed:** `set_updateCertificate`, `set_os`, `set_installUserapp` (both `*_schema_feedback.md` and `scenarios/*_scenario.md`); added `set_mode_schema_feedback.md` + `scenarios/set_mode_scenario.md`; both `README.md` indexes updated.

---

## 4. `set_mode` — request for full definitions + examples

**What:** Added a request for the developer to add complete schema definitions **and worked examples** for complex `set_mode` fields that currently appear only in examples (or not at all):
`selects`, `accesses`, `tagMetaData` (object forms), `radioStartConditions`, `radioStopConditions`, `reportFilter`, `modeSpecificSettings`, plus array forms of `antennaStopCondition`/`query`.

**Files changed:** `RestAPI/developer_feedback/set_mode_schema_feedback.md`, `RestAPI/developer_feedback/scenarios/set_mode_scenario.md`

---

## 5. Global typo fixes

**What:** Repo-wide search-and-replace of common misspellings.

| Typo | Corrected |
|------|-----------|
| `environement` | `environment` |
| `retrive` | `retrieve` |
| `certficate` | `certificate` |
| `accesss` | `accesses` |

**Source files corrected:**
- `openAPISpec.yaml`, `Command Schemas.json`, `Response Schemas.json`
- `RestAPI/openapi.yaml`, `RestAPI/FXR90.yaml`
- `schemas/commands_expanded/control/get_mode.json`, `set_mode.json`
- `schemas/response_expanded/control/get_mode_response.json`
- `schemas/response/certificate/set_update_cert_response.json`, `schemas/response_expanded/certificate/set_update_cert_response.json`
- `schemas/references/shared/operatingMode.v1.yaml`
- `schemas/references/request_payload/get_mode_command.yaml`
- `schemas/references/response_payload/update-certificate-response-2.yaml`

**Rebuilt (generated):** `RestAPI/FXR90-rest-api.yaml`, `docs/openapi_md.json`

**Verified:** repo-wide search for all four typos returns no matches.

---

## Build commands (for reference)

After editing source YAML/JSON or operation descriptions, rebuild both doc sites:

```powershell
py -3 RestAPI/scripts/build_openapi.py        # REST -> RestAPI/FXR90-rest-api.yaml
py -3 scripts/generate_openapi_tags_md.py     # MQTT -> docs/openapi_md.json
```

## Key files

| Purpose | File |
|---------|------|
| REST viewer | `RestAPI/swagger.html` → `RestAPI/FXR90-rest-api.yaml` (generated) |
| REST source | `RestAPI/openapi.yaml`, `RestAPI/paths/**`, `RestAPI/operation_descriptions/*.md` |
| MQTT viewer | `docs/index.html` → `docs/openapi_md.json` (generated) |
| Developer reference spec | `openAPISpec.yaml` |
| MQTT command/response schemas | `Command Schemas.json`, `Response Schemas.json`, `schemas/**` |
| Developer feedback | `RestAPI/developer_feedback/**` |
