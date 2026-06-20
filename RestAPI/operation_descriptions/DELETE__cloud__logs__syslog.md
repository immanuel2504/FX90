The `DELETE /cloud/logs/syslog` REST endpoint is used to purge Log.

Use this endpoint to:

- Purge Log.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `DELETE /cloud/logs/syslog` |
| Description Key | `DELETE__cloud__logs__syslog` |
| MQTT Command | `del_logs_syslog` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `del_logs_syslog` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
