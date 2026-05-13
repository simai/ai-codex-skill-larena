# Data Settings Props

Owns settings, storage, universal properties, page/layout data and cross-platform data semantics.

## Load When

- task touches `larena/setting`, `larena/property`, storage, filesystem metadata, page constructor data, import/export formats or Bitrix/SF5 data model alignment.

## Required Knowledge

- [knowledge-packs/settings-storage-props-layout.md](../../knowledge-packs/settings-storage-props-layout.md)
- [knowledge/modules/access.md](../../knowledge/modules/access.md)

## Gatekeeper Rules

- Separate UI/input/render contracts from persistence.
- Prefer scoped settings with schema/value/history/pending path where product needs it.
- Preserve stable codes/identifiers for export/import and update packages.
- Consider element-level ACL, encryption and logging for storage-like entities.
