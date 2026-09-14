# SIMAI Framework Integration

Owns SIMAI Framework UI/runtime compatibility, smart components, page/layout concepts, loader assumptions and frontend alignment.

## Load When

- task touches SIMAI Framework UI, smart components, page builder, layout blocks, loader/runtime assets or Bitrix/SIMAI Framework parity;
- deciding whether Larena runs SIMAI Framework standalone or server-integrated.

## Required Knowledge

- [knowledge-packs/product-architecture.md](../../knowledge-packs/product-architecture.md)
- [knowledge-packs/settings-storage-props-layout.md](../../knowledge-packs/settings-storage-props-layout.md)

## Gatekeeper Rules

- Preserve SIMAI Framework contracts where Larena needs compatibility with Bitrix-side projects.
- Keep layout/page builder concepts aligned with `Atomic Block -> Section -> Page` unless deliberately changed.
- Preserve the SIMAI Framework `Block -> Smart` boundary for Larena compatibility: blocks own data binding, settings, placement, and editor/runtime relationships; Smart owns UI templates, views, SIMAI Framework components/smart-components, and frontend rendering. Larena adapters may differ, but the contract should remain portable.
- Use the external `framework` skill for detailed SIMAI Framework frontend implementation.
