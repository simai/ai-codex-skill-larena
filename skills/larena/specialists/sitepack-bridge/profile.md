# SitePack Bridge

Owns SitePack usage as shared transport for Bitrix <-> Larena data, product packaging, backup/restore and migration.

## Load When

- `.sitepack` packages, export/import, content migration, backup/restore, product data packaging, blobs or adapters are involved;
- mapping Larena settings/storage/props/layout/Docara data to portable transport;
- comparing Bitrix adapter needs with Larena adapter needs.

## Required Knowledge

- [knowledge-packs/sitepack-bridge.md](../../knowledge-packs/sitepack-bridge.md)
- [knowledge-packs/settings-storage-props-layout.md](../../knowledge-packs/settings-storage-props-layout.md)

## Gatekeeper Rules

- SitePack is portable standard; Larena-specific behavior belongs in adapter/package.
- Importers should use manifest+catalog as source of truth.
- Follow recorded artifact paths; do not assume fixed blob layout.
- Prefer SHA-256 blob conventions and two-pass relation resolution.
- Unknown artifacts or entity types should become warnings where the spec allows, not fatal crashes by default.
