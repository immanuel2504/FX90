The `PUT /cloud/cloudConfig` REST endpoint and the `set_importCloudConfig` MQTT command import cloud endpoint configuration onto the reader. Use this operation to define how tag data, command responses, and management events are delivered.

This operation configures:
- Data event endpoints under `endpointConfig.data.event`
- Control command-response endpoints under `endpointConfig.control.commandResponse`
- Management event endpoints under `endpointConfig.management.event`
- Management command-response endpoints under `endpointConfig.management.commandResponse`

## 1. Operation Details

| Property | Value |
|---|---|
| Pattern Name | Cloud Endpoint Configuration Import |
| Supported Protocols | REST (HTTP/HTTPS), MQTT |
| Communication Type | Synchronous (REST), Bidirectional (MQTT) |
| Applies To | FXR90 |
| Related Operations | config, certificates |
| REST Endpoint | `PUT /cloud/cloudConfig` |

## 2. Before You Begin

Gather the endpoint details before sending the request. An incorrect hostname, port, topic, or certificate reference will prevent the reader from connecting to the cloud backend.

| What You Need | Details |
|---|---|
| Endpoint channels | `data.event`, `control.commandResponse`, `management.event`, `management.commandResponse`. |
| Connection type | `mqtt`, `httpPost`, `tcpip-server`, `WEBSOCKET`, `mqtt-AZURE`, `mqtt-AWS`, or another supported endpoint type. |
| Host, port, and topics | MQTT endpoints require `hostName`, `port`, `protocol`, `publishTopic`, and command-response `subscribeTopic`. |
| Certificates and auth | TLS certificate references or inline PEM paths, plus optional `basicAuthentication` credentials. |

## 3. Connection Types

| Type | Description |
|---|---|
| `mqtt` | Standard MQTT broker connection. |
| `httpPost` | HTTP POST delivery for data events. |
| `tcpip-server` | TCP/IP server socket endpoint. |
| `WEBSOCKET` | WebSocket endpoint connection. |
| `mqtt-AZURE` | Azure IoT Hub MQTT connection. |
| `mqtt-AWS` | AWS IoT Core MQTT connection. |
| `keyboard-emulation` | Keyboard emulation output. |
