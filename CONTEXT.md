# digitalgarage-ai — Context

## Goal
Build a car-selling platform where listings are ingested from WhatsApp group messages, extracted into structured vehicle data, reviewed in admin, then published.

## Core Flow
1. Ingest WhatsApp group messages (allowlisted groups)
2. Extract listing fields (brand/model/year/price/km/seller phone/images/messageId)
3. Dedupe by messageId
4. Save as pending_review
5. Admin review/edit/approve
6. Publish listing to marketplace

## Proposed Stack
- Backend API: FastAPI (Python)
- DB: PostgreSQL
- ORM: SQLAlchemy
- Migrations: Alembic
- Background jobs: Celery + Redis
- Frontend: Next.js + TypeScript + Tailwind + shadcn/ui
- Media storage: S3-compatible bucket
- Containerization: Docker + Docker Compose (dev and single-server deploy baseline)
- Reverse proxy/TLS: Nginx (or Caddy) in front of frontend/backend

## Initial Domain Objects
- Listing
- Seller
- SourceMessage
- MediaAsset
- ReviewDecision

## Constraints
- Keep extraction pipeline auditable
- Preserve raw message text for reprocessing
- Avoid duplicate listings
- Keep moderation step before publish
