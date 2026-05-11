# Module YAML Standard

Use this pack when work touches `module.yaml`, Composer package metadata, package release readiness, update-server package discovery, package docs, package validators, or AI-agent-readable package manifests.

For full package completion, combine this pack with [package-completion-standard.md](./package-completion-standard.md). `module.yaml` is the machine-readable manifest layer, but a package is not complete until repository shape, DNA, architecture, documentation, demonstrator, tests, security, install/update/rollback and roadmap artifacts are also accounted for.

## Canonical Source

The current first committed schema baseline lives in `simai/larena`:

- `docs/developer/module-yaml-schema.md`
- `docs/developer/schemas/module.schema.json`
- `docs/developer/examples/module-yaml/`

The current validator command in `simai/larena`:

```bash
php artisan larena:validate-packages
composer run validate:packages
```

Default validator mode is warning-only. Use `--strict` only when warnings should fail CI/release gates.

For P0 platform package reviews and release candidates, use contract mode with explicit package paths:

```bash
php artisan larena:validate-packages --contract --strict --path=/path/to/larena-setting
```

Contract mode checks capabilities, owned data, endpoint session modes, declared rate limits, documentation paths, concept alignment, audit events, rollback notes, health checks, external-network policy and operational risks. Until every installed `vendor/larena/*` release contains expanded manifests, do not treat a full default `--contract --strict` scan of the starter app as the baseline gate; target the package repositories being reviewed or released.

As of the first full local alignment pass, the 14 local Larena repositories can be checked together by passing explicit paths for `larena-setting`, `larena-filesystem`, `larena-access`, `larena-auth`, `larena-2fa`, `larena-rest`, `larena-rest-doc`, `larena-props`, `larena-admin`, `larena-lang`, `larena-docara-core`, `larena-docara-admin`, `larena-update`, and `larena-update-registration`.

## Purpose

`module.yaml` is the canonical Larena package/service manifest. It must make a package understandable by:

- developers;
- installer/update tooling;
- admin/runtime;
- release checks;
- marketplace tooling;
- AI agents.

Do not treat `module.yaml` as a loose README summary. It is a machine-readable contract.

## Compatibility Rule

Keep the useful current vocabulary:

- `depends_on`
- `integrations`
- `provides`
- `installs`
- `observability`

Add governance/discovery fields gradually:

- `capabilities`
- `owned_data`
- `edition`
- `product_layer`
- `license`
- `distribution`
- `admin`
- `api_operations`
- `permissions`
- `events`
- `jobs`
- `settings`
- `docs`
- `health_checks`
- `audit`
- `support`
- `update`
- `rollback`

For P0 platform subsystems, `capabilities` and `owned_data` should be treated as first-class contract fields even while the machine schema remains permissive.

`capabilities` should explain what the package contributes as reusable platform building blocks, not only which Laravel files it installs.

`owned_data` should declare the tables, config files, storage areas, value identities and scope models owned by the package. This prevents future packages from silently inventing parallel settings, access, props, storage or API models.

## Required Identity Fields

Every official package should declare:

```yaml
name: admin
package: larena/admin
version: "1.1.0"
status: stable
edition: core
product_layer: core
license: Apache-2.0
title: Larena Admin
description: Modular administration platform for Larena.
```

Allowed `status` values:

- `draft`
- `partial`
- `experimental`
- `stable`
- `deprecated`
- `internal`

Allowed `edition` / `product_layer` values:

- `core`
- `free`
- `pro`
- `industry`
- `enterprise`
- `cloud`
- `marketplace`
- `internal`

Allowed `distribution.access` values:

- `public`
- `private`
- `internal`

Allowed `api_operations.visibility` values:

- `public`
- `authenticated`
- `internal`
- `agent`

Allowed `health_checks.type` values:

- `artisan`
- `phpunit`
- `pest`
- `http`
- `manual`

## Dependency Rule

Composer remains the canonical PHP dependency graph.

If `module.yaml.depends_on` names a required Larena package, the matching Composer package should also be present in `composer.json require`, unless the dependency is explicitly optional and the code safely degrades without it.

Use `integrations.optional` for optional Larena integrations.

When resolving dependency drift, inspect actual source imports, service providers, commands, migrations and routes before changing metadata:

- if code imports another package class or middleware directly, add the matching `larena/*` package to Composer `require` and keep it in `module.yaml.depends_on`;
- if the relationship is only a future extension point, UI affinity, optional feature, or documented compatibility target, keep it out of Composer `require` and declare it under `integrations.optional`;
- do not add hard Composer dependencies only to silence the validator;
- do not remove a manifest dependency that represents a real runtime import.

After dependency alignment, tag the package and update the bootstrap repository lock if the entry app currently installs the stale contract.

## Product Boundary Rule

`edition`, `product_layer`, `license`, and `distribution.access` must make the package's product position explicit.

Working Docara boundary:

- `larena/docara-core`: free runtime/viewer direction.
- `larena/docara-admin`: paid admin/professional direction.

Do not silently change license, paid/free status, public/private distribution, or update channel without a product decision.

## Platform Subsystem Contract Rule

For core/P0 packages such as settings, access, props, admin, REST and future jobs/agents, standardization must produce two layers:

1. implementation layer: current Laravel code, migrations, routes, services, commands and views;
2. contract layer: package role, owned data, capabilities, permissions, session/API policy, jobs/events, health checks, docs and known operational risks.

The contract layer belongs in `module.yaml` plus `docs/developer/concept-alignment.md`.

Before calling a P0 package ready, verify:

- every important capability is declared;
- owned tables/config/storage are explicit;
- endpoints have session mode and permission metadata;
- endpoint rate limits are declared under `rate_limits`;
- stateful admin/UI routes are not presented as background, AI or external integration APIs;
- audit, rollback and health-check expectations are written down;
- gaps are tracked as blockers or follow-up decisions rather than hidden in chat.

Example: `larena/setting` owns `sf_setting`, `sf_setting_value` and category JSON schema files. Its current UI/admin endpoints are `stateful`; future background/API/AI consumers need a separate resolver/facade/API contract, not direct reuse of `/settings/*` routes.

## API Safety Rule

If a package exposes API behavior, declare it under `api_operations`.

Public operations require explicit operation metadata, permission/access model, and audit/risk controls where needed.

Dynamic class/method runners must not become arbitrary public APIs without allowlist, ACL and audit controls.

## Health Check Rule

Every official package should eventually define at least one `health_checks` entry:

- artisan command;
- PHPUnit/Pest test;
- HTTP route;
- admin/browser check;
- manual check when automation is not ready.

Release readiness must state which health check was run or why it cannot run.

## Provider Bootstrap Rule

Laravel service providers are part of the package install contract.

Provider `register()` and `boot()` must not break Composer/Laravel package discovery when `.env` is missing, DB is unavailable, or migrations have not run yet.

Allowed during provider boot:

- register bindings;
- merge/publish config;
- load routes, views, translations and migrations;
- register commands.

Not allowed during provider discovery/boot:

- require migrated DB tables;
- execute long-running work;
- fetch external URLs;
- write runtime state;
- fail the whole install because optional lifecycle tables are absent.

DB-aware state checks must fail open before migrations and move writes to explicit commands, HTTP/runtime paths, queue jobs or post-install flows.

## Package Alignment Workflow

For each package:

1. Read `composer.json`, current `module.yaml`, README/SPEC/docs, commands, routes and service provider.
2. Run `php artisan larena:validate-packages --path=/path/to/package`.
3. For P0/package-release checks, also run `php artisan larena:validate-packages --contract --strict --path=/path/to/package`.
4. Preserve existing valid manifest fields.
5. Add missing governance fields.
6. For P0 packages, add or update `docs/developer/concept-alignment.md`.
7. Resolve safe Composer/manifest mismatches.
8. Do not change runtime behavior only to satisfy the manifest.
9. Update package docs/SPEC/CHANGELOG when the manifest changes release behavior or developer contract.
10. Re-run validator and record unresolved product questions.

## Current Known Drift

Current package scans have found:

- legacy `simai/*` Composer names in some installed packages;
- missing `module.yaml` in some package copies;
- missing `edition`, `license`, `product_layer`, `docs`, `health_checks`;
- `depends_on` entries not reflected in Composer `require`;
- `larena-update` is the canonical update-server source; `larena-upserv` is legacy naming only and should survive only as explicit compatibility alias.
