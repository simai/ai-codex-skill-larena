# Changelog

## Unreleased

### Added

- Restructured the skill into the standard Codex skill repository layout under `skills/larena/`.
- Added Larena engineering-council architecture with kernel rules, activities, specialists, quality templates and knowledge packs.
- Added product DNA, platform scope and non-negotiables for Larena as a SIMAI/Laravel/SF5 CMS platform.
- Added knowledge packs for product architecture, package map, `module.yaml` standard, update/registration, Docara proof, REST safety, SitePack bridge, settings/storage/props/layout, admin platform, ordinary-hosting scheduler and AI-agent service architecture.
- Added session-safe background enrichment knowledge for link preview, external fetch, AI-agent context gathering, endpoint session modes, queue bulkheads, circuit breakers and diagnostics.
- Added package install readiness guidance for `larena:doctor` and provider bootstrap safety during Composer/Laravel package discovery.
- Clarified repository roles: `simai/larena` is the free starter bootstrap/distribution entry, `larena-*` repositories are package/code source of truth, and monorepo/workspace is development-only.
- Added package-installer guidance for `composer.json`, `module.yaml`, install/update contracts and the `simai/larena` package validator.
- Added routing and decision-policy rules for package diagnostics, entry install readiness, update/registration, SitePack, Docara, REST/API, docs, runtime and release-readiness work.

### Changed

- Moved old root-level knowledge, modules, checklists, examples and templates into `skills/larena/` so the repository root can stay reserved for service metadata, `source/`, docs and CI.
- Updated `$larena` to treat `docs/developer/module-yaml-schema.md` and `docs/developer/schemas/module.schema.json` in `simai/larena` as the first `module.yaml` schema baseline.
- Updated `$larena` to use committed Larena governance anchors in `simai/larena`: product DNA, package contract, release gates and ADR 0001.

### Verification

- `skills/larena/SKILL.md` frontmatter contains `name: larena`.
- Activity JSON manifests validate.
- `~/.codex/skills/larena` points to `/Users/rim/Documents/GitHub/ai-codex-skill-larena/skills/larena`.
