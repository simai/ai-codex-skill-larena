# Changelog

## Unreleased

- Added package-installer guidance to run `migrate --force` and idempotent `simai:install` after updating installed `larena/*` packages before browser smoke, so runtime access/menu metadata stays synced with package config.
- Added package-completion audit guidance that rollback notes must match `module.yaml` `owned_data`, migrations, persistent storage and config files; stale rollback claims block `L4`.
- Added admin-platform guidance for synchronized Admin/Layout DNA: `larena/admin` owns object-based admin UI composition, while future `larena/layout` owns public page composition.
- Added package-completion guidance for the code quality, legacy and logging standard: classify fallback/legacy, gate development logs, use package channels where needed and flag duplicated semantic logic.
- Updated `larena/access` package knowledge with the 2026-05-13 deep audit result, L4 verdict, legacy cleanup and remaining non-blocking rollout/downstream conditions.
- Added legacy-registry guidance to package-completion knowledge: active compatibility, dangerous legacy and historical legacy must be tracked in `docs/developer/legacy/registry.json`.
- Added `larena/setting` cleanup guidance: helper/UI reads should use `SettingValueLookup`, audit/pending actor-source metadata should use `SettingActorResolver`, and pending payloads should use `SettingPendingSerializer`.
- Added package deep-audit guidance: requests to check a package against the standard must run the batch methodology, not only bulk validators.

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
- Added current `larena/access` DNA compliance guidance: status is `L4 partial`; decision-layer, grants/context, security/operations and demonstrator baselines are implemented, installed-site HTTP smoke passed on `larena.test`, and visual browser evidence remains the next package-completion step.
- Added `larena/access` runtime doctor guidance: `php artisan access:doctor` is the package-local read-only diagnostics gate for config, tables, middleware, routes, contracts and bypass-token safety.
- Added `larena/access` visual smoke guidance and noted the remaining legacy update/upserv asset URL cleanup found during local browser verification.
- Added `larena/access` token-scope storage guidance: API keys now have additive `sf_access_api_key.scopes`, `AccessTokenScopePolicy`, and config-gated enforcement via `ACCESS_TOKEN_SCOPE_ENFORCEMENT`.
- Added `larena/access` audit dispatcher guidance: token middleware decisions emit sanitized `AccessAuditRecorded` events and durable storage can be enabled through the configurable audit sink.
- Added `larena/access` token rate-limit guidance: `AccessRateLimitPolicy` wires `access.token` to Laravel `RateLimiter` through config-gated named profiles and sanitized `access.token.rate_limited` audit events.
- Added `larena/access` durable audit sink and API-key scope assignment guidance: `sf_access_audit_log`, `ACCESS_AUDIT_SINK`, sanitized database payloads, CRUD `scopes` metadata and masked-key plus `hashed_key` storage.
- Added `larena/access` scoped grant storage guidance: RFC 0001, `sf_access_grant`, `AccessScopedGrantStore`, rollout flag `ACCESS_SCOPED_GRANTS_ENABLED`, legacy fallback, scoped deny precedence and `access:doctor` 46-check baseline.
- Added `larena/access` cache and SitePack grant mapping guidance: `AccessCache` versioned invalidation hooks, `AccessSitePackMapper` config-KV namespace `larena.access.grants`, dry-run/manual/private import policy and `access:doctor` 48-check baseline.
- Expanded `larena/access` integration-hardening guidance: SitePack config-KV now covers operations, profiles and scoped grants; sessionless API-token and custom virtual-target resolver smoke tests are part of the package baseline.
- Updated `larena/access` status to L4-ready baseline with `AccessVirtualTargetCatalog`, `access:resolver-catalog`, `/admin/access-explain`, rollout smoke evidence and 57-check `access:doctor` guidance.
- Added package standards guidance for central Package Graph entries and package demonstrator compliance as L4 readiness requirements.
- Updated package graph guidance with the first central baseline entries for `larena/access`, `larena/admin`, `larena/auth`, `larena/rest`, `larena/setting`, `larena/props`, `larena/docara-core` and `larena/docara-admin`.
- Updated package graph guidance with the remaining baseline entries for `larena/update`, `larena/update-registration`, `larena/filesystem`, `larena/lang` and `larena/two-fa`, plus the generated impact-matrix and graph-validation commands.
- Updated package graph guidance with `larena/mcp`, `larena/rest_doc`, planned `larena/storage` and the package-local status card expectation.
- Updated package graph guidance with strict graph-to-`module.yaml` validation and the central package-local gaps report.
- Added package-completion guidance that `larena/admin`, `larena/auth`, `larena/rest` and `larena/rest_doc` now have installed-site demonstrator evidence and are L4 package-readiness references with tracked L4+ notes.
- Added `larena/access` admin UX guidance: scoped grant CRUD at `/admin/access-grants`, read-only operator audit review at `/admin/access-audit-log`, guarded CRUD configs and `access:doctor` 52-check baseline.
- Added `larena/access` rollout policy guidance: `AccessPackPolicy`, `AccessRolloutPolicy`, `access:rollout-policy`, installed-route `access:api-smoke`, 54-check doctor baseline and sessionless API evidence on `larena.test`.
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
- Added AI demonstrator testing guidance: package checks must build a test matrix against DNA, `module.yaml`, package graph, security/session rules and runtime evidence; missing package DNA is marked `not_ready` instead of guessed.
- Tightened L4 readiness guidance: installed-site smoke is preparation evidence only, while full L4 requires package DNA or an accepted exception, explicit DNA/package-standard audit, architecture/contract docs, demonstrator coverage and AI demonstrator testing evidence.
- Added package naming standard guidance: official Larena technical package identifiers use singular module/domain keys by default, while public/UI titles may use natural English plural forms.
- Added AI/MCP exposure guidance: packages publish MCP tools/resources for the central gateway and execution must be scoped to the effective user, service account or capability token.
- Added local Larena vhost guidance: ServBay/Caddy/nginx/Apache document roots must point to Laravel `public/`, and ServBay UI changes can overwrite generated Caddyfile fixes.
- Added routing and decision-policy rules for package diagnostics, entry install readiness, update/registration, SitePack, Docara, REST/API, docs, runtime and release-readiness work.
- Added explicit package-standard audit routing: requests like "проверь пакет на стандарт" now trigger full package-completion audit with L0-L5 verdict, artifact matrix, DNA/contract gaps, verification evidence and nearest next batch.
- Clarified package-standardization target: L4 is the current goal for official Larena packages, while L5 is deferred until the Laravel update-server/distribution standard exists.

### Changed

- Updated Larena standards path guidance: canonical package standards now live under `docs/developer/standards/`; old direct developer-doc paths are compatibility stubs only.
- Moved old root-level knowledge, modules, checklists, examples and templates into `skills/larena/` so the repository root can stay reserved for service metadata, `source/`, docs and CI.
- Updated `$larena` to treat `docs/developer/standards/module-yaml-schema.md` and `docs/developer/schemas/module.schema.json` in `simai/larena` as the first `module.yaml` schema baseline.
- Updated `$larena` to use committed Larena governance anchors in `simai/larena`: product DNA, package contract, release gates and ADR 0001.
- Updated Larena positioning so backend/package DNA uses Larena as the canonical identity; `SF5` remains only a historical/frontend reference or migration compatibility term.

### Verification

- `skills/larena/SKILL.md` frontmatter contains `name: larena`.
- Activity JSON manifests validate.
- `~/.codex/skills/larena` points to `/Users/rim/Documents/GitHub/ai-codex-skill-larena/skills/larena`.
