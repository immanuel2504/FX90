## 1. Description

The `set_gpo` command sets the output state of a single General Purpose Output (GPO) pin on the reader.

This command allows you to configure:

- The target GPO port number through `port`
- The desired output state (HIGH or LOW) through `state`

Use this command to:

- Drive an external device such as a light stack, horn, or gate via a GPO pin
- Signal application logic results on physical outputs
- Toggle a GPO pin in response to tag read events or inventory state changes

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | GPO Control |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/gpo` |
| Related Commands | [get_gpostatus](get_gpostatus.md), [get_gpi_status](get_gpi_status.md), [get_readerCapabilities](get_readerCapabilities.md) |
| Required Payload Fields | `port`, `state` |
| Supported Port Values | 1-4 (varies by reader model - see `get_readerCapabilities`) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Know the port number and desired output state before sending this command. Setting a port beyond the reader's capacity will result in an error.

| What You Need | Details |
|---|---|
| Port number | The GPO port to target (integer, 1-4). Use `get_readerCapabilities` to confirm the maximum number of GPO pins available on this reader model. |
| Output state | `true` to drive the pin HIGH (active), `false` to drive the pin LOW (inactive). |
| External device wiring | Confirm the wired device is rated for the GPO pin's voltage and current output before asserting a HIGH state. |

