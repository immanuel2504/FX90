# FXR90 SET / Config Endpoint Test Scenarios

**Ready-to-copy test payloads for every SET/configuration command — 262 scenarios across 23 commands, both protocols.**

## Folder layout — one folder per command

```
set_network/
├── SCENARIOS.md       <- read first: every scenario's expectation, why, analogy, verify step
├── WHAT_YOU_NEED.md   <- (deep commands) equipment, pre-test state, risk level, recovery
├── mqtt/              <- pure MQTT command envelopes - publish as-is
└── rest/              <- pure REST request bodies - send as-is
```

- **JSON files contain ONLY the payload** - no wrapper - copy/paste or pipe them directly.
- **All explanation lives in each folder's `SCENARIOS.md`.**
- MQTT-envelope tests (missing `command_id`, misspelled command) exist only under `mqtt/`.

## How to run

**MQTT** - publish the file to the reader's command topic, watch the response topic:

```bash
mosquitto_pub -h <reader-ip> -t zebra/cmd -f set_hostname/mqtt/01_valid_full.json
mosquitto_sub -h <reader-ip> -t zebra/response
```

**REST** - send the file as the request body (method + path are in the folder's SCENARIOS.md header):

```bash
curl -X PUT https://<reader-ip>/cloud/hostName   -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"   -d @set_hostname/rest/01_valid_full.json
```

## What you are testing (the checks)

| # | Check | The user in whose shoes you stand |
|---|---|---|
| 1 | **Golden path works** (`01_valid_*`) | A customer following the documentation exactly. If this fails, docs or firmware are wrong. |
| 2 | **Every documented variant works** (`*_variant_*`) | A returning customer ordering a different item off the same menu - all spec examples must work, not just the first. |
| 3 | **Missing required fields rejected** (`*_missing_required_*`) | A developer who forgot a field - needs an error that *names the field*. |
| 4 | **Wrong types rejected** (`*_wrong_type_*`) | Code that sends `"60"` instead of `60`. |
| 5 | **Enum values enforced** (`*_invalid_enum_*`) | Someone guessing a value - the error should list valid choices. |
| 6 | **Boundaries enforced** (`*_boundary_*`) | A typo like `threshold: 900` - must be refused, **not silently clamped**. |
| 7 | **Known weak spots probed** (`*_probe_*`) | A known pothole where schema and firmware are suspected to disagree - record what actually happens. |
| 8 | **Conflicts caught** (`*_conflict_*`, `*_duplicate_*`) | Contradictory settings in one payload - reject or document, never pick silently. |
| 9 | **Envelope rules hold** (`*_mqtt_*`, `*_unknown_field`, `*_empty_payload`) | A customer with a typo - nothing should be half-applied. |

**Every REJECTED scenario:** read the setting back afterwards - reader state must be unchanged.

## Known weak spots - test these hardest

| Area | Suspicion | Folder |
|---|---|---|
| `set_mode.transmitPower` | Schema says **array**, docs example used a bare number - probes send both forms. | `set_mode/` 25-26 |
| `set_network` IPv6 `prefix` | Schema says **string**, examples use integer `64` - probes send both. | `set_network/` 25-26 |
| `batching: null` | Allowed via a construct that is invalid OpenAPI 3.0 - firmware behaviour unverified. | `set_config/` |
| Unbounded thresholds | `managementEventConfig` thresholds have no min/max - probes send 0/100/900. | `set_config/` |
| `enabled` boolean vs string | eSIM `enabled` was string in MQTT, boolean in REST before alignment. | `set_eSimConfig/` |
| `get_SupportedRegionList` | Response enum contains `"success "` **with a trailing space**. | (response-side) |
| Unknown-field handling | Must be *consistent* across all commands. | every `*_unknown_field` |

## Commands covered (23 folders, 262 scenarios)

| Folder | REST endpoint | Scenarios | |
|---|---|---|---|
| [`set_appled/`](set_appled/SCENARIOS.md) | `PUT /cloud/app-led` | 9 |
| [`set_bleConfig/`](set_bleConfig/SCENARIOS.md) | `PUT /cloud/ble-config` | 15 | 🔎 deep
| [`set_cableLossCompensation/`](set_cableLossCompensation/SCENARIOS.md) | `PUT /cloud/cableLossCompensation` | 5 |
| [`set_config/`](set_config/SCENARIOS.md) | `PUT /cloud/config` | 20 | 🔎 deep
| [`set_dataToRG/`](set_dataToRG/SCENARIOS.md) | `PUT /cloud/setdataToRG` | 5 |
| [`set_eSimConfig/`](set_eSimConfig/SCENARIOS.md) | `PUT /cloud/eSimConfig` | 8 | 🔎 deep
| [`set_gpo/`](set_gpo/SCENARIOS.md) | `PUT /cloud/gpo` | 10 |
| [`set_hostname/`](set_hostname/SCENARIOS.md) | `PUT /cloud/hostName` | 6 |
| [`set_impinjGen2X/`](set_impinjGen2X/SCENARIOS.md) | `PUT /cloud/impinjGen2X` | 18 | 🔎 deep
| [`set_importCloudConfig/`](set_importCloudConfig/SCENARIOS.md) | `PUT /cloud/cloudConfig` | 10 | 🔎 deep
| [`set_installCACertificate/`](set_installCACertificate/SCENARIOS.md) | `(MQTT only)` | 11 | 🔎 deep
| [`set_logs/`](set_logs/SCENARIOS.md) | `PUT /cloud/logs` | 6 |
| [`set_mode/`](set_mode/SCENARIOS.md) | `PUT /cloud/mode` | 19 | 🔎 deep
| [`set_network/`](set_network/SCENARIOS.md) | `PUT /cloud/network` | 28 | 🔎 deep
| [`set_ntpServer/`](set_ntpServer/SCENARIOS.md) | `PUT /cloud/ntpServer` | 10 |
| [`set_os/`](set_os/SCENARIOS.md) | `PUT /cloud/os` | 12 |
| [`set_passthru/`](set_passthru/SCENARIOS.md) | `PUT /cloud/pass-through` | 8 |
| [`set_password/`](set_password/SCENARIOS.md) | `PUT /cloud/updatePassword` | 11 |
| [`set_preSelection/`](set_preSelection/SCENARIOS.md) | `PUT /cloud/preSelection` | 6 |
| [`set_region/`](set_region/SCENARIOS.md) | `PUT /cloud/region` | 9 |
| [`set_req_usr_app/`](set_req_usr_app/SCENARIOS.md) | `PUT /cloud/apps/{appname}/pass-through` | 11 | 🔎 deep
| [`set_timeZone/`](set_timeZone/SCENARIOS.md) | `PUT /cloud/timeZone` | 8 |
| [`set_update_cert/`](set_update_cert/SCENARIOS.md) | `PUT /cloud/certificates` | 17 | 🔎 deep

**🔎 deep** = extended coverage: every documented spec variant (17 network security modes, 8 endpoint types,
12 Gen2X features...), weak-spot probes, conflict/duplicate cases - plus **`WHAT_YOU_NEED.md`** listing
equipment, pre-test state to capture, risk level and recovery steps. **Read it first -
`set_network`, `set_config` and `set_importCloudConfig` can take the reader offline if run without a fallback path.**

**Notes**
- `set_appled`, `set_dataToRG`, `set_logs`, `set_mode` have **no documented example payload** in the API docs;
  their `01_valid_full` payloads were synthesized from per-field schema examples (a docs gap worth fixing).
- Certificates via REST: `name` travels as the `{certname}` path parameter, `type` as a query parameter.
- Events are intentionally **not** covered (project rule: no event changes).

## Recording results

Per scenario: `folder/file - PASS / FAIL - actual response - notes`.
Firmware behaviour that differs from the expectation goes into `project_resources/analysis_reports/FXR90_fix_backlog.xlsx` as a new row.
