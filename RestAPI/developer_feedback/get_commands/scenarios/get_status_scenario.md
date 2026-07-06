# `get_status` — schema clarification (scenario)

**Command:** `get_status`  
**REST endpoint:** `GET /cloud/status`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_status` command for `/cloud/status` in `openAPISpec.yaml`.

When I call `GET /cloud/status`, the example response includes:

```json
{
  "antennas": { "1": "disconnected", "5": "connected" },
  "radioActivity": "inactive",
  "radioConnection": "connected",
  "powerSource": "PWR_BRICK"
}
```

But these state fields are defined only as `type: string` with no `enum`:

```yaml
radioActivity:
  type: string
radioConnection:
  type: string
antennas:
  properties:
    1: { type: string }
```

The MQTT `get_status` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal constrains them:

* `antennas.1` … `antennas.6` → `enum: [connected, disconnected]`
* `radioActivity` → `enum: [active, inactive]`
* `radioConnection` → `enum: [connected, disconnected]`

Could you please add these `enum`s? Most other fields (`cpu`, `flash`, `ntp`, `ram`, `powerSource`, `temperature`, `uptime`, …) also have no descriptions in `openAPISpec.yaml`, whereas the Zebra IoTC MQTT documentation describes each — please port those descriptions too. (The `impinjGen2X` and `ble` blocks are already aligned — thank you.)
