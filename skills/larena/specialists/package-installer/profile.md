# Package Installer

Owns Composer packages, service providers, commands, migrations, install/update contracts, package metadata and bootstrap flow.

## Load When

- task touches `composer.json`, package graph, install commands, migrations or service providers;
- checking whether `simai/larena` can install without update server;
- adding or diagnosing a `larena/*` package;
- planning package update/install scripts.

## Required Knowledge

- [knowledge-packs/package-map.md](../../knowledge-packs/package-map.md)
- [knowledge-packs/package-completion-standard.md](../../knowledge-packs/package-completion-standard.md)
- [knowledge-packs/module-yaml-standard.md](../../knowledge-packs/module-yaml-standard.md)
- [knowledge/simai-package-rules.md](../../knowledge/simai-package-rules.md)
- [knowledge/quickstart.md](../../knowledge/quickstart.md)

## Gatekeeper Rules

- Package install commands must be idempotent and non-interactive.
- Prefer minimum install UX for developers now and ordinary users later.
- Do not duplicate global install steps inside package-specific install commands.
- Keep package docs and Composer names consistent with current `larena/*` namespace.
- Treat Composer `require` as the canonical install dependency graph. If `module.yaml.depends_on` names a required Larena package, the matching Composer package must also be present in `require`, unless the integration is explicitly documented as optional and code safely degrades without it.
- When auditing packages, compare Composer package name, `module.yaml.package`, provider registration, declared install commands, route/config/migration assets, and README install names before claiming a package is ready.
- When asked whether a package is complete, evaluate it against the package completion levels: `L0 Code Exists`, `L1 Repository Ready`, `L2 Contract Ready`, `L3 DNA Aligned`, `L4 Demonstration Ready`, `L5 Release / Marketplace Ready`. Return missing artifacts and the nearest useful batch, not only code findings.
- For entry app readiness, verify both CLI install and web serving. A Laravel/Larena site is not ready until the web server document root points to `public/`, routes respond over HTTP(S), and Composer can actually fetch `larena/*` packages through the documented distribution path.
- When a package source repository already contains a fix but the bootstrap repo still shows the old behavior, inspect Composer tags and `composer.lock`. The entry repo may need a stable package tag plus a targeted `composer update <package>`, not another source patch.
- Use `php artisan larena:validate-packages` or `composer run validate:packages` in `simai/larena` as the first package governance check. It is warning-mode by default and should be treated as a drift detector until existing packages are aligned with the manifest contract.
- For P0 package reviews and release candidates, run `php artisan larena:validate-packages --contract --strict --path=/path/to/package`. Contract mode checks capabilities, owned data, endpoint `session_mode`, declared rate limits, docs, concept alignment, audit, rollback, health checks, external-network policy and operational risks. Target explicit package paths until installed `vendor/larena/*` releases all contain expanded manifests.
- Use `php artisan larena:doctor` or `composer run doctor` in `simai/larena` as the first entry-runtime readiness check after Composer dependencies and `.env` exist.
- Treat `docs/developer/standards/module-yaml-schema.md` and `docs/developer/schemas/module.schema.json` in `simai/larena` as the current first baseline for `module.yaml`. Keep existing `depends_on`, `provides`, `installs`, and `observability` vocabulary while adding governance fields such as `edition`, `product_layer`, `distribution`, `docs`, `health_checks`, `support`, `update`, and `rollback`.
- Service providers must be safe during Composer/Laravel package discovery: provider `register()` and `boot()` must not require migrated tables, a live DB or external services. DB-aware lifecycle state should fail open before migrations and defer writes to explicit commands/runtime paths.
- Package runtime code must not assume it is installed at `base_path("vendor/larena/<package>")`. Official packages can run from Composer vendor, path repositories, monorepos, local development checkouts and update-server extracted layouts. Resolve package resources from package-relative paths such as `__DIR__`/provider base path or a package `PackagePaths` helper, and add regression tests for path-sensitive package resources.
- If behavior changes, update package docs/SPEC/CHANGELOG when present.
