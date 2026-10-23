# Mirai Graph Adoption Report mirai-graph-adoption-report.larena-repo-local-adoption-gga8-20260529

- Target: `skill:larena`
- Owner skill: `larena`
- Adoption: `GGA8` `federation_ready`
- Status: `blocked`
- Headline: Mirai Graph adoption is at GGA8; blockers must be cleared before migration claim.
- GRS: `80`
- CQS: `None`
- Semantic verdict: `pass_with_notes`
- Effectiveness verdict: `improved`

## Checks

| Check | Status |
| --- | --- |
| `source_inventory_done` | `pass` |
| `seed_validated` | `pass` |
| `embryo_generated` | `pass` |
| `control_dashboard_generated` | `pass` |
| `grs_generated` | `pass` |
| `cqs_generated` | `unknown` |
| `proposal_gate_available` | `pass` |
| `semantic_preservation_passed` | `pass` |
| `effectiveness_checked` | `pass` |
| `federation_export_validated` | `pass` |
| `agents_integration_reviewed` | `unknown` |
| `hooks_integration_reviewed` | `unknown` |

## Blockers

- `graph`: AGENTS.md and hooks integration review has not passed -> run mirai-graph-integration-review with durable AGENTS.md and hook/CI refs

## Next Actions

- run mirai-graph-integration-review with AGENTS.md and hook/CI refs
- do not claim GGA9 until integration review passes
