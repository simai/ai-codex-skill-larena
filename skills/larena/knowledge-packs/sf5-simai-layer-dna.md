# SF5 SIMAI Layer DNA For Larena

Use this knowledge pack when a task compares Bitrix SF5 `/simai` or
`/simai.data` with Larena, or when Larena needs to implement blocks, sections,
smart artifacts, design packs, overlays, or SitePack portability.

## Rule

Preserve the SF5 layer DNA, not the Bitrix filesystem literally:

```text
/simai      = system library layer
/simai.data = project/site/path overlay layer
```

## Larena Mapping

Recommended Larena mapping:

```text
Bitrix /simai
  -> vendor/simai/*/resources/simai
  -> public/simai/asset only for published assets

Bitrix /simai.data
  -> resources/simai-data
  -> storage/app/simai-data
  -> optional overlay database registry

Bitrix /company/simai.data
  -> route/path-scoped overlay for /company/
```

## Separation

Do not let overlay storage become settings storage.

- Overlay layer owns available and overridden reusable artifacts:
  blocks, sections, smart artifacts, design packs and package assets.
- Storage owns content, site tree, pseudo-static pages, dynamic pages and
  page section calls.
- Settings own values, preferences and contextual overrides.
- Property owns field definitions, editors, validation and control rendering.

## Resolver Expectations

Larena should provide a resolver equivalent in meaning to the Bitrix path
resolver:

```text
system package layer
+ project overlay
+ site overlay
+ path overlays
+ user/context settings where applicable
```

More local overlays override more general overlays. The resolved chain must be
included in compiled runtime cache keys and SitePack import/export mapping.

## Canonical Docs

- `larena/docs/developer/dna/simai-layer-dna.md`
- `bx-simai.main/docs/developer/specifications/larena-simai-layer-dna.md`

