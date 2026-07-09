# set_impinjGen2X — what you should have before testing

## Risk level: 🟠 MEDIUM — tagProtect can leave TEST TAGS permanently protected

## Equipment & access you need
- Gen2X-capable Impinj tags (M780/M830 family) — ordinary Gen2 tags will NAK these features
- SACRIFICIAL tags for protect/unprotect tests — a forgotten password can brick a tag
- The access passwords you set, written down BEFORE sending protect commands

## Capture BEFORE the first test (so you can restore)
- `get_impinjGen2X` response saved
- List of test-tag EPCs used for protect tests

## If it goes wrong — recovery
1. unprotect_tag with the recorded password for every tag you protected
2. Reset feature flags via the disable_* variants

## Command-specific notes
- Run protect/unprotect as a pair per tag, never protect-only.
- The combined-features scenario checks atomicity: on failure NOTHING should be applied.
