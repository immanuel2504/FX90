## 1. Description

The `GET /cloud/readerLocation` REST endpoint retrieves the reader's last reported GPS coordinates.

This endpoint returns:

- Latitude and longitude values
- Altitude (where available)

No request body is required. The returned values represent the most recent location data known to the reader.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/readerLocation` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. When to Use This Endpoint

Use `GET /cloud/readerLocation` to:

- Record reader location for asset tracking or fleet management
- Confirm GPS availability on a deployed reader
- Feed location data into site, inventory, or logistics systems

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `latitude` | Is a valid latitude value returned? | A null or zero value may indicate the reader does not have a GPS fix yet. |
| `longitude` | Is a valid longitude value returned? | Combined with latitude, this identifies the reader's physical position. |
| `altitude` | Is altitude data present? | Useful in multi-floor or elevated deployments where vertical position matters. |
