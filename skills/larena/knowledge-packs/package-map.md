# Package Map

Current package map should be verified against the active repository, but use this as the working start:

- `larena/admin`: admin UI, CRUD, route macros, install orchestration.
- `larena/access`: permissions, access operations, API tokens, entity abilities.
- `larena/auth`: users, login/admin user creation, auth integration.
- `larena/two-fa`: two-factor authentication.
- `larena/setting`: settings UI/storage.
- `larena/property`: universal property definitions and rendering/edit/filter contracts.
- `larena/filesystem`: files/uploads/downloads/archive storage.
- `larena/lang`: translations, custom language overrides and regional settings. Do not expand AI translation, language packs or SitePack localization flows until command/access/audit/SitePack contracts are accepted.
- `larena/rest`: REST runner/API runtime.
- `larena/rest-doc`: Swagger/OpenAPI docs.
- `larena/docara-core`: public documentation engine.
- `larena/docara-admin`: Docara admin/editor/revisions/import.
- `larena/update`: canonical Composer package name for the update server. From `1.6.49`, it has canonical provider/config/command aliases (`Simai\Update\...`, `simai_update`, `simai:update:*`) while preserving the legacy implementation layer.
- `larena/upserv`: legacy Composer alias historically associated with update server. Keep only for backward compatibility; do not create new docs, requirements or product identity under this name.
- `larena/logs`: documented package/repo, but verify whether it is in first baseline.

Known cleanup risks:

- root app may still identify as `laravel/laravel`;
- docs may still mention old `simai/*` package names;
- `larena-update` is the canonical Git source; `larena-upserv`, `Simai\Upserv`, `simai_upserv` and old `simai:upserv:*` commands are legacy compatibility surfaces unless a major-safe migration explicitly replaces them;
- package default branches may be unusual and should not be assumed stable without verification.

When diagnosing packages, inspect:

- `composer.json`;
- service provider;
- `module.yaml`;
- config `simai_*.php`;
- commands `simai:install-*`;
- migrations;
- routes;
- resources/lang parity;
- tests and docs.
