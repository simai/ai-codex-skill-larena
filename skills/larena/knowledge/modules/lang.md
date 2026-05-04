# `larena/lang`

Canonical Composer package: `larena/lang`.

Legacy compatibility surface: old docs and operation codes may still use `simai/lang` or `simai.translation.*`. New Larena-facing docs and package contracts should use `larena/lang` while preserving compatibility intentionally.

## Role

`larena/lang` owns the core localization and regional-settings layer:

- package-owned source translations under package `resources/lang`;
- application-owned custom overrides under `resources/lang_custom`;
- locale list and default locale behavior;
- regional settings CRUD;
- admin translation workflows;
- translation reports and sync/watch commands.

It is a core platform package, not a product-specific AI translation engine or language-pack marketplace by itself.

## Current Package Notes

- Current provider registers these package commands:
  - `simai:install-lang`
  - `lang:force-custom-loader`
  - `lang:watch`
  - `lang:scheduled-watch`
  - `lang:sync`
  - `lang:report`
  - `simai:test-loader`
- Source contains `LangImportCommand`, `LangExportCommand` and `EnhancedWatchTranslationsCommand`, but they are not currently registered by `SLangProvider`.
- `LangImportCommand` and `LangExportCommand` currently have empty typed handlers and must not be advertised as usable release commands until implemented and registered.
- The package globally replaces Laravel's translation loader, so boot-order regression coverage is required before production hardening.

## Invariants

- Treat package translations as source data and `resources/lang_custom` as project/user override data.
- Do not overwrite custom translations without an explicit import/sync policy and rollback/audit trail.
- Do not run watch/scanner operations from normal web requests; use commands, scheduler, queues or bounded background workers.
- Translation scanners must have runtime limits because broad vendor/project scans can become expensive.
- Regional settings APIs and translation write operations need explicit permission policy, not only generic authenticated admin access.
- SitePack localization must map source translations, custom overrides and regional settings as separate portable concepts.

## Gates Before New Localization Features

Do not build AI translation, language packs, marketplace translation flows, SitePack localization import/export or external translation-service automation until these decisions are accepted:

- canonical operation namespace and legacy alias policy;
- explicit route access matrix for all translation/regional-settings read and write routes;
- registered import/export command contract and file formats;
- audit events for import, sync, overrides, ignore/reset actions and regional settings changes;
- SitePack mapping for translations, custom overrides and regional settings;
- loader boot-order regression tests;
- scanner/backpressure limits and background execution policy.

## Smoke Checks

Use the Larena entry app to verify installed behavior:

```bash
/Applications/ServBay/bin/php artisan larena:validate-packages --path=/Users/rim/Documents/GitHub/larena-lang --strict
/Applications/ServBay/bin/php artisan route:list --path=admin/translations
/Applications/ServBay/bin/php artisan route:list --path=admin/regional-settings
/Applications/ServBay/bin/php artisan route:list --path=api/v1/regional-settings
/Applications/ServBay/bin/php artisan list | rg "lang:|simai:install-lang"
/Applications/ServBay/bin/php artisan lang:report --format=json
```
