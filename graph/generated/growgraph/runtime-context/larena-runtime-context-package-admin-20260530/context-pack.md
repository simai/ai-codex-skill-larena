# GrowGraph Runtime Context: larena

- Task: `Проверить Larena package, modular admin, installer update flow и release readiness`
- Objects: 10
- Relations: 12
- Canonical writes: false

## Included Objects

- `skill.larena.core` (0.87): Coordinates Larena Laravel CMS/platform work across entry app, packages, admin, update/registration, SitePack, Docara, REST, settings/storage/props/layout, release and runtime.
- `capability.larena.release-readiness` (0.72): Gate package/platform release readiness and QA evidence.
- `policy.larena.platform-boundary` (0.69): Keep Larena package/platform facts in owner skill, preserve SitePack as transport, keep update/registration security explicit and coordinate UX/SEO/docs/tester gates.
- `capability.larena.admin-platform` (0.54): Coordinate modular admin, CRUD, slots, settings and UI contracts.
- `capability.larena.entry-install-readiness` (0.54): Check starter entry app install/run baseline and bootstrap constraints.
- `capability.larena.package-diagnostics` (0.54): Diagnose Larena packages, providers, migrations, module metadata and readiness.
- `capability.larena.new-package` (0.36): Plan and scaffold Larena package contracts and package docs.
- `capability.larena.ops-runtime` (0.36): Coordinate hosting, queues, cron, Laravel runtime and update-server environments.
- `capability.larena.update-registration` (0.36): Handle update server, registration/licensing and delivery channels.
- `capability.larena.docara-product` (0.18): Use Docara as first product proof and acceptance scenario.

## Raw Source Refs

- `skills/larena/SKILL.md`
- `skills/larena/activities/release-readiness.json`
- `skills/larena/kernel/platform-scope.md`
- `skills/larena/kernel/non-negotiables.md`
- `skills/larena/activities/admin-platform.json`
- `skills/larena/activities/entry-install-readiness.json`
- `skills/larena/activities/package-diagnostics.json`
- `skills/larena/activities/new-package.json`
- `skills/larena/activities/ops-runtime.json`
- `skills/larena/activities/update-registration.json`
- `skills/larena/activities/docara-product.json`

## Runtime Boundary

Graph context is routing/capability orientation only. Raw skill files remain authoritative.
