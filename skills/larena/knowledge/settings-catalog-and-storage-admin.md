# Settings Catalog And Storage Admin

> Источник: larena-workspace `packages/setting`, `packages/admin`, `packages/storage` (git log, routes), larena `CHANGELOG.md` · Проверено: 2026-10-23 · Версия: setting b660fad, admin 97a456e0, storage 2790549, larena bce7b637

Facts added in October 2026. Package READMEs lag behind (the `setting`
README still describes the pre-catalog foundation) — trust commits, tests and
Specs over README prose. Model rules (who owns settings, props, storage,
layout) stay in [settings-storage-props-layout.md](./settings-storage-props-layout.md).

## Settings catalog (`larena/setting` + `larena/admin`)

- One `SettingDefinition` model: group, allowed levels, `inherits`, `lockable`,
  `when` conditions, source, rights. Definitions are validated through
  `larena/property` (hidden, readonly, hint, conditions honoured).
- Values are kept **by level** with locale: default → installation → site →
  sections (page-tree ancestors) → page. Each level value has a revision and
  an optional lock; a site-level setting refuses a page value.
- Resolution per page reads one cached per-site snapshot; an explain view
  shows which level a value came from.
- Tables: `larena_setting_definitions`, `larena_setting_level_values` (beside
  the older `larena_setting_values`); the migration copies existing values.
- Changes go through drafts: publish, discard, revert; history per setting
  (an archived setting's history is read-only). Definition changes are checked
  against stored values. Settings take part in SitePack transfer.
- Admin (under «Настройки»): «Каталог настроек» `/admin/settings/catalog`
  (custom settings, package overrides, values on every level with source,
  reset and lock), «Черновики и публикация» `/admin/settings/changes` with a
  pending-drafts counter, history `/admin/settings/history`; site settings
  read and write the catalog. Operation: `setting.catalog.manage`.

## Storage section «Хранилище» (`larena/storage` + `larena/admin`)

- Lists `/admin/storage` and per-structure pages `/admin/storage/<id>`,
  structure settings `/admin/storage/<id>/settings`; a workbench at
  `/admin/storage-workbench`.
- Field editor is built from the property type's declared settings; edits
  that change data count affected records and ask for confirmation
  (`checkFieldChange()`); edits that touch no data (mask, placeholder, step,
  unit) need no migration. Searchable, sortable, indexable and encryptable
  types come from the `larena/property` declaration.
- Lists default to newest first (system sort key `_created_at`); record search
  is limited to 100 characters.
- Field encryption (`larena/secret`): turn on/off for filled fields, rotate and
  rewrap keys; encrypted fields never go to CSV, are not sortable and never
  become a list title. Operations include `storage.encryption.manage`,
  `storage.workbench.record.decrypt`.
- Transfer: CSV export/import (`storage.export.csv`, `storage.import.plan`,
  `storage.import.apply`) and storage SitePack export/import
  (`storage.sitepack.export`, `storage.sitepack.import`: plan first, ids kept
  or remapped, drafts by default).
- Record lists can be placed on a site page from the admin.
- Storage declares names for all its operations (51 on 2026-10-23); roles show
  human names for every operation.

## QA hooks

Root tests that cover these surfaces: `AdminSettingsCatalogTest`,
`MinimalCmsRootIntegrationTest`, `StorageSectionTest`,
`DurableBackgroundOperationsSqliteTest` (migration/table counts change with
each slice — read the current numbers from the test, not from here).
