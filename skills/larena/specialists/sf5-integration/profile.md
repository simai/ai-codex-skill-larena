# SF5 Integration

Owns SF5 UI/runtime compatibility, smart components, page/layout concepts, loader assumptions and frontend alignment.

## Load When

- task touches SF5 UI, smart components, page builder, layout blocks, loader/runtime assets or Bitrix/SF5 parity;
- deciding whether Larena runs SF5 standalone or server-integrated.

## Required Knowledge

- [knowledge-packs/product-architecture.md](../../knowledge-packs/product-architecture.md)
- [knowledge-packs/settings-storage-props-layout.md](../../knowledge-packs/settings-storage-props-layout.md)

## Gatekeeper Rules

- Preserve SF5 contracts where Larena needs compatibility with Bitrix-side projects.
- Keep layout/page builder concepts aligned with `Atomic Block -> Section -> Page` unless deliberately changed.
- Use the external `sf5` skill for detailed SF5 frontend implementation.
