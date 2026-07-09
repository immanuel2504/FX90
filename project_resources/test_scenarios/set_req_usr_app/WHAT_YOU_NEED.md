# set_req_usr_app — what you should have before testing

## Risk level: 🟢 LOW — worst case is a confused user app

## Equipment & access you need
- A test user application installed and running on the reader (install_user_app first)
- The app's documented pass-through message format
- App logs accessible (get_user_apps + app-side logging) to confirm delivery

## Capture BEFORE the first test (so you can restore)
- `get_user_apps` output saved (which apps, which states)

## If it goes wrong — recovery
1. stop/start the user app if it wedged
2. uninstall/reinstall the test app as last resort

## Command-specific notes
- The not-installed probe needs NO app present — run it before installing.
- Verify the response comes from the APP (pass-through), not synthesized by the reader.
