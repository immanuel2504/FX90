# `get_availableWifiNetworks` — schema clarification (scenario)

**Command:** `get_availableWifiNetworks`  
**REST endpoint:** `GET /cloud/wifiNetworks`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_availableWifiNetworks` command for `/cloud/wifiNetworks` in `openAPISpec.yaml`.

When I call `GET /cloud/wifiNetworks`, the example response is:

```json
{
  "availableWifiNetworks": [
    {
      "capabilities": ["WPA2", "WPA3"],
      "configuration": { "autoConnect": false },
      "essid": "GLaDOS",
      "signalStrength": "100%"
    }
  ]
}
```

The schema types the fields correctly, but none of them have descriptions:

```yaml
essid: { type: string }
signalStrength: { type: string }
configuration:
  properties:
    autoConnect: { type: boolean }
```

The MQTT `get_availableWifiNetworks` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal describes each field (e.g. `essid` = "Wi-Fi network name", `signalStrength` = "Wi-Fi signal strength reported by the reader", `configuration.autoConnect` = "Whether the reader is configured to automatically connect to this network").

Could you please add these field descriptions (and confirm whether `availableWifiNetworks` should be `required`)?
