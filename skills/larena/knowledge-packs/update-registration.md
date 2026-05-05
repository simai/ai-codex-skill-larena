# Update And Registration

## Roles

- `larena-update`: canonical update server.
- `larena-upserv`: historical/legacy naming for update server. Do not use `larena-upserv` for new package identity, docs or Composer requirements. Keep `larena/upserv` only as a Composer `replace` alias when maintaining backward compatibility. The canonical Composer package should be `larena/update`.
- `larena-update-registration`: closed-contour registration/licensing server.

## Registration Server Boundary

`larena/update-registration` is a standalone internal Laravel application, not a customer-installable Larena package.

The accepted request chain is:

```text
Customer site -> larena/update -> larena/update-registration
```

Do not design new customer-site, package-installer, public-user or AI-agent flows that call registration directly. Registration is the private entitlement backend behind the update server.

Before expanding entitlement/licensing flows, require:

- service-to-service authentication from `larena/update` to registration;
- private network/IP or equivalent deployment boundary;
- redacted update-server-facing response DTOs;
- audit events for license/coupon/key lookup, mutation and migration;
- rate limits and replay protection;
- Key V2 rollout, rollback and legacy fallback retirement notes.

Current registration code still has legacy API routes and an authorization TODO in `routes/api.php`; treat direct public exposure as forbidden until the hardening batch is implemented and verified.

Key V2 direction is valid: keep public key format stable while storing fingerprint, cipher, mask, last4, version and migration timestamp. Use dry-run migration before writes and do not commit real keys, coupon values, ciphers, raw responses or customer data.

## Canonical Alias Migration Rule

Do not mass-rename legacy update-server internals in one patch. Use alias-first migration:

- Composer requirements, new docs and new install instructions must use `larena/update`.
- New commands should prefer the canonical `simai:update:*` and `simai:install-update` names.
- New config publishing may use `simai_update`, while keeping `simai_upserv` as the old implementation config.
- Keep `Simai\Upserv`, `simai_upserv`, `UPSERV_*`, `upserv.*`, legacy DB tables and `simai:upserv:*` as a backward-compatible implementation layer until major-safe migrations exist.
- New source can add `Simai\Update\...` wrappers, provider aliases and command aliases that delegate to the old implementation.
- Rename tables, permissions, env keys or URL contracts only with explicit migration, aliases, rollback notes and runtime verification.
- User-facing documentation must lead with `larena/update`, `config/simai_update.php`, `simai:install-update` and `simai:update:*`. Legacy `upserv` directory names, wrapper filenames, env keys, table names and commands may remain visible only when they are explicitly labeled as compatibility or historical runtime evidence.

This avoids breaking existing update-server installs while making `larena/update` the visible product contract.

Current safe alias documentation baseline is complete when the update repo contains:

- `docs/developer/alias-contract.md`;
- `docs/developer/concept-alignment.md`;
- `docs/developer/smoke.md`;
- canonical `larena/update` identity in `SPEC.md`;
- `module.yaml.concept_alignment` and update-server operational risks.

After this baseline, do not keep spending effort on cosmetic `upserv` naming cleanup. The next meaningful work is functional architecture/hardening: registration service-auth, signed artifact trust, channel/licensing policy, response redaction, audit/rate limits, and only then major-safe legacy migration planning.

## Repository/Runtime Source Of Truth

Before changing update or registration servers, reconcile production runtime with repositories:

- update server package changes go to `larena-update`;
- registration/licensing changes go to `larena-update-registration`;
- Bitrix update-client changes go to the Bitrix module repository, for example `bx-simai.update`;
- legacy/scratch repositories must not receive production-only fixes.

For the update server, the Laravel app may not be a root git checkout. Verify the package source through Composer:

```bash
cd /home/simai/www/update.simai.ru
sudo -u simai composer show larena/update
```

Record the package version, source URL and source reference before deploy and after deploy. Production code changes are not complete until the matching source repository has a commit/tag and the runtime package reference points to it.

For the registration server, verify the app checkout itself:

```bash
cd /home/simai/www/reg-internal.local
sudo -u simai git status --short --branch
sudo -u simai git log --oneline -5 --decorate
```

Treat production database fixes, uploaded release artifacts and temporary fixtures as operational changes: save snapshots, record IDs/files, verify cleanup, and decide whether a permanent command, migration or monitor is needed. Do not confuse these data/runtime actions with source-code fixes.

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

Aggregate zip generation is successful only after the generated file exists and at least one source archive was actually added. Guard every `filemtime()`, size calculation and signed URL generation behind that check; missing source archives should be logged with distribution/file/storage context and returned as a controlled item/API diagnostic, not as a feed-wide HTML 500.

Do not compute checksums for every large generated archive synchronously inside the update feed request. Either precompute/cache archive checksums out of the request path, or emit checksums only below a configured size threshold and treat checksum fields as optional for large archives. Always keep `size` available for disk/preflight checks.

Archive corruption tests must cover nested archives, not only the top-level aggregate zip. A valid aggregate zip can still contain a corrupt `<version>.zip`; update clients should fail the download/unpack step controlled, preserve the detailed error in operation state, and avoid printing duplicate concatenated `ERR_...` responses.

For `larena/update` runtime maintenance, prefer the packaged read-only command before ad-hoc tinker snippets. Use canonical command names when available; legacy `upserv` command names may still work for backward compatibility:

```bash
sudo -u simai php artisan simai:update:distribution-files:audit --json --include-orphans
sudo -u simai php artisan simai:update:distribution-files:audit --strict
```

The command audits `sf_distribution_files.file -> sf_file.id -> sf_file.url -> storage/app/<url>`, reports missing file rows/URLs/physical archives, size mismatches and linked deleted files. `--strict` must fail non-zero when real defects are present, so it is suitable for monitoring. Treat orphan `sf_file` rows as a separate storage-policy signal, not an automatic release blocker.

## Product Segmentation

Core/minimum CMS should be free/open. Paid products and solution layers should be delivered through update/product infrastructure later. Exact free-core key policy remains product/marketing decision.

Docara is currently treated as a paid product direction with a free documentation runtime/viewer layer. Do not classify the whole Docara surface as free merely because `docara-core` exists; keep professional editing, governance, revisions, import/sync, SitePack workflows, AI-assisted documentation, advanced search/branding, support and commercial updates in paid Docara Admin/Pro unless product strategy later changes.

## Monetization And Channel Rules

Do not make the update server a purely paid feature. Larena adoption depends on a safe, simple update path for free users too.

Accepted channel baseline:

- `public-core`: free core, baseline packages, security fixes and bugfixes.
- `stable`: normal stable updates. Free packages remain available; paid packages require entitlement.
- `commercial`: paid products, Pro packages, industry packs and premium modules.
- `beta`: opt-in developer/test/early access channel.

Reserved future channels:

- `enterprise-lts`: paid long-term support and controlled enterprise version lines.
- `staged-rollout`: percent/cohort/tenant staged rollout.

Working rules:

- Community/Core can use the update server.
- Core, security and bugfix updates should be free.
- Official baseline modules can be free when they define the minimum useful platform.
- Commercial modules, industry packs, Pro tools, LTS channels, enterprise rollout controls and support-backed updates are license/subscription value.
- A subscription ending should not break an already running site; it should stop access to commercial updates/support/paid channels according to policy.
- Admin update UI should show available updates and clearly explain which packages or channels require a license.
- License/entitlement state should control visible packages and channels, while the registration server remains closed and is queried only by the update server.
- Expired paid subscription must not break a running site or already installed paid package.
- Expiration blocks commercial/Pro/Enterprise updates, paid support, LTS/enterprise channels, paid cloud/AI services and new premium package/template versions.
- Free core/security/bugfix updates remain available after paid subscription expiration.
- Admin UI should explain expiration clearly, e.g. "License expired. Renew to receive commercial updates."

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

## Artifact Trust Model

Update delivery should evolve in phases:

1. service-auth between `larena/update` and `larena-update-registration`;
2. `sha256`/checksum verification for archives;
3. signed update manifest with package name, version, channel, size, checksum and metadata;
4. later full artifact signing and release transparency/audit.

Signed manifests are the target architecture. They do not have to be the first implementation task, but update/package schemas should not block adding them later.

For the next architecture batch, prioritize service-auth and redacted entitlement responses before signed artifacts.
