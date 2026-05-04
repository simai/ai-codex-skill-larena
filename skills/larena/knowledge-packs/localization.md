# Localization

Larena localization should be designed as a portable platform primitive, not as isolated Laravel language-file management.

## Target Model

- Package source translations belong to packages.
- Project custom translations belong to the application/site and should be represented as override data.
- Regional settings belong to the platform configuration layer and need clear API/admin permissions.
- Future SitePack adapters should be able to transport localization data without mixing source files, custom overrides and runtime settings.

## Safe Defaults

- Translation reads may use normal Laravel translation loading.
- Translation writes, import/export, sync, scanner and watch operations are administrative operations and must be permissioned, audited and bounded.
- Scanner/watch tasks should run through CLI, scheduler, queue or another bounded background path, not as ordinary web/AJAX requests.
- AI-assisted localization must use explicit tools/capabilities, limits and audit policy; it must not crawl or rewrite arbitrary language files without a manifest-backed policy.

## Package Standardization Rule

For packages that touch translations or regional settings, require:

- `module.yaml` command list that matches registered Artisan commands;
- route/API documentation with session mode and permission expectations;
- smoke check for route registration and at least one report/export/read path;
- concept-alignment notes for Bitrix/SF5/SitePack parity;
- clear note about source translations versus custom overrides.
