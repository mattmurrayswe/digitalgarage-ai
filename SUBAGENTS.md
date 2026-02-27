# Sub-agent Operating Plan (OpenClaw)

## Recommended Sub-agents
1) architecture-lead
- Owns architecture decisions, ADRs, boundaries, contracts.
- Outputs: ARCHITECTURE.md, ADRs, API contracts.

2) backend-builder
- Owns FastAPI, DB schema, extraction pipeline, tests.
- Outputs: backend code + migrations + tests.

3) frontend-builder
- Owns Next.js marketplace and admin review UI.
- Outputs: frontend code + component tests.

4) qa-reviewer
- Owns test plans, E2E checks, integration validation.
- Outputs: TEST_PLAN.md + validation reports.

## Delegation Template
Use this context block in each delegated task:
- Project: digitalgarage-ai
- Source of truth: ./digitalgarage-ai/CONTEXT.md
- Output contract: file paths + acceptance checklist
- Non-goals: do not change stack without approval

## Acceptance Gate (all sub-agents)
- Must state assumptions
- Must provide changed files list
- Must include test steps
- Must include risks + rollback
