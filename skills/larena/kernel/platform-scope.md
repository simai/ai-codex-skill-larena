# Platform Scope

## Entry App

`simai/larena` is the user-facing bootstrap/distribution entry repository for the free starter set. It must support a practical install path before update-server bootstrap exists.

Do not treat `simai/larena` as the full platform implementation or as the package source of truth. It connects official packages, provides install/readiness tooling and documents the starting path.

Allowed work:

- Laravel app install/readiness diagnostics;
- root `composer.json`, docs and env examples;
- install instructions and health checks;
- package graph verification;
- smoke and runtime checks.

## Larena Packages

`larena-*` repositories / `larena/*` Composer packages implement CMS/platform capabilities and are the primary source of platform code.

Expected surfaces:

- service provider;
- routes;
- config;
- migrations;
- commands;
- language files;
- tests;
- `module.yaml`;
- package README/SPEC/CHANGELOG when present.

## Development Workspace

A monorepo/workspace may exist for technical cross-package development, local path repositories and combined QA. It is development-only and must not replace the customer-facing bootstrap/update-server distribution model.

## Update And Registration

- `larena-update`: canonical update server.
- `larena-upserv`: legacy alias/historical naming for update server. New Composer/manifests/docs should use `larena/update`; keep `larena/upserv` only as compatibility alias where needed.
- `larena-update-registration`: closed registration/licensing server.

Registration server is not a public surface; update server is the public/controlled gateway.

## SitePack

SitePack is platform-neutral data transport. Larena should use an adapter/package for import/export, not change the core standard for Larena-only needs.

## Larena And Migration References

Larena is the canonical product/platform identity for backend packages, access, settings, props, storage, REST, admin and update flows.

SIMAI Framework (formerly "SF5") is the frontend/UI layer owned by `$framework`; Larena consumes it through `larena/ui` and the component package `larena`. Do not name new Larena backend contracts after the framework.

Bitrix and older SIMAI implementations may provide migration references and adapter targets. They should not define Larena's package identity, runtime architecture or public product naming.

## Docara

Docara (`larena/docara`) is the likely first product-level proof that Larena is
a usable CMS platform. On 2026-10-23 it is workspace-only (not in the Root
assembly); check [../references/canonical-package-portfolio.md](../references/canonical-package-portfolio.md)
before claiming it runs in the entry app.

## SIMAI Framework Layer DNA

Preserve the meaning of the SIMAI Framework `/simai` and `/simai.data` system-library and
overlay layers, but implement it through Laravel-native package resources,
storage, database registries and adapters. Cross-platform mapping:
[../knowledge/simai-layer-dna.md](../knowledge/simai-layer-dna.md).
