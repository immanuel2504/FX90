# Typo Fixes — Global Search & Replace

Record of a repo-wide spelling cleanup so the change is traceable.

**Date:** 2026-07-05

---

## Typos corrected

| Typo | Fixed to |
|------|----------|
| `environement` | `environment` |
| `retrive` | `retrieve` |
| `certficate` | `certificate` |
| `accesss` | `accesses` |

---

## Source files corrected

- `openAPISpec.yaml`
- `Command Schemas.json`
- `Response Schemas.json`
- `RestAPI/openapi.yaml`
- `RestAPI/FXR90.yaml`
- `schemas/commands_expanded/control/get_mode.json`
- `schemas/commands_expanded/control/set_mode.json`
- `schemas/response_expanded/control/get_mode_response.json`
- `schemas/response/certificate/set_update_cert_response.json`
- `schemas/response_expanded/certificate/set_update_cert_response.json`
- `schemas/references/shared/operatingMode.v1.yaml`
- `schemas/references/request_payload/get_mode_command.yaml`
- `schemas/references/response_payload/update-certificate-response-2.yaml`

---

## Generated files rebuilt

These picked up the fixes automatically after rebuilding, and both validate clean:

- `RestAPI/FXR90-rest-api.yaml`
- `docs/openapi_md.json`

Rebuild commands:

```powershell
py -3 RestAPI/scripts/build_openapi.py
py -3 scripts/generate_openapi_tags_md.py
```

---

## Notes

- The `RestAPI/FX90.yaml` / `RestAPI/FX90-rest-api.yaml` paths from the initial search do not actually exist in the working tree (both Glob and edit reported "not found"), so there was nothing to fix there.
- Final verification: a repo-wide search for all four typos returns **no matches**.
