Parse the Apache-style access log located at `/app/access.log`.

Success criteria:

1. Read the file `/app/access.log`.
2. Produce a JSON file named `/app/report.json`.
3. The JSON object must contain exactly these keys:
   - `total_requests`
   - `unique_ips`
   - `top_path`
4. `total_requests` is the number of log entries.
5. `unique_ips` is the number of distinct client IP addresses.
6. `top_path` is the most frequently requested path in the log.