# `set_os` — schema clarification (scenario)

**Command:** `set_os`  
**REST endpoint:** `PUT /cloud/os`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_os` command for `/cloud/os` in `openAPISpec.yaml`.

I need clarification using this scenario:

The schema defines the credentials object as `options`:

```yaml
options:
  type: object
  properties:
    username:
      type: string
    password:
      type: string
```

But the `set_os` example uses `authenticationOptions` instead:

```json
{
  "url": "https://.../FXR90_2.0.10.tar.bz2",
  "authenticationType": "NONE",
  "authenticationOptions": { "username": "test", "password": "test" }
}
```

So the schema field name (`options`) and the example field name (`authenticationOptions`) do not match. `Command Schemas.json` confirms the correct field name is **`options`** (with `required: [username, password]`), so the schema is right and only the **example** needs fixing to use `options`.

`authenticationType` already has an `enum` (`NONE`, `BASIC`) — thank you.

Also, please:

* fix the example to use `options` instead of `authenticationOptions`
* add descriptions for `options.username`, `options.password`, and `url` (already present in `Command Schemas.json`)
* consider adding the extra fields from `Command Schemas.json` (`verifyPeer`, `verifyHost`, `CACertificateFileLocation`, `CACertificateFileContent`, `headers`, `retry`) if supported over REST
* add a response schema for the `200` response (currently `description: OK` only, with no body defined)

This will make the OpenAPI specification clearer and avoid confusion for API users.
