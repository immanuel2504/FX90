The `revertback` command reverts the reader firmware to the previous OS version on the secondary partition.

Use this command to:

- Roll back after a failed or unwanted `set_os` upgrade
- Restore the last known-good firmware
- Recover from compatibility issues with a new OS build

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Firmware Rollback |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_os](set_os.md), [get_version](get_version.md), [reboot](reboot.md) |
| Supported API Versions | V1.0 |

MQTT command key: `set_revertbackOS`.

## Before You Begin

Plan for downtime — the reader reboots to the secondary partition. Monitor `firmwareUpdateProgress` events during rollback.
