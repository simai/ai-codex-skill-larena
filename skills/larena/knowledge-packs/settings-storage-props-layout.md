# Settings Storage Props Layout

Larena should align with Bitrix/SF5 concepts while staying Laravel-native.

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

When moving an existing `category + code` settings implementation toward SF5 Settings DNA, do not start with a destructive schema rewrite. First add a compatibility layer:

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
- document remaining gaps separately: dependency/conflict policy for schema-pack discovery and resolver overlay of pending values.

Do not remove legacy `code`, `area_id`, `page_id`, `user_id` until installed projects, admin forms, import/export and tests have moved to the canonical model. Runtime schema publication, value history and pending review already exist as baselines; new import/export workflows should build on them instead of bypassing them.

The first settings history/audit baseline now exists in `larena/setting`:

- `sf_setting_history` is append-only value history for `SettingService` writes and deletes;
- `SettingAuditService` records old/new value, namespace/key, context, actor/source metadata and operation metadata when the history table exists;
- `sf_setting_schema_history` is append-only schema-pack install/update history for `SettingSchemaRegistry` publication;
- `SettingSchemaAuditService` records schema pack and legacy category schema install/update events with old/new snapshots, source path, format and definitions count;
- this is a settings value/schema audit baseline, not the final workflow layer.

The first settings pending-review baseline now exists in `larena/setting`:

- `sf_setting_pending_changes` stores proposed settings changes with status `pending`, `applied` or `rejected`;
- `SettingPendingService` supports `proposeSet`, `proposeDelete`, legacy propose, `apply` and `reject`;
- `apply` writes through `SettingService`, so normal value history is also recorded in `sf_setting_history`;
- `/admin/settings/pending` provides the first stateful admin/API review surface for listing pending changes and applying or rejecting them;
- the pending review routes are admin/session routes protected by settings view/edit access, not sessionless background endpoints;
- SitePack/config-KV imports and AI-generated settings changes should stage proposals through the pending layer first instead of writing directly to runtime values.

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

Richer schema-pack dependency/conflict policy and resolver overlay of pending values remain separate future layers.

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

Current `larena/props` is a file-based property type/template package, not the final universal property value model. It ships JSON definitions, translations and Blade templates and exposes admin template editing/import/export.

When inspecting or extending `larena/props`, require an explicit safety gate before functional growth:

- do not treat submitted translation/template content as safe executable code;
- custom translation textarea parsing must stay structured and non-executing; JSON arrays are the current safe baseline;
- template save and preview paths must be restricted to approved property template roots for the selected property;
- ZIP import must use canonical path checks, extension/path allowlists and per-entry size limits;
- protect admin routes with explicit `larena/access` operations, not only generic `auth`;
- add audit/rollback for executable Blade template edits;
- document any remaining trusted-admin Blade execution as an operational risk rather than exposing it to public/background/API/AI flows;
- keep SitePack mapping separate until property schema and entity-bound values are accepted.

## Storage

Storage 2.0 reference:

- storage registry metadata, not arbitrary user-data table;
- stable `code`;
- active/sort;
- MV profile;
- encryption flag;
- element-level ACL flag;
- logging flag;
- `settings_json`;
- audit fields.

Compare with Larena filesystem/assets and SitePack SHA-256 blob conventions.

## Layout

Reference model: `Atomic Block -> Section -> Page`.

Larena page builder should map:

- data provider;
- view;
- renderer;
- SF5 components/smart components;
- machine-readable specs for editor/developer/AI workflows.
