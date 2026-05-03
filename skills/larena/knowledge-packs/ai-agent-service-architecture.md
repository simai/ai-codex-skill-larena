# AI-Agent Service Architecture

Larena is designed for a world where AI agents help assemble, configure, diagnose and extend products.

## Core Principle

Treat each important package/module/service as an agent-readable building block.

A Larena building block can run:

- inside one Laravel application;
- as a package/module in a larger Larena product;
- as a separate internal service;
- as an external service connected through API contracts.

The architecture goal is Lego-like composition: humans and AI agents should be able to discover what exists, understand contracts, combine compatible units, and generate or configure missing glue without reverse-engineering the whole ecosystem.

## SF5 Analogy

Use SF5 as the frontend analogy:

- utilities are atomic primitives;
- components compose utilities into reusable UI units;
- smart components add events, state, data loading, interaction and templating;
- blocks/pages compose higher-level interfaces;
- prepared assets can be loaded and cached on ordinary hosting without requiring a local frontend build server;
- page configuration can change dynamically because assets/classes/blocks are already generated and available.

Larena should seek the same quality for backend/platform functionality:

- primitive services/packages;
- domain modules;
- admin/settings/props/storage surfaces;
- safe REST/API operation layer;
- SitePack transport;
- update-server distribution;
- documentation and skill knowledge for AI orientation.

## Required Building-Block Properties

Prefer designs where each package/service exposes:

- product classification (`kind`, `tier`, `distribution`, edition/channel/license policy);
- purpose and ownership;
- capabilities;
- dependencies;
- install/update/rollback path;
- configuration keys;
- commands, queues and schedules;
- API operations and event contracts;
- data/storage contracts;
- security scopes and permission rules;
- audit/protocol behavior;
- extension points;
- smoke/test commands;
- links to user/developer docs.

Existing `module.yaml` files are the first candidate for this manifest layer. The already proposed `product:` block is useful but not enough; future manifest design should cover capabilities, APIs, events, commands, jobs, security scopes, audit/protocol behavior and documentation links.

This can be human-readable docs first, but the long-term direction should allow machine-readable manifests or generated docs.

## API Direction

Dynamic REST is strategically useful as an interoperability layer, but not as arbitrary public method execution.

For production, prefer:

- explicit operation registration/declaration;
- public APIs by resource/operation whitelist;
- metadata for purpose, input, output, side effects, permissions and risk;
- token-aware and ACL-aware OpenAPI/Swagger;
- separation of internal API, service-to-service API, public API and AI-agent tool API;
- deny-by-default for dangerous operations;
- audit/protocol records for executed operations.

Treat `/run` as internal/service/agent operation infrastructure by default. If exposed beyond trusted contexts, it needs whitelist, ACL, throttle, audit, risk metadata and explicit confirmation for dangerous actions.

## Ordinary Hosting And Background Work

Agent/service architecture must still work on ordinary hosting. Prefer background-work designs that can degrade from queue workers to:

- DB-backed job store;
- bounded `simai:tick` command;
- cron sub-ticks with budget/limit;
- hit fallback with lock and rate limit;
- retry/backoff with jitter;
- job attempt logs and queue metrics.

## Documentation And Skill Rule

Each Larena repository should have enough documentation for an AI-assisted developer to orient quickly according to `$dev` repository documentation rules.

Stable reusable Larena rules should be promoted into `$larena` at the narrowest useful place. Project-only facts remain in repository docs or `source/memory/`.

## Review Questions

When reviewing or designing a package/service, ask:

- Can an AI agent identify what this unit does without reading all code?
- Are safe operations discoverable through docs, manifest or API metadata?
- Are dangerous operations gated by permissions, confirmation, audit and limits?
- Can this unit run only in-process, or can it later be separated behind an API?
- Is the install/update/rollback path explicit enough for update-server delivery?
- Does the package expose enough tests/smoke checks for automated validation?
