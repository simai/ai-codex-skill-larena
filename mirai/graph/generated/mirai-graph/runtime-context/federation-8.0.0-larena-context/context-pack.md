# Mirai Graph Runtime Context: larena

- Task: `Sync raw source changes for larena: federation-impact, methodology, routing-impact, runtime`
- Objects: 12
- Relations: 12
- Canonical writes: false

## Included Objects

- `skill.larena.core` (0.51): Coordinates Larena Laravel CMS/platform work across entry app, packages, admin, update/registration, SitePack, Docara, REST, settings/storage/props/layout, release and runtime.
- `capability.larena.ops-runtime` (0.36): Coordinate hosting, queues, cron, Laravel runtime and update-server environments.
- `policy.larena.platform-boundary` (0.33): Keep Larena package/platform facts in owner skill, preserve SitePack as transport, keep update/registration security explicit and coordinate UX/SEO/docs/tester gates.
- `capability.larena.admin-platform` (0.18): Coordinate modular admin, CRUD, slots, settings and UI contracts.
- `capability.larena.docara-product` (0.18): Use Docara as first product proof and acceptance scenario.
- `capability.larena.entry-install-readiness` (0.18): Check starter entry app install/run baseline and bootstrap constraints.
- `capability.larena.new-package` (0.18): Plan and scaffold Larena package contracts and package docs.
- `capability.larena.package-diagnostics` (0.18): Diagnose Larena packages, providers, migrations, module metadata and readiness.
- `capability.larena.release-readiness` (0.18): Gate package/platform release readiness and QA evidence.
- `capability.larena.rest-api` (0.18): Coordinate REST Runner, OpenAPI, unsafe method boundaries and ACL checks.
- `capability.larena.settings-storage-props-layout` (0.18): Map settings, storage, universal props, layout and content data models.
- `capability.larena.sitepack-bridge` (0.18): Keep SitePack portable transport separate from platform adapters.

## Raw Source Refs

- `skills/larena/SKILL.md`
- `skills/larena/activities/ops-runtime.json`
- `skills/larena/kernel/platform-scope.md`
- `skills/larena/kernel/non-negotiables.md`
- `skills/larena/activities/admin-platform.json`
- `skills/larena/activities/docara-product.json`
- `skills/larena/activities/entry-install-readiness.json`
- `skills/larena/activities/new-package.json`
- `skills/larena/activities/package-diagnostics.json`
- `skills/larena/activities/release-readiness.json`
- `skills/larena/activities/rest-api.json`
- `skills/larena/activities/settings-storage-props-layout.json`
- `skills/larena/activities/sitepack-bridge.json`

## Runtime Boundary

Graph context is routing/capability orientation only. Raw skill files remain authoritative.
