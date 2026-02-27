# digitalgarage-ai — Architecture v0.1

## High-Level Components
- **frontend**: Next.js app (public marketplace + admin review UI)
- **api**: FastAPI app (listing APIs, moderation actions, ingestion control)
- **worker**: Celery worker (extraction, normalization, dedupe, enrichment jobs)
- **beat**: Celery beat scheduler (periodic reconciliation/reprocessing)
- **db**: PostgreSQL (core relational data)
- **redis**: queue + cache
- **storage**: S3-compatible bucket for media assets
- **proxy**: Nginx/Caddy for TLS + routing

## Docker Strategy
Use Docker for both local dev and first production deploy.

### Services (docker-compose)
1. `frontend` (Next.js)
2. `api` (FastAPI + Uvicorn/Gunicorn)
3. `worker` (Celery)
4. `beat` (Celery beat)
5. `db` (Postgres)
6. `redis` (Redis)
7. `proxy` (Nginx/Caddy)

### Why Docker here
- Reproducible environment for all contributors/sub-agents
- Easy handoff to VPS/server
- Isolated dependency management (Python + Node)
- Simple scaling path (split services later)

## Initial Deployment Model
- Single VPS/server with Docker Compose
- `proxy` routes:
  - `/` -> `frontend`
  - `/api/*` -> `api`
- `worker/beat` run privately (no public ports)
- Persistent volumes for Postgres and uploads cache

## Data Flow (MVP)
1. WhatsApp ingest event lands in pipeline
2. Raw message stored in `source_messages`
3. Extraction job parses fields + media refs
4. Dedupe by source `messageId`
5. Listing created as `pending_review`
6. Admin approves/edits -> `published`
7. Frontend surfaces published inventory

## Existing Data Bootstrap (Current Memory)
Current extracted inventory already exists and must be treated as bootstrap source:
- Path: `/Users/mattmurrayswe/.openclaw/workspace/digitalgarage-ai/data/car-leads.ndjson`
- Current baseline: 29 vehicle records (excluding `_meta` rows)

### Import Contract (NDJSON -> DB)
- Read each line as one JSON listing event
- Skip rows containing `_meta`
- Dedupe key: `messageId` (hard unique)
- Preserve raw payload reference for traceability/reprocessing

### Expected Fields from current extractor
- `capturedAt`, `publishedAt`
- `group`, `groupId`, `messageId`
- `sellerWhatsApp`
- `brand`, `model`, `year`
- `priceBRL`, `rawPriceText`
- `image` / `imageRef`
- `source`

### Mapping notes
- `source_messages.external_message_id` <= `messageId`
- `listings.status` defaults to `pending_review` for imported rows unless explicitly marked otherwise
- Keep original NDJSON value snapshots to allow parser improvements without data loss
- Store media under project control at `digitalgarage-ai/data/media/` and persist project-relative references (e.g., `data/media/<file>`) in listing payloads

## Non-Functional Baseline
- Structured logs per container
- Health endpoints: `/health` (api), readiness for frontend
- Daily DB backup job
- Basic metrics: queue depth, extraction success/failure, publish latency
