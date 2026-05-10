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
- publish existing `config/settings/*.json` categories with an explicit command such as `php artisan setting:schema-publish --all`;
- keep a `--dry-run` mode for install/update diagnostics;
- make settings forms prefer runtime schema definitions when present;
- keep legacy JSON materialization only as compatibility fallback for unpublished categories;
- document remaining gaps separately: final `settings.schema-pack.json`, history, pending changes, audit, and SitePack/config-KV import/export.

Do not remove legacy `code`, `area_id`, `page_id`, `user_id` until installed projects, admin forms, import/export and tests have moved to the canonical model. Only after runtime schema publication is verified should history, pending and SitePack/config-KV import/export be implemented.

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
