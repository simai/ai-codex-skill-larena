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

## Required Legacy Probes

### Active Runtime Legacy

Check for:

- fake users or fake actors after token/API auth;
- legacy JSON/config workflows still used by admin UI;
- old-model fields or stale relations in export/import/list code;
- boolean compatibility APIs used inside new explainable/typed flows.

### Fail-Open Compatibility

Security-sensitive paths must fail closed.

Check:

- object ACL receives a real subject/model;
- route parameters survive into authorization;
- fallback does not return allowed/neutral when resolver input is missing;
- config switches cannot silently disable access/session/API safety in normal mode.

### Test-Backed Legacy

Read tests as possible legacy contracts.

Flag tests that normalize:

- fake user token flows;
- legacy hash fallbacks;
- synchronous execution behind `async` names;
- generic permission checks where granular operations are expected;
- stale controllers/routes as valid behavior.

### Route/Controller Drift

Build route-to-controller inventory for the package.

Flag:

- old controllers still reachable after migration to CRUD registrars/macros;
- route names from removed surfaces;
- stale views referenced by active controllers;
- public utility routes with broad file access.

### Duplicate Responsibility Layers

Search for old and new stacks that own the same domain responsibility.

Useful probes:

- active controllers that still inject `Services/*` while the package has newer `Support/*`, `Crud/*` or `Query/*` contracts;
- parallel filter/sort/search pipelines;
- multiple response abstractions with the same public name but different payload semantics;
- duplicate breadcrumb/menu/navigation builders;
- generic method invocation jobs that bypass the current batch/job payload contract.

Treat runtime-reachable duplicate layers as active legacy even when the code does not use old package names.

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
