## 1. Description

The `GET /cloud/readPoints` REST endpoint retrieves the read points available on the reader.

This endpoint returns:

- The list of read-point identifiers available on this reader

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/readPoints` |
| Operation ID | `getReadPoints` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_readPoints` |
| MQTT Equivalent | `get_readPoints` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/readPoints` to:

- Identify available read-point identifiers before configuring cable loss compensation
- Map physical read points before configuring inventory mode settings
- Verify read-point availability before referencing them in antenna configuration

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Read-point list | How many read points are returned? | Determines how many antenna ports are physically available for use. |
| Read-point IDs | Do the returned IDs match expected port numbering? | Read-point identifiers must match exactly when used in `PUT /cloud/cableLossCompensation` or `PUT /cloud/mode`. |
