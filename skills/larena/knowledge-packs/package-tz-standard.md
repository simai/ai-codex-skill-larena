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

Semantic validator:

```text
/Users/rim/Documents/GitHub/larena/scripts/validate-package-tz.php
composer package-tz:validate
composer package-tz:validate:strict
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

## Validation Rule

When the user asks whether a package TZ is ready, do not rely only on manual reading.

Use the validation layers in this order:

1. `composer package-graph:validate` to verify package graph metadata and readiness block shape.
2. `composer package-tz:validate` to verify linked Markdown TZ document evidence.
3. For a package-specific review, run `php scripts/validate-package-tz.php --package=larena/<name> --verbose`.
4. For promotion to `T4`, run `composer package-tz:validate:strict` or package-specific strict validation and resolve warnings.

Normal TZ validation is a review/report mode. Warnings mean the graph claims a readiness state that the linked Markdown document does not clearly evidence. The correct fix is one of:

- add or rename the missing section in the package TZ;
- lower the readiness item from `complete` to `partial`;
- mark the item `not_applicable` only when the package truly does not own that concern.

The validator is evidence-oriented and does not replace architecture review. It is a guard against silently marking weak or underspecified TZ documents as implementation-ready.
