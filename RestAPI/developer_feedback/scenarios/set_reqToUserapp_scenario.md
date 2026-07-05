# `set_reqToUserapp` — schema clarification (scenario)

**Command:** `set_reqToUserapp`  
**REST endpoint:** `PUT /cloud/apps/{appname}/pass-through`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_reqToUserapp` command for `/cloud/apps/{appname}/pass-through` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/apps/mylogger/pass-through`, the example request is:

```json
{
  "command": { "message": "Hello World!!!" },
  "userapp": "mylogger"
}
```

On success, the response schema is defined only as:

```yaml
type: object
```

There are no `properties`, description, or example, so it is unclear what the response contains. Since this is a pass-through to a user application, the response is probably application-defined. Could you confirm this and add a description noting that the payload is passed through from the user application (and is not a fixed schema)?

Also, please add descriptions for the request fields `command`, `command.message`, and `userapp`.

This will make the OpenAPI specification clearer and avoid confusion for API users.
