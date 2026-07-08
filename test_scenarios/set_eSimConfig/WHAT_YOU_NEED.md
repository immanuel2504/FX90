# set_eSimConfig — what you should have before testing

## Risk level: 🟠 MEDIUM — can drop the WAN link; carrier operations may be slow/billable

## Equipment & access you need
- FXR90 with eSIM and an active carrier profile (or a test profile)
- Awareness that profile switches can take minutes and may incur carrier-side effects
- A non-WAN access path to the reader (ethernet/Wi-Fi) — never test eSIM over the eSIM link

## Capture BEFORE the first test (so you can restore)
- `get_eSimConfig` response saved (profile list + which is enabled)

## If it goes wrong — recovery
1. Re-enable the original profile from the snapshot
2. Carrier portal access if a profile ends up disabled on the carrier side

## Command-specific notes
- The enabled-as-string probe targets a real schema history bug — record the exact behaviour.
