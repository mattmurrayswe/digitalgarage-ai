# job-search module (digitalgarage-ai)

Purpose: Keep LinkedIn job/post scans versioned in Git with deterministic output format and dedupe state.

## Command routing
- "Job search" => LinkedIn Posts tab only.
- "Job search jobs" => LinkedIn Jobs tab only.

## Output rules
- Always list searched keyword buckets.
- If no new matches in a bucket, output exactly: "no new fitting roles this scan".
- Keep response structure consistent across chat/email.
- Always sort results by latest/newest first.

## Match line format (when roles exist)
Role - Company/post author - Posted age (hours) - Link - Fit (Strong/Medium/Skip) - 1-line note

## Dedupe
Use `STATE.json.reportedLinks` to avoid repeating previously reported links.
