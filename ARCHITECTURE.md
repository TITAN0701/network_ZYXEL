# Architecture Overview (network_ZYXEL)

This folder contains pytest-based automation scripts for Zyxel DUTs. The code is split into two primary layers:

1) Test scenarios
2) Web UI operation helpers

External dependencies (not in this folder) provide shared utilities and device control.

## Contents

### Test scenarios

- `Stress.py`
  - Environment setup (reset, firmware upgrade, WAN/IPv6, WKS reboot).
  - Multiple stress scenarios: power cycle, GUI FW upgrade loops, TR-069 provisioning, link down/up cycles.
- `WAP_Function.py`
  - WAP/Extender validation flows: Wi-Fi (2.4/5G), guest SSID, user account, time, TR-069.
  - Firmware downgrade/upgrade and configuration persistence checks.

### Web UI operation helpers

- `Web_FW_Upgrade.py`
  - GUI firmware upgrade workflow, with `no/full_reset/partial_reset`.
- `Web_Setup_DMZ.py`
  - DMZ IP configuration and apply flow.
- `Web_Setup_uPnP.py`
  - uPnP and uPnP NAT-T enable/disable flow.
- `Web_Setup_User_Account.py`
  - User account add/edit/delete flow; variants for specific customers.

## Layered structure

```
Tests (pytest + allure)
  ├─ Stress.py
  └─ WAP_Function.py
        ↓
Device abstraction layer (external modules)
  ├─ module.Device_Web / Device_Console / Device_TR69 / Reset_Device / Device_Config
        ↓
Common APIs (external)
  ├─ api.WebApp / api.Console / api.Misc / api.TR
        ↓
Shared utilities (external)
  ├─ lib.Common (e.g., VAR), lib.globalvar, Web driver classes
```

## Typical test flow

1) Environment setup (reset, firmware upgrade, WAN config).
2) Configure services (Wi-Fi, SIP, TR-069, accounts).
3) Verify via Web UI and console.
4) Stress loop (power cycles, link toggles, FW upgrades).
5) Re-verify configuration persistence and service availability.

## Key dependencies (external)

- `lib.Common`: variable and utility helpers (e.g., `VAR()`).
- `api.*`: low-level actions for UI, console, TR-069, and misc utilities.
- `module.*`: DUT abstractions (Web UI, console, TR-069, reset, config).

## Known structural risk

- `Stress.py` defines multiple methods with the same name `test_case` in a single class. In Python, later definitions overwrite earlier ones, so only the last `test_case` per class is executed. If all scenarios are intended to run, they should be renamed to unique test function names.

