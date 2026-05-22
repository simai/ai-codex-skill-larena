# Feature Graph

Use this knowledge pack when a Larena task asks how one cross-cutting feature is adopted by many packages.

Canonical project docs:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/feature-graph/README.md
/Users/rim/Documents/GitHub/larena/docs/developer/feature-graph/features/*.yaml
```

Generated outputs:

```text
/Users/rim/Documents/GitHub/larena/docs/developer/feature-graph/generated/feature-adoption-matrix.md
/Users/rim/Documents/GitHub/larena/docs/developer/feature-graph/generated/package-feature-gaps.md
```

Validation and generation:

```text
composer feature-graph:validate
composer feature-graph:generate
composer package-graph:generate
composer package-graph:validate
```

## Core Rule

Package graph answers:

```text
How are packages connected to each other?
```

Feature graph answers:

```text
Which packages must adopt one platform feature, contract or cross-cutting mechanism?
```

Do not rely only on package graph when auditing a package that touches shared mechanisms such as operation runtime, cache, access query scope, audit events, licensing capabilities, search indexing, storage profiles or SitePack import/export.

## Audit Rule

When the user asks to check a package against Larena standards, include feature graph evidence:

1. Find feature entries where `adoption.package` equals the package under review.
2. Check `role`, `status`, `required`, `operations` and `next`.
3. Treat `needs_design`, `needs_mapping` and `partially_described` as active gaps unless explicitly deferred.
4. Do not mark a package as implementation-ready if a required critical feature adoption is still unresolved.

## Implementation Rule

When designing a new package TZ or updating an existing package TZ:

- add package obligations to existing feature graph entries;
- create a new feature graph entry only for real cross-package mechanisms;
- keep low-level package internals out of feature graph;
- regenerate `feature-graph/generated/*`;
- run `composer feature-graph:validate`.

Feature graph is a planning and consistency layer, not a replacement for package-local `module.yaml`, `api.yaml`, `access.yaml`, `audit.yaml`, `capabilities.yaml` or package TZ documents.
