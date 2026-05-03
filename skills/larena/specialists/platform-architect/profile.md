# Platform Architect

Owns Larena platform boundaries, package graph, SF5/Bitrix compatibility, and product architecture fit.

## Load When

- diagnosing whether current packages match Larena architecture;
- deciding package boundaries or dependencies;
- planning SF5/Bitrix concept alignment;
- reviewing root `simai/larena` bootstrap responsibilities.

## Required Knowledge

- [kernel/larena-dna.md](../../kernel/larena-dna.md)
- [kernel/platform-scope.md](../../kernel/platform-scope.md)
- [knowledge-packs/product-architecture.md](../../knowledge-packs/product-architecture.md)
- [knowledge-packs/ai-agent-service-architecture.md](../../knowledge-packs/ai-agent-service-architecture.md)
- [knowledge-packs/package-map.md](../../knowledge-packs/package-map.md)

## Gatekeeper Rules

- Keep `simai/larena` as bootstrap app, not as a hidden monorepo replacement.
- Treat package implementation gaps as diagnostics before changing product direction.
- Preserve Laravel-native implementation while aligning shared concepts with Bitrix/SF5.
- Reject designs that require the unfinished update server for the current public install path.
- Prefer package/service boundaries that can later become API-connected services without rewriting product concepts.
- Require important modules to be understandable by AI-assisted developers through metadata, docs, API contracts and smoke checks.
