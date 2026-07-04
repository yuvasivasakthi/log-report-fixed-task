import json
from pathlib import Path


REPORT = Path("/app/report.json")


def test_report_exists():
    assert REPORT.exists(), "report.json was not created"


def test_report_is_valid_json():
    data = json.loads(REPORT.read_text())

    assert "total_requests" in data
    assert "unique_ips" in data
    assert "top_path" in data

    assert isinstance(data["total_requests"], int)
    assert isinstance(data["unique_ips"], int)
    assert isinstance(data["top_path"], str)


def test_report_values():
    data = json.loads(REPORT.read_text())

    assert data["total_requests"] > 0
    assert data["unique_ips"] > 0
    assert len(data["top_path"]) > 0