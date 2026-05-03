# Package Map

Current package map should be verified against the active repository, but use this as the working start:

- `larena/admin`: admin UI, CRUD, route macros, install orchestration.
- `larena/access`: permissions, access operations, API tokens, entity abilities.
- `larena/auth`: users, login/admin user creation, auth integration.
- `larena/two-fa`: two-factor authentication.
- `larena/setting`: settings UI/storage.
- `larena/props`: universal property rendering/edit/filter contracts.
- `larena/filesystem`: files/uploads/downloads/archive storage.
- `larena/lang`: translations and custom language lifecycle.
- `larena/rest`: REST runner/API runtime.
- `larena/rest-doc`: Swagger/OpenAPI docs.
- `larena/docara-core`: public documentation engine.
- `larena/docara-admin`: Docara admin/editor/revisions/import.
- `larena/upserv`: Composer package name historically associated with update server.
- `larena/logs`: documented package/repo, but verify whether it is in first baseline.

Known cleanup risks:

- root app may still identify as `laravel/laravel`;
- docs may still mention old `simai/*` package names;
- `larena-upserv` vs `larena-update` Git source must be technically reconciled;
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
