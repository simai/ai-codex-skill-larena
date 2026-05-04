# Module YAML Standard

Use this pack when work touches `module.yaml`, Composer package metadata, package release readiness, update-server package discovery, package docs, package validators, or AI-agent-readable package manifests.

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
3. Preserve existing valid manifest fields.
4. Add missing governance fields.
5. Resolve safe Composer/manifest mismatches.
6. Do not change runtime behavior only to satisfy the manifest.
7. Update package docs/SPEC/CHANGELOG when the manifest changes release behavior or developer contract.
8. Re-run validator and record unresolved product questions.

## Current Known Drift

Current package scans have found:

- legacy `simai/*` Composer names in some installed packages;
- missing `module.yaml` in some package copies;
- missing `edition`, `license`, `product_layer`, `docs`, `health_checks`;
- `depends_on` entries not reflected in Composer `require`;
- unresolved `larena-update` versus `larena-upserv` source-of-truth question.
