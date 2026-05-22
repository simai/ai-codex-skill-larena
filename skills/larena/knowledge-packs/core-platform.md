# Larena Core Platform

Use this knowledge pack when designing, reviewing, or explaining the future `larena/core` package.

Canonical documentation lives in `/Users/rim/Documents/GitHub/larena/docs/developer/core/`:

- `README.md`;
- `core-package-tz.md`;
- `core-package-and-laravel-compatibility-rfc.md`;
- `core-machine-contracts.md`;
- `core-doctor-baseline.md`;
- `core-registry-lifecycle.md`;
- `core-operation-runtime.md`;
- `core-integration-review.md`;
- `core-team-handoff.md`.

## Baseline Decision

`larena/core` is a future thin platform kernel.

It owns:

- platform identity;
- platform version;
- compatibility matrix;
- installed package registry;
- package dependency graph;
- contract registry orchestration;
- shared Operation Runtime / Execution Pipeline contract;
- `larena:doctor` runner;
- package doctor check registration;
- update preflight decision;
- managed/protected area policy;
- machine-readable platform reports.

It must not own:

- login/session/MFA;
- access grants and permission decisions;
- admin shell/rendering;
- settings values/schemas;
- localization data;
- property rendering;
- storage records;
- REST/MCP/admin transport-specific execution engines;
- audit storage/sinks;
- licensing truth;
- update server catalog/delivery;
- local update execution;
- product logic such as Docara.

## Operation Runtime

`larena/core` owns the shared `OperationRuntime` contract for governed platform operations.

REST, MCP, admin UI, CLI commands and queue workers must not each invent their own access, licensing, audit, queue, cache and result/error pipeline. They adapt to the same core runtime when executing a meaningful governed operation.

Canonical flow:

```text
caller / transport
  -> OperationRuntime
  -> operation definition
  -> EntryObject/channel context
  -> validation
  -> access decision
  -> capability/quota decision
  -> rate limit
  -> cache/idempotency where allowed
  -> sync/queue decision
  -> transaction policy
  -> audit lifecycle
  -> package handler
  -> normalized result/error
```

Core owns the engine, metadata shape, pipeline order and result envelope.

Feature packages own handlers and business logic.

Transport boundaries:

- `larena/rest` maps HTTP/API operations to OperationRuntime;
- `larena/mcp` maps allowlisted AI tools to OperationRuntime;
- `larena/admin` maps operator actions to OperationRuntime;
- queue/CLI may use OperationRuntime when executing governed platform operations.

Do not implement a separate REST/MCP/admin execution engine for package actions.

## Laravel Policy

Larena must not fork Laravel.

For new architecture docs and future implementation planning, treat Laravel as upstream runtime foundation. Compatibility is controlled through:

- platform release line;
- Laravel/PHP/DB compatibility matrix;
- package dependency graph;
- CI/release gates;
- signed platform artifacts for ordinary hosting;
- `larena:doctor` and update preflight.

Do not design direct Laravel framework patches as the default path. Use Laravel-native extension points first: service providers, middleware, events, commands, migrations, validation, config, package discovery and container bindings.

## Core And Update Client Boundary

Keep `larena/core` and future `larena/update-client` separate.

Core answers:

```text
Can this platform state safely move to the requested target release?
```

Update client answers:

```text
How do we execute the approved local update plan safely?
```

Core owns registry, graph, compatibility, doctor, managed/protected area policy and preflight. Update client owns API v2 calls, local operation state, artifact download/verification, trust store, backup/recovery, step execution and reporting.

Do not merge destructive update execution into core.

## Registry And Contracts

Core discovers and orchestrates package contracts, but domain packages validate their own semantics.

Examples:

- `larena/access` validates access operations and targets;
- `larena/rest` validates API operations;
- `larena/lang` validates language packs and translation units;
- `larena/audit` validates audit event declarations;
- `larena/admin` validates admin contributions.

Runtime registries are derived state. Source contracts stay canonical and must be rebuildable from package files and release metadata.

## Doctor Baseline

`larena:doctor` is a common diagnostic runner, not a single package-specific smoke script.

Core owns the runner, severity model, JSON output and common checks. Packages register their own checks.

Baseline checks include:

- Laravel/PHP/DB support;
- required extensions;
- `APP_TIMEZONE=UTC`;
- storage/cache/queue health;
- package registry;
- dependency graph;
- contract registry;
- migrations;
- update/maintenance lock;
- managed/protected area policy;
- audit adapter availability or explicit dev-mode disablement.

Doctor output must be consumable by CLI, admin diagnostics, CI, support bundles, update preflight and AI diagnostics. It must not leak secrets.

## Current Phase

Core is documentation-phase complete, not implementation-ready.

Before coding:

1. review the core docs;
2. perform gap analysis against current starter/packages;
3. decide repository/package identity;
4. start with interface-only/dry-run registry and doctor reports;
5. defer destructive updater logic until core registry, doctor and preflight are stable.
