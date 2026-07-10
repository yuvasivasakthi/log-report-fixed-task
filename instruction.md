There is an Apache-style access log at `/app/access.log`. Parse it and write a JSON
summary report to `/app/report.json`.

The report must be a single JSON object with exactly these keys:

- `total_requests` (integer): the total number of request lines in the log.
- `unique_ips` (integer): the number of distinct client IP addresses that made requests.
- `top_path` (string): the request path (e.g. `/index.html`) that received the most requests.

Success criteria:

1. `/app/report.json` exists and contains valid JSON.
2. It has the keys `total_requests`, `unique_ips`, and `top_path`, with the types described above.
3. Each value is correct for the contents of `/app/access.log`.
