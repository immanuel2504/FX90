# `get_version` — schema clarification (scenario)

**Command:** `get_version`  
**REST endpoint:** `GET /cloud/version`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_version` command for `/cloud/version` in `openAPISpec.yaml`.

When I call `GET /cloud/version`, the example response is:

```json
{
  "availableOsUpgrades": {},
  "cloudAgentApplication": "0.6.2.25",
  "model": "FXR90",
  "radioControlApplication": "0.2.58.6",
  "radioFirmware": "2.1.57.0",
  "readerApplication": "2.0.7-5",
  "revertBackFirmware": {},
  "serialNumber": "233575230D0028"
}
```

But `model` is defined only as:

```yaml
model:
  type: string
```

Since there is no `enum`, any string is valid. The MQTT `get_version` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal constrains `model` to:

```yaml
enum:
  - FXR90
  - FX7500
  - FX9600
  - ATR7000
```

Could you please add this `enum` for `model`, and add descriptions for the version fields (`serialNumber`, `radioFirmware`, `readerApplication`, etc.), which the Zebra IoTC MQTT documentation provides but `openAPISpec.yaml` does not?
