from app import detect

def test_detects_five_failures():
    rows = [(f"2026-10-10T12:00:{i:02d}", "192.0.2.10", "student", "failure") for i in range(5)]
    assert len(detect(rows)) == 1

def test_does_not_alert_for_four():
    rows = [(f"2026-10-10T12:00:{i:02d}", "192.0.2.10", "student", "failure") for i in range(4)]
    assert detect(rows) == []


def test_successful_logins_do_not_trigger_alert():
    rows = [
        (f"2026-10-10T12:00:{i:02d}", "192.0.2.10", "student", "success")
        for i in range(6)
    ]
    assert detect(rows) == []


def test_failures_from_different_ips_do_not_trigger_alert():
    rows = [
        (f"2026-10-10T12:00:{i:02d}", f"192.0.2.{i+10}", "student", "failure")
        for i in range(5)
    ]
    assert detect(rows) == []


def test_five_failures_outside_five_minutes():
    rows = [
        (f"2026-10-10T12:{i*2:02d}:00", "192.0.2.10", "student", "failure")
        for i in range(5)
    ]
    assert detect(rows) == []