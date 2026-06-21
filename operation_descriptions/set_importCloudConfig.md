## 1. Description

The `set_importCloudConfig` command imports a full cloud endpoint configuration onto the reader, defining how tag data, control responses, and management events are delivered to cloud systems.

This command allows you to configure:

- Data event delivery endpoints through `endpointConfig.data.event`
- Control command-response channels through `endpointConfig.control.commandResponse`
- Management event channels through `endpointConfig.management.event`
- Management command-response channels through `endpointConfig.management.commandResponse`
- Batching and retention options per connection through `additionalOptions`

Use this command to:

- Provision MQTT, HTTP, WebSocket, Azure IoT Hub, or AWS IoT Core endpoints in a single request
- Configure control and management command channels alongside data delivery channels
- Set tag data retention and batching behavior
- Restore a full endpoint configuration from a saved profile during fleet provisioning

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Cloud Endpoint Configuration Import |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_config](get_config.md), [set_config](set_config.md), [get_certs](get_certs.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | `endpointConfig` |
| Supported Connection Types | `mqtt`, `httpPost`, `tcpip-server`, `WEBSOCKET`, `mqtt-AZURE`, `mqtt-AWS` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather all endpoint details before sending this command. An incorrect hostname, port, certificate reference, or topic will prevent the reader from connecting to your cloud backend.

| What You Need | Details |
|---|---|
| Endpoint channels | Decide which channels to configure: `data.event`, `control.commandResponse`, `management.event`, and/or `management.commandResponse`. Only include channels you are provisioning. |
| Connection type | Per connection, choose the transport type: `mqtt`, `httpPost`, `tcpip-server`, `WEBSOCKET`, `mqtt-AZURE`, or `mqtt-AWS`. |
| Host, port, and topics | For MQTT connections: `hostName`, `port`, `protocol`, publish topics (`publishTopic`), and subscribe topics (`subscribeTopic` for command-response channels). |
| TLS and certificates | For secure connections: reference an installed certificate by name and type, or enable security and provide the CA certificate path. |
| MQTT client settings | `clientId`, `keepAlive`, `qos`, `cleanSession`, `reconnectDelay`, and `reconnectDelayMax` for each MQTT connection. |
| Retention and batching | For data event connections: configure `retention.maxNumEvents`, `retention.maxEventRetentionTimeInMin`, and `retention.throttle` as needed. |
| Local REST | For control channels: set `enableLocalRest: true` to allow local REST API access alongside cloud connectivity. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or the reader to be unable to connect to the configured endpoints.

### Connection Configuration

- Each connection must have a `name` and a `type`. The `name` must be unique within its channel. Duplicate names within the same channel array will be rejected or may overwrite previous entries.
- `type` must be one of the supported connection type strings. Unrecognized type values will be rejected.

### MQTT Settings

- For `mqtt` connections, `hostName`, `port`, and `protocol` are required. Missing any of these will result in a connection that cannot be established.
- `publishTopic` and `subscribeTopic` are arrays. For command-response channels, at least one `subscribeTopic` must be provided for the reader to receive commands.
- `qos` must be `0`, `1`, or `2`. An unrecognized QoS value will be rejected.

### TLS and Certificate References

- If `enableSecurity` is `true`, a valid installed certificate name must be referenced. The named certificate must already be installed on the reader (see `set_update_cert`).
- Referencing a certificate that does not exist on the reader will cause TLS connection establishment to fail.

### Retention and Batching

- `maxNumEvents` sets the maximum number of events buffered before the oldest are dropped. Set this to a value appropriate for your network reliability and data volume.
- `throttle` sets the maximum event delivery rate in events per second.

### Apply Timing

- The configuration is applied immediately after the command is acknowledged. Existing connections are replaced with the new configuration.
- The reader reconnects to all configured endpoints using the new configuration. Expect a brief interruption in data delivery during reconnection.

### Security Note

- Never hardcode MQTT credentials, TLS passwords, or bearer tokens in your payload. Supply all sensitive values from a secrets manager or environment variable at runtime.
- Use TLS (`enableSecurity: true`) for all MQTT and HTTP connections in production deployments to protect tag data and command traffic in transit.
