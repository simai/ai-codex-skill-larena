# Larena Access Platform

Use this knowledge pack when reviewing or designing `larena/access`, API token access, MCP/AI capability access, package permissions, admin access UX, or package operation manifests.

## Core Model

Access decisions must use the Larena-native formula:

```text
EntryObject + Operation + Resource + Context -> AccessDecision
```

For list/data filtering, use the companion formula:

```text
EntryObject + Operation + QueryResource + Context -> AccessQueryScope
```

Do not reduce access to "user has permission". Larena must support users, API clients, API keys, AI agents, services, background jobs and future entry objects.

## Package Operations

Every package must declare stable package-scoped operations. Operations are atomic capabilities, not UI buttons or raw routes.

Do not auto-generate permissions from every PHP method. Methods are implementation details. Access operations must represent stable protected actions that matter to users, admins, REST, MCP, audit or security policy.

Examples:

- `docara.page.view`
- `docara.page.edit`
- `filesystem.upload`
- `admin.resource.delete`

Operations should be machine-readable, versioned through package metadata, installable/updateable by package lifecycle, and deny-by-default when unknown.

Create operations for:

- admin actions that read, change, delete, publish or export protected data;
- REST operations and MCP tools;
- public/account actions touching protected data;
- commands/jobs that can be triggered by a user, service, API client or AI agent;
- package methods that expose files, settings, users, tokens, licenses or security state;
- actions with their own risk level, audit policy, rate limit or token constraint.

Do not create operations for:

- private/internal helper methods;
- DTOs, mappers, normalizers or formatters;
- validation helpers without independent data access;
- view/render helpers without protected data access;
- service methods that only implement part of an already checked operation;
- low-level repository methods that must always be called through a checked service/action.

## Access Levels And Presets

An access level is a package-scoped bundle of operation values.

Do not confuse:

- access level with user group;
- operation with route;
- preset with grant;
- token constraints with access grants.

Presets are UX-level shortcuts over one or more access levels, such as `read-only`, `content-editor`, `package-admin`, `integration-read-only`, or `AI safe`.

## Operation Value Types

Access is not always boolean. Check for these values and require package docs/tests when they appear:

- `no`
- `yes`
- `own`
- `own_group`
- `own_group_tree`
- `custom`

If a package uses `own`, `own_group`, `participant`, `editor`, organization membership or another contextual access value, it must define the resource ownership/resolver contract and smoke-test both allow and deny cases.

## Resource And Query Scope

Packages that protect records/entities must expose ownership data through a stable contract or resolver:

- resource type/id;
- owner;
- group/organization/tenant;
- parent group/tree when needed;
- participants/editors when needed.

For list pages and APIs, a simple `allowed/denied` decision is not enough when the user can see only "own" or group-scoped records. The package must use `AccessQueryScope` or an equivalent access-approved filter instead of inventing ad hoc query conditions.

## Install Bootstrap

Package install/update flow should register:

- operations;
- operation value types;
- default access levels;
- recommended presets;
- optional safe default bindings;
- migration notes for changed operations or access levels.

Dangerous default bindings require documentation, release gate review and explicit explainability.

## Audit And Cache

Access checks may be cached, but cache is never the source of truth.

Cache invalidation must account for:

- package operation changes;
- access level changes;
- grants/bindings;
- user/group membership;
- organization/group hierarchy;
- token constraints;
- package enabled/disabled state.

Security-relevant access changes and denials should emit audit events through the common audit platform once it exists.

## Review Checklist

When auditing an access-related package, verify:

- operations are declared and stable;
- access levels/presets are not hidden in settings;
- unknown operations deny safely;
- token constraints narrow access and never silently expand it;
- package data filtering is access-aware for `own`/group scenarios;
- virtual targets have resolvers and smoke tests;
- admin/explain output does not reveal secrets;
- SitePack/export-import does not depend on raw table dumps.
