# Package TZ Standard

Use this knowledge pack when a user asks to prepare, audit, improve or compare Larena package TZ documents.

Larena Package TZ is now a Larena-specific profile of the universal graph-based TZ standard owned by `$graph`.

```text
/Users/rim/Documents/GitHub/ai-codex-skill-graph/skills/graph/references/universal-graph-tz-standard.md
```

Use the universal standard for graph object roles, relations, readiness, evidence, adoption and AI context. Use this Larena profile for package graph, Larena contracts and repository validators.

Canonical graph-based project standard:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/standards/graph-package-tz-standard.md
```

Transitional text-first standard:

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

Cross-package feature adoption:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/feature-graph/README.md
/Users/rim/Documents/GitHub/larena/docs/developer/feature-graph/features/*.yaml
composer feature-graph:validate
composer feature-graph:gaps
php scripts/list-package-feature-gaps.php --package=larena/<name>
```

## Core Rule

Do not treat a package TZ as implementation-ready just because a document exists.

New package TZ work should start from the graph-based profile:

```text
Universal Graph TZ Standard
  -> Software Package TZ Profile
    -> Larena Package TZ Profile
      -> larena-specs/graph/specs
```

Package TZ maturity is tracked separately from package completion:

- `T0_idea`;
- `T1_captured`;
- `T2_structured`;
- `T3_reviewed`;
- `T4_specification_ready`;
- `T5_implementation_ready`;
- `T6_validated`;
- `T7_operating`;
- `T8_evolving`.

Current implementation target is `T5_implementation_ready`.

Larena package completion `L5` remains deferred until the Laravel update-server/module packaging standard is finalized.

## Graph Readiness And Content Quality Gate

Larena package TZ readiness must be checked with both metrics:

- `GRS` / TZ Conglomeration GRS: structural graph readiness, cross-package
  integration, adoption coverage and evidence links.
- `CQS` / Content Quality Score: quality of the specification content for the
  intended work.

Do not average these into one hidden number. A package can have strong graph
structure and still have weak content, or strong prose and weak cross-package
integration.

Default Larena thresholds:

```text
Discussion draft                  GRS >= 60, CQS >= 60
Team review                       GRS >= 75, CQS >= 75
Implementation planning           GRS >= 85, CQS >= 85
AI-assisted implementation         GRS >= 90, CQS >= 88
Critical/runtime architecture      GRS >= 90, CQS >= 90
```

For ordinary Larena packages, target `GRS >= 85` and `CQS >= 85` before
implementation planning.

For platform-critical packages, target at least `GRS >= 90` and `CQS >= 88`;
prefer `CQS >= 90` when the package defines security, runtime, update,
licensing, data or API foundations. Platform-critical packages include:

- `larena/core`;
- `larena/admin`;
- `larena/auth`;
- `larena/access`;
- `larena/audit`;
- `larena/licensing`;
- `larena/update`;
- `larena/update-client`;
- `larena/update-registration`;
- `larena/queue`;
- `larena/storage`;
- `larena/filesystem`;
- `larena/rest`;
- `larena/mcp`.

If either score is below its target, do not start broad autonomous
implementation. First raise the lower side:

- low GRS: add or fix graph objects, relations, adoption records, acceptance
  links and evidence;
- low CQS: refine purpose, contracts, examples, edge cases, failure modes,
  acceptance, test expectations and implementation boundaries.

Do not chase perfect `100/100` scores. When a package reaches its target and the
remaining issues are minor examples, naming or release details, move those
items into implementation planning, roadmap or team review notes.

## Required Audit Focus

When auditing a package TZ, check:

- package purpose;
- scope and non-goals;
- data ownership;
- lifecycle;
- package-local contracts: `module.yaml`, `api.yaml`, `access.yaml`, `audit.yaml`, `capabilities.yaml`;
- required feature graph adoption for cross-package mechanisms;
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

## Post-TZ Implementation Planning Gate

When Larena package TZs reach the agreed `GRS`/`CQS` gate and pass package/team
review, the next step is implementation planning, not immediate coding.

Use this sequence:

```text
Package TZ ready
  -> AI/team review accepted for implementation planning
  -> implementation plan
  -> tests and acceptance plan
  -> smoke evidence plan
  -> code implementation
  -> installed-site smoke evidence
  -> release/readiness audit
```

Implementation planning must be cluster-based. Do not plan all packages at once
unless the user explicitly asks for a full ecosystem implementation roadmap.

For each selected cluster, create a durable planning artifact that defines:

- package order and dependency order;
- contracts to stabilize first: `module.yaml`, `api.yaml`, `access.yaml`,
  `audit.yaml`, `capabilities.yaml`, `queue.yaml`, `scheduler.yaml`,
  `monitoring.yaml` or other package descriptors;
- database tables, migrations, commands, services, admin screens and public/API
  surfaces expected in the first implementation batch;
- package boundaries and source-of-truth rules that must not be violated;
- licensing/capability behavior and Free/Pro/deferred gates;
- security and privacy invariants: no raw secrets, no fail-open access, no
  unsafe dynamic method execution, no local pro flags, no local audit systems;
- runtime constraints for ordinary hosting: cron/tick/queue/cache/fallback
  behavior, no hidden Redis/Horizon/SQS requirement unless explicitly gated;
- test plan: unit, integration, descriptor validation, security/negative,
  migration/config and cross-package interaction tests;
- smoke evidence plan for an installed Larena: commands, admin/API/browser
  checks, screenshots/log snippets/JSON responses and where evidence is stored;
- release/readiness audit checklist: code matches TZ, no legacy/fallback debt,
  docs/status updated, package audit passed, smoke evidence present, rollback or
  update path clear.

Use the generated graph TZ as the planning source, but write a compact human
handoff for the implementation cluster before code work starts.

Recommended first cluster after TZ completion:

```text
security_runtime:
  larena/core
  larena/auth
  larena/access
  larena/audit
  larena/rest
  larena/mcp
  larena/admin
  larena/licensing
```

This cluster is the foundation for later package implementation because it
defines the shared path:

```text
entry object -> access decision -> operation runtime -> audit event -> admin explain
```

Do not call a package release-ready until code, package tests, installed-site
smoke evidence and release/readiness audit are complete.

## Package Graph Rule

Package graph and feature graph are transitional compatibility views until their
data is migrated into or generated from `larena-specs/graph/specs`.

Each official package graph entry should have a `tz` block:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/package-graph/packages/*.yaml
```

Use `tz.maturity`, `tz.readiness`, `tz.blockers` and `tz.next_step` as the quick machine-readable view before deciding whether a package TZ can drive implementation.

## Feature Graph Rule

For cross-package mechanisms, also check:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/feature-graph/features/*.yaml
```

Feature graph is required when a feature spans several packages, for example:

- core operation runtime;
- cache;
- access query scope;
- audit event flow;
- licensing capabilities;
- search indexing;
- storage profiles;
- SitePack import/export.

A package TZ can be structurally strong but still not ready for implementation if its required feature graph adoption is `needs_design`, `needs_mapping` or `partially_described` for a critical feature.

For package-specific audits, include:

```bash
php scripts/list-package-feature-gaps.php --package=larena/<name>
```

T4 gate:

```text
A package cannot be promoted to T4 if it has an unresolved required critical feature adoption with status needs_design or needs_mapping, unless the package TZ explicitly documents a safe deferral that does not affect the implementation target.
```

## Validation Rule

When the user asks whether a package TZ is ready, do not rely only on manual reading.

Use the validation layers in this order:

1. `composer package-graph:validate` to verify package graph metadata and readiness block shape.
2. `composer package-tz:validate` to verify linked Markdown TZ document evidence.
3. For a package-specific review, run `php scripts/validate-package-tz.php --package=larena/<name> --verbose`.
4. Run `php scripts/list-package-feature-gaps.php --package=larena/<name>` to inspect cross-package feature obligations.
5. For promotion to `T4`, run `composer package-tz:validate:strict` or package-specific strict validation and resolve warnings.

Normal TZ validation is a review/report mode. Warnings mean the graph claims a readiness state that the linked Markdown document does not clearly evidence. The correct fix is one of:

- add or rename the missing section in the package TZ;
- lower the readiness item from `complete` to `partial`;
- mark the item `not_applicable` only when the package truly does not own that concern.

The validator is evidence-oriented and does not replace architecture review. It is a guard against silently marking weak or underspecified TZ documents as implementation-ready.
