# set_bleConfig — what you should have before testing

## Risk level: 🟢 LOW — worst case is BLE scanning off/noisy

## Equipment & access you need
- 1+ BLE beacons: iBeacon and Eddystone if you test protocol filters (phone apps can simulate both)
- Known beacon UUIDs/MACs for filter tests, at a known distance for RSSI thresholds

## Capture BEFORE the first test (so you can restore)
- `get_bleConfig` response saved

## If it goes wrong — recovery
1. Replay saved config, or `disable_ble` then re-enable

## Command-specific notes
- RSSI boundary: -127 is the physical floor — verify -200 is rejected and +10 is handled sanely.
- Filters while disabled: record whether stored, ignored, or rejected.
