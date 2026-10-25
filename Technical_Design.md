# CyberWatch — Requirements and System Design

## Problem and audience
Security teams need to identify clusters of unsuccessful logins. CyberWatch is an educational, local demonstration for students and entry-level security analysts using synthetic CSV authentication logs.

## Functional requirements
1. Upload a CSV containing `timestamp`, `ip`, `username`, and `result`.
2. Validate timestamps, IP addresses, results, and presence of usernames.
3. Persist imported events in SQLite.
4. Detect five or more failed logins from the same IP within five minutes.
5. Display summary counts, a chart, alerts, and the latest events.
6. Search and filter events, filter alerts by status, and resolve alerts.

## Nonfunctional requirements
- Runs locally with Python and Flask.
- Uses a 2 MB upload limit.
- Uses parameterized SQL statements for database writes.
- Intended for synthetic data, not production or confidential log files.
- Interface is browser-based and supports common desktop sizes.

## Architecture
```text
Browser (HTML/Bootstrap/Chart.js)
            | HTTP
            v
Flask app.py (routes /, /upload, /alerts/<id>/resolve)
            |
            +--> CSV parser and validation
            |         |
            |         v
            |    Detection function
            |
            +--> SQLite (events, alerts)
```

## Database schema
`events(id, timestamp, ip, username, result)`

`alerts(id, ip, timestamp, failures, status)`

## Main workflows
**Upload:** select CSV -> validate -> detect bursts -> insert events and alerts -> redirect to dashboard.

**Review:** dashboard -> filter alerts -> resolve an open alert.

**Investigate:** search or filter recent events by IP, username, timestamp, or result.

## UI wireframe
```text
[CyberWatch header]
[Total events] [Failed] [Successful] [Open alerts]
[Outcome chart]           [Detection rule]
[Upload CSV + Analyze]
[Alerts table + status filter + Resolve]
[Recent events + search + result filter]
```

## Risks and limitations
No live log ingestion, user login, access controls, or production deployment hardening. Data is imported, not continuously streamed. The dashboard limits the event list to 200 and alerts to 100, so counts and visible rows can differ. Repeated imports append duplicates. External CDN assets may require internet access. The development secret and debug mode in `app.py` are not suitable for public deployment.
