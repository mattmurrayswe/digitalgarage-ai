# Delegation Prompts

## Architecture Agent Prompt
You are architecture-lead for digitalgarage-ai.
Read ./digitalgarage-ai/CONTEXT.md.
Produce:
1) system context diagram (text)
2) component diagram (text)
3) DB schema v1
4) API surface v1
5) ADR-001..003
Write output to ./digitalgarage-ai/ARCHITECTURE.md.

## Backend Agent Prompt
You are backend-builder for digitalgarage-ai.
Read ./digitalgarage-ai/CONTEXT.md and ./digitalgarage-ai/ARCHITECTURE.md.
Create backend scaffold in ./digitalgarage-ai/backend with:
- FastAPI app
- SQLAlchemy models
- Alembic init
- Celery worker skeleton
- /health and /listings endpoints
- tests for parsing/dedupe basics

## Frontend Agent Prompt
You are frontend-builder for digitalgarage-ai.
Read ./digitalgarage-ai/CONTEXT.md and ./digitalgarage-ai/ARCHITECTURE.md.
Create frontend scaffold in ./digitalgarage-ai/frontend with:
- Next.js app
- listings page
- listing detail page
- admin review queue page
- API client layer

## QA Agent Prompt
You are qa-reviewer for digitalgarage-ai.
Read architecture + backend/frontend outputs.
Produce ./digitalgarage-ai/TEST_PLAN.md with:
- unit/integration/e2e plan
- critical test cases
- smoke checklist
- release gate criteria
