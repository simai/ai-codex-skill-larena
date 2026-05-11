# Changelog

## Unreleased

### Added

- Added `$docs` coordination rules so `$larena` keeps ownership of Larena
  facts, package contracts, runtime constraints, and Docara product specifics
  while `$docs` owns substantial documentation method, writing, screenshots,
  and content-quality gates.
- Added SEO Contract implementation guidance so `$larena` treats `$seo` as the owner of public-route SEO decisions while Larena implements them through routes, meta storage, Blade/UI, sitemap/robots middleware, packages, and Docara bridge surfaces.
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
- Added concept-alignment governance guidance: Larena package repositories must pass repository/docs baseline and Larena canonical concept audit, with Bitrix/older-SIMAI migration references where useful, before new package functionality is added.
- Added platform subsystem contract guidance for P0 packages: `module.yaml` should declare capabilities, owned data, endpoint session modes, permissions, audit, rollback, health checks and operational risks alongside `docs/developer/concept-alignment.md`.
- Added current `larena/access` DNA compliance guidance: status is `L4 partial`; decision-layer and grants/context baseline are implemented, and the next safe layer is token scopes, audit, rate limits and root/bypass policy before broad API/AI exposure.
- Clarified repository roles: `simai/larena` is the free starter bootstrap/distribution entry, `larena-*` repositories are package/code source of truth, and monorepo/workspace is development-only.
- Added package-installer guidance to check Composer tags and bootstrap `composer.lock` when a package source fix is present but the entry repository still installs old behavior.
- Added package-installer guidance for `composer.json`, `module.yaml`, install/update contracts and the `simai/larena` package validator.
- Added package-installer guidance that official packages must resolve resources through package-relative paths instead of assuming `base_path("vendor/larena/<package>")`.
- Added settings/storage/props guidance to evolve legacy `category + code` settings through a tested compatibility resolver/explain layer before destructive schema migrations.
- Added settings/storage/props guidance for additive canonical settings persistence: nullable `namespace/key`, `level/scope_id`, legacy backfill, canonical resolver preference and legacy fallback.
- Added settings/storage/props guidance for explicit pending overlay preview: normal resolver reads remain committed-only, while `resolveWithPending()` / `explainWithPending()` expose review proposals for admin, AI and diagnostics.
- Added settings/storage/props guidance for schema-pack policy v2: dry-run/publish reports dependencies, conflicts, namespace-prefix issues and version downgrade warnings, while publication blocks policy errors.
- Added settings/storage/props guidance for pending review UI baseline: filters, side-by-side current/proposed comparison and stateful bulk apply/reject for pending rows.
- Added package completion standard guidance so `$larena` audits packages by readiness levels `L0`-`L5` and reports missing artifacts, blockers, nearest useful batch and next-level verification.
- Extended package completion guidance with AI development contract and package status card checks for safer AI-assisted package work.
- Added package naming standard guidance: official Larena technical package identifiers use singular module/domain keys by default, while public/UI titles may use natural English plural forms.
- Added AI/MCP exposure guidance: packages publish MCP tools/resources for the central gateway and execution must be scoped to the effective user, service account or capability token.
- Added local Larena vhost guidance: ServBay/Caddy/nginx/Apache document roots must point to Laravel `public/`, and ServBay UI changes can overwrite generated Caddyfile fixes.
- Added routing and decision-policy rules for package diagnostics, entry install readiness, update/registration, SitePack, Docara, REST/API, docs, runtime and release-readiness work.

### Changed

- Moved old root-level knowledge, modules, checklists, examples and templates into `skills/larena/` so the repository root can stay reserved for service metadata, `source/`, docs and CI.
- Updated `$larena` to treat `docs/developer/module-yaml-schema.md` and `docs/developer/schemas/module.schema.json` in `simai/larena` as the first `module.yaml` schema baseline.
- Updated `$larena` to use committed Larena governance anchors in `simai/larena`: product DNA, package contract, release gates and ADR 0001.
- Updated Larena positioning so backend/package DNA uses Larena as the canonical identity; `SF5` remains only a historical/frontend reference or migration compatibility term.

### Verification

- `skills/larena/SKILL.md` frontmatter contains `name: larena`.
- Activity JSON manifests validate.
- `~/.codex/skills/larena` points to `/Users/rim/Documents/GitHub/ai-codex-skill-larena/skills/larena`.
