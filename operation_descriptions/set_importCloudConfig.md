## 1. Description

The `set_importCloudConfig` command imports a cloud endpoint configuration onto the reader, defining how tag data, control responses, and management events are delivered.

Use it to:

- Provision MQTT, HTTP, WebSocket, or cloud-specific (Azure/AWS) data endpoints
- Configure control and management command-response channels
- Set batching and retention options per connection

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Cloud Endpoint Configuration Import |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_config](get_config.md), [set_config](set_config.md), [get_certs](get_certs.md) |
| Supported Operations | Import cloud endpoint configuration |
| Supported API Versions | V1.0 |


## 3. Before You Begin

Gather these details before sending the command. An incorrect hostname, port, or certificate reference will prevent the reader from connecting to your cloud backend.

| What You Need | Details |
|---|---|
| Endpoint channels | Which channels to configure: `data.event`, `control.commandResponse`, `management.event`, `management.commandResponse`. |
| Connection type | Per connection: `mqtt`, `httpPost`, `tcpip-server`, `WEBSOCKET`, `mqtt-AZURE`, `mqtt-AWS`, etc. |
| Host / port / topics | MQTT: `hostName`, `port`, `protocol`, `publishTopic`, `subscribeTopic` (for cmdResp). |
| Certificates / auth | TLS cert name/type or inline PEM; `basicAuthentication` username/password if used. |

## 4. Connection Types

The `type` field in each `connections[]` entry defines the transport.

| type | Description | Authentication |
|---|---|---|
| `mqtt` | Standard MQTT broker | TLS + optional basic auth |
| `httpPost` | HTTP POST data delivery | TLS + basic auth |
| `tcpip-server` | TCP/IP server socket | TLS optional |
| `WEBSOCKET` | WebSocket connection | TLS optional |
| `mqtt-AZURE` | Azure IoT Hub MQTT | Azure-specific options |
| `mqtt-AWS` | AWS IoT Core MQTT | AWS-specific options |
| `keyboard-emulation` | Keyboard emulation output | N/A |
