## 1. Description

The `GET /cloud/eSimConfig` REST endpoint retrieves eSIM identity and profile information from the reader.

This endpoint returns:

- The reader EID (eSIM identifier) and IMEI
- Installed eSIM profile names, nicknames, and activation states

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/eSimConfig` |
| Operation ID | `GET__cloud__eSimConfig` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Equivalent | `get_eSimConfig` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/eSimConfig` to:

- Audit cellular or eSIM provisioning status on the reader
- Check the EID and IMEI values for SIM registration or support cases
- Review installed eSIM profiles before enabling or switching a profile

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `eid` | Is the EID correct for this SIM profile? | The EID uniquely identifies the eSIM hardware and is required for carrier provisioning. |
| `imei` | Is the IMEI registered with the carrier? | An unregistered IMEI cannot establish a cellular data connection. |
| Profile names | Which profiles are installed and which is active? | Only one profile can be active at a time; confirms the correct carrier profile is enabled. |
