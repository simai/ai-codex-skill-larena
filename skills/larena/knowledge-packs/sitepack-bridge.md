# SitePack Bridge

Repository: `/Users/rim/Documents/GitHub/sitepack`

SitePack is the shared portable package format for moving website data between systems.

## SitePack v0.4.0 Facts

- canonical extension: `.sitepack`;
- default container: ZIP;
- required root files: `sitepack.manifest.json`, `sitepack.catalog.json`;
- manifest+catalog are source of truth;
- supported core media types include entity graph, asset index, config key-value and recordsets;
- `relations` values are arrays of links;
- CMS-style relation keys can use `property.<CODE>` and `field.<CODE>`;
- asset blobs may be chunked;
- verify chunks and assets by SHA-256 and size;
- canonical blob recommendation: `artifacts/assets/blobs/sha256/<sha256>[.<ext>]`;
- volume sets support split package distribution;
- secure transfer uses external age envelope.

## Larena Role

Larena should use SitePack through an adapter/package, not by changing the platform-neutral standard.

Likely layers:

1. shared conceptual specs for settings, storage, props, layout, relations and assets;
2. SitePack profiles/artifacts for transport;
3. Larena adapter mapping Eloquent/tables/packages to SitePack;
4. Bitrix adapter mapping iblocks/HL/module options/files/SF payloads to SitePack.

## Import Behavior

- Use manifest+catalog.
- Follow artifact `path`.
- Treat unknown media/entity types as warnings when allowed.
- Prefer two-pass import for relations.
- Produce import/export reports with warnings and mappings.

## Settings Config-KV Mapping

`larena/setting` has a package-local `larena.settings.config-kv` transport through `SettingConfigKvTransport`.

When designing the Larena SitePack adapter for settings:

- wrap the settings config-KV payload as the SitePack config key-value artifact instead of inventing a second settings format;
- keep import review-first: SitePack settings import should create `sf_setting_pending_changes`, support dry-run/report, and never write runtime settings directly;
- preserve namespace/key/context metadata so Bitrix/SF5 and Larena adapters can converge on the same conceptual settings model;
- treat secrets and environment-only values as skipped or review-required entries, not as automatic imports.

## Docara Import/Export Baseline

`simai/larena` has a committed draft contract for the first Docara SitePack product scenario:

- `docs/developer/rfc/0003-docara-sitepack-import-export.md`
- `docs/developer/docara-sitepack-acceptance.md`
- `docs/developer/examples/sitepack/docara-docs-site/`

Use this baseline when designing or reviewing SitePack adapters,
`larena/docara` import/export capabilities, or SitePack product packs for
documentation. `larena/sitepack` is not a current 2026-07 package-portfolio
member, so do not create it without an approved package proposal.

Working rules:

- minimum Docara profiles are `site-structure` and `content-assets`;
- `config-only` is review-first and must never auto-apply secrets;
- `product-package` may describe paid/free documentation products, but must not auto-install executable code;
- map SitePack `site-map.pages[]` into Docara route/tree/menu fields and store source ids under `meta.sitepack`;
- map `document.page` entities into filesystem-backed markdown and `docara_page_revisions`;
- import uses two passes for page creation and parent/asset relation resolution;
- admin UI should dispatch queued/CLI-backed jobs rather than run import/export as a long web request;
- unsupported extensions, unknown entity types and missing optional assets are warnings, not crashes.

The example package should validate with the SitePack PHP validator before implementation is considered ready:

```bash
cd /Users/rim/Documents/GitHub/sitepack/sitepack-tools-php
/Applications/ServBay/bin/php bin/sitepack-validate package /Users/rim/Documents/GitHub/larena/docs/developer/examples/sitepack/docara-docs-site --profile site-structure --no-digest --check-asset-blobs
/Applications/ServBay/bin/php bin/sitepack-validate package /Users/rim/Documents/GitHub/larena/docs/developer/examples/sitepack/docara-docs-site --profile content-assets --no-digest --check-asset-blobs
```
