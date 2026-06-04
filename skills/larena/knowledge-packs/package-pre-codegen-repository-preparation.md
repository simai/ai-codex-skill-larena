# Package Pre-Codegen Repository Preparation

Use this knowledge pack before writing implementation code for any Larena
package repository.

## Purpose

This process prepares a clean Larena package repository for high-quality AI
codegen and developer work.

The main goal is not legacy analysis. If old code has a verified backup, empty
the active repository tree and recreate the package from the Larena baseline.
The important work is what happens after that: package identity, specs link,
launch context, Composer commands, hooks, CI, scope checks, evidence and graph
sync proposal boundaries.
The repository must also be visible to the central Larena Specs process through
an enforcement checklist, repository preparation validation, coverage/readiness
reports and a committed clean baseline before coding starts.

Canonical detailed process:

- `/Users/rim/Documents/GitHub/larena-specs/docs/standards/package-repository-reset-and-pre-codegen-preparation.md`
- `/Users/rim/Documents/GitHub/larena-specs/specs/standards/package-repository-reset-and-pre-codegen-preparation.json`

## Mandatory Rule

Do not start Larena package coding from a markdown plan, old repository,
prototype package, legacy branch or partially prepared repo.

Required sequence:

```text
backup confirmed
-> empty active repository tree
-> clean Larena package baseline
-> specs reference
-> launch context
-> package-local command contract
-> hooks and CI enforcement
-> scope and evidence checks
-> repository validation
-> launch record
-> ready_to_code
-> coding_started
```

`repository_prepared` is not `ready_to_code`.
`ready_to_code` is not `coding_started`.

## Legacy Reset Rule

For old repositories with confirmed backup:

```text
remove everything from the active tree except .git
-> recreate the package from clean Larena templates
```

Do not keep old source, migrations, configs, docs, tests, routes, scripts or
old package names in active `main`. Do not copy the old codebase into an active
`legacy/` folder. Backup, tag, branch or archive is enough.

## Clean Package Baseline

Create the standard package repository structure:

```text
composer.json
module.yaml
README.md
LICENSE
.env.example
.gitignore
.larena/
  spec-ref.json
  launch-context.json
.githooks/
  pre-commit
  pre-push
.github/workflows/
  larena-package-ci.yml
scripts/
  analyse.php
  check-evidence.php
  lint.php
  test-placeholder.php
  validate-larena-package.php
tools/
  larena-scope-check.php
phpstan.neon.dist
src/
tests/
config/
database/
docs/
```

This is not package implementation code. It is the controlled workspace for
future implementation.

## Required Preparation Steps

1. Classify repository:
   - `new_empty_repository`;
   - `legacy_repository_rewrite_from_scratch`;
   - `legacy_reference_only`;
   - `continuation_repository`;
   - `server_side_private_repository`.
2. Confirm backup for old repositories.
3. Empty active tree for rewrite-from-scratch packages.
4. Create package identity:
   - package id;
   - repo name;
   - local path;
   - Composer package name;
   - PHP namespace;
   - distribution/license model;
   - implementation planning cluster.
5. Create `.larena/spec-ref.json`.
6. Create `.larena/launch-context.json` with `coding_allowed: false`.
7. Create `composer.json` with standard commands:
   - `test`;
   - `test:unit`;
   - `lint`;
   - `analyse`;
   - `validate:larena`;
   - `evidence:check`;
   - `scope:check`;
   - `quality:gate`.
   The commands must point to real package-local scripts or equivalent
   executable commands. Script names alone are not enough.
8. Create `module.yaml`.
9. Create hygiene files:
   - `.gitignore`;
   - `.env.example`;
   - `LICENSE`;
   - `README.md`.
10. Create hooks:
    - `.githooks/pre-commit`;
    - `.githooks/pre-push`.
11. Activate hooks:

```bash
git config core.hooksPath .githooks
```

12. Create CI:

```text
.github/workflows/larena-package-ci.yml
```

13. Create scope checker:

```text
tools/larena-scope-check.php
```

14. Create or update the central enforcement checklist in `larena-specs`:

```text
specs/implementation-planning/repository-preparation/<package>-enforcement-kit.json
```

15. Prepare future evidence and graph sync proposal paths.
16. Add placeholder validation tests proving repository preparation, not
    package functionality.
17. Run repository preparation validation and package enforcement validation.
18. Commit the clean baseline and push it when repository access allows.
19. Confirm the package appears in repository coverage and mass coding
    readiness reports.

## Coding Gate

Code can start only after:

- active tree is clean for rewrite-from-scratch packages;
- clean Larena baseline exists;
- package identity matches `larena-specs`;
- `.larena/spec-ref.json` exists;
- `.larena/launch-context.json` exists and keeps coding disabled;
- Composer command contract exists;
- package-local script files and static analysis configuration exist;
- hooks exist and active `core.hooksPath` points to `.githooks`;
- CI workflow exists;
- scope checker exists;
- central package enforcement checklist exists;
- evidence and graph-sync proposal paths are declared;
- central coverage/readiness reports account for the package;
- clean baseline is committed or there is an explicit pre-codegen blocker;
- launch record exists and is validated;
- action gates pass.

## Stop Conditions

Stop before preparation or coding when:

- old code backup is not confirmed;
- uncommitted user changes exist;
- package identity is unclear;
- package spec or package DNA is missing;
- expected repository path is wrong;
- secrets or private logs are detected;
- hooks cannot be activated;
- package command contract cannot be installed;
- CI cannot be created;
- scope checker cannot run.

## Coordinator Behavior

When preparing a package repository:

1. Run federation/action gates.
2. Confirm repository class and backup status.
3. Empty active tree if it is a rewrite-from-scratch legacy repo.
4. Build clean Larena package baseline.
5. Link the repo to `larena-specs`.
6. Install Composer command contract, package-local scripts, static analysis,
   hooks, CI and scope checker.
7. Create the enforcement checklist in `larena-specs`.
8. Validate repository preparation, enforcement checklist, bootstrap, coverage
   and mass coding readiness.
9. Commit the clean baseline or record the exact blocker.
10. Stop at `repository_prepared` unless a separate launch record starts coding.

Do not hide a partially prepared repository behind a successful cleanup.
Cleanup is only the first small step; preparation and enforcement are the real
codegen gate.
