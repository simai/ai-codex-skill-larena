# SIMAI Framework Integration

Owns how Larena consumes SIMAI Framework (formerly "SF5"): `larena/ui`, the
component package `larena` (admin Smart components), Smart manifests, asset
activation, page/layout concepts and frontend alignment. The Framework itself,
its components and their release belong to `$framework`.

## Load When

- task touches `larena/ui`, Smart registry/manifests, admin components
  (`sf-table`, `sf-data-view`, `sf-property-view`, `sf-admin-menu`), the
  pinned admin kit, page builder, layout blocks, loader/runtime assets or
  Bitrix/SIMAI Framework parity;
- deciding whether Larena runs the Framework standalone or server-integrated.

## Required Knowledge

- [knowledge/larena-ui-components.md](../../knowledge/larena-ui-components.md)
- [knowledge/product-architecture.md](../../knowledge/product-architecture.md)
- [knowledge/settings-storage-props-layout.md](../../knowledge/settings-storage-props-layout.md)

## Gatekeeper Rules

- Larena pins an exact Framework pair (Framework build + `larena` component
  kit); install, update and sealing refuse a runtime whose lock does not pin
  every component set the installed packages declare. Never hand-edit a kit
  inside Root — change it at its source and re-pin.
- Preserve Framework contracts where Larena needs compatibility with
  Bitrix-side projects.
- Keep layout/page builder concepts aligned with `Atomic Block -> Section -> Page` unless deliberately changed.
- Preserve the `Block -> Smart` boundary: blocks own data binding, settings,
  placement, and editor/runtime relationships; Smart owns UI templates, views,
  Framework components/smart components and frontend rendering. Larena
  adapters may differ, but the contract should remain portable.
- Component behaviour and visual fixes go to `$framework` (and `$designer` for
  visual QA); Larena owns the host side: ports, data, rights, messages.
