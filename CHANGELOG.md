# Changelog

## Unreleased

### Added

- Added UX implementation contract guidance for Larena modular admin,
  settings/storage/props/layout UI, install/update UI, registration/licensing,
  and Docara product interfaces.
- Restructured the skill into the standard Codex skill repository layout under `skills/larena/`.
- Added Larena engineering-council architecture with kernel rules, activities, specialists, quality templates and knowledge packs.
- Added product DNA, platform scope and non-negotiables for Larena as a SIMAI/Laravel/SF5 CMS platform.
- Added knowledge packs for product architecture, package map, `module.yaml` standard, update/registration, Docara proof, REST safety, SitePack bridge, settings/storage/props/layout, admin platform, ordinary-hosting scheduler and AI-agent service architecture.
- Added session-safe background enrichment knowledge for link preview, external fetch, AI-agent context gathering, endpoint session modes, queue bulkheads, circuit breakers and diagnostics.
- Added package install readiness guidance for `larena:doctor` and provider bootstrap safety during Composer/Laravel package discovery.
- Added Docara acceptance gate guidance for `larena:doctor --docara`, `docara:sync --dry-run`, route checks and the next browser/admin product gate.
- Added Docara browser/admin gate guidance for real installed-stand checks: login, page tree, create/edit/save, public render, revisions, rollback, denial and cleanup.
- Added Docara SitePack import/export baseline guidance with links to RFC 0003, acceptance gate and validator-friendly example package.
- Added update-server canonical alias migration guidance: use `larena/update`, `simai:update:*` and `simai_update` for new contracts while preserving `Simai\Upserv`, `simai_upserv` and legacy commands as compatibility surfaces.
- Added update-server documentation migration guidance: user-facing docs must lead with canonical `larena/update` and `simai:update:*`, while legacy `upserv` names remain compatibility or historical evidence only.
- Added update artifact trust guidance: stored distribution archives require `archive_size_bytes` / `archive_sha256` baseline before publication, and signed manifests should use public-key verification with client-side size/SHA-256 checks.
- Added the current signed manifest implementation baseline for `larena/update` and the Bitrix update-client verifier seed.
- Added signed manifest rollout guidance: Ed25519 keygen/rotation, private-key storage, Bitrix `SIGNED_MANIFEST_MODE=off|diagnostic|enforce`, and staged `public-core` rollout before enforcement.
- Added concept-alignment governance guidance: Larena package repositories must pass repository/docs baseline and shared SIMAI/SF5/Larena concept audit before new package functionality is added.
- Clarified repository roles: `simai/larena` is the free starter bootstrap/distribution entry, `larena-*` repositories are package/code source of truth, and monorepo/workspace is development-only.
- Added package-installer guidance to check Composer tags and bootstrap `composer.lock` when a package source fix is present but the entry repository still installs old behavior.
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
