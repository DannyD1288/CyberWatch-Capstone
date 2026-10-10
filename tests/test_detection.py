from app import detect

def test_detects_five_failures():
    rows = [(f"2026-10-10T12:00:{i:02d}", "192.0.2.10", "student", "failure") for i in range(5)]
    assert len(detect(rows)) == 1

def test_does_not_alert_for_four():
    rows = [(f"2026-10-10T12:00:{i:02d}", "192.0.2.10", "student", "failure") for i in range(4)]
    assert detect(rows) == []
