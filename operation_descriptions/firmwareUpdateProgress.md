## 1. Description

The `firmwareUpdateProgress` event reports the status and progress of an in-flight firmware update initiated by `set_os`.

This event includes:

- The current update `status` string indicating the active phase
- Per-image download or write progress as a percentage
- Overall update progress across all firmware partitions
- Failure reason details or per-partition progress in `updateProgressDetails`

Use this event to:

- Track the progress of an OS firmware update started with `set_os`
- Display real-time update progress in an operator dashboard or deployment tool
- Detect update failures and retrieve failure details for troubleshooting
- Confirm the reader rebooted as the final step of a successful update

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Firmware Update Progress |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published during an active firmware update, on each status or progress change |
| Related Events | [async-events](async-events.md), [error](error.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes `firmwareUpdateProgress` automatically after `set_os` initiates a firmware update, as the update transitions through each phase. No further command is required. The event is delivered inside the `async-events` envelope with `type: firmwareUpdateProgress`.

| `status` | State / Behavior | Notes |
|---|---|---|
| `started` | Update has been initiated | Published immediately after `set_os` is acknowledged and the download begins. |
| `downloading-<image>` | Downloading a firmware partition | `imageDownloadProgress` reflects the current partition's download progress (0–100). |
| `erasing-<image>` | Erasing storage for the partition | Precedes writing the new image data to flash. |
| `writing-<image>` | Writing the partition to flash | `imageDownloadProgress` reflects write progress for the current partition. |
| `rebooting` | Reader rebooting to apply the update | Final `firmwareUpdateProgress` event before the reader goes offline for reboot. |
| `failed` | Update failed | `updateProgressDetails` contains the failure reason or error details. |

> **Note:** When `status` is `failed`, inspect `updateProgressDetails` for the specific failure cause. After a failed update, the reader remains on the previous firmware version. Use `revertback` if the reader entered an inconsistent state, or retry `set_os` after resolving the failure condition.
