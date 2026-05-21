# Package TZ Standard

Use this knowledge pack when a user asks to prepare, audit, improve or compare Larena package TZ documents.

Canonical project standard:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/standards/package-tz-standard.md
```

Template:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/standards/package-tz-template.md
```

Machine-readable readiness schema:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/schemas/package-tz-readiness.schema.json
```

## Core Rule

Do not treat a package TZ as implementation-ready just because a document exists.

Package TZ maturity is tracked separately from package completion:

- `T0`: idea;
- `T1`: draft;
- `T2`: structured;
- `T3`: integrated;
- `T4`: implementation-ready;
- `T5`: release-governed.

Current implementation target is `T4`.

`T5` is deferred until the Laravel update-server/module packaging standard is finalized.

## Required Audit Focus

When auditing a package TZ, check:

- package purpose;
- scope and non-goals;
- data ownership;
- lifecycle;
- package-local contracts: `module.yaml`, `api.yaml`, `access.yaml`, `audit.yaml`, `capabilities.yaml`;
- implementation contract;
- invariants;
- negative requirements;
- cross-package contract;
- API/access/audit/capability behavior;
- admin UX;
- runtime/cache/queue/session safety;
- licensing/trial behavior;
- acceptance scenarios;
- test contract;
- AI implementation hints;
- migration, rollback and deprecation.

## AI Implementation Gate

Do not start a major implementation batch for a package below `T4` unless the batch is explicitly discovery/prototype work.

For AI-assisted code generation, the TZ must include:

- implementation contract;
- invariants;
- negative requirements;
- cross-package contract;
- acceptance scenarios;
- test contract;
- AI implementation hints.

These sections prevent code that works locally but violates Larena architecture.

## Package Graph Rule

Each official package graph entry should have a `tz` block:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/package-graph/packages/*.yaml
```

Use `tz.maturity`, `tz.readiness`, `tz.blockers` and `tz.next_step` as the quick machine-readable view before deciding whether a package TZ can drive implementation.
