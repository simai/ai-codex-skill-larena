# Package Completion Standard

Use this pack when auditing, standardizing, releasing or planning work for any Larena package.

## Canonical Source

The canonical project document lives in `simai/larena`:

- `docs/developer/standards/package-completion-standard.md`

Related documents:

- `docs/developer/standards/package-audit-methodology.md`
- `docs/developer/package-audit-template.md`
- `docs/developer/standards/package-contract.md`
- `docs/developer/standards/module-yaml-schema.md`
- `docs/developer/standards/README.md`
- `docs/developer/standards/package-demonstrator-standard.md`
- `docs/developer/standards/ai-demonstrator-testing-standard.md`
- `docs/developer/standards/package-dependency-impact-standard.md`
- `docs/developer/standards/code-quality-legacy-logging-standard.md`
- `docs/developer/standards/legacy-registry-standard.md`
- `docs/developer/legacy/registry.json`
- `docs/developer/package-graph/README.md`
- `docs/developer/standards/release-gates.md`
- `docs/developer/repository-standardization-plan.md`
- `docs/developer/dna/`

## Core Rule

A Larena package is not complete only because its code works.

It is complete only when it is understandable, installable, diagnosable, demonstrable and safe for:

- human developers;
- Larena installer/update tooling;
- modular admin/runtime;
- testers;
- support operators;
- future AI agents.

When auditing a package, always return:

1. current completion level `L0`-`L5`;
2. missing artifacts;
3. blockers;
4. nearest useful batch;
5. checks that prove the next level.

If the user asks in Russian or English to "check a package against the standard",
"audit the package by standard", "проверь пакет на стандарт", or similar, treat it
as a full package-completion audit request. Do not answer with a short opinion and do not rely on a single bulk validator pass.

Use two layers:

1. **Fast Gate** for quick automated checks across packages: Composer, `module.yaml`, package graph, required docs presence and basic smoke.
2. **Deep Package Audit** for one package at a time: execute the batch methodology from `docs/developer/standards/package-audit-methodology.md`.

The audit must read the package repository and the central Larena standards, then
produce a structured verdict with:

1. package identity and repository path;
2. current level `L0`-`L5` and why it is not higher;
3. artifact compliance matrix for all required layers;
4. DNA alignment verdict and missing package-DNA items;
5. `module.yaml` / machine-readable contract gaps;
6. package graph and cross-package impact gaps;
7. demonstrator and smoke evidence status;
8. security/access/session/API/MCP risks;
9. documentation, changelog, install/update/rollback gaps;
10. code quality, legacy/fallback, package logging and duplicated semantic logic findings;
10.1. central legacy registry entries for active compatibility, dangerous legacy and historical legacy;
11. exact commands or browser/API checks that were run or could not run;
12. nearest useful batch to raise the package one level;
13. remaining work grouped into required versus future improvements.

Do not claim `L4` or `L5` from code quality or installed-site smoke alone.
Completion levels require the standard artifacts and evidence listed below.

For deep audits, use the report template from `docs/developer/package-audit-template.md` and store package-local reports as `docs/developer/package-standard-audit-YYYY-MM-DD.md` unless the repository has a more specific convention.

## Required Artifact Layers

Check these layers before calling a package complete:

1. **Package code**: provider, source, config, migrations, routes, resources, commands, events/jobs/listeners, tests or smoke.
2. **Repository shape**: README, CHANGELOG, Composer metadata, `module.yaml`, docs, tests/smoke, `.gitignore`, safe `.env.example`.
3. **Composer contract**: canonical PHP dependency graph, provider discovery, autoload, license and safe scripts.
4. **Package manifest**: `module.yaml` identity, product layer, dependencies, installs, endpoints, permissions, settings, jobs, health, audit, rollback and risks.
5. **Structured capability contract**: capabilities, owned data, consumed services, extension points and package interactions.
5.1. **Package graph entry**: central graph entry in `docs/developer/package-graph/packages/<package-key>.yaml`, with provides/consumes/edges/impact rules and required checks.
6. **Package DNA**: why the package exists, Larena canonical principles, migration references, boundaries and forbidden anti-patterns.
7. **Architecture docs**: components, data model, lifecycle, extension points, security, operations and integration flows.
8. **User/developer docs**: usage, install, config, commands, API, admin behavior, permissions, update/rollback and troubleshooting.
9. **Concept alignment**: Larena canonical model, Bitrix/older-SIMAI migration references, gaps, standard decisions and blockers.
10. **Demonstrator**: acceptance surface that shows real public/admin/API/integration behavior and role/permission states.
11. **Tests/smoke/health**: automated or documented proof that the package is alive.
12. **Security/access/session safety**: auth, permissions, session modes, CSRF/tokens, rate limits, audit, network access and queues.
13. **Install/update/rollback**: idempotent install path, migrations, config, seed/demo policy, update steps and rollback limits.
14. **Roadmap/known gaps**: ready state, postponed work, blockers and future decisions.
15. **AI development contract**: read-first docs, MCP tools/resources if exposed, safe read-only operations, effective user/service/capability context, write operations requiring approval, forbidden operations, neighbor package checks, required smoke checks and audit/risk notes.
16. **Package status card**: short `docs/developer/package-status.md` passport with current `L0`-`L5`, ready/missing/blockers, nearest batch, related packages, key docs and verification state.
17. **Code quality / legacy / logging review**: classify legacy as dangerous, active compatibility, dead or historical; document fallback; gate development logs; prefer package log channels; and record duplicated semantic logic cleanup items.

Rollback notes must match `module.yaml` `owned_data`, migrations, persistent storage and config files. Stale claims such as "the package owns no database tables" block an `L4` verdict when migrations or owned data already exist.

Package audits must apply the code quality, legacy and logging standard. Silent fallback, read-path mutations, noisy development logs in `laravel.log`, and repeated platform-contract logic are not acceptable as unnoticed background debt.

Active compatibility, dangerous legacy and historical legacy must be recorded in the central Larena legacy registry:

```text
docs/developer/legacy/registry.json
```

Do not rely on chat memory or scattered audit notes for compatibility layers that must be migrated later.

## Completion Levels

Current Larena package-standardization target is `L4 Demonstration Ready`.

Treat `L5 Release / Marketplace Ready` as a deferred gate until the Laravel
update-server/distribution standard exists for module artifacts, package data
packing, delivery channels, signatures/checksums, update plans and rollback
policy. Do not block L4 standardization work on L5, and do not claim L5 for
ordinary packages unless a separate release architecture decision explicitly
opens that gate.

### L0: Code Exists

Code exists and may work locally, but completion artifacts are missing or unreliable. Do not treat the package as platform-ready.

### L1: Repository Ready

Repository is understandable and mechanically usable.

Minimum: README, CHANGELOG, valid `composer.json`, `module.yaml` where applicable, basic docs, install notes and smoke/test path.

### L2: Contract Ready

Package is machine-readable and validator-friendly.

Minimum: expanded `module.yaml`, capabilities, owned data, endpoints/session modes, permissions, settings/schema packs, jobs/events, rate/external policy, audit, rollback, health checks and operational risks.

Use:

```bash
php artisan larena:validate-packages --contract --strict --path=/path/to/package
```

If it cannot pass yet, record exact exceptions and blockers.

### L3: DNA Aligned

Package is aligned with Larena direction and documented migration references.

Minimum: package DNA, architecture doc, concept alignment doc, known gaps, future decisions and no unresolved blocker that makes further development unsafe.

For platform primitives, also require an AI development contract or a recorded exception.

### L4: Demonstration Ready

Package has an acceptance surface.

Minimum: demonstrator or documented exception, admin/public/API scenarios where applicable, role/permission scenarios, smoke instructions and clear mapping to docs/DNA/contract.

Also require a package graph entry or documented exception. The demonstrator must map at least one important package graph edge to an executable or manual check.

Do not raise a package to L4 from installed-site smoke alone. L4 requires package DNA or an accepted exception, an explicit audit against Larena Product DNA and package DNA, current architecture/contract docs, demonstrator coverage and smoke evidence that follows the AI demonstrator testing standard.

When a package has known legacy/fallback-heavy areas, L4 audit must record which legacy is dangerous, active compatibility, dead or historical. Dangerous legacy that affects the demonstrator or canonical package DNA blocks L4 until fixed or isolated behind an explicit compatibility adapter.

### L5: Release / Marketplace Ready

Package is ready for distribution.

Status: deferred gate for the current Larena standardization phase.

Minimum: L1-L4 complete, package status card updated, version/changelog/release notes, install/update/rollback verified, license/product layer finalized, update artifacts/checksums/signatures when applicable, security/release gates passed and support policy clear.

## AI Development Contract Rule

The AI development contract prevents agents from treating Larena packages as ordinary Laravel code without platform context.

Recommended location:

```text
docs/developer/ai-contract.md
```

It should define:

- read-first documents;
- MCP tools/resources if exposed;
- safe read-only operations;
- effective user, service account or capability-token context;
- write operations requiring human approval;
- forbidden operations;
- required neighbor package checks;
- required smoke checks;
- audit and risk notes.

Be conservative by default. AI agents should not infer permission to run destructive migrations, mutate licenses, change update delivery, call external services, expose APIs or alter security boundaries unless the package contract and current task explicitly allow it.

If a package exposes MCP tools/resources, execution must be scoped to the effective Larena user, service account or capability token that authorized the MCP session. MCP must not silently grant broader access than that context has through normal Larena UI/API. Elevated service tools must be separate declared service/capability modes with explicit permission, audit and approval policy.

## Package Status Card Rule

The package status card is a short orientation passport, not a replacement for detailed docs.

Recommended location:

```text
docs/developer/package-status.md
```

When present, it should include current completion level, checked date, product layer, ready items, missing items, blockers, nearest batch, related packages, key docs and verification state.

Use it to quickly answer "where is this package now and what should be done next?"

## Demonstrator Rule

For packages with public, admin, API or integration behavior, prefer a demonstrator as an acceptance surface, not as a marketing page.

Valid demonstrator forms:

- admin showcase page;
- demo seed command;
- protected demo route behind a config flag;
- demo docs page;
- API collection;
- browser smoke scenario;
- package-specific Docara demo.

The demonstrator should show happy path, denied/empty/error states, permissions, settings/configuration, package integrations and the connection between DNA, manifest and implementation.

Demo behavior must be safe by default and must not expose production-sensitive features without explicit config and permission.

Use the project demonstrator standard:

```text
docs/developer/standards/package-demonstrator-standard.md
```

When AI agents test a demonstrator, also use:

```text
docs/developer/standards/ai-demonstrator-testing-standard.md
```

The AI check must build an explicit matrix from Larena Product DNA, package DNA when available, `module.yaml`, package status, architecture docs, package graph entry, security/session rules and runtime evidence. If package DNA is missing, do not invent intent and do not claim DNA compliance; mark the DNA-specific layer as `not_ready` and test only the general Larena/package contract. Evidence must record inputs read, commands/routes checked, verdicts, security/session notes, test data cleanup and remaining blockers.

## Package Graph Rule

Use the central Package Graph for cross-package impact tracking:

```text
docs/developer/package-graph/packages/<package-key>.yaml
```

The graph entry should declare:

- what the package provides;
- what it consumes;
- explicit graph edges;
- high-risk contracts;
- impact rules;
- required cross-package smoke checks.

Use the project dependency/impact standard:

```text
docs/developer/standards/package-dependency-impact-standard.md
```

A new package is not fully Larena-compatible until it is woven into the package graph or has a documented exception. This is especially important for third-party packages because upstream packages cannot know every future consumer.

Current first-party baseline entries in `simai/larena` cover:

- `larena/access`;
- `larena/admin`;
- `larena/auth`;
- `larena/rest`;
- `larena/setting`;
- `larena/props`;
- `larena/docara-core`;
- `larena/docara-admin`.
- `larena/update`;
- `larena/update-registration`;
- `larena/filesystem`;
- `larena/lang`;
- `larena/two-fa`.
- `larena/mcp`;
- `larena/rest_doc`;
- planned placeholder `larena/storage`.

When working on these packages, check the graph entry together with the package-local `module.yaml`. `module.yaml` explains what is inside the package; the package graph explains what other packages and smoke checks are affected when its contracts change.

The human-readable impact matrix is generated from the graph entries:

```bash
php scripts/generate-package-impact-matrix.php
```

or:

```bash
composer package-graph:generate
```

Validate graph entries before relying on the matrix:

```bash
composer package-graph:validate
```

Use strict validation when graph entries must be checked against package-local `module.yaml`:

```bash
composer package-graph:validate:strict
```

Baseline package repositories should also have a package-local status card:

```text
docs/developer/package-status.md
```

The status card is intentionally short: it records current level, ready/missing items, nearest batch, related packages, key docs and verification state. Do not use it as a replacement for DNA, architecture, demonstrator or smoke evidence.

Use the central gaps report to decide which package-local demonstrator/status-card work should happen next:

```text
docs/developer/package-graph/generated/package-local-gaps.md
```

Current first-priority demonstrator contracts and installed-site evidence exist for:

- `larena/admin`;
- `larena/auth`;
- `larena/rest`;
- `larena/rest_doc`.

Treat them as preparation evidence, not as L4 readiness by itself. These packages still require package DNA and explicit package-standard audit before any L4 claim:

- `larena/admin`: installed-site admin smoke passed after fail-closed admin access defaults and `admin.access` coverage for legacy update-server admin routes.
- `larena/auth`: installed-site auth smoke passed; ordinary registered users are denied admin access, but the registration redirect to `/admin` remains backlog.
- `larena/rest`: installed-site sessionless API smoke passed; add a dedicated allowed-token `200` fixture during the real package audit.
- `larena/rest_doc`: installed-site Swagger safety smoke passed; public placeholder has empty paths and generated spec is token-protected.

Current DNA-baseline packages that were worked through and still need re-audit under the updated rules:

- `larena/setting`;
- `larena/access`;
- `larena/mcp`.

## Practical Output Template

When asked whether a package is complete, answer in this shape:

```text
Completion level: L<N> - <name>

Ready:
- ...

Missing:
- ...

Blockers:
- ...

Nearest useful batch:
- ...

Verification for next level:
- ...

Status card:
- present/missing/stale

AI contract:
- present/missing/not applicable

MCP exposure:
- none / declared / unsafe / unknown

Package graph:
- present/missing/exception/stale

Demonstrator:
- present/missing/exception/stale
```

Do not hide missing artifacts behind vague phrases such as "needs docs" or "needs tests". Name the exact missing file, manifest field, scenario or gate.
