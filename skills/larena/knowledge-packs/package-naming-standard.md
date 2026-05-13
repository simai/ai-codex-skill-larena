# Package Naming Standard

Use this pack when creating, auditing, renaming or documenting official Larena packages.

## Canonical Source

The canonical project document lives in `simai/larena`:

- `docs/developer/standards/package-naming-standard.md`

Related documents:

- `docs/developer/standards/package-contract.md`
- `docs/developer/standards/package-completion-standard.md`
- `docs/developer/standards/module-yaml-schema.md`
- `docs/developer/standards/release-gates.md`

## Core Rule

Technical Larena package identifiers use a singular module/domain key by default.

Human-facing titles may use natural English, including plural words where that is clearer for users.

Example:

```text
Repository:       larena-setting
Composer package: larena/setting
module.yaml name: setting
Human title:      Larena Settings
UI label:         Settings
```

`larena/setting` is therefore correct as the technical identity. Do not rename it to `larena/settings` or `larena-settings` only because the user-facing English term is plural.

## Identifier Layers

Keep these layers consistent:

- repository: `larena-{module-key}`;
- Composer package: `larena/{module-key}`;
- `module.yaml` `name`: `{module-key}`;
- `module.yaml` `package`: exact Composer package;
- PHP namespace/classes: package/domain name in StudlyCase;
- public/UI title: natural English.

Technical identity is optimized for automation and long-term stability. UI/product text is optimized for humans.

## Singular By Default

Use singular package keys for domain or subsystem owners:

- `larena/setting`;
- `larena/access`;
- `larena/auth`;
- `larena/admin`;
- `larena/filesystem`;
- `larena/lang`;
- `larena/rest`;
- `larena/update`.

Plural or non-singular keys are acceptable only when they are the established technical term or a product compound, for example `larena/rest-doc`, `larena/docara-core`.

Current universal properties decision:

- canonical identity: `larena/property`;
- repository: `larena-property`;
- module key: `property`;
- human title: `Larena Properties`;
- old `larena/props`, repository `larena-props` and older `simai/props` are compatibility surfaces after the completed initial Composer/starter/package-graph migration.

Do not create new package contracts, architecture direction or user-facing docs under `props` except when documenting legacy compatibility.

## Rename Rule

Do not rename a stable package only for grammar.

Package rename requires an ADR or architecture note plus migration plan:

- Composer alias/replace/provide strategy where applicable;
- update-server compatibility plan;
- `module.yaml` migration notes;
- docs, README and release notes;
- validator transition rules;
- rollback notes.

Renames are acceptable for semantic mistakes, collisions, legal/trademark issues, pre-public packages with no contract, or explicit major-version migrations.

## Audit Output

When auditing package naming, report:

1. whether repository, Composer and `module.yaml` identity match;
2. whether the module key follows singular-by-default or has a documented exception;
3. whether human-facing titles use natural English;
4. whether a proposed rename is grammar-only or has a real platform/product reason;
5. what migration artifacts are required before a rename can be approved.

For universal properties, report `larena/property` as canonical and `larena/props` / `simai/props` as compatibility aliases. Future audits should verify package metadata, starter dependency, package graph and update-server metadata do not regress to `props` as canonical identity.
