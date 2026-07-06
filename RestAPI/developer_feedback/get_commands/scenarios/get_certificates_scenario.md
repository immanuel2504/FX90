# `get_certificates` — schema clarification (scenario)

**Command:** `get_certificates`  
**REST endpoint:** `GET /cloud/certificates`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_certificates` command for `/cloud/certificates` in `openAPISpec.yaml`.

When I call `GET /cloud/certificates`, the example response is an array of certificate objects:

```json
[
  {
    "name": "Server",
    "type": "server",
    "installTime": "Thu May 16 23:25:22 2024",
    "issuerName": "FXR90C5F314",
    "serial": "0x686E2A53",
    "subjectName": "FXR90C5F314",
    "validityStart": "16/05/2024",
    "validityEnd": "11/05/2044"
  }
]
```

But `type` is defined only as `type: string` with no `enum`:

```yaml
type:
  type: string
```

The MQTT `get_certificates` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal constrains it:

```yaml
type:
  enum: [server, client, app]
```

Could you please add this `enum` for `type`, add descriptions for the certificate fields (`name`, `installTime`, `issuerName`, `serial`, `subjectName`, `validityStart`, `validityEnd`, `publickey`), and confirm the item-level `required` list (the Zebra IoTC MQTT documentation marks all of these as required)?
