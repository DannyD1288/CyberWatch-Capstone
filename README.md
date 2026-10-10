# CyberWatch — CIT Capstone Starter MVP

## Run on Windows
1. Install Python 3.11+ from python.org (check **Add Python to PATH**).
2. Open this folder in VS Code, then open **Terminal > New Terminal**.
3. Run `py -m venv .venv`.
4. Run `.venv\Scripts\activate` (PowerShell may require `Set-ExecutionPolicy -Scope Process Bypass`).
5. Run `pip install -r requirements.txt`.
6. Run `python app.py`.
7. Open http://127.0.0.1:5000 in your browser.
8. Upload `sample_data/sample_log.csv`; check that an alert appears.

## Tests
Run `python -m pytest -q`.

## What this starter does
CSV upload, validation, simple 5-failures-in-5-minutes detection, SQLite event/alert storage, dashboard counters, alert resolution, and basic browser filtering.

## Known limitations / next steps
This is a learning prototype, not production security software. No authentication, CSRF protection, real-time monitoring, robust duplicate suppression across uploads, or full date filtering. Detection operates within each uploaded file, and reuploading duplicates records. Dashboard shows the most recent 200 events and 100 alerts. The alert counter represents the displayed alerts, not necessarily all historical alerts. Do not expose the Flask development server publicly or use real personal/security data. Add date filters, charts, secure configuration, stronger tests, diagrams, and documentation during the semester.
