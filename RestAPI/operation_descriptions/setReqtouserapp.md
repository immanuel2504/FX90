The `PUT /cloud/apps/{appname}/pass-through` REST endpoint is used to send Request to Userapp.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `set_req_usr_app` |
| REST Endpoint | `PUT /cloud/apps/{appname}/pass-through` |
| Operation ID | `setReqToUserApp` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
