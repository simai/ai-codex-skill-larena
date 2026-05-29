# Larena Repo GrowGraph Migration

Дата: 2026-05-29

## Scope

Repo-local GrowGraph companion layer for:

```text
skill:larena
```

This migration does not rewrite `skills/larena/SKILL.md` and does not move
Larena domain knowledge out of the Larena skill.

## Source Boundaries

Used sources:

```text
skills/larena/SKILL.md
skills/larena/kernel/larena-dna.md
skills/larena/kernel/platform-scope.md
skills/larena/kernel/non-negotiables.md
skills/larena/kernel/output-contract.md
skills/larena/rules/skill-mesh-balance.md
skills/larena/rules/routing.md
skills/larena/activities/activity-registry.json
skills/larena/activities/package-diagnostics.json
skills/larena/activities/admin-platform.json
skills/larena/activities/update-registration.json
skills/larena/activities/sitepack-bridge.json
skills/larena/activities/docara-product.json
skills/larena/knowledge-packs/product-architecture.md
```

Excluded:

```text
.env
secrets
credentials
raw client data
production exports
screenshots
logs
output/
root source/
```

## Generated Artifacts

```text
graph/source/growgraph/seeds/larena-repo-local-seed-20260529.json
graph/generated/seed-validation/larena-repo-local-seed-validate-20260529/
graph/generated/seed-expansions/larena-repo-local-seed-expand-20260529/
graph/generated/embryo-proposals/larena-repo-local-embryo-proposals-20260529/
graph/generated/control-dashboards/larena-repo-local-control-dashboard-20260529/
graph/generated/growgraph/semantic-preservation/larena-repo-local-semantic-review-20260529/
graph/generated/growgraph/effectiveness-reports/larena-repo-local-effectiveness-20260529/
graph/generated/readiness-scores/larena-repo-local-score-20260529/
graph/federation/exports/larena-repo-local-federation-export-20260529/
graph/generated/growgraph/integration-reviews/larena-repo-local-integration-review-active-gate-20260529/
graph/generated/growgraph/adoption-reports/larena-repo-local-adoption-gga9-active-gate-20260529/
```

## Result

```text
seed validation: success
seed expansion: 36 candidate objects, 33 candidate relations
proposal queue: 69 actions
semantic preservation: pass_with_notes
effectiveness: improved
GRS: 80 / G4_controlled_runtime_candidate
federation export: success
integration review: pass_with_notes
adoption: GGA9 federation_integrated
```

## Active Gate

Repo-local active gate:

```text
scripts/growgraph_contract_gate.py
```

CI integration:

```text
.github/workflows/validate.yml
```

Repo policy:

```text
AGENTS.md
graph/federation/hooks/growgraph-contract-gate.md
```

## Boundary

This is `GGA9 federation_integrated` for the repo-local companion layer.

It is not yet `GGA10` because full graph-first source-of-truth migration has
not been accepted for this repository.

## Next

Create the first-wave adoption dashboard across all migrated skill
repositories.
