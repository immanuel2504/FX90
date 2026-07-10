## 1. Description

The `PUT /cloud/config` REST endpoint updates the reader's full configuration, including RF/XML settings, GPIO and LED defaults, and reader-gateway endpoint configuration.

Use this endpoint to:

- Push a complete or partial reader XML configuration
- Configure GPIO/LED default states and event-triggered actions
- Set tag-data retention, batching, and data/management endpoint connections

## 2. Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | Reader Configuration Update |
| REST Endpoint | `PUT /cloud/config` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |
| Related Endpoints | [getConfig](getConfig.md), [setImportCloudConfig](setImportCloudConfig.md), [getStatus](getStatus.md) |
| Supported Operations | Update reader configuration |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the request. An invalid XML string or misconfigured endpoint can disrupt tag reporting and management events.

| What You Need | Details |
|---|---|
| Configuration scope | Full `xml` string and/or partial `GPIO-LED` / `READER-GATEWAY` objects. |
| GPIO/LED defaults | Desired GPO pin defaults (`HIGH`/`LOW`) and LED colors per pin. |
| Endpoint connections | Data and management channel types (`mqtt`, `httpPost`, `tcpip-server`, etc.) with host, port, and security. |
| Certificates | Pre-installed or inline PEM content for TLS endpoints (see `GET /cloud/certificates`). |
