# Data Settings Props

Owns settings, storage, universal properties, search/indexing, page/layout data and cross-platform data semantics.

## Load When

- task touches `larena/setting`, `larena/property`, storage, filesystem metadata, search/indexing, page constructor data, import/export formats or Bitrix/SIMAI Framework data model alignment.

## Required Knowledge

- [knowledge/settings-storage-props-layout.md](../../knowledge/settings-storage-props-layout.md)
- [knowledge/settings-catalog-and-storage-admin.md](../../knowledge/settings-catalog-and-storage-admin.md)
- [knowledge/search-platform.md](../../knowledge/search-platform.md)
- [knowledge/packages/access.md](../../knowledge/packages/access.md)

## Gatekeeper Rules

- Separate UI/input/render contracts from persistence.
- Prefer scoped settings with schema/value/history/pending path where product needs it.
- Preserve stable codes/identifiers for export/import and update packages.
- Consider element-level ACL, encryption and logging for storage-like entities.
- Treat search as access-aware, locale-aware and bounded; do not let search become client-side filtering over broad datasets.
