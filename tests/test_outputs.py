import json
from pathlib import Path

REPORT = Path("/app/report.json")

# Expected values, computed independently (by hand, not by reusing the
# solution's regex/Counter logic) from the fixed environment/access.log
# shipped with this task:
#
#   192.168.0.1  GET /index.html   -> counts toward index.html
#   192.168.0.2  GET /about.html   -> counts toward about.html
#   192.168.0.1  GET /index.html   -> counts toward index.html
#   10.0.0.5     POST /api/login   -> counts toward api/login
#   192.168.0.2  GET /index.html   -> counts toward index.html
#   10.0.0.5     GET /about.html   -> counts toward about.html
#
# 6 requests total, 3 distinct IPs (192.168.0.1, 192.168.0.2, 10.0.0.5),
# /index.html is requested 3 times (the most of any path).
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load_report():
    assert REPORT.exists(), "no /app/report.json found"
    assert REPORT.stat().st_size > 0, "/app/report.json is empty"
    with open(REPORT) as f:
        return json.load(f)


def test_report_has_required_keys():
    """The report is valid JSON with the required keys and types."""
    data = _load_report()
    assert isinstance(data, dict), "report.json is not a JSON object"
    for key in ("total_requests", "unique_ips", "top_path"):
        assert key in data, f"missing key: {key}"
    assert isinstance(data["total_requests"], int)
    assert isinstance(data["unique_ips"], int)
    assert isinstance(data["top_path"], str)


def test_total_requests_correct():
    """total_requests matches the real number of log lines."""
    data = _load_report()
    assert data["total_requests"] == EXPECTED_TOTAL_REQUESTS, (
        f"expected {EXPECTED_TOTAL_REQUESTS} requests, got {data['total_requests']}"
    )


def test_unique_ips_correct():
    """unique_ips matches the real number of distinct client IPs."""
    data = _load_report()
    assert data["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"expected {EXPECTED_UNIQUE_IPS} unique IPs, got {data['unique_ips']}"
    )


def test_top_path_correct():
    """top_path matches the actual most-requested path."""
    data = _load_report()
    assert data["top_path"] == EXPECTED_TOP_PATH, (
        f"expected top_path {EXPECTED_TOP_PATH!r}, got {data['top_path']!r}"
    )
