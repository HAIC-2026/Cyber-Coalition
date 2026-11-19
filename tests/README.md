# Browser test harness

Run the HAIC static planning demonstrator through a local HTTP server and open the dependency-free harness.

From the repository root:

```powershell
python -m http.server 8000
```

Open `http://localhost:8000/tests/harness.html` in a current desktop browser. The harness loads `web/index.html) in a same-origin iframe, checks the tabs, keyboard navigation, data filters, required-field validation, synthetic record handling, conservative pairing rules, 375 px and 1280 px document overflow, and session reset after reload.

It requires no package installation, API key, ArcGIS login, live service, or CI configuration. It uses synthetic records and does not write to the demonstrator or external systems. Read the visible result list and confirm every check passes. This is a browser test harness, not validation of ArcGIS data, agency workflows, accessibility compliance, operational readiness, or statewide coverage.
