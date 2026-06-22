## 1. Description

The `get_eSimConfig` command retrieves eSIM identity and profile information from the reader.

This command returns:

- The reader EID (eSIM identifier) and IMEI
- Installed eSIM profile names, nicknames, and activation states

No additional payload fields are required to retrieve the eSIM configuration.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | eSIM Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/eSimConfig` |
| Related Commands | [set_eSimConfig](set_eSimConfig.md), [get_network](get_network.md), [set_network](set_network.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve eSIM identity and installed profile details |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_eSimConfig` to:

- Audit cellular or eSIM provisioning status on the reader
- Check the EID and IMEI values for SIM registration or support cases
- Review installed eSIM profiles before enabling or switching a profile with `set_eSimConfig`

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `eid` | Is the EID correct for this SIM profile? | The EID uniquely identifies the eSIM hardware and is required for carrier provisioning. |
| `imei` | Is the IMEI registered with the carrier? | An unregistered IMEI cannot establish a cellular data connection. |
| Profile names | Which profiles are installed and which is active? | Only one profile can be active at a time; use this to confirm the correct carrier profile is enabled. |
