# Package Map

> Источник: larena-specs `specs/registry.json`, larena `composer.json` · Проверено: 2026-10-23 · Версия: larena-specs a19a9f10a, larena bce7b637

Always verify the package map against the active project Specs, Workspace
inventory and Root Composer files. Numbers and the command to re-check them:
[../references/canonical-package-portfolio.md](../references/canonical-package-portfolio.md).
On 2026-10-23: 44 packages in Specs, 26 in the Root assembly, 18 workspace-only.

Assembly (26):

- platform and administration: `larena/core`, `larena/admin`,
  `larena/cockpit`, `larena/ui`, `larena/dataview`, `larena/layout`;
- identity and governance: `larena/auth`, `larena/access`, `larena/audit`,
  `larena/licensing`, `larena/secret`;
- data and content: `larena/storage`, `larena/property`, `larena/setting`,
  `larena/search`, `larena/lang`;
- files and links: `larena/filesystem`, `larena/file-manager`, `larena/link`;
- runtime services: `larena/queue`, `larena/scheduler`,
  `larena/monitoring`, `larena/notification`;
- integration and operations: `larena/rest`, `larena/backup`, `larena/update`.

Workspace-only (18):

- content and documentation: `larena/docara`; `larena/content` (retired
  2026-09-23, Storage owns records and publication);
- AI and automation: `larena/ai`, `larena/ai-provider`, `larena/automation`,
  `larena/mcp`;
- communication and security: `larena/chat`, `larena/telephony`,
  `larena/security`, `larena/visibility`;
- update platform: `larena/update-client`, `larena/update-registration`;
- workflow platform and adapters: `larena/workflow`,
  `larena/workflow-amocrm`, `larena/workflow-bitrix24`,
  `larena/workflow-email`, `larena/workflow-github`,
  `larena/workflow-messenger`.

MFA/2FA is a capability of `larena/auth`, not a separate package. The retired
`larena/two-fa` identity may appear only in archive, migration or compatibility
evidence; never restore it into the current package portfolio.

Likewise, `larena/upserv`, split `larena/docara-core` /
`larena/docara-admin`, `larena/rest-doc` and `larena/logs` are historical
identities, not current package-map entries. Preserve an old name only at a
bounded compatibility boundary and do not use it for new product ownership.

Known cleanup risks:

- root app identifies as `simai/larena`; older checkouts may still say `laravel/laravel`;
- docs may still mention old `simai/*` package names;
- `larena/update` is the current package identity; `larena/upserv`,
  `Simai\Upserv`, `simai_upserv` and old `simai:upserv:*` commands are legacy
  compatibility surfaces unless a bounded migration explicitly replaces them;
- package default branches may be unusual and should not be assumed stable without verification.

When diagnosing packages, inspect:

- `composer.json`;
- service provider;
- `module.yaml`;
- config `config/larena-<package>.php` (older SIMAI-era packages: `simai_*.php`);
- commands `larena:*` (installer: `php artisan larena:install`; older: `simai:install-*`);
- migrations;
- routes;
- resources/lang parity;
- tests and docs.
