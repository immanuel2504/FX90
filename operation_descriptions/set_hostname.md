## 1. Description

The `set_hostname` command sets the network hostname of the reader.

Use it to:

- Assign a recognizable hostname for network identification
- Standardize naming conventions across a fleet
- Update hostname after device relocation or re-provisioning

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Hostname Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_hostname](get_hostname.md), [set_network](set_network.md), [get_network](get_network.md) |
| Supported Operations | Set the reader hostname |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the command. Duplicate hostnames on the same network can cause resolution conflicts.

| What You Need | Details |
|---|---|
| Hostname | Desired hostname string (payload key is `hostname`, lowercase). |
