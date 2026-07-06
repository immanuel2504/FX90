# `get_availableWifiNetworks` — OpenAPI schema feedback

**Command:** `get_availableWifiNetworks`  
**REST endpoint:** `GET /cloud/wifiNetworks`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_availableWifiNetworks` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_availableWifiNetworks` command and compared the `GET /cloud/wifiNetworks` response in `openAPISpec.yaml` with the MQTT `get_availableWifiNetworks` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The shape matches (`availableWifiNetworks` array), but descriptions are missing.

---

## 1. Fields have no descriptions

- The response fields have no descriptions in `openAPISpec.yaml`: `availableWifiNetworks`, and per entry `capabilities`, `configuration.autoConnect`, `essid`, `signalStrength`.
- The Zebra IoTC MQTT documentation describes each (e.g. `essid` = "Wi-Fi network name", `signalStrength` = "Wi-Fi signal strength reported by the reader", `configuration.autoConnect` = "Whether the reader is configured to automatically connect to this network"). Please port these descriptions.

---

## 2. No `required` list

- The Zebra IoTC MQTT documentation marks `availableWifiNetworks` as `required` on the payload. `openAPISpec.yaml` has no `required` list — please confirm and add if appropriate.

---

## Note

The MQTT `get_availableWifiNetworks` command in the Zebra IoTC documentation is the complete reference. This endpoint is well typed; the only ask is field descriptions (and optionally the `required` list).
