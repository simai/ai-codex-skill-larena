---
name: larena
description: Build, diagnose, document, and evolve Larena, the SIMAI Laravel CMS/platform branch of SF5. Use for Larena application and larena/* package work, modular admin, installer/update flows, registration/licensing integration, SitePack bridge, Docara product proof, REST/API safety, settings/storage/props/layout alignment with Bitrix/SF5, release readiness, QA, and repository knowledge capture.
---

# Larena

Use this skill as a Larena engineering council, not as one monolithic Laravel expert. The coordinator identifies the work mode, loads only the relevant specialists and knowledge packs, then synthesizes one implementation, review, architecture, QA, or documentation decision.

Before any activity logic, load and obey:

- [kernel/larena-dna.md](./kernel/larena-dna.md)
- [kernel/platform-scope.md](./kernel/platform-scope.md)
- [kernel/non-negotiables.md](./kernel/non-negotiables.md)
- [kernel/output-contract.md](./kernel/output-contract.md)

Use existing legacy/developer materials in `knowledge/`, `modules/`, `checklists/`, `examples/`, and `templates/` as detailed references only after routing selects the relevant surface.

## Core Operating Model

Follow this sequence for substantial Larena tasks:

1. Identify the target surface: entry app, Composer package, update server, registration server, SitePack bridge, Docara product, SF5 integration, docs, runtime/ops, or QA.
2. Identify the primary activity from [activities/activity-registry.json](./activities/activity-registry.json).
3. Select the smallest sufficient specialist set using [rules/routing.md](./rules/routing.md).
4. Load only selected specialist profiles and knowledge packs referenced by those profiles.
5. For modular admin, settings/storage/props/layout UI, install/update UI, registration/licensing screens, Docara UI, or package admin screens, read [knowledge-packs/ux-implementation-contract.md](./knowledge-packs/ux-implementation-contract.md) and use `$ux` screen spec or UX handoff as the interface contract.
6. Apply the baseline Larena contracts from kernel and knowledge packs.
7. For non-trivial work, collect compact specialist assessments before finalizing.
8. Run the coordinator gate from [rules/decision-policy.md](./rules/decision-policy.md).
9. Return one practical result: patch, diagnostic verdict, architecture decision, release/readiness report, QA result, documentation update, or blocker.

Do not load every reference file. Keep `SKILL.md` lean and use progressive disclosure.

When new repeatable project experience should improve this skill, apply [rules/learning.md](./rules/learning.md): teach the narrowest specialist or knowledge pack, not the whole skill.

## Platform Scope Matrix

- `simai/larena` entry app: bootstrap/distribution repository for the free starter set that must install and run before Larena update-server bootstrap exists; it is not the full platform implementation.
- `larena-*` repositories / `larena/*` Composer packages: modular CMS/platform packages with provider, config, commands, migrations, language files, tests, `module.yaml`, and package docs; these are the primary source of Larena platform code.
- Development monorepo/workspace: technical cross-package development surface only, not the customer-facing distribution model.
- `larena-update`: canonical update server that stores installers/updates and coordinates developer/server and user/server flows.
- `larena-upserv`: legacy alias/historical naming for the update server; do not create new package identity or docs under this name.
- `larena-update-registration`: closed-contour registration/licensing server used by the update server for entitlement checks.
- `SitePack`: portable data transport standard between Bitrix and Larena; keep adapters platform-specific.
- `Docara`: likely first product-level proof that Larena is a usable CMS platform.
- `SF5`: frontend/runtime standard and compatibility target with Bitrix-side SF5 concepts.

## Default Activities

Use activity manifests as the first routing layer:

- [activities/package-diagnostics.json](./activities/package-diagnostics.json)
- [activities/entry-install-readiness.json](./activities/entry-install-readiness.json)
- [activities/new-package.json](./activities/new-package.json)
- [activities/admin-platform.json](./activities/admin-platform.json)
- [activities/update-registration.json](./activities/update-registration.json)
- [activities/sitepack-bridge.json](./activities/sitepack-bridge.json)
- [activities/docara-product.json](./activities/docara-product.json)
- [activities/rest-api.json](./activities/rest-api.json)
- [activities/settings-storage-props-layout.json](./activities/settings-storage-props-layout.json)
- [activities/release-readiness.json](./activities/release-readiness.json)
- [activities/documentation.json](./activities/documentation.json)
- [activities/ops-runtime.json](./activities/ops-runtime.json)

If no activity matches, create a temporary activity with `activity_id`, `title`, `triggers`, `required_specialists`, `optional_specialists`, `knowledge_packs`, `required_gates`, and `required_outputs`.

## Specialists

Default specialist roles:

- `platform-architect`: Larena/SF5 platform boundaries, package graph, compatibility with Bitrix concepts.
- `package-installer`: Composer packages, service providers, `simai:install`, migrations, module metadata, install/update contracts.
- `modular-admin`: admin kernel, extension points, slots, contributions, CRUD, UI contracts.
- `update-registration`: update server, registration server, licensing, channels, product delivery.
- `sitepack-bridge`: SitePack profiles, artifacts, import/export, Bitrix/Larena adapters, SHA-256 blobs.
- `sf5-integration`: SF5 UI, loader, smart components, layout/page builder contracts.
- `rest-api`: REST Runner, OpenAPI/Swagger, method safety, ACL-aware API contracts.
- `data-settings-props`: settings, storage, universal properties, layout/content data models.
- `docara-product`: Docara Core/Admin as first product proof and acceptance scenario.
- `qa-validation`: tests, smoke, install checks, browser checks, release gates.
- `ops-runtime`: hosting, queues, cron, Laravel runtime, update-server environments, deploy diagnostics.
- `documentation-learning`: user/developer docs, Docara docs, skill knowledge promotion.
- `security-permissions`: auth/access/2FA, secrets, tokens, license checks, unsafe method execution boundaries.

Load specialist files only when selected:

- [specialists/platform-architect/profile.md](./specialists/platform-architect/profile.md)
- [specialists/package-installer/profile.md](./specialists/package-installer/profile.md)
- [specialists/modular-admin/profile.md](./specialists/modular-admin/profile.md)
- [specialists/update-registration/profile.md](./specialists/update-registration/profile.md)
- [specialists/sitepack-bridge/profile.md](./specialists/sitepack-bridge/profile.md)
- [specialists/sf5-integration/profile.md](./specialists/sf5-integration/profile.md)
- [specialists/rest-api/profile.md](./specialists/rest-api/profile.md)
- [specialists/data-settings-props/profile.md](./specialists/data-settings-props/profile.md)
- [specialists/docara-product/profile.md](./specialists/docara-product/profile.md)
- [specialists/qa-validation/profile.md](./specialists/qa-validation/profile.md)
- [specialists/ops-runtime/profile.md](./specialists/ops-runtime/profile.md)
- [specialists/documentation-learning/profile.md](./specialists/documentation-learning/profile.md)
- [specialists/security-permissions/profile.md](./specialists/security-permissions/profile.md)

## Coordinator Rules

The coordinator must:

1. keep the task inside the current Larena phase and stated repository;
2. choose the smallest sufficient specialist set;
3. separate product direction from current implementation findings;
4. treat mismatches in current packages as diagnostic findings, not automatic direction changes;
5. keep update/registration security boundaries explicit;
6. preserve SitePack as portable transport and keep platform adapters separate;
7. require install, migration, release, rollback, and QA artifacts when the selected activity demands them;
8. update durable knowledge in repo `source/` or this skill when a stable reusable rule is learned.

For simple edits, one primary specialist plus `qa-validation` is enough. For install/update, licensing, SitePack, REST safety, admin architecture, or product proof work, use explicit gatekeepers.

## Assessment Format

For non-trivial review or architecture tasks, use compact specialist assessments:

```json
{
  "specialist": "sitepack-bridge",
  "status": "approved_with_conditions",
  "summary": "Primary conclusion in 1-2 sentences.",
  "findings": [
    {
      "severity": "medium",
      "issue": "What is wrong or risky.",
      "recommendation": "What should be changed or verified."
    }
  ],
  "acceptance": {
    "passed": true,
    "missing": []
  }
}
```

Allowed statuses: `approved`, `approved_with_conditions`, `needs_revision`, `rejected`.

Use:

- [quality/specialist-assessment-template.md](./quality/specialist-assessment-template.md)
- [quality/coordinator-gate-template.md](./quality/coordinator-gate-template.md)
- [quality/release-readiness-template.md](./quality/release-readiness-template.md)

## Baseline Verification

Prefer repository-native commands when available:

- Composer/package graph: `composer validate`, `composer install`, `composer show`, `composer dump-autoload`.
- Laravel app checks: `php artisan about`, `php artisan route:list`, `php artisan migrate --pretend` when safe, package install commands.
- Existing monorepo checks when present: `composer run validate:repo`, `composer run lint:changed`, package PHPUnit suites.
- REST/OpenAPI: route list, Swagger generation/tests, 401/403/2xx access checks.
- UI/admin/docara: browser smoke when a runnable target exists.
- SitePack: Node/PHP validators from `/Users/rim/Documents/GitHub/sitepack` when inspecting `.sitepack` packages.

If checks cannot run, report why and provide the closest safe static verification.

## Legacy Reference Map

Use old developer-authored materials when selected by routing:

- General package rules: [knowledge/simai-package-rules.md](./knowledge/simai-package-rules.md)
- Current package manifest standard: [knowledge-packs/module-yaml-standard.md](./knowledge-packs/module-yaml-standard.md)
- Session-safe background enrichment: [knowledge-packs/session-safe-background-enrichment.md](./knowledge-packs/session-safe-background-enrichment.md)
- Quick start: [knowledge/quickstart.md](./knowledge/quickstart.md)
- Admin package: [knowledge/modules/admin.md](./knowledge/modules/admin.md)
- Access package: [knowledge/modules/access.md](./knowledge/modules/access.md)
- REST package: [knowledge/modules/rest.md](./knowledge/modules/rest.md)
- RestDoc package: [knowledge/modules/rest-doc.md](./knowledge/modules/rest-doc.md)
- Lang package: [knowledge/modules/lang.md](./knowledge/modules/lang.md)
- Docara Core/Admin: [knowledge/modules/docara-core.md](./knowledge/modules/docara-core.md), [knowledge/modules/docara-admin.md](./knowledge/modules/docara-admin.md)
- Work scenarios: [knowledge/work-scenarios.md](./knowledge/work-scenarios.md)
- Checklists: [checklists/](./checklists/)
- Artifact templates: [templates/artifacts/](./templates/artifacts/)
