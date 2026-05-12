# Package Completion Standard

Use this pack when auditing, standardizing, releasing or planning work for any Larena package.

## Canonical Source

The canonical project document lives in `simai/larena`:

- `docs/developer/package-completion-standard.md`

Related documents:

- `docs/developer/package-contract.md`
- `docs/developer/module-yaml-schema.md`
- `docs/developer/standards/README.md`
- `docs/developer/standards/package-demonstrator-standard.md`
- `docs/developer/standards/package-dependency-impact-standard.md`
- `docs/developer/package-graph/README.md`
- `docs/developer/release-gates.md`
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

## Completion Levels

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

### L5: Release / Marketplace Ready

Package is ready for distribution.

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

When working on these packages, check the graph entry together with the package-local `module.yaml`. `module.yaml` explains what is inside the package; the package graph explains what other packages and smoke checks are affected when its contracts change.

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
