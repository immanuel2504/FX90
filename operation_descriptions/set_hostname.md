## 1. Description

The `set_hostname` command sets the network hostname of the reader.

This command allows you to configure:

- The reader's network hostname through `hostname`

Use this command to:

- Assign a recognizable hostname for network identification during provisioning
- Standardize hostname naming conventions across a fleet
- Update the hostname after a reader is relocated or re-provisioned

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Hostname Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/hostName` |
| Related Commands | [get_hostname](get_hostname.md), [set_network](set_network.md), [get_network](get_network.md) |
| Required Payload Fields | `hostname` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Have the desired hostname ready before sending this command. Duplicate hostnames on the same network can cause resolution conflicts.

| What You Need | Details |
|---|---|
| Hostname string | The desired hostname (payload key: `hostname`). Must be a valid RFC 1123 hostname - alphanumeric characters and hyphens only; no underscores or spaces. |
| Network uniqueness | Verify the chosen hostname is not already in use on the network segment to avoid DNS or mDNS conflicts. |
