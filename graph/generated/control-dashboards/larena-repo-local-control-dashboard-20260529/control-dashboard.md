# Graph Control Dashboard control-dashboard.larena-repo-local-control-dashboard-20260529

- Graph: `ai-codex-skill-larena.graph`
- Status: `control_ready`
- Canonical state: `sha256:574a07a9bad2c2bed7c639883202a37cdf60752f7c6f4bfdd3c3326bfdca9de2`
- Headline: Seed and embryo are available; use projection views and score reports for next decision.

## Control Surfaces

| Surface | Status | Ref |
| --- | --- | --- |
| `seed` | `success` | `graph/source/growgraph/seeds/larena-repo-local-seed-20260529.json` |
| `embryo` | `available` | `graph/generated/seed-expansions/larena-repo-local-seed-expand-20260529/graph-embryo.json` |
| `readiness` | `missing` | `` |
| `quality` | `missing` | `` |
| `proposal_queue` | `available` | `graph/generated/embryo-proposals/larena-repo-local-embryo-proposals-20260529/action-proposals.json` |

## Embryo Summary

- Candidate objects: `36`
- Candidate relations: `33`
- Source files: `14`
- Average confidence: `0.543`
- Review groups: `10`
- Duplicate groups: `0`

## Projection Views

- `seed_summary`: `graph/generated/seed-expansions/larena-repo-local-seed-expand-20260529/projection-view.json`

## Stale Artifacts

- none

## Next Actions

- run graph readiness-score for the target mode
- run graph quality-review or quality-dashboard when content quality matters
- review pending proposal actions before canonical write
