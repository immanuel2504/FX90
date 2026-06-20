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
| Supported Operations | Retrieve eSIM configuration |
| Supported API Versions | V1.0 |

## Before You Begin

No command payload fields are required. Use this command before `set_eSimConfig` when you need to confirm available profile nicknames.
