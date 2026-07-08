## 1. Description

The `PUT /cloud/stack-led` REST endpoint updates the stack LED state on the reader.

Supported colors: `red`, `amber`, `green`, `blue`, `off`.

Supported brightness: `low`, `med`, `high` (defaults to `low`).

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/stack-led` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |

## 3. Request Body

| Field | Type | Description |
|---|---|---|
| `color` | string | LED color: `red`, `amber`, `green`, `blue`, or `off` |
| `brightness` | string | `low`, `med`, or `high` |
| `flash` | boolean | Whether the LED should blink |
| `seconds` | integer | Duration in seconds; use `0` for indefinite |

## 4. When to Use This Endpoint

Use `PUT /cloud/stack-led` to:

- Set a visual indicator on the reader stack LED
- Temporarily override the default LED state with a timed color/flash pattern
