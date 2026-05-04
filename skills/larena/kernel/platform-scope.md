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

- `larena-update`: update server.
- `larena-upserv`: alias or historical naming for update server.
- `larena-update-registration`: closed registration/licensing server.

Registration server is not a public surface; update server is the public/controlled gateway.

## SitePack

SitePack is platform-neutral data transport. Larena should use an adapter/package for import/export, not change the core standard for Larena-only needs.

## SF5 And Bitrix Alignment

Larena should preserve shared concepts with Bitrix/SF5 where useful, but implementation remains Laravel-native.
