# `set_installUserapp` — schema clarification (scenario)

**Command:** `set_installUserapp`  
**REST endpoint:** `PUT /cloud/apps/install`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_installUserapp` command for `/cloud/apps/install` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/apps/install`, the `openAPISpec.yaml` example request is:

```json
{
  "authenticationType": "BASIC",
  "authenticationOptions": { "username": "labuser", "password": "L@bu$3rs" },
  "filename": "mylogger_1.0.1.deb",
  "url": "sftp://10.117.229.15/home/labuser/EV1/"
}
```

But the Zebra IoTC MQTT documentation defines the credentials object as `options`, not `authenticationOptions`:

```json
{
  "authenticationType": "BASIC",
  "options": { "username": "labuser", "password": "L@bu$3rs" },
  "filename": "mylogger_1.0.1.deb",
  "url": "https://example.com/apps/"
}
```

So the two specs disagree on the field name (`authenticationOptions` vs `options`). Could you confirm which one the device actually expects and align `openAPISpec.yaml`?

`authenticationType` already has an `enum` (`NONE`, `BASIC`) — thank you. Two more items:

- None of the fields are marked `required` in `openAPISpec.yaml`, so an empty body `{}` would be valid even though `filename` and `url` are needed. Which fields are required?
- The Zebra IoTC MQTT documentation also documents extra fields (`verifyPeer`, `verifyHost`, `CACertificateFileLocation`, `CACertificateFileContent`, `headers`, `retry`) that are missing from `openAPISpec.yaml` — should these be added for REST too?

This will make the OpenAPI specification clearer and avoid confusion for API users.
