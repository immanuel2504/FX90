# `set_password` — schema clarification (scenario)

**Command:** `set_password`  
**REST endpoint:** `PUT /cloud/updatePassword`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_password` command for `/cloud/updatePassword` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/updatePassword`, the example request is:

```json
{
  "currentPassword": "change",
  "newPassword": "Mypass@123",
  "userName": "admin"
}
```

Two things are unclear from the schema:

1. **Required fields** — none of the three fields are marked `required`, so according to the schema I could send an empty body `{}` and it would be valid. Should `currentPassword`, `newPassword`, and `userName` all be `required`?

2. **Password rules** — `newPassword` is defined only as:

```yaml
newPassword:
  type: string
```

The example `Mypass@123` suggests complexity rules (uppercase, digit, special character), but the schema has no `pattern`/`minLength`. Could you document the password requirements?

Also, please add:

* descriptions for `currentPassword`, `newPassword`, `userName`
* a description for the `200` response, which currently returns an empty string

This will make the OpenAPI specification clearer and avoid confusion for API users.
