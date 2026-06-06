---
name: larena
description: Build, diagnose, document, and evolve Larena, the SIMAI Laravel CMS/application platform. Use for Larena application and larena/* package work, modular admin, installer/update flows, registration/licensing integration, SitePack bridge, Docara product proof, REST/API safety, settings/storage/props/layout/search alignment, migration references from Bitrix/older SIMAI systems, release readiness, QA, and repository knowledge capture.
---

# Larena

Use this skill as a Larena engineering council, not as one monolithic Laravel expert. The coordinator identifies the work mode, loads only the relevant specialists and knowledge packs, then synthesizes one implementation, review, architecture, QA, or documentation decision.

Before any activity logic, load and obey:

- [kernel/larena-dna.md](./kernel/larena-dna.md)
- [kernel/platform-scope.md](./kernel/platform-scope.md)
- [kernel/non-negotiables.md](./kernel/non-negotiables.md)
- [kernel/output-contract.md](./kernel/output-contract.md)
- [rules/skill-mesh-balance.md](./rules/skill-mesh-balance.md)

Use existing legacy/developer materials in `knowledge/`, `modules/`, `checklists/`, `examples/`, and `templates/` as detailed references only after routing selects the relevant surface.

## Mirai Graph Runtime Entry

For substantial `larena` tasks, use repo-local `graph/specs` and the latest Mirai Graph runtime context as the first machine-readable index for capability selection, routing, readiness, companion contracts and scenario evidence. The graph layer may choose the owner boundary, required gates, related skills and raw-source fallback path for Larena platform, Laravel packages, admin/runtime flows and product-platform judgement. Raw `larena` sources remain authoritative for detailed methodology, judgement, longform playbooks, sensitive rules, reporting format and final domain verdicts. Sensitive/runtime/security and safe-write decisions require raw-source fallback and the relevant owner gate. Platform-specific playbooks stay in the owner skill; the central graph may point to them but must not absorb them. This is Mirai Graph Hybrid SOT, not graph-only runtime.

Larena uses Mirai Graph Technological Process Control as the domain realization
of its development conveyor. For package work, apply the same universal
contracts through Larena-specific DNA, package specs, launch record, allowed
files, evidence package, graph sync proposal, review gates and runtime feedback.
Do not start broad package coding from a markdown plan alone; require the
process contract and Larena/package source-of-truth context.

For user-level Larena goals and stages/milestones, load
[knowledge-packs/larena-goal-execution-profile.md](./knowledge-packs/larena-goal-execution-profile.md).
Use the hierarchy `goal -> milestone -> batch -> checkpoint/evidence -> Kaizen`.
In Russian user-facing Larena replies, say `этап` for canonical `milestone`;
keep `веха` only as a legacy user input alias. Do not rename machine-readable
process keys, launch records or evidence fields.
If the user says `делай цель`, `делай в режиме цели`, or `доведи до результата`,
continue safe Larena batches until the agreed `Done When`, a real blocker,
runtime/destructive approval boundary, or planned human checkpoint.

Before writing implementation code for any Larena package repository, load and
obey [knowledge-packs/package-pre-codegen-repository-preparation.md](./knowledge-packs/package-pre-codegen-repository-preparation.md).
Existing legacy repositories with confirmed backup should be emptied in the
active tree and then rebuilt as clean Larena package repositories. The required
pre-codegen work is repository preparation: package identity, specs reference,
launch context, Composer command contract, hooks, CI, scope checker, evidence
paths, graph-sync proposal boundary and validation before `ready_to_code`.
Installing enforcement on top of old active code is not enough.

In executable Process Control mode, Larena package work must pass the active
state-machine transition before coding, release or acceptance claims. A package
spec or markdown plan can prepare the human projection, but the coding batch
starts only from launch record scope, allowed files, action-gate result and
evidence path; recovery resumes from workflow/launch/evidence/git state.

## Core Operating Model

Follow this sequence for substantial Larena tasks:

1. Identify the target surface: entry app, Composer package, update server, registration server, SitePack bridge, Docara product, Larena UI/frontend integration, docs, runtime/ops, or QA.
2. Identify the primary activity from [activities/activity-registry.json](./activities/activity-registry.json).
3. Select the smallest sufficient specialist set using [rules/routing.md](./rules/routing.md).
4. Load only selected specialist profiles and knowledge packs referenced by those profiles.
5. For modular admin, settings/storage/props/layout UI, install/update UI, registration/licensing screens, Docara UI, or package admin screens, read [knowledge-packs/ux-implementation-contract.md](./knowledge-packs/ux-implementation-contract.md) and use `$ux` screen spec or UX handoff as the interface contract.
6. For public routes, Blade/UI, meta storage, sitemap/robots middleware, Docara bridge, structured data, documentation/product pages, or SEO Contract implementation, treat `$seo` as the contract owner. Implement the SEO Contract through Larena-native routes, storage, views, middleware, packages, or Docara bridge surfaces and return changed routes/templates/config for `$seo` review and `$tester` acceptance. If the SEO Contract conflicts with Larena constraints, report a blocker to `$seo`; do not silently rewrite SEO decisions.
7. For substantial documentation, docs maps, screenshots, user/developer/API guides, or documentation audits, use `$docs` as the technical-writing owner. Keep `$larena` responsible for Larena facts, package contracts, runtime constraints, and Docara product specifics.
8. For package coding, resolve the technological process contract and ensure launch record, allowed files, tests, evidence path and graph sync proposal path are known before implementation.
9. For existing or legacy package repositories, load [knowledge-packs/package-pre-codegen-repository-preparation.md](./knowledge-packs/package-pre-codegen-repository-preparation.md) and complete clean repository preparation: empty old active content when backup is confirmed, create the Larena baseline, link specs, install command contract/hooks/CI/scope checker, validate evidence boundaries and only then allow a launch-record transition.
10. Apply the baseline Larena contracts from kernel and knowledge packs.
11. For non-trivial work, collect compact specialist assessments before finalizing.
12. Run the coordinator gate from [rules/decision-policy.md](./rules/decision-policy.md).
13. Return one practical result: patch, diagnostic verdict, architecture decision, release/readiness report, QA result, documentation update, or blocker.

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
- `SF5`: historical/internal label and frontend/UI reference where useful; Larena backend/package contracts should use Larena names as the canonical identity.
- SF5 `/simai` and `/simai.data` layer DNA: preserve the system-library/overlay meaning, but implement it through Laravel-native package resources, storage, database registries and adapters. Read [knowledge-packs/sf5-simai-layer-dna.md](./knowledge-packs/sf5-simai-layer-dna.md) for cross-platform mapping.

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

- `platform-architect`: Larena platform boundaries, package graph, and compatibility/migration references from Bitrix or older SIMAI systems.
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
- `documentation-learning`: Larena facts, Docara docs context, and skill knowledge promotion; coordinate substantial writing method with `$docs`.
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
- Package repository structure standard: [knowledge-packs/package-repository-structure.md](./knowledge-packs/package-repository-structure.md)
- Core platform baseline: [knowledge-packs/core-platform.md](./knowledge-packs/core-platform.md)
- Search platform baseline: [knowledge-packs/search-platform.md](./knowledge-packs/search-platform.md)
- Package naming standard: [knowledge-packs/package-naming-standard.md](./knowledge-packs/package-naming-standard.md)
- Package completion/readiness standard: [knowledge-packs/package-completion-standard.md](./knowledge-packs/package-completion-standard.md)
- Package TZ standard: [knowledge-packs/package-tz-standard.md](./knowledge-packs/package-tz-standard.md)
- Feature graph standard: [knowledge-packs/feature-graph.md](./knowledge-packs/feature-graph.md)
- Legacy detection patterns: [knowledge-packs/legacy-detection-patterns.md](./knowledge-packs/legacy-detection-patterns.md)
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
