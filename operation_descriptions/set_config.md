## 1. Description

The `set_config` command updates the reader's full configuration, including RF settings, GPIO and LED defaults, and reader-gateway endpoint configuration.

Use this command to:

- Configure GPIO/LED default states and event-triggered actions
- Set tag-data retention, batching, and data/management endpoint connections

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Configuration Update |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/config` |
| Related Commands | [get_config](get_config.md), [set_importCloudConfig](set_importCloudConfig.md), [get_status](get_status.md) |
| Supported Operations | Update reader configuration |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the command. A misconfigured endpoint can disrupt tag reporting and management events.

| What You Need | Details |
|---|---|
| Configuration scope | Partial or full `GPIO-LED` and/or `READER-GATEWAY` objects. |
| GPIO/LED defaults | Desired GPO pin defaults (`HIGH`/`LOW`) and LED colors per pin. |
| Endpoint connections | Data and management channel types (`mqtt`, `httpPost`, `tcpip-server`, etc.) with host, port, and security. |
| Certificates | Pre-installed or inline PEM content for TLS endpoints (see `get_certs`). |
