# `reboot` — schema clarification (scenario)

**Command:** `reboot`  
**REST endpoint:** `PUT /cloud/reboot`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `reboot` command for `/cloud/reboot` in `openAPISpec.yaml`.

I need clarification using this scenario:

The description says the reader is restarted "with the device ID provided":

> `reboot` — Restarts the reader with the device ID provided

But when I call `PUT /cloud/reboot`, the endpoint defines **no request body and no parameters** — there is nowhere to provide a device ID. It just returns:

```json
""
```

Could you please confirm:

* Is a device ID actually required for the REST call? If yes, where should it go (body or path/query)?
* If the device ID is implied by the connection/topic (MQTT only), could the REST description be adjusted so it does not imply a body is needed?

Also, please add a description for the `200` response, which currently returns an empty string.

This will make the OpenAPI specification clearer and avoid confusion for API users.
