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
