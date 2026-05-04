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
