# Larena DNA

Larena is the Laravel CMS and application platform of the SIMAI ecosystem. It is not just a Laravel application and not just a package collection.

Strategic ambition: Larena is intended to become a world-class CMS/platform that can compete with and surpass existing CMS ecosystems by accessibility, usability, security, update experience, extensibility and ecosystem growth.

Founder/attribution context: Larena is part of the SIMAI ecosystem created through SIMAI by Rim Zabarov / Забаров Рим. Public product artifacts should be English-first and preserve authorship professionally where suitable through copyright, license, README, package metadata, documentation or product story.

AI-agent context: Larena is being created for a world where AI agents help assemble, configure, diagnose and extend systems. Packages, modules and services should be documented, protocolled and discoverable enough to work as agent-readable building blocks.

Default priorities:

0. Move from general to specific: first understand Larena's product role, strategic direction, platform boundaries and user/developer scenarios; then evaluate architecture; only after that decide package-level or code-level actions.
0.1. Before adding new package functionality, run a concept-alignment audit: verify that the package matches the Larena canonical model for its domain, and record what is native Larena versus migration/compatibility reference.
1. Preserve the user-facing bootstrap path through `simai/larena` until the Larena update-server flow is ready.
2. Keep Larena compatible with useful Bitrix and older SIMAI concepts where that helps future migration, but keep Larena names and contracts canonical: settings, storage, props, layout, SitePack, update delivery.
3. Treat `larena/*` packages as modular platform units with explicit install, metadata, access, docs and tests.
4. Keep modular admin extensible through typed extension points, slots, contributions and manifests.
5. Keep SitePack as portable transport; implement Bitrix and Larena adapters instead of mixing standard and platform runtime.
6. Keep update server and registration server responsibilities separate.
7. Treat Docara as the likely first product proof and acceptance scenario.
8. Prefer practical diagnostics against real code over speculative architecture.
9. Keep SIMAI Environment as the preferred controlled runtime path, but do not lock Larena to it; ordinary hosting/VPS support is part of the adoption goal.
10. Treat modularity as both in-process and service-oriented: a capability may live inside one Larena product or as a separate service connected through safe internal/external APIs.
11. Require agent-ready documentation and metadata for important packages/services so AI-assisted work can discover capabilities, APIs, dependencies, install/update paths and safety boundaries.

When speed conflicts with install/update safety, choose a smaller scoped result with explicit risks.

When a task asks for a private technical decision but the strategic context is unclear, briefly restate the product-level assumption before choosing the technical path.

Larena DNA is not only a description. Treat it as a governance layer:

- human-readable product constitution;
- package/service manifest contracts;
- review and release gates;
- CI/package validators;
- ADR/decision log;
- AI skill knowledge;
- developer onboarding.

Future work should protect platform coherence across repositories and developers. A local package decision is not acceptable if it damages the shared product model, install/update trust, modular admin, SitePack portability, safe APIs, free/paid boundary, Docara product proof, or AI-agent readability.

Repository standardization has two gates before functional expansion:

1. Repository and documentation baseline: README, CHANGELOG, `module.yaml`, user/developer docs, install/update/rollback notes and smoke/test path.
2. Concept alignment audit: `docs/developer/concept-alignment.md` or an explicit tracked exception that compares the package with the Larena canonical concept and any migration references before new behavior is built on top.

Committed governance anchors in the `simai/larena` repository:

- `docs/product/larena-dna.md`
- `docs/developer/standards/package-contract.md`
- `docs/developer/standards/release-gates.md`
- `docs/developer/adr/0001-product-dna.md`
