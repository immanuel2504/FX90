# `get_hostname` — schema clarification (scenario)

**Command:** `get_hostname`  
**REST endpoint:** `GET /cloud/hostName`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_hostname` command for `/cloud/hostName` in `openAPISpec.yaml`.

When I call `GET /cloud/hostName`, the example response is:

```json
{
  "hostName": "FXR90C60C001"
}
```

The schema types this correctly and uses the correct camelCase key (`hostName`):

```yaml
hostName:
  type: string
  example: FXR90C60C001
```

Compared with the MQTT `get_hostname` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal, the only missing items are a **description** for `hostName` ("Hostname of the reader") and the **`required` list**.

Could you please add the description (and confirm whether `hostName` should be `required`)?

> Side note: the GET response uses `hostName` (camelCase), while the `set_hostName` **request** body uses `hostname` (lowercase). That casing inconsistency is tracked separately in the `set_hostName` feedback.
