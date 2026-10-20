---
name: larena
description: "Larena: SIMAI CMS на Laravel. Приложение и пакеты larena/*, модульная админка, установщик, обновления, лицензирование, SitePack, REST/API, настройки, layout, поиск, миграции с Bitrix, QA."
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

Executable technology: [technologies/platform-delivery.json](./technologies/platform-delivery.json)
(scenarios: package delivery, diagnostics, release readiness).

Load when relevant:

- [rules/process-control.md](./rules/process-control.md): graph entry,
  launch record, pre-codegen repository preparation;
- [rules/goal-execution.md](./rules/goal-execution.md): goals and stages;
- [rules/developer-feedback.md](./rules/developer-feedback.md): review findings;
- [rules/routing.md](./rules/routing.md) and
  [references/specialist-roster.md](./references/specialist-roster.md);
- [references/baseline-verification.md](./references/baseline-verification.md)
  and [references/reference-map.md](./references/reference-map.md).

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

Use `dev` for repository delivery, `framework` for shared frontend contracts, `docs`
for documentation method, `ops` for runtime/deploy, `tester` for acceptance,
`seo`/`ux` for their contracts, and `bitrix` for migration/source behavior.

## Output

Return goal/surface, selected activity and owners, confirmed facts versus
inference, changed package/contracts, checks, migration/rollback impact,
remaining risk and next action.

Status wording must match evidence. With no changed files, say "решение/план",
never "цель достигнута", "добавлено" or "реализовано". Name only resources the
sources confirm (package, slot, contract fields); unknown concrete values
(action id, permission, handler, wording) are required inputs, not
"existing" items or placeholders presented as facts.
