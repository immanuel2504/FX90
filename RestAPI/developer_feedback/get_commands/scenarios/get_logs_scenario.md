# `get_logs` — schema clarification (scenario)

**Command:** `get_logs`  
**REST endpoint:** `GET /cloud/logs`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_logs` command for `/cloud/logs` in `openAPISpec.yaml`.

When I call `GET /cloud/logs`, the example response is:

```json
{
  "components": [
    { "componentName": "radio_control", "level": "INFO" },
    { "componentName": "reader_gateway", "level": "INFO" }
  ],
  "radioPacketLog": false
}
```

But `componentName` and `level` are defined only as `type: string` with no `enum`:

```yaml
componentName:
  type: string
level:
  type: string
```

The MQTT `get_logs` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal constrains them:

```yaml
componentName:
  enum: [radio_control, reader_gateway]
level:
  enum: [DEBUG, INFO, WARNING, ERROR]
```

Could you please add these `enum`s, plus descriptions for `componentName`, `level`, and `radioPacketLog`? (The Zebra IoTC MQTT documentation also notes that `radio_control` supports only `INFO`, while `reader_gateway` supports `INFO`, `DEBUG`, `WARNING`, `ERROR`.)
