## 1. Description

The `set_cableLossCompensation` command configures cable loss compensation values for each antenna read point on the reader.

This command allows you to configure:

- Cable length and loss-per-hundred-feet for read points `1` through `4`

Use this command to:

- Compensate for signal attenuation caused by long antenna cable runs
- Tune compensation independently per port for multi-antenna deployments with different cable lengths
- Improve read range accuracy by accounting for passive cable loss in the RF path

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Cable Loss Compensation Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/cableLossCompensation` |
| Related Commands | [get_cableLossCompensation](get_cableLossCompensation.md), [get_readPoints](get_readPoints.md), [get_readerCapabilities](get_readerCapabilities.md) |
| Supported Read Point Keys | `"1"`, `"2"`, `"3"`, `"4"` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Measure the physical cable runs for each antenna port before sending this command. Incorrect values will produce inaccurate compensation and may reduce read range.

| What You Need | Details |
|---|---|
| Read point keys | Use numeric string keys `"1"` through `"4"` in the payload. Only include keys for ports that have physical cables attached. |
| Cable length | The length of the antenna cable in the unit expected by the reader (feet). Measure the actual cable run from the reader port to the antenna. |
| Cable loss per hundred feet | The attenuation rating of the cable type in dBm per 100 feet. This value is specified by the cable manufacturer. |
| Available read points | Use `get_readPoints` to confirm which read point IDs are available on this reader before sending. |

