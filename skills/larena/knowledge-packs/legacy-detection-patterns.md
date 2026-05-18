# Legacy Detection Patterns

Use this knowledge pack during Larena package diagnostics, package completion audits and L3/L4 readiness reviews.

Do not search only for old names, dead files or package aliases. Legacy often survives as active runtime behavior behind new APIs.

## Why Previous Audits Can Miss Legacy

Common weak spots:

- reviewing manifests/docs more deeply than live route/controller/service behavior;
- treating tests as proof without checking whether they codify old behavior;
- finding old package names but missing old runtime semantics;
- accepting compatibility fallback without checking fail-open behavior;
- checking path traversal but not broader public source disclosure;
- accepting `async` labels without verifying queue/job isolation.
- searching for duplicated lines but missing duplicated responsibilities, where old and new stacks implement the same behavior through different class names.
- checking controllers/services but not package template IDs, asset publication paths and generated placeholder files.

## Required Legacy Probes

### Active Runtime Legacy

Check for:

- fake users or fake actors after token/API auth;
- legacy JSON/config workflows still used by admin UI;
- old-model fields or stale relations in export/import/list code;
- boolean compatibility APIs used inside new explainable/typed flows.
- package editors that read from one source but save to another source;
- UI forms that expose only legacy context fields while the runtime already has canonical context fields;
- executable template/runtime editing surfaces that are treated as ordinary CRUD.

### Source-Of-Truth Drift

Build a source-of-truth map for every package surface that edits, imports, exports
or renders package-owned data.

Flag:

- admin list reads from schema/database, but edit/save writes directly to JSON or
  Blade files;
- create/update forms post old field names while services expect canonical field
  names;
- import/export serializes a different model than the runtime resolver uses;
- views call `file_get_contents`, scan package directories, or infer filesystem
  paths instead of using a package service/registry;
- old JSON category/config workflows remain reachable after a schema-pack or
  resolver layer exists.

Do not mark a package L4-ready when users can change data through a legacy
source path that bypasses the canonical service, audit, pending-review, access
or rollback layer.

### Trusted Runtime Surfaces

Treat template editors, Blade/PHP preview, dynamic include, package import, ZIP
import and admin "developer tools" as runtime surfaces, not simple forms.

Flag:

- `eval`, raw Blade compilation, dynamic include/require, or executable template
  writes without an explicit trusted-admin/development policy;
- admin views that directly write package files or public assets;
- preview endpoints that execute submitted templates or external content without
  isolation, audit, limits and rollback;
- external CDN/editor dependencies in packages whose manifest denies external
  network access;
- debug `console.log` or internal path/error output in production admin flows.

Safe handling requires a named policy: allowed environment, allowed role,
access operation, audit event, rollback or backup behavior, and smoke tests.
Until that exists, keep such features disabled, local-only, or clearly
trusted-admin only.

### Canonical Scope And Context Drift

For settings, access, storage, property, admin and REST packages, follow context
fields end to end.

Flag when new runtime contracts exist but UI/admin/API still only supports old
fields:

- settings context: `level`, `scope_id`, `role_id`, `site_id` must survive
  form, pending, import/export and resolver paths;
- access context: actor type, resource, package, scope, source and metadata
  must survive middleware, controller, checker and audit paths;
- admin context: entity, operation, route parameters and policy source must not
  collapse into one generic permission code;
- SitePack context: platform-neutral context must not collapse into
  package-local table columns only.

Do not accept "compatibility" if the new context is silently dropped before the
decision, audit or export layer.

### Fail-Open Compatibility

Security-sensitive paths must fail closed.

Check:

- object ACL receives a real subject/model;
- route parameters survive into authorization;
- fallback does not return allowed/neutral when resolver input is missing;
- config switches cannot silently disable access/session/API safety in normal mode.
- plugin compatibility fallback cannot load unversioned or unbounded plugins by
  default;
- fail-open env flags are limited to install/development profiles and are
  visible in doctor/smoke output.

### Test-Backed Legacy

Read tests as possible legacy contracts.

Flag tests that normalize:

- fake user token flows;
- legacy hash fallbacks;
- synchronous execution behind `async` names;
- generic permission checks where granular operations are expected;
- stale controllers/routes as valid behavior.
- package-local test harness bootstraps another package's runtime contracts
  instead of installing that package or using the package's documented provider.

### Actor Principal Compatibility

Token, service, MCP and AI-agent access must not be hidden behind fake human
users.

Flag:

- API-token middleware creates a user-like object and uses it as the primary
  authorization subject;
- actor type is not carried into `AccessContext`, audit payload, rate-limit key
  and scoped-grant matching;
- tests only assert that `Auth::user()` exists, but do not assert the native
  actor (`api_key`, `service`, `ai_agent`, `user`) and masked token metadata;
- old hash formats such as raw SHA-256 fallback remain accepted without a
  migration/sunset plan.

Temporary user-compatible principals may exist only as a documented adapter for
Laravel/Auth or old ownership checks. The canonical decision path must use the
native actor context and record the remaining compatibility in the legacy
registry.

### Route/Controller Drift

Build route-to-controller inventory for the package.

Flag:

- old controllers still reachable after migration to CRUD registrars/macros;
- route names from removed surfaces;
- stale views referenced by active controllers;
- public utility routes with broad file access.
- routes that point to non-existent controller methods; do not accept route URI presence as proof that an action is live.

### Template And Asset Contract Drift

For packages that ship Blade templates, field templates, themes, UI components or public assets, build a template/asset contract map:

- definition/config template identifier;
- expected Blade view name;
- actual file path;
- allowed path segment format;
- asset source path;
- publish target;
- runtime URL helper.

Flag:

- dotted template IDs such as `sf4.button` when the filesystem or editor policy accepts only path-safe segments such as `sf4-button`;
- empty Blade files that exist only to satisfy an old path but contain no implementation;
- duplicate template directories for the same visual theme, for example both `sf4.button` and `sf4-button`;
- view definitions that use a non-canonical namespace or old package identity after a package rename;
- asset helpers that generate one public URL while the service provider publishes another path;
- templates that call asset helpers for files that do not exist in the package source;
- stale `public/vendor/<old-package>` trees kept in the package after the canonical asset source moved to `resources/assets`.

Treat template/asset drift as active legacy when it can break admin editors, demonstrators, browser smoke, package publication or update-server packaging. If there are no live external consumers, normalize identifiers and paths now instead of preserving empty compatibility placeholders.

### Duplicate Responsibility Layers

Search for old and new stacks that own the same domain responsibility.

Before deciding that a package is L4-ready, build a compact responsibility map:

- responsibility name;
- canonical owner class/service/manifest/doc;
- alternate owners or adapters;
- route/controller/command/test/doc entry points;
- runtime reachability;
- whether the duplicate is intentional compatibility or accidental architecture drift.

Useful probes:

- active controllers that still inject `Services/*` while the package has newer `Support/*`, `Crud/*` or `Query/*` contracts;
- parallel filter/sort/search pipelines;
- multiple response abstractions with the same public name but different payload semantics;
- duplicate breadcrumb/menu/navigation builders;
- generic method invocation jobs that bypass the current batch/job payload contract.
- parallel description/scaffold contracts where one class family only converts back into the canonical contract, for example `*Resource` wrappers around an `EntityConfig` model;
- generators, tests and docs that preserve the duplicate layer even after runtime code has moved to the canonical contract.
- route defaults that advertise one contract while runtime code uses another, for example `responder` route defaults ignored by CRUD actions;
- async and sync transports that assemble the same query/source independently, for example lookup endpoints and server-side option builders;
- package-local bootstrapping of contracts owned by another package, for example a feature package registering admin route macros itself;
- middleware paths that infer the same permission/entity operation independently before delegating to the same checker;
- thin aliases or wrappers with the same basename as the real model/manager/service, unless explicitly documented as compatibility.

Treat runtime-reachable duplicate layers as active legacy even when the code does not use old package names.

If a package has no live external consumers yet, prefer removing the duplicate contract immediately instead of adding a long deprecation tail. Keep only the canonical contract in routes, generators, docs and tests.

When a duplicate layer is found, choose one of three outcomes:

1. remove now when there are no live consumers;
2. collapse to the canonical owner and keep transport/output adapters thin;
3. record as compatibility with owner, risk, removal condition and tests.

Do not accept a package as fully L4-ready when a duplicate layer affects core runtime behavior such as query semantics, responder selection, access checks, install/update flow, settings resolution, REST execution, or data import/export.

### Parameter Collapse

Follow operation identifiers end to end.

Examples:

- `custom:<slug>` must not collapse into generic `custom`;
- `show/edit/destroy` must map to the canonical abilities expected by the checker;
- scoped operations must keep `scope`, `resource`, tenant/site and actor context.

### Public Source Disclosure

For public asset routes, path traversal checks are not enough.

Require allowlists for:

- package roots;
- public asset subdirectories;
- file extensions;
- content types;
- maximum size where applicable.

Never expose arbitrary `vendor/<package>/**`.

### Fake Async

`202 Accepted` or `batch_id` does not prove background isolation.

Verify:

- work is actually dispatched to queue/job/worker;
- response returns before heavy work runs;
- timeout/rate/concurrency limits exist;
- tests do not lock synchronous execution as expected async behavior.

## Audit Output Rule

When these patterns are found:

- classify each as dangerous legacy, active compatibility, dead legacy or historical legacy;
- record it in package audit/status/roadmap;
- add central legacy registry records for active compatibility or dangerous/deferred legacy;
- do not raise a package readiness level if dangerous legacy affects the current acceptance path.
