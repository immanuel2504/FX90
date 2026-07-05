# `set_hostName` — schema clarification (scenario)

**Commands:** `get_hostName`, `set_hostName`  
**REST endpoints:** `GET /cloud/hostName`, `PUT /cloud/hostName`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_hostName` and `set_hostName` commands for `/cloud/hostName` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/hostName`, the example request uses `hostname` (all lowercase):

```json
{
  "hostname": "FXR90C60C001"
}
```

But when I call `GET /cloud/hostName`, the response uses `hostName` (camelCase):

```json
{
  "hostName": "FXR90C60C001"
}
```

The request field name (`hostname`) and the response field name (`hostName`) do not match. Could you confirm which casing the device actually expects for the request? The GET and PUT field names should be consistent unless there is a specific reason they differ.

Also, please add:

* a description for the hostname field
* any validation rules (allowed characters, max length)
* a description for the `200` response, which currently returns an empty string

This will make the OpenAPI specification clearer and avoid confusion for API users.
