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

## Update Domain Boundary

Keep platform/runtime domains explicit:

- `update.simai.ru` is the current update server for Bitrix products and legacy Bitrix update-client flows.
- `update.simai.io` is the planned global Larena/update platform hub and interface for partners/developers.
- `ru.update.simai.io` is the planned Russia legal/commercial segment update server for Larena distribution.

Shared update-platform code and standards are allowed, but do not mix these domains in docs, clients, rollout plans or smoke evidence. Larena clients should not default to `update.simai.ru`, and Bitrix legacy aggregate API behavior must not become the target Larena update flow. Segment endpoints should be based on legal/commercial operating segments, not necessarily one endpoint per country.

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

Legacy Bitrix `/api/v1/update` is a cold-cache risk because it can synchronously build large aggregate zip files on the first request. During rollout/testing, distinguish:

- PHP/server failure: `502`, PHP-FPM child timeout or `max_execution_time` kill;
- client timeout: `499` from nginx while the update server may still be warming aggregate archives;
- warmed-cache success: repeat request returns `200` quickly and the update admin pages load.

Do not treat a single admin page HTTP `200` as full update-flow proof when nginx shows `502`/`499` for `/api/v1/update`. Check update-server access/error logs and PHP-FPM logs, then repeat after cache warm-up or run the dedicated prewarm command when available. The target hardening direction is a packaged prewarm/background/cache-observability flow, not relying on an operator to warm archives manually.

For `larena/update` versions that include the API v1 aggregate prewarm command, use it before broad Bitrix update checks or releases:

```bash
sudo -u simai php artisan simai:update:api-v1-aggregate-prewarm --version-type=release --strict
```

The latest JSON report defaults to `storage/app/upserv/monitoring/api-v1-aggregate-prewarm-latest.json`. A clean warmed-cache report should have `failed_count=0` and `missing_source_count=0`; after a full prewarm, a repeat run should mostly report aggregates as `existing`.

Do not compute checksums for every large generated archive synchronously inside the update feed request. Either precompute/cache archive checksums out of the request path, or emit checksums only below a configured size threshold and treat checksum fields as optional for large archives. Always keep `size` available for disk/preflight checks.

Signed manifest rollout for the current legacy Bitrix v1 client must stay in `diagnostic` until artifact semantics are aligned. Legacy `/api/v1/update` returns generated aggregate zip files, so the signed manifest must include `entity_type=aggregate` artifacts with `compatibility=bitrix-api-v1`, exact `size` and 64-character SHA-256 for the aggregate zip actually downloaded by the client. The Bitrix verifier should prefer those aggregate artifacts for legacy v1 downloads and only fall back to module/source artifacts for future artifact-level flows. Do not enable Bitrix `SIGNED_MANIFEST_MODE=enforce` for this flow until aggregate artifacts are present and diagnostic verification passes on the real client flow, or until the Bitrix client moves to a v2 artifact-level download contract.

Aggregate manifest artifacts must be sourced from a prewarmed/cache report, not by building or hashing large zips inside public `GET /api/v2/manifest`. For `larena/update`, the practical sequence is:

```bash
sudo -u simai php artisan simai:update:api-v1-aggregate-prewarm --version-type=release --strict
sudo -u simai php artisan simai:update:manifest:generate --channel=public-core --path=upserv/manifests/public-core.json --strict
```

The prewarm report must have `failed_count=0`, `missing_source_count=0`, and non-empty SHA-256 checksums for included aggregate artifacts before any client-side enforcement.

When enabling Bitrix client diagnostic mode on a test stand, do not leave `ENABLE_LOGS=Y` unless the page rendering is being specifically debugged: the current `simai_update.php` verbose tab can dump the full update context and exhaust memory on large feeds.

Archive corruption tests must cover nested archives, not only the top-level aggregate zip. A valid aggregate zip can still contain a corrupt `<version>.zip`; update clients should fail the download/unpack step controlled, preserve the detailed error in operation state, and avoid printing duplicate concatenated `ERR_...` responses.

For `larena/update` runtime maintenance, prefer the packaged read-only command before ad-hoc tinker snippets. Use canonical command names when available; legacy `upserv` command names may still work for backward compatibility:

```bash
sudo -u simai php artisan simai:update:distribution-files:audit --json --include-orphans
sudo -u simai php artisan simai:update:distribution-files:audit --strict
```

The command audits `sf_distribution_files.file -> sf_file.id -> sf_file.url -> storage/app/<url>`, reports missing file rows/URLs/physical archives, size mismatches and linked deleted files. `--strict` must fail non-zero when real defects are present, so it is suitable for monitoring. Treat orphan `sf_file` rows as a separate storage-policy signal, not an automatic release blocker.

## Archive Integrity Baseline

Stored distribution archives in `larena/update` must have a first-class integrity baseline on `sf_distribution_files`:

- `archive_size_bytes`;
- `archive_sha256`;
- `archive_integrity_status`;
- `archive_integrity_checked_at`;
- `archive_integrity_error`.

`sf_file.hash` is still an MD5-level filesystem deduplication field and must not be treated as the update artifact trust baseline.

Capture or refresh the baseline whenever a distribution archive file is assigned:

1. module archive upload;
2. chunked upload;
3. admin archive replacement;
4. final processed output from `SimaiArchiveQueue`.

For existing servers, run migrations first, then:

```bash
sudo -u simai php artisan simai:update:distribution-files:integrity-backfill --only-missing
sudo -u simai php artisan simai:update:distribution-files:audit --strict
```

Legacy aliases may remain available:

```bash
sudo -u simai php artisan simai:upserv:distribution-files:integrity-backfill --only-missing
sudo -u simai php artisan simai:upserv:distribution-files:audit --strict
```

Strict audit must fail when integrity columns are missing, a ready baseline is missing, or `archive_size_bytes` / `archive_sha256` differ from the physical archive.

## Product Segmentation

Core/minimum CMS should be free/open. Paid products and solution layers should be delivered through update/product infrastructure later. Exact free-core key policy remains product/marketing decision.

Docara is currently treated as a paid product direction with a free documentation runtime/viewer layer. Do not classify the whole Docara surface as free merely because `docara-core` exists; keep professional editing, governance, revisions, import/sync, SitePack workflows, AI-assisted documentation, advanced search/branding, support and commercial updates in paid Docara Admin/Pro unless product strategy later changes.

## Licensing Platform Direction

Use `larena/licensing` as the canonical local runtime package name for Larena licensing. Treat licensing as a capability/entitlement platform, not as scattered package-local `pro` flags.

Canonical project docs live in `simai/larena`:

- `docs/developer/licensing/README.md`;
- `docs/developer/licensing/licensing-platform-tz.md`;
- `docs/developer/licensing/capability-contract.md`;
- `docs/developer/licensing/entitlement-lifecycle.md`;
- `docs/developer/licensing/trial-entitlements-and-abuse-prevention.md`;
- `docs/developer/licensing/package-and-bundle-licensing.md`;
- `docs/developer/licensing/admin-licensing-ux.md`.

Core rules:

- packages declare capabilities in package contracts and ask `CapabilityGate`; they must not implement independent licensing checks;
- capability availability is not an access grant;
- trial is a separate entitlement mode, not a temporary free license;
- ordinary trial denies export, bulk export, API export and SitePack export by default;
- development mode is explicit and never bypasses commercial/trial restrictions;
- local development may use mocks, demo data, UI preview, contract tests and demonstrators, but not real paid cloud resources or production usage without entitlement;
- paid/subscription expiration must be policy-based through `ExpirationPolicy`, not globally hardcoded;
- customer sites use signed entitlement snapshots from `larena/update`; they must not call `larena-update-registration` directly.

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
2. required `archive_size_bytes` and `archive_sha256` baseline for stored distribution archives;
3. signed update manifest with package name, version, channel, size, checksum and metadata;
4. later full artifact signing and release transparency/audit.

Signed manifests are the target architecture. Use Ed25519-style public verification for customer-facing manifests; do not use HMAC for client manifest verification because customers must not receive signing secrets.

A manifest artifact is eligible only when the distribution row has `archive_integrity_status=ready`, non-empty `archive_size_bytes` and a 64-character lowercase SHA-256. Clients must verify the manifest signature first, then downloaded archive size and SHA-256 before installation.

Current implementation baseline:

- `larena/update` exposes `GET /api/v2/manifest`.
- `larena/update` provides `simai:update:manifest:generate` and legacy `simai:upserv:manifest:generate`.
- `larena/update` provides `simai:update:manifest:keygen` and legacy `simai:upserv:manifest:keygen` for Ed25519 keypair generation; the command prints secrets for operator placement, but never stores them in git.
- Key-generation dotenv output uses `--dotenv`, not `--env`; Laravel reserves `--env` as a global environment option and package commands must not reuse it.
- Manifest signing is config-gated with `UPSERV_SIGNED_MANIFEST_ENABLED`, `UPSERV_SIGNED_MANIFEST_KEY_ID`, `UPSERV_SIGNED_MANIFEST_PRIVATE_KEY_BASE64` and optional public key config.
- Unsigned diagnostic generation is allowed only through explicit `--allow-unsigned` command mode.
- Private Ed25519 keys belong only in the update-server `.env`/secret store. Rotate by publishing the new public key to clients before switching server `key_id`; keep old public keys for the rollback/update window.
- Bitrix update module has reusable `SIMAI\Main\Update\Manifest\ManifestVerifier`, feature-flagged `SIMAI\Main\Update\Manifest\ManifestClient`, and `scripts/smoke_manifest_verifier.php`.
- Bitrix `SIGNED_MANIFEST_MODE` must default to `off`; use `diagnostic` first to log manifest/signature/archive mismatches without blocking, then `enforce` to block installation before unpacking when verification fails.

For the next architecture batch, run production update-server migration/backfill/audit, configure signed-manifest keys with server signing disabled, smoke `public-core`, enable `UPSERV_SIGNED_MANIFEST_ENABLED=true`, and only then move Bitrix clients from `diagnostic` to `enforce`.

## Service Auth Contract

Use HMAC-SHA256 signed internal requests for `larena/update` -> `larena-update-registration`.

Headers:

- `X-Larena-Service`
- `X-Larena-Timestamp`
- `X-Larena-Nonce`
- `X-Larena-Signature`

Signature format:

```text
X-Larena-Signature: v1=<hex-hmac-sha256>
```

Signed payload is newline-joined:

```text
v1
service_id
unix_timestamp
nonce
HTTP_METHOD
path_with_query
sha256(raw_body)
```

Default policy:

- service id: `larena-update`;
- clock skew: 300 seconds;
- replay protection: cache-backed nonce claim for at least 600 seconds;
- update-side env: `UPSERV_REGISTRATION_SERVICE_AUTH_ENABLED`, `UPSERV_REGISTRATION_SERVICE_ID`, `UPSERV_REGISTRATION_SERVICE_SECRET`;
- registration-side env: `REGISTRATION_SERVICE_AUTH_ENABLED`, `REGISTRATION_SERVICE_AUTH_UPDATE_ID`, `REGISTRATION_SERVICE_AUTH_UPDATE_SECRET`, `REGISTRATION_SERVICE_AUTH_UPDATE_PREVIOUS_SECRET`, `REGISTRATION_SERVICE_AUTH_ALLOWED_SKEW_SECONDS`, `REGISTRATION_SERVICE_AUTH_REPLAY_CACHE_TTL_SECONDS`.

Safe rollout for already-running servers:

1. deploy both code changes with enforcement disabled;
2. configure the same long random secret on update and registration;
3. enable update-side signing first;
4. verify existing entitlement/coupon/license calls still work;
5. enable registration-side enforcement;
6. verify unsigned direct registration calls return `401`;
7. rollback by disabling registration-side enforcement first.

Do not replace this with a public static token in query params or body. Do not expose registration directly to customer sites even when service-auth exists.

For secret rotation, temporarily configure registration with the new secret as current and the old secret as `REGISTRATION_SERVICE_AUTH_UPDATE_PREVIOUS_SECRET`, switch the update server to the new secret, verify signed calls, then remove the previous secret.

## Entitlement Response Redaction

`larena/update` is the public-facing boundary and must redact registration-derived entitlement responses before returning them to customer sites, portals or public clients.

Default update-side env:

```text
UPSERV_REGISTRATION_REDACT_ENTITLEMENT_RESPONSES=true
UPSERV_REGISTRATION_REDACT_KEYS=key,coupon_key,hash,license_hash,activation_token,key_cipher,key_fingerprint,key_mask,key_last4,contact,log,logs,c_name,c_second_name,c_company_name,c_phone,c_email,email,phone
```

Redaction should replace sensitive values with `[REDACTED]` while preserving product/update metadata needed for decisions: package technical names, package names, statuses, date ranges, operation metadata, secure archive links, archive size and checksum.

Apply redaction at the update-server API boundary even if registration later gains safer resources, because registration is an internal service and update is the layer exposed to clients.

Do not return raw registration `LicenseResource`, `CouponResource`, customer contact fields, activation tokens, key hashes, key ciphers or raw logs from public/portal update APIs.

## Service Auth Audit And Rate Limits

Registration service-auth should also bound trusted internal traffic:

- `REGISTRATION_SERVICE_AUTH_RATE_LIMIT_ENABLED=true`
- `REGISTRATION_SERVICE_AUTH_READ_PER_MINUTE=240`
- `REGISTRATION_SERVICE_AUTH_MUTATION_PER_MINUTE=120`
- `REGISTRATION_SERVICE_AUTH_AUDIT_ENABLED=true`
- `REGISTRATION_SERVICE_AUTH_AUDIT_SUCCESS_READS=false`
- `REGISTRATION_SERVICE_AUTH_AUDIT_SUCCESS_MUTATIONS=true`

Failures, bad signatures, replay attempts and rate-limit blocks should be logged as warnings without secrets. Successful mutations should be logged as info. Successful reads should be opt-in to avoid log noise. This log audit is the first boundary and does not replace later DB-backed entitlement audit events. Prefer routing these records through the future `audit.yaml` event contract with recommended sinks/channels such as `larena.update` or `larena.licensing`, instead of package-local ad hoc log files.

## Signed Manifest Runtime Publishing

When publishing Bitrix-compatible update artifacts from `larena/update`, remember that legacy Bitrix `/api/v1/update` downloads aggregate ZIP files, not only source `sf_distribution_files` archives.

Required publishing rules:

- source archives must live under the path resolved by `storage_path('app/'.sf_file.url)`;
- private file URLs like `private/<module>/<token>/<version>.zip` must physically exist under `storage/app/private/...`;
- `sf_distribution_files.archive_integrity_status` must be `ready`, not `verified`;
- `archive_size_bytes` and `archive_sha256` must match the physical archive;
- run `simai:update:distribution-files:audit --strict` before manifest generation;
- run a full `simai:update:api-v1-aggregate-prewarm --version-type=release --strict --json` before generating a production manifest, because module-only prewarm can leave an incomplete latest monitoring report;
- generate the signed manifest only after prewarm: `simai:update:manifest:generate --channel=public-core --path=upserv/manifests/public-core.json --strict`.

For Bitrix diagnostic rollout, a real legacy download is accepted only when client logs include:

- `status=verified`;
- `artifact_entity_type=aggregate`;
- `artifact_compatibility=bitrix-api-v1`.

Do not enable `SIGNED_MANIFEST_MODE=enforce` for legacy Bitrix clients until aggregate artifacts are present in the signed manifest and the diagnostic period has no mismatch/failure signals.

## Artifact-Level Update API V2 Direction

The SIMAI update system is a universal update platform. Larena is one client/adapter of this platform, not the only reason the platform exists.

Larena update client should be v2-first and artifact-level from the beginning. Do not design new Larena update flows around legacy aggregate ZIPs.

Strategic flow:

```text
preview -> plan -> operation -> per-step download token -> artifact verification -> step execution -> resume/rollback
```

Reasons:

- every downloaded artifact is independently verified by size, SHA-256 and signature metadata;
- server resolves dependencies, channel, edition, entitlement and route into a clear machine-readable plan;
- client can resume from the last safe step instead of restarting an opaque aggregate ZIP;
- diagnostics point to an exact package/version/step;
- update server does not need to build many source-version to target-version aggregate combinations;
- AI agents can inspect plans and capabilities safely without arbitrary download or install behavior.

Legacy aggregate artifacts remain a compatibility adapter for existing Bitrix `/api/v1/update` clients only. They should be secured, prewarmed and monitored, but not treated as the target architecture for Larena.

Universal concepts should remain platform-neutral:

- products;
- packages;
- releases;
- artifacts;
- channels;
- manifests/signatures;
- entitlement;
- plans;
- operations;
- steps;
- audit and monitoring.

Platform-specific behavior belongs to adapters such as `bitrix-module`, `larena-package`, `sitepack` and `docara-product`.

Canonical docs live in `/Users/rim/Documents/GitHub/larena-update-docs`, especially:

- `docs/architecture/universal-update-platform.md`;
- `docs/roadmap/artifact-level-v2-update-flow.md`.

In the Larena architecture repository, the current canonical Update Platform v2 docs live in `/Users/rim/Documents/GitHub/larena/docs/developer/update/`:

- `update-platform-v2-architecture.md`;
- `update-platform-v2-domain-model.md`;
- `update-api-v2-contract.md`;
- `update-package-manifest-contract.md`;
- `update-client-engine-contract.md`;
- `core-update-client-boundary-decision.md`;
- `release-pipeline-signing-contract.md`;
- `update-server-catalog-data-model-contract.md`;
- `update-operator-admin-ux-contract.md`;
- `private-registration-api-hardening-contract.md`;
- `update-platform-v2-integration-review.md`;
- `larena-update-package-tz.md`.

Related canonical docs outside the update folder:

- `/Users/rim/Documents/GitHub/larena/docs/developer/audit/audit-implementation-baseline.md`.

Use `larena-update-package-tz.md` as the package-level audit baseline for the `larena-update` repository. The package role is update server/catalog/API/delivery/entitlement-proxy/operator UX; it must not become the registration source of truth, local update executor, package source repository, or signing-key runtime.

Use `larena-update-registration-package-tz.md` as the package-level audit baseline for `larena-update-registration`. Treat it as the private registration/entitlement authority: customers, licenses, subscriptions, trials, coupons, site/installation bindings, entitlement decisions, signed entitlement snapshots, revocations, service-auth, redaction and regional/legal segment policy. It must not expose public client-site APIs, deliver artifacts, build update plans, or leak raw customer/license/coupon/payment data through `larena/update`.

Use `update-client-engine-contract.md` as the baseline for Larena-side installation/update execution. The local client must be shared-hosting-safe, v2-first and fail-closed: it requests preview/plan/operation from update server, downloads only step-authorized artifacts, verifies size/SHA-256/signature/trust/compatibility locally, executes only declared handlers, stores resumable operation state, creates backups for risky steps, reports redacted status, and never calls registration server directly.

Use `core-update-client-boundary-decision.md` to keep `larena/core` thin. Core owns platform truth, package registry, dependency graph, compatibility matrix, doctor, managed/protected area policy and update preflight. Future `larena/update-client` owns API v2 client, local operation store, artifact download/verification, trust-store maintenance, backup/recovery, step execution and reporting. Do not merge update execution into core.

Use `release-pipeline-signing-contract.md` as the baseline for source-to-artifact publication. The release pipeline must build from fixed clean source identity, validate package/manifests, generate immutable artifact metadata, require size/SHA-256/detached signatures, keep private signing keys outside normal update-server runtime, publish only after gates pass, and support normal lifecycle operations: publish, withdraw and revoke.

Use `update-server-catalog-data-model-contract.md` as the baseline for update server catalog ownership. `larena/update` may own product/package/bundle/release/artifact/channel/route/plan/mirror/server-operation catalog data and redacted entitlement references, but raw customers, licenses, subscriptions, trials, coupons and site-binding truth stay in `larena-update-registration`; local execution state stays in the update client.

Use `update-operator-admin-ux-contract.md` as the baseline for update-server operator interfaces. Admin surfaces should be table-first, explainable and audit-safe: show catalog hierarchy, lifecycle state, publish gates, artifact trust, rollout, mirrors, operation reports, redacted entitlement decisions and diagnostics; separate routine actions from destructive publish/withdraw/revoke/rollout/key actions; never expose raw secrets, private signing keys, raw tokens or raw registration/customer data.

Use `private-registration-api-hardening-contract.md` as the baseline for closed-contour update-to-registration calls. Private registration endpoints must use service-auth, scoped service identity, replay protection, idempotency for mutations, DTO-only responses, redaction at registration and update-server boundaries, signed entitlement snapshots, controlled errors, rate limits and audit. Customer sites, AI tools and partner packages must never call registration directly.

Use `update-platform-v2-integration-review.md` as the current cross-package consistency verdict. Treat the update/registration TZ layer as approved for documentation-phase review, not as permission to implement. Before coding, prepare gap analysis against the contracts and keep unresolved decisions such as update-client/core split, table names, signing-service implementation, audit baseline, admin framework details, region/legal policy and legacy Bitrix v1 aggregate policy out of implementation until accepted.

Use `audit-implementation-baseline.md` before designing runtime update/registration/licensing/admin logs. Update/registration flows must emit common `AuditEvent` records through the audit baseline or a compatible temporary adapter; do not create package-local security/action log systems, do not store raw entitlement/customer/license/coupon payloads, and keep `correlation_id` across update-server and registration calls when possible.

## Multi-Region Update Distribution

Treat regional delivery as an update-platform concern, not as a package-local licensing check.

Canonical Larena project doc:

- `/Users/rim/Documents/GitHub/larena/docs/developer/update/multi-region-distribution-rfc.md`.

Core rule:

```text
Build once, sign once, distribute many times, entitle regionally.
```

Separate these layers:

- global artifact registry: package identity, versions, artifacts, size/SHA-256, signed manifests, compatibility, channels and capability metadata without customer PII;
- regional entitlement authority: customer, license, trial, subscription, legal entity, billing provider and entitlement truth for a region;
- artifact mirrors: regional/global file delivery without license decisions and without customer PII;
- local client runtime: verifies signed entitlement snapshot, manifest, artifact size and SHA-256.

Do not design one global customer/license/PII database by default. Do not duplicate package builds per region unless the artifact content itself is region-specific. Artifact mirrors must not decide whether a customer has rights; they only deliver signed artifacts allowed by update plans.

Region selection must be explicit and explainable. Prefer license/entitlement region, customer-selected activation region, legal entity/billing region and admin-configured update endpoint. Treat IP geolocation only as a diagnostic hint, not as the source of truth.

For future signed entitlement snapshots and update plans, include regional diagnostics such as `region`, `legal_entity`, `billing_provider`, `entitlement_authority`, allowed mirrors, allowed channels and data-residency policy. Keep registration private:

```text
Customer site -> regional update endpoint -> regional registration/entitlement authority
```

When discussing laws or regional data residency, state that architecture must be legal-review ready but is not itself a legal opinion.
