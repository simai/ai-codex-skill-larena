---
name: larena
description: Build, diagnose, document, and evolve Larena, the SIMAI Laravel CMS/application platform. Use for Larena application and larena/* package work, modular admin, installer/update flows, registration/licensing integration, SitePack bridge, Docara product proof, REST/API safety, settings/storage/props/layout/search alignment, migration references from Bitrix/older SIMAI systems, release readiness, QA, and repository knowledge capture.
---

# Larena

`larena` owns Larena platform facts, packages, modular admin, install/update,
registration, SitePack adapters, Docara proof, API safety and package readiness.

Before any activity load:

- [kernel/larena-dna.md](./kernel/larena-dna.md);
- [kernel/platform-scope.md](./kernel/platform-scope.md);
- [kernel/non-negotiables.md](./kernel/non-negotiables.md);
- [kernel/output-contract.md](./kernel/output-contract.md);
- [references/canonical-package-portfolio.md](./references/canonical-package-portfolio.md);
- [rules/skill-mesh-balance.md](./rules/skill-mesh-balance.md).

## Mirai Graph Runtime Entry

Use federation route, Larena process contract, launch record and graph context
for substantial work. Raw Larena/package sources remain authoritative. A
markdown plan alone does not authorize package coding or release.

Load [FULL_RUNTIME_PLAYBOOK.md](./FULL_RUNTIME_PLAYBOOK.md) for goal execution,
developer feedback, legacy repository preparation, full activity/specialist
routing, platform matrix and migration reference map.

## Core Workflow

1. Identify surface: entry app, package, admin, update/registration, SitePack,
   Docara, REST, data/settings/layout, docs, runtime or QA.
2. Select activity from `activities/activity-registry.json` and the smallest
   specialist set.
3. Load only selected knowledge packs and package/project source of truth.
4. For package code, require process contract, launch scope, allowed files,
   tests, evidence path and graph-sync proposal boundary.
5. Check Larena concept alignment before expanding package functionality.
6. Implement/diagnose the smallest coherent platform slice.
7. Run package/install/migration/API/browser checks proportional to risk.
8. Update package metadata, docs, changelog and rollback/release artifacts when
   behavior or delivery contracts changed.

## Non-Negotiable Boundaries

- `simai/larena` is the bootstrap entry, not the full platform source.
- The current Specs registry and Workspace profile define the canonical
  `larena/*` portfolio; do not reconstruct it from historical package files.
- `larena-upserv`, split Docara packages, `rest_doc`, standalone 2FA and old
  SIMAI/Bitrix/SF5 models are compatibility or migration references only.
- Keep update server and closed registration/licensing server separate.
- Keep SitePack platform-neutral and Larena adapters platform-specific.
- Never expose arbitrary REST class/method execution without registration,
  allowlist, ACL, audit and risk controls.
- Keep Blade presentation-only and assets/data logic in owned layers.
- Preserve useful free/core capability and baseline safety.
- Install/update must be idempotent with explicit migration and rollback notes.

## Companion Ownership

Use `dev` for repository delivery, `sf5` for shared frontend contracts, `docs`
for documentation method, `ops` for runtime/deploy, `tester` for acceptance,
`seo`/`ux` for their contracts, and `bitrix` for migration/source behavior.

## Output

Return goal/surface, selected activity and owners, confirmed facts versus
inference, changed package/contracts, checks, migration/rollback impact,
remaining risk and next action.
