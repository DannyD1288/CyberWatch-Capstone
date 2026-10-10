import csv
import io
import sqlite3
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "development-only-change-before-deployment"
DB = Path(__file__).with_name("cyberwatch.db")
MAX_BYTES = 2 * 1024 * 1024
app.config["MAX_CONTENT_LENGTH"] = MAX_BYTES

def connect():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with connect() as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, timestamp TEXT NOT NULL, ip TEXT NOT NULL, username TEXT NOT NULL, result TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY, ip TEXT NOT NULL, timestamp TEXT NOT NULL, failures INTEGER NOT NULL, status TEXT NOT NULL DEFAULT 'Open');
        """)

def detect(events):
    """One alert per IP for each consecutive burst of >=5 failures within 5 minutes."""
    by_ip = defaultdict(list)
    for event in events:
        if event[3] == "failure":
            by_ip[event[1]].append(datetime.fromisoformat(event[0]))
    alerts = []
    for ip, times in by_ip.items():
        times.sort()
        start = 0
        last_alert_end = -1
        for end, time in enumerate(times):
            while time - times[start] > timedelta(minutes=5):
                start += 1
            if end - start + 1 >= 5 and start > last_alert_end:
                alerts.append((ip, time.isoformat(timespec="seconds"), end-start+1))
                last_alert_end = end
    return alerts

@app.route("/")
def index():
    init_db()
    with connect() as db:
        events = db.execute("SELECT * FROM events ORDER BY timestamp DESC LIMIT 200").fetchall()
        alerts = db.execute("SELECT * FROM alerts ORDER BY timestamp DESC LIMIT 100").fetchall()
        total = db.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        failed = db.execute("SELECT COUNT(*) FROM events WHERE result='failure'").fetchone()[0]
    return render_template("index.html", events=events, alerts=alerts, total=total, failed=failed)

@app.post("/upload")
def upload():
    file = request.files.get("file")
    if not file or not file.filename.lower().endswith(".csv"):
        flash("Choose a CSV file.", "danger")
        return redirect(url_for("index"))
    try:
        content = file.read().decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(content))
        if not reader.fieldnames or not {"timestamp", "ip", "username", "result"}.issubset(reader.fieldnames):
            raise ValueError("CSV requires timestamp, ip, username, result columns")
        records = []
        for row in reader:
            timestamp = datetime.fromisoformat(row["timestamp"].strip()).isoformat(timespec="seconds")
            ip = row["ip"].strip()
            username = row["username"].strip()
            result = row["result"].strip().lower()
            if not ip or not username or result not in ("success", "failure"):
                raise ValueError("Invalid IP, username, or result")
            records.append((timestamp, ip, username, result))
        if not records:
            raise ValueError("CSV is empty")
        alerts = detect(records)
        with connect() as db:
            db.executemany("INSERT INTO events(timestamp,ip,username,result) VALUES (?,?,?,?)", records)
            db.executemany("INSERT INTO alerts(ip,timestamp,failures) VALUES (?,?,?)", alerts)
        flash(f"Imported {len(records)} events and created {len(alerts)} alerts.", "success")
    except (ValueError, UnicodeError, csv.Error, TypeError) as exc:
        flash(f"Upload failed: {exc}", "danger")
    return redirect(url_for("index"))

@app.post("/alerts/<int:alert_id>/resolve")
def resolve(alert_id):
    with connect() as db:
        db.execute("UPDATE alerts SET status='Resolved' WHERE id=?", (alert_id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
