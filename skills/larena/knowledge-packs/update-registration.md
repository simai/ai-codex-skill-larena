# Update And Registration

## Roles

- `larena-update`: update server.
- `larena-upserv`: alias/historical naming for update server.
- `larena-update-registration`: closed-contour registration/licensing server.

## Current Bitrix Flow

1. User runs update-server install script, e.g. `update.simai.ru/install`.
2. Script installs the Bitrix update module.
3. User installs modules/updates through that update module.
4. Update server checks entitlement through registration server when required.

## Target Larena Flow

Larena should later get the same class of flow:

1. ordinary user installs Larena/update client with minimal friction;
2. update client connects to update server;
3. update server delivers packages/products/updates by channel/version/license;
4. registration server remains private and answers entitlement checks only to update server.

Until then, `simai/larena` is the bootstrap repository.

## Install/Update Script Rules

Historical direction from developer chat:

- strict `install.php` and `update.php` package script names are preferred if script files are used;
- do not search arbitrary trees for install/update scripts;
- do not expose direct archive/file paths;
- upload/temp storage must be non-executable;
- clean temporary files;
- use file identifiers so future object/S3 storage is possible;
- provide developer templates/examples;
- support multilingual product/update names.

## Archive Integrity Diagnostics

When a Bitrix or Larena update client reports an API failure while reading the product/update feed, and the update server logs point to archive generation, diagnose the storage chain before changing client code:

1. identify the failing package, channel and version from the update API response, server log or generated archive path;
2. inspect the distribution/archive row, its linked file row and the physical storage object in one chain;
3. check generated aggregate cache files separately from source archive files;
4. save a row snapshot before any data-fix;
5. prefer restoring the missing file/object; use a narrow rebind to an existing matching archive only after explicit approval and after checking package, version, type, channel, size/hash or other available evidence;
6. verify the update API, client admin page/render and fresh server logs after the fix;
7. record the finding and residual hardening task in project docs.

The update server must fail controlled with JSON when an archive source is missing. Do not patch vendor/runtime code directly on production as a substitute for a proper deployment.

## Product Segmentation

Core/minimum CMS should be free/open. Paid products and solution layers should be delivered through update/product infrastructure later. Exact free-core key policy remains product/marketing decision.

Docara is currently treated as a paid product direction with a free documentation runtime/viewer layer. Do not classify the whole Docara surface as free merely because `docara-core` exists; keep professional editing, governance, revisions, import/sync, SitePack workflows, AI-assisted documentation, advanced search/branding, support and commercial updates in paid Docara Admin/Pro unless product strategy later changes.

## Monetization And Channel Rules

Do not make the update server a purely paid feature. Larena adoption depends on a safe, simple update path for free users too.

Working rules:

- Community/Core can use the update server.
- Core, security and bugfix updates should be free.
- Official baseline modules can be free when they define the minimum useful platform.
- Commercial modules, industry packs, Pro tools, LTS channels, enterprise rollout controls and support-backed updates are license/subscription value.
- A subscription ending should not break an already running site; it should stop access to commercial updates/support/paid channels according to policy.
- Admin update UI should show available updates and clearly explain which packages or channels require a license.
- License/entitlement state should control visible packages and channels, while the registration server remains closed and is queried only by the update server.

Before the update/registration servers are production-ready, enforce paid/free boundaries primarily through package access:

- free packages are public or included in the free install preset;
- paid packages are private Composer packages, private GitHub repositories or delivered archives;
- offline signed license files can be used as secondary local checks, but should not be the only boundary if the paid code is already shipped;
- expired paid subscriptions should normally stop paid updates/support/channels rather than break already running customer content.

Candidate feeds/channels:

- public core feed;
- commercial feed;
- enterprise/LTS feed;
- stable channel;
- beta/dev channel;
- staged rollout/test channel for Enterprise.
