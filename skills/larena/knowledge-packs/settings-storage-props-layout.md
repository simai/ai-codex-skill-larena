# Settings Storage Props Layout

Larena should define native Larena settings/storage/props/layout contracts while preserving useful migration references from Bitrix and older SIMAI implementations.

## Settings

Reference direction from Bitrix `simai.main`:

- schema;
- value;
- history;
- pending;
- scoped resolver;
- facade API;
- import/export;
- explainable direct vs resolved values.

Larena question: evolve `larena/setting` toward this model or split lower-level platform settings package.

Canonical central package TZ now lives at `/Users/rim/Documents/GitHub/larena/docs/developer/setting/setting-package-tz.md`.

Use it as the audit baseline for `larena/setting`. Treat the package as the Larena configuration layer: schema packs, runtime schema registry, `namespace + key`, `site_id + level + scope_id`, resolver/explain, pending review, config-KV and SitePack config-only adapter. Do not let settings become generic business-data storage, file storage, property storage, REST gateway, MCP write surface, licensing truth or update-server install policy.

When reviewing `larena/setting`, check its links to:

- `larena/core` for registry/doctor/preflight status;
- `larena/auth` for EntryObject/actor identity;
- `larena/access` for settings operations;
- `larena/admin` for operator UX;
- `larena/property` for typed controls only, not value ownership;
- `larena/audit` for future normalized audit events;
- `larena/rest` and `larena/mcp` for governed API/tool exposure;
- `larena/licensing` for capabilities, without local pro flags;
- `larena/lang` for schema labels/messages;
- SitePack/update for config transport and schema-pack delivery.

When moving an existing `category + code` settings implementation toward Larena Settings DNA, do not start with a destructive schema rewrite. First add a compatibility layer:

- value object for `namespace + key` identity mapped to the current legacy code;
- value object for context that exposes DNA fields while preserving current storage fields;
- resolver service that returns direct/default/resolved/missing metadata;
- explain output with candidate layers and unsupported layers called out explicitly;
- tests against the current legacy tables so future migrations preserve behavior.

After this layer is stable, the next safe migration step is additive canonical persistence:

- add nullable `namespace` and `key` columns to definition and value tables;
- add nullable `level` and `scope_id` columns to value tables;
- backfill legacy rows as `simai.settings.legacy + code`;
- backfill legacy context into `level + scope_id` without dropping old columns;
- make the resolver prefer canonical `namespace/key + level/scope_id` values while falling back to legacy columns;
- support `all_users` as `level = all_users, scope_id = null`;
- support role values as `level = role, scope_id = role_id`.

The first resolver-first read API baseline now exists in `larena/setting`:

- `SettingService::get()` keeps the legacy scalar signature but reads through `SettingResolver`;
- new package code should prefer `resolve*()` / `explain*()` whenever it needs direct/default/missing metadata, source layer, candidates, diagnostics, REST, SitePack, AI-agent context, migrations or health checks;
- convenience methods include `getNamespaceKey()`, `getCategoryCode()`, `explainNamespaceKey()`, `setting_resolved()` and `setting_explain()`;
- helper/UI read paths should use the shared `SettingValueLookup` and resolver-first reads instead of local raw `sf_setting.code` / `sf_setting_value` lookups;
- the settings JSON read endpoint can return additive `resolved` metadata next to the legacy scalar `value`;
- `get()` remains acceptable for simple template reads and legacy scalar compatibility.
- pending overlays are explicit: `resolveWithPending()` / `explainWithPending()` and namespace/category variants show review proposals under `pending`, while normal `resolve*()` / `explain*()` keep committed effective values only;
- the `value` field in pending preview still means committed effective value; pending rows are review/diagnostic data and must not be treated as applied runtime state;
- use `setting_explain_pending()` or service `explainWithPending()` for admin/AI/REST diagnostics that need to preview pending proposals.

After additive persistence, introduce runtime schema storage through explicit publication, not through hidden UI reads:

- add schema-pack and schema-definition runtime tables;
- treat package-level `settings.schema-pack.json` as the canonical package contract for runtime schema publication;
- require schema packs to declare `schema_version`, pack identity/version, install/update semantics, rollback notes, UI binding, and machine-readable definitions with `namespace`, `key`, legacy mapping, type, default, levels, presentation, validation/options, and migration hints;
- publish the canonical schema pack with `php artisan setting:schema-publish --all` when the file is available;
- keep explicit publication of legacy `config/settings/*.json` categories available only as a compatibility path, for example through `php artisan setting:schema-publish --all --legacy-categories` or a direct category command;
- keep a `--dry-run` mode for install/update diagnostics;
- make settings forms prefer runtime schema definitions when present;
- keep legacy JSON materialization only as compatibility fallback for unpublished categories;
- discover installed package schema packs explicitly with `php artisan setting:schema-publish --discover --dry-run` and then `php artisan setting:schema-publish --discover`;
- never auto-apply package schema packs during web requests, form rendering, Laravel package discovery, or AI-agent context gathering;
- document remaining gaps separately: dependency/conflict policy for schema-pack discovery and richer schema-pack install policy.

Do not remove legacy `code`, `area_id`, `page_id`, `user_id` until installed projects, admin forms, import/export and tests have moved to the canonical model. Runtime schema publication, value history and pending review already exist as baselines; new import/export workflows should build on them instead of bypassing them.

Current active compatibility records for `larena/setting` are tracked in the central Larena legacy registry:

- `setting.category_code_identity`;
- `setting.service_get_scalar_api`;
- `setting.legacy_json_schema_publication`.

The first settings history/audit baseline now exists in `larena/setting`:

- `sf_setting_history` is append-only value history for `SettingService` writes and deletes;
- `SettingAuditService` records old/new value, namespace/key, context, actor/source metadata and operation metadata when the history table exists;
- `sf_setting_schema_history` is append-only schema-pack install/update history for `SettingSchemaRegistry` publication;
- `SettingSchemaAuditService` records schema pack and legacy category schema install/update events with old/new snapshots, source path, format and definitions count;
- `SettingActorResolver` is the shared actor/source resolver for value audit, schema audit and pending changes; do not duplicate auth/session probing in separate services;
- this is a settings value/schema audit baseline, not the final workflow layer.

The first settings pending-review baseline now exists in `larena/setting`:

- `sf_setting_pending_changes` stores proposed settings changes with status `pending`, `applied` or `rejected`;
- `SettingPendingService` supports `proposeSet`, `proposeDelete`, legacy propose, `apply` and `reject`;
- `apply` writes through `SettingService`, so normal value history is also recorded in `sf_setting_history`;
- `/admin/settings/pending` provides the first stateful admin/API review surface for listing pending changes and applying or rejecting them;
- the pending review routes are admin/session routes protected by settings view/edit access, not sessionless background endpoints;
- SitePack/config-KV imports and AI-generated settings changes should stage proposals through the pending layer first instead of writing directly to runtime values.
- pending review UI baseline includes status/action/source/level filters, side-by-side current/proposed value comparison and bulk apply/reject for selected pending rows;
- pending admin/API output and resolver pending overlays should use `SettingPendingSerializer`, so list and preview payloads do not drift;
- bulk pending actions must process only rows that are still in `pending` status and must remain stateful admin actions, not background/sessionless endpoints.

The first config-KV settings transport baseline now exists in `larena/setting`:

- `SettingConfigKvTransport` exports and imports `larena.settings.config-kv` payloads;
- import supports dry-run/report mode and creates pending changes through `SettingPendingService`;
- unchanged values are skipped by default;
- command entrypoint: `php artisan setting:config-kv export|import <path>`;
- this is the package-local settings transport baseline; SitePack mapping must wrap this format rather than write settings values directly.

The first SitePack settings adapter baseline now exists in `larena/setting`:

- `SettingSitePackAdapter` maps settings config-KV to SitePack `config-only` packages;
- command entrypoint: `php artisan setting:sitepack export|import <package-dir>`;
- export writes `sitepack.manifest.json`, `sitepack.catalog.json` and `artifacts/config/kv.ndjson`;
- the artifact media type is `application/vnd.sitepack.config-kv+ndjson`;
- Larena-specific context is stored in the optional `larena` field while standard SitePack fields keep `scope`, `namespace`, `key`, `value`, `sensitivity` and `applyPolicy`;
- import converts SitePack config entries back into `larena.settings.config-kv` and stages pending changes;
- entries with `applyPolicy=never` are skipped by default, because secrets and non-portable values must not be applied automatically.

The first package-to-package schema-pack discovery baseline now exists in `larena/setting`:

- installed Composer packages may ship root-level `settings.schema-pack.json`;
- `setting:schema-publish --discover --dry-run` scans `vendor/*/*/settings.schema-pack.json` and reports publishable packs without writing runtime schema;
- `setting:schema-publish --discover` publishes discovered packs through the same runtime schema registry and schema-change audit path as direct schema-pack publication;
- install/update flows should run dry-run first, review the report, then explicitly publish accepted schema packs;
- discovery is a package install policy baseline, not a hidden runtime side effect.
- schema-pack policy v2 now reports required dependencies, duplicate `namespace + key` definitions, cross-pack definition ownership conflicts, definitions outside `pack.namespace_prefix`, and version downgrade warnings;
- real schema-pack publication must be blocked when policy errors are present; warnings are review diagnostics.

Richer schema-pack dependency ordering and marketplace/update-server install policy remain separate future layers. Pending overlay preview already exists as an explicit read mode and should stay opt-in.

## Universal Properties

Bitrix `simai.property` is a reference for reusable property controls in view/edit/filter contexts.

Observed types include:

- entity;
- URL;
- file;
- color;
- checkbox;
- sort;
- link;
- phone;
- map.

Larena should separate property storage, UI render/edit/filter contracts and CRUD integration.

Current `larena/property` is a file-based property type/template package, not the final universal property value model. Historical `larena/props` / `simai/props` aliases were removed before production adoption and must not be used as active package identities.

Canonical central package TZ now lives at `/Users/rim/Documents/GitHub/larena/docs/developer/property/property-package-tz.md`.

Use it as the audit baseline for `larena/property`. Treat the package as the typed field/property contract layer: property types, definitions, host binding, value lifecycle, render model, modes/surfaces, provider bindings, template policy, import/export shape and property demonstrator. Do not overclaim the current implementation as the final entity-bound value subsystem until `larena/storage`, `larena/filesystem`, provider registry and SitePack property profile are designed and implemented.

When reviewing `larena/property`, check its links to:

- `larena/core` for package registry/doctor status;
- `larena/setting` for using property controls in settings UI without owning settings values;
- `larena/admin` for shell/contributions and operator UX;
- `larena/access` for property operations;
- `larena/audit` for definition/value/template/import/export events;
- `larena/filesystem` for file/blob references;
- `larena/storage` for entity-bound records;
- `larena/rest` and `larena/mcp` for safe DTO/tool exposure;
- `larena/licensing` for advanced property packs/capabilities;
- `larena/lang` for labels/options/messages;
- SitePack/update for portable property profiles and package delivery.

After the 2026-05-13 L4 batch, treat `larena/property` as `L4 Demonstration Ready` for its current file-backed definition/rendering/admin boundary. It has canonical package identity, `module.yaml`, architecture/demonstrator/roadmap docs, a package audit report, `property:doctor`, explicit `property.access:<operation>` route policy and installed-site smoke evidence.

Do not overclaim `larena/property` as the final universal property platform yet. Entity-bound property value storage, SitePack property profile, deeper render/import tests and production-grade template write audit/rollback remain post-L4 roadmap items.

When inspecting or extending `larena/property`, require an explicit safety gate before functional growth:

- do not treat submitted translation/template content as safe executable code;
- custom translation textarea parsing must stay structured and non-executing; JSON arrays are the current safe baseline;
- template save and preview paths must be restricted to approved property template roots for the selected property;
- ZIP import must use canonical path checks, extension/path allowlists and per-entry size limits;
- protect admin routes with explicit `property.access:<operation>` operations, not only generic `auth`;
- run `php artisan property:doctor --json` on the installed Larena app after package changes;
- add audit/rollback for executable Blade template edits;
- document any remaining trusted-admin Blade execution as an operational risk rather than exposing it to public/background/API/AI flows;
- keep SitePack mapping separate until property schema and entity-bound values are accepted.

## Storage

For Larena, treat `storage` as a Larena-native universal dynamic data storage layer. It stores arbitrary dynamic structured data through explicit storage structures, typed property bindings, access-aware queries and SitePack import/export.

Terminology:

- In user-facing and Russian developer docs prefer "storage structure" / "структура хранилища" or "описание хранилища".
- Use `schema` only for machine-readable contracts such as `storage.schema.yaml`.
- Avoid "constructor" unless it clearly means the admin UI for creating/configuring storage structures.

Bitrix `simai.storage` is a reference and migration source, not the Larena runtime blueprint. Compatibility with Bitrix means data transport through SitePack:

```text
Bitrix source adapter -> SitePack storage profile -> Larena storage import
```

Do not copy Bitrix admin UI, `D/R/W` rights, table naming, module installer mechanics, or per-storage generated tables as mandatory Larena baseline.

Storage 2.0 reference ideas worth preserving:

- storage registry metadata, not arbitrary user-data table;
- stable `code`;
- active/sort;
- MV profile;
- encryption flag;
- element-level ACL flag;
- logging flag;
- `settings_json`;
- audit fields.

History/revisions are an optional capability, not a mandatory baseline for every storage. Public/private is not a storage type; visibility is decided by access policy, publication state and target surface.

When reviewing or drafting `larena/storage`, require these checks from the Storage TZ:

- explicit storage lifecycle: draft, validate, dry-run, publish/apply, active, change proposal, dry-run impact, background migration/apply, archive/disable;
- heavy operations must be dry-run/preflight first and then background jobs with progress, verification, report and audit event;
- formal Filter/Sort DSL with type-aware allowed operators, no arbitrary SQL and seek/cursor pagination;
- query planner must be explainable and choose between canonical values, typed indexes, detached/index tables, projections and search adapters;
- admin UX must expose consequences, progress, query/access explain and health diagnostics, not low-level database controls;
- acceptance must cover value shapes, localization, file references, access-filtered lists/counts, cursor pagination, projection fallback and import dry-run/idempotency;
- delivery must be phased: R1 Core, R2 workflow data, R3 sensitive data, R4 search, R5 optimization tooling, R6 advanced admin/enterprise.

Compare with Larena filesystem/assets and SitePack SHA-256 blob conventions.

## Layout

Reference model: `Atomic Block -> Section -> Page`.

Larena page builder should map:

- data provider;
- view;
- renderer;
- SF5 components/smart components;
- machine-readable specs for editor/developer/AI workflows.
