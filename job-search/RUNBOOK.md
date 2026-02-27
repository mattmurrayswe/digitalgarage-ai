# Runbook

## Manual run flow
1. Read `KEYWORDS.md`.
2. For each bucket, scan LinkedIn according to selected mode (`posts` or `jobs`).
3. Filter out links already in `STATE.json.reportedLinks`.
4. Save timestamped report to `reports/YYYY-MM-DDTHH-mm-ss.md`.
5. Update `STATE.json`:
   - `lastRunAt`
   - `lastReportPath`
   - append new links into `reportedLinks`

## Report template (no matches)
Posts scan (Past 24h) completed
Searched keyword buckets:
- "..." — no new fitting roles this scan

## Notes
- Keep format strict and stable.
- Prefer deterministic wording.
