# Package `larena/docara`

## Role

`larena/docara` is the single documentation-product package. It owns the
public documentation runtime, Docara-specific content rules, navigation,
localization, rendering, import/export and admin contribution surfaces.

Generic content lifecycle should converge on `larena/content`; Docara must not
create a second long-term owner for generic type, item, revision, slug, status,
publication pointer or public-projection contracts.

## Product boundary

- Free/runtime capabilities: read and render installed/imported public
  documentation, local assets, navigation and access-safe public projection.
- Paid/editor capabilities: authoring, revision governance, scheduled
  publication, import/export, product packs and AI-assisted workflows.

These are capability/edition boundaries inside `larena/docara`. The retired
`larena/docara-core` and `larena/docara-admin` identities must not be recreated.

## Key surfaces

- package provider and contracts under `packages/docara/src`;
- public and admin routes under `packages/docara/routes`;
- Docara-owned migrations under `packages/docara/database/migrations`;
- feature and unit suites under `packages/docara/tests`;
- access, audit and API declarations owned by the package.

## Invariants

- public runtime never exposes draft/private/stale revisions or closed assets;
- access denial, stale CAS and audit failure fail closed without partial writes;
- install, copy/migration and rollback/reapply paths are explicit and
  repeatable;
- runtime assets are local and do not require a CDN;
- edition checks use central licensing contracts rather than scattered flags;
- generic page lifecycle has one owner after the Docara-on-Content transition.

## Required checks

- package validation, lint, analysis and full package test suite;
- Root integration and exact-revision acceptance;
- public/admin route, create/edit/history/restore/publish/unpublish and Search
  projection tests;
- negative access/audit/CAS and private-data projection tests;
- clean install, no-op reinstall, SQLite and isolated MySQL migration/rollback
  tests when persistence changes.
