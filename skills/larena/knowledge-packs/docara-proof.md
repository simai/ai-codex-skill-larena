# Docara Product Proof

Docara is the likely first real product proof for Larena.

## Why Docara

Docara can validate that Larena is usable as a CMS platform, not just a package set:

- public documentation;
- admin editing;
- auth/access;
- settings;
- filesystem/assets;
- localization;
- revisions/import/sync;
- future update packaging;
- future SitePack import/export.

## Product Boundary

Keep Docara split into two deliberate layers:

- `larena/docara-core`: free public runtime for installed/imported documentation, local assets, public routes, file/DB reads and view access checks.
- `larena/docara-admin`: paid/Pro editor/admin layer for page management, create/edit/save, preview, revisions, rollback, sync/import, product packs and AI-assisted documentation workflows.

Do not blur this boundary during package work. Commercial entitlement should later be enforced through the Larena update/registration server flow, not through ad hoc package-local checks.

## Product First Version

Docara running on Larena with enough base packages for real work:

- auth/access;
- admin;
- settings;
- docs/content storage;
- filesystem/assets;
- localization;
- install and health diagnostics;
- REST/docs if needed.

## Platform Milestone

Later milestone: ordinary users install Larena/update client through update server flow and then install products such as Docara without developer friction.

## Acceptance Direction

Use Docara to define:

- minimum package baseline;
- user install path without update server;
- future update-server install path;
- first `.sitepack` package scenario for content/config transfer.

## Current Acceptance Gate

The `simai/larena` bootstrap repository has a first committed Docara acceptance gate. Use it before calling the starter install product-ready:

```bash
php artisan larena:doctor --docara
php artisan docara:sync --dry-run
php artisan test --filter=DocaraAcceptanceDoctorTest
php artisan route:list | grep -E "docara|docs|vendor/docara|search-index"
```

Expected local result:

- `larena:doctor --docara` exits with 0 errors;
- `QUEUE_CONNECTION=sync` may be a local warning, but production-like checks should use a real queue;
- `docara:sync --dry-run` reports `Errors: 0`;
- focused acceptance test passes;
- route list includes public docs, assets, search index and admin Docara routes.

This gate is still not the full product acceptance. The next product-facing gate must add browser/admin checks for login, list, create/edit, preview, save, revision history, rollback, sync/import and permission denial.

## Browser/Admin Gate

After the command-level gate passes, use the committed browser/admin gate in `simai/larena`:

- `docs/developer/docara-browser-admin-acceptance.md`

Minimum accepted browser/admin scenario:

- guest `/admin/docara/pages` redirects to login;
- admin login works;
- page tree renders grouped by version and locale;
- editor assets load locally without CDN dependency;
- admin creates a temporary page through `/admin/docara/pages/create`;
- created page opens in `/admin/docara/pages/{id}/edit`;
- public page renders under `/docs/{version}/{locale}/{slug}`;
- editor save creates an `editor_save` revision;
- rollback restores an earlier revision;
- authenticated user without Docara access receives `403`;
- temporary page, temporary content file and no-access user are cleaned up.

Known live-smoke caveat: current editor create/save is asynchronous. Do not rely only on navigation after clicking `Create` or `Save`; verify status text plus database/public page state.

## SitePack Gate

After browser/admin acceptance, the next Docara product proof is portable import/export through SitePack. Use these committed references in `simai/larena`:

- `docs/developer/rfc/0003-docara-sitepack-import-export.md`
- `docs/developer/docara-sitepack-acceptance.md`

Minimum direction:

- Free Docara Core remains the public runtime for already installed/imported documentation.
- Paid Docara Admin/Pro owns managed import/export, conflict resolution, revision governance, scheduled sync, product packs and AI-assisted documentation workflows.
- SitePack import/export must validate manifest+catalog first, avoid long web requests, use non-executable temp storage, import markdown through `larena/filesystem`, create revisions, and produce machine-readable reports.
- SitePack is the neutral transport. Do not build a direct Bitrix-to-Docara converter as the durable architecture; use Bitrix -> SitePack -> Docara/Larena.
