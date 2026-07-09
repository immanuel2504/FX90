# set_importCloudConfig — what you should have before testing

## Risk level: 🔴 HIGH — replaces control AND management plane endpoints; a bad value orphans the reader from the cloud

## Equipment & access you need
- Bench reader + your own MQTT broker for the new control/management endpoints
- Valid certificates if the target endpoint uses TLS
- REST access as the fallback channel (this command can kill the MQTT path you send it on)

## Capture BEFORE the first test (so you can restore)
- Current cloud config (`get_config` READER-GATEWAY section) saved to file
- Note the exact broker/topics the reader is currently attached to

## If it goes wrong — recovery
1. Reconnect via REST (bearer token) and re-import the saved cloud config
2. If REST auth also broke: factory reset + re-enrol the reader

## Command-specific notes
- Test with the reader attached to a THROWAWAY broker so losing it costs nothing.
- empty connections [] is documented as 'clear all' — verify scope is data-plane only.
