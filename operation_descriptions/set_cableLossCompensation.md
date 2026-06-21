The `set_cableLossCompensation` command sets cable loss compensation values on the reader for read points `1` through `4`.

Use it to:

- Compensate for signal loss due to antenna cable length
- Tune compensation per read point for multi-antenna deployments

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Cable Loss Compensation Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_cableLossCompensation](get_cableLossCompensation.md), [get_config](get_config.md) |
| Supported Operations | Set cable loss compensation per read point |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the command. The payload uses fixed read-point keys `1`, `2`, `3`, and `4`.

| What You Need | Details |
|---|---|
| Read points | Per read-point keys `"1"`, `"2"`, `"3"`, and `"4"`. |
| Cable length | Length of antenna cable. |
| Cable loss | Loss per hundred feet of cable. |

## 4. Payload Shape

Provide numeric string keys `"1"` through `"4"`, each containing its own `cableLength` and `cableLossPerHundredFt`.
