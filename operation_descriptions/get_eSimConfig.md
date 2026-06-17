## Description

The `get_eSimConfig` command retrieves eSIM identity and profile information from the reader.

Use this command to:

- Audit cellular/eSIM provisioning
- Check the reader EID and IMEI values
- Review installed eSIM profiles before enabling or switching a profile

## Command Details

| Property | Value |
|---|---|
| Pattern Name | eSIM Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_eSimConfig](set_eSimConfig.md), [get_network](get_network.md), [set_network](set_network.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Retrieve eSIM configuration |
| Supported API Versions | V1.0 |

## Before You Begin

No command payload fields are required. Use this command before `set_eSimConfig` when you need to confirm available profile nicknames.

## Response Payload Summary

| Field | Type | Description |
|---|---|---|
| `payload.eid` | string | Embedded SIM identifier. |
| `payload.imei` | string | Cellular modem IMEI. |
| `payload.profiles` | array of objects | Installed eSIM profiles. |
| `payload.profiles[].enabled` | string | Whether the profile is enabled. |
| `payload.profiles[].iccid` | string | ICCID of the eSIM profile. |
| `payload.profiles[].profileNickName` | string | Profile nickname used by `set_eSimConfig`. |
| `payload.profiles[].provider` | string | Profile provider/carrier label. |
