## 1. Description

The `PUT /cloud/eSimConfig` REST endpoint updates the eSIM profile state on the reader.

This endpoint allows you to configure:

- The eSIM operation to perform through `operation`
- The target profile nickname through `profileNickName`

Use this endpoint to:

- Enable a specific eSIM carrier profile on the reader
- Switch between installed eSIM profiles for different cellular network providers
- Apply eSIM provisioning changes from your carrier management system

## 2. Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | eSIM Configuration |
| REST Endpoint | `PUT /cloud/eSimConfig` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |
| Related Endpoints | [getEsimConfig](getEsimConfig.md), [getNetwork](getNetwork.md), [updateNetwork](updateNetwork.md) |
| Supported Operations | `enable`, `disable` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Use `GET /cloud/eSimConfig` first to retrieve the exact profile nickname available on the reader before sending this request.

| What You Need | Details |
|---|---|
| Operation | The eSIM operation to perform: `enable` to activate the selected profile, or `disable` to deactivate it. |
| Profile nickname | The exact nickname of the eSIM profile to enable, as returned by `GET /cloud/eSimConfig`. The nickname must match exactly - case-sensitive. |
| Active SIM setting | After enabling an eSIM profile, confirm the `wan0.activeSim` is set to `esim` in the network configuration (see `PUT /cloud/network`) for the profile to be used for data. |
