The `PUT /cloud/stack-led` REST endpoint is used to color:Green, Brightness:Low(Default), Solid.

Use this endpoint to:

- Color:Green, Brightness:Low(Default), Solid.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `set_stackled` |
| REST Endpoint | `PUT /cloud/stack-led` |
| Operation ID | `setStackled` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_stackled` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
