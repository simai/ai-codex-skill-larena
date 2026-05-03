# Package Installer

Owns Composer packages, service providers, commands, migrations, install/update contracts, package metadata and bootstrap flow.

## Load When

- task touches `composer.json`, package graph, install commands, migrations or service providers;
- checking whether `simai/larena` can install without update server;
- adding or diagnosing a `larena/*` package;
- planning package update/install scripts.

## Required Knowledge

- [knowledge-packs/package-map.md](../../knowledge-packs/package-map.md)
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
- For entry app readiness, verify both CLI install and web serving. A Laravel/Larena site is not ready until the web server document root points to `public/`, routes respond over HTTP(S), and Composer can actually fetch `larena/*` packages through the documented distribution path.
- Use `php artisan larena:validate-packages` or `composer run validate:packages` in `simai/larena` as the first package governance check. It is warning-mode by default and should be treated as a drift detector until existing packages are aligned with the manifest contract.
- Treat `docs/developer/module-yaml-schema.md` and `docs/developer/schemas/module.schema.json` in `simai/larena` as the current first baseline for `module.yaml`. Keep existing `depends_on`, `provides`, `installs`, and `observability` vocabulary while adding governance fields such as `edition`, `product_layer`, `distribution`, `docs`, `health_checks`, `support`, `update`, and `rollback`.
- If behavior changes, update package docs/SPEC/CHANGELOG when present.
