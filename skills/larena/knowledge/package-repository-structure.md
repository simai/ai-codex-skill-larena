# Package Repository Structure

Use this pack when work creates, rewrites, audits, standardizes or prepares a
`larena/*` package repository.

Canonical source: `larena-specs/docs/standards/package-repository-structure.md`
and `larena-specs/specs/standards/package-repository-structure.json`.

## Core Rule

Each Larena package is a separate Composer/Laravel package repository.

`larena-specs` is the source of truth for package identity, features,
relations, readiness, distribution, licensing and implementation planning.
Package repositories are implementation and evidence spaces.

## Recommended Layout

```text
larena-<package>/
  README.md
  LICENSE
  composer.json
  module.yaml

  src/
    <Package>ServiceProvider.php
    Contracts/
    DTO/
    Events/
    Exceptions/
    Facades/
    Http/
    Jobs/
    Models/
    Policies/
    Services/
    Support/

  config/
    <package>.php

  database/
    migrations/
    seeders/
    factories/

  routes/
    web.php
    api.php
    console.php

  resources/
    views/
    lang/
    assets/
      css/
      js/
      images/
    stubs/

  docs/
    index.md
    installation.md
    configuration.md
    api.md
    extension-points.md
    testing.md
    changelog.md

  tests/
    Unit/
    Feature/
    Integration/
    Fixtures/
    Pest.php
    TestCase.php

  graph/
    implementation-status.json
    sync-report.json
    local-evidence/
    sync-proposals/

  source/
    workflow/
    evidence/
    handoff/

  .github/
    workflows/

  .larena/
    package.json
    spec-ref.json
```

## Required Root Files

- `composer.json`: canonical Composer package metadata and dependency graph.
- `module.yaml`: Larena package manifest and machine-readable runtime/update
  summary.
- `README.md`: public English package overview.
- `LICENSE`: license matching `larena-specs` distribution metadata.

## Public Docs Rule

Public package docs must be English-only by default.

Russian internal TZ belongs in `larena-specs`, not in public package
repositories.

## Local Graph Evidence

Package repos may contain local graph evidence:

```text
graph/
  implementation-status.json
  sync-report.json
  local-evidence/
  sync-proposals/
```

These files are not canonical graph copies. They are local implementation
status and proposals for coordinator review.

## `.larena/spec-ref.json`

Every package repo should eventually declare the specs revision used by the
implementation:

```json
{
  "schema": "larena.package_spec_ref.v1",
  "package": "larena/core",
  "specs_repo": "larena-specs",
  "specs_ref": "main",
  "implemented_features": [],
  "sync_state": "proposal_required"
}
```

For releases, `specs_ref` should be a commit hash or signed release tag.

## Do Not Store

Do not store:

- canonical graph copies as independent source-of-truth data;
- Russian internal TZ as public docs;
- raw secrets, `.env`, tokens, cookies, passwords or private keys;
- customer-private raw logs;
- local licensing bypasses;
- duplicated access, queue, audit, secret, auth or filesystem mechanisms owned
  by other Larena packages.

## Gatekeeper Checklist

Before calling a package repo structure acceptable, verify:

- root files exist or have a justified implementation-batch reason;
- `composer.json`, `module.yaml` and `.larena/spec-ref.json` agree on package
  identity;
- public docs are English-only;
- local graph evidence is proposal-gated;
- tests exist or are planned in the active implementation batch;
- source code does not redefine another package boundary.
