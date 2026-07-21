# Package Map

Always verify the package map against the active project Specs, Workspace
profile and Root release manifest. The canonical 2026-07 baseline is 42 unique
packages: 23 in the accepted runnable assembly and 19 workspace-only.

Runnable assembly:

- platform and administration: `larena/core`, `larena/admin`,
  `larena/cockpit`, `larena/ui`, `larena/dataview`, `larena/layout`;
- identity and governance: `larena/auth`, `larena/access`, `larena/audit`,
  `larena/licensing`;
- content and documentation: `larena/content`, `larena/docara`,
  `larena/property`, `larena/search`, `larena/lang`;
- files and links: `larena/filesystem`, `larena/file-manager`,
  `larena/storage`, `larena/link`;
- integration and operations: `larena/rest`, `larena/setting`,
  `larena/backup`, `larena/update`.

Workspace-only portfolio:

- AI and automation: `larena/ai`, `larena/ai-provider`, `larena/automation`,
  `larena/mcp`;
- runtime services: `larena/chat`, `larena/monitoring`,
  `larena/notification`, `larena/queue`, `larena/scheduler`, `larena/secret`,
  `larena/visibility`;
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

- root app may still identify as `laravel/laravel`;
- docs may still mention old `simai/*` package names;
- `larena/update` is the current package identity; `larena/upserv`,
  `Simai\Upserv`, `simai_upserv` and old `simai:upserv:*` commands are legacy
  compatibility surfaces unless a bounded migration explicitly replaces them;
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
