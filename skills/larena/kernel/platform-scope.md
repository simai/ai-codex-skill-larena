# Platform Scope

## Entry App

`simai/larena` is the user-facing bootstrap repository. It must support a practical install path before update-server bootstrap exists.

Allowed work:

- Laravel app install/readiness diagnostics;
- root `composer.json`, docs and env examples;
- install instructions and health checks;
- package graph verification;
- smoke and runtime checks.

## Larena Packages

`larena/*` Composer packages implement CMS/platform capabilities.

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

## Update And Registration

- `larena-update`: update server.
- `larena-upserv`: alias or historical naming for update server.
- `larena-update-registration`: closed registration/licensing server.

Registration server is not a public surface; update server is the public/controlled gateway.

## SitePack

SitePack is platform-neutral data transport. Larena should use an adapter/package for import/export, not change the core standard for Larena-only needs.

## SF5 And Bitrix Alignment

Larena should preserve shared concepts with Bitrix/SF5 where useful, but implementation remains Laravel-native.
