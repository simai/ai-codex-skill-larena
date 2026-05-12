# Пакет `larena/access` (паспорт)

## Роль
- Единая модель прав доступа, middleware и operation-коды для пакетов Larena.
- `simai/access` допускается только как Composer compatibility alias.

## Текущий статус
- Completion level: `L4 ready for current package-completion baseline`.
- Каноническая ДНК: `simai/larena/docs/developer/dna/access-dna.md`.
- Пакетные документы: `docs/developer/dna/access-dna.md`, `docs/developer/access-dna-compliance.md`, `docs/developer/architecture.md`, `docs/developer/ai-contract.md`, `docs/developer/package-status.md`.
- Текущая реализация полезна как compatibility layer: access profiles, operations, operation values, user/group bindings, middleware, API keys.
- Первый explainable decision-layer реализован: `AccessValue`, `AccessContext`, `AccessDecision`, `AccessControl::decide()` и `AccessChecker::decide()`.
- Grants/context baseline реализован без миграций: `AccessActorType`, `AccessScope`, `AccessResource`, `AccessGrantTarget`, `AccessGrantTargetResolver`.
- Security/operations baseline реализован: `AccessTokenScope`, `AccessAuditEvent`, policy docs, negative tests for missing token and unsafe bypass config.
- L4 demonstrator baseline описан: decision explain, missing grant, group grant, token safety, installed admin/API smoke.
- Installed-site HTTP and visual browser smoke по `larena.test` прошёл для main admin access pages и `/admin/access-explain`. Browser Use в текущей сессии был недоступен, поэтому визуальный smoke выполнен через CLI Playwright fallback.
- Package-local `access:doctor` реализован и проверен на `larena.test`: 57 checks, 0 warnings после token-scope, rate-limit, durable-audit, scoped-grant, cache, SitePack, admin UX, access-pack policy, rollout policy, resolver catalog и explain-view baseline. Команда read-only, не выводит секреты и проверяет config, tables, token-scope/scoped-grant/audit storage, rate-limit profiles, cache/SitePack services, middleware, routes, contracts, admin CRUD configs и bypass-token safety.
- Token-scope storage baseline реализован: `sf_access_api_key.scopes`, `AccessTokenScopePolicy`, config-gated middleware enforcement через `ACCESS_TOKEN_SCOPE_ENFORCEMENT`. Enforcement выключен по умолчанию для совместимости.
- API-key scope assignment baseline реализован: `ApiKeyEntityConfig` exposes `scopes` as form/filter/writable CRUD metadata; generic CRUD stores masked `key` plus Laravel `hashed_key`, and runtime validation still accepts legacy SHA-256 hashes for compatibility.
- Audit dispatcher baseline реализован: `AccessAuditDispatcher` emits `AccessAuditRecorded` Laravel events for token middleware decisions; payload sanitation strips raw tokens, authorization headers, hashed keys, passwords and secrets.
- Durable audit sink baseline реализован: `sf_access_audit_log`, `AccessAuditLog`, `ACCESS_AUDIT_SINK=event|database|both|off`, `ACCESS_AUDIT_FAIL_OPEN=true|false`. Default sink remains `event` for compatibility; `database`/`both` writes sanitized payloads.
- Token rate-limit baseline реализован: `AccessRateLimitPolicy` wires `access.token` to Laravel `RateLimiter`, config-gated through `ACCESS_TOKEN_RATE_LIMITS_ENABLED`, with named profiles (`admin-default`, `admin-sensitive`, `api-sensitive`, `tool-sensitive`, `internal-service`). Limit exceeded returns `429 rate_limited` with `Retry-After` and emits sanitized `access.token.rate_limited`.
- Scoped grant storage baseline реализован через RFC 0001: `sf_access_grant`, `AccessGrant`, `AccessScopedGrantStore`, `AccessGrantResolverRegistry`, `ResolvedScopedGrant`, `ACCESS_SCOPED_GRANTS_ENABLED=false` by default. When enabled, `AccessControl::decide()` checks scoped grants before legacy user/group fallback and explains `details.grant.source=scoped_grant`.
- Access cache baseline реализован: `AccessCache` uses versioned cache keys for `hasAccess()` and `isUserInGroup()` compatibility helpers. Eloquent hooks invalidate cache versions on access profile, operation, user group, user and scoped grant save/delete. Direct SQL writes and low-level pivot-table changes still require explicit `AccessCache::invalidateAll()`, `invalidateUser()` or `invalidateGroup()`.
- Access SitePack baseline реализован: `AccessSitePackMapper` exports/imports operations (`larena.access.operations`), profiles (`larena.access.profiles`) and scoped grants (`larena.access.grants`) as config-KV. Imports are dry-run capable, `applyPolicy=manual`, and profiles bind operations by stable operation code instead of local database ids.
- Access-pack install policy реализован: `AccessPackPolicy` validates marketplace/update-server config-KV access packs, allows only known access namespaces, requires `applyPolicy=manual`, rejects raw secret/token payloads and keeps scoped grants under operator review.
- Rollout profile policy реализован: `AccessRolloutPolicy` and `php artisan access:rollout-policy` expose machine-readable rollout profiles for shared hosting, secure VPS, managed enterprise and read-only AI tools. Profiles define token-scope enforcement, rate limits, audit sink, scoped grants, external API exposure, backup need and required smoke gates.
- Installed-route API smoke реализован: `php artisan access:api-smoke --url=https://larena.test --json` creates disposable API-key data, checks missing-token `401`, checks authorized disposable request, verifies no `Set-Cookie` on API response, cleans up test data and never prints the raw token. Verified on `larena.test` after correcting the vhost document root to Laravel `public/`.
- Sessionless API-token smoke реализован: normal `access.token` API-key flow does not start a web session; bypass-token flow remains special/internal and requires explicit `ACCESS_BYPASS_USER_ID > 0`.
- Custom resolver smoke реализован: `AccessGrantResolverRegistry` can register package-defined resolvers for virtual targets such as `participant`.
- Virtual target resolver catalog реализован: `AccessVirtualTargetCatalog` and `php artisan access:resolver-catalog --json` list `owner`, `participant`, `editor`, `organization_member`; non-built-in targets require package-defined resolver registration and allow/deny smoke.
- Scoped grant admin UX baseline реализован: `/admin/access-grants`, `AccessGrantEntityConfig`, guarded CRUD/status actions via `access.view_grants`, `access.create_grants`, `access.edit_grants`, `access.delete_grants`. This is an operator baseline, not yet a production rollout wizard.
- Operator audit review baseline реализован: `/admin/access-audit-log`, `AccessAuditLogEntityConfig`, read-only CRUD over sanitized `sf_access_audit_log` rows via `access.view_audit_logs`.
- Operator explain-view реализован: `/admin/access-explain` is a read-only admin screen that lets an operator select user, operation, owner/resource/scope/package context and see `allowed/denied`, reason and audit-safe `AccessDecision::explain()` JSON.
- Visual smoke note: access pages render, but legacy update/upserv asset URLs under `/vendor/larena/upserv/public/...` return 404. Это не блокер `larena/access`, но должно уйти в update/upserv cleanup batch.
- До следующего уровня развития Larena Access остаются downstream package-specific resolver smoke for packages that introduce custom virtual targets, production operator approval notes for strict rollout profiles and optional richer resource-oriented explain UX. Legacy update/upserv asset 404 is a separate update/upserv cleanup task, not an access blocker.

## Ключевые точки
- Сервисы: `AccessChecker`, `AccessManagement`, `AccessControl`, `AccessTokenScopePolicy`, `AccessAuditDispatcher`, `AccessCache`, `AccessRateLimitPolicy`, `AccessScopedGrantStore`, `AccessSitePackMapper`, `AccessPackPolicy`, `AccessRolloutPolicy`, `AccessGrantResolverRegistry`, `AccessVirtualTargetCatalog`, `ApiKeyManager`.
- Events: `AccessAuditRecorded`.
- Durable audit model: `AccessAuditLog` over `sf_access_audit_log`.
- Scoped grant model: `AccessGrant` over `sf_access_grant`.
- Decision-layer: `AccessValue`, `AccessContext`, `AccessDecision`.
- Grants/context baseline: `AccessActorType`, `AccessScope`, `AccessResource`, `AccessGrantTarget`, `AccessGrantTargetResolver`.
- Security/operations baseline: `AccessTokenScope`, `AccessAuditEvent`.
- Middleware: `access`, `access.token`, `access.entity`.
- Контракт проверки entity-прав: `EntityAbilityChecker`.
- Admin CRUD configs: `AccessGrantEntityConfig`, `AccessAuditLogEntityConfig`.
- Runtime diagnostics: `php artisan access:doctor`, `php artisan access:doctor --json`, `php artisan access:resolver-catalog --json`, `php artisan access:rollout-policy`, `php artisan access:rollout-smoke`, `php artisan access:api-smoke`.
- Конфиг токенов/обходов: `config/auth_tokens.php`.
- Источник операций/уровней для модулей: `config/simai_<module>.php`.

## Инварианты
- Новые операции доступа объявляются в module config, не хардкодом.
- API-маршруты с токенами используют `access.token`.
- CRUD-проверки идут через `access.entity` + EntityConfig ability map.
- Каждый защищенный endpoint должен быть отражен в `Access Matrix`.
- Для новых модулей доступы должны подхватываться install-flow через `simai:install`.
- Новый функционал должен идти через Larena Access DNA, а не через SF5-брендинг.
- `hasAccess()` остается compatibility boolean API; новый код должен использовать `AccessChecker::decide()` там, где нужна объяснимость.
- Для нового кода `AccessContext` должен передавать actor type, package, resource, scope и source, если эти данные доступны.
- Bypass token не должен проходить без явного `ACCESS_BYPASS_USER_ID > 0`; bypass не является публичным API credential.

## Архитектурные правила интеграции
1. При добавлении нового модуля сначала опиши операции в `config/simai_<module>.php`.
2. Привяжи маршруты к `access.token`/`access.entity` на уровне routing, а не только в контроллере.
3. Для SimaiCrud действия должны иметь явный ability map в `EntityConfig`.
4. Любой bypass (service token/impersonation) должен быть задокументирован и покрыт тестами.
5. При изменении модели доступа обновляй `SPEC.md`, `CHANGELOG.md` и `Access Matrix`.

## Ближайший безопасный батч
1. Для downstream packages that introduce `participant`, `editor`, `organization_member` or another virtual target, require package-specific resolver smoke with allow and deny cases.
2. Add production operator approval notes when token scopes, rate limits or scoped grants are enabled on a real target.
3. Позже улучшить resource-oriented explain UX only if it is needed by real operator workflows.
4. Для update/upserv отдельно почистить legacy asset URLs, найденные visual smoke.

Не начинать с переименования `sf_access_*` таблиц. Scoped grants are additive and rollout-disabled by default; production enablement requires migration smoke, backup and rollback notes.

## Типовые риски
- Разнобой operation-кодов между конфигом и кодом.
- Утечки доступа из-за обхода middleware.
- Неправильная обработка bypass token и impersonation.
- API keys без назначенных scopes/enforcement/audit/rate-limit rollout дают слишком широкий контур для внешних клиентов и AI/MCP. Не включать broad MCP/REST/AI-write до назначения scopes, включения enforcement и smoke-проверки rate-limit профилей.
- Root/bypass policy без тестов может создать неявный супердоступ.

## Обязательные проверки
- Негативные тесты `401/403` для критичных действий.
- Проверки `access.entity` для `store/update/destroy/status`.
- Проверка корректного поведения токенов и срока действия ключей.
- `php artisan access:doctor` после install/update пакета; нормальный baseline: exit code `0`, `PASS`, no secrets, JSON mode пригоден для CI.
- Проверка token-scope enforcement: missing/wrong scope -> `403 scope_denied`, matching scope -> request continues to normal access check.
- Проверка audit dispatcher: token middleware decisions dispatch `AccessAuditRecorded` without raw token or hashed key in payload.
- Проверка durable audit sink: when `ACCESS_AUDIT_SINK=database|both`, sanitized events are written to `sf_access_audit_log` and raw token/authorization/hashed_key fields are not persisted.
- Проверка API-key scope assignment: `/admin/key-api` CRUD metadata exposes `scopes` as form/filter/writable field; raw key input is stored only as masked key plus `hashed_key`.
- Проверка token rate limits: when `ACCESS_TOKEN_RATE_LIMITS_ENABLED=true`, excessive token requests return `429 rate_limited`, include `Retry-After`, and dispatch `access.token.rate_limited` without raw token or hashed key in payload.
- Проверка scoped grants: after migration, `php artisan access:doctor` should see `sf_access_grant`; with `ACCESS_SCOPED_GRANTS_ENABLED=true`, temporary owner/user grant should resolve through `AccessChecker::decide()` with `details.grant.source=scoped_grant`; with the flag off, legacy fallback behavior must remain unchanged.
- Проверка access cache: saving/deleting scoped grants, access profiles, operations, groups and users should bump the corresponding `AccessCache` version; direct SQL/pivot writes require explicit invalidation.
- Проверка SitePack access pack: `AccessSitePackMapper` should export operations, profiles and scoped grants as config-KV namespaces `larena.access.operations`, `larena.access.profiles`, `larena.access.grants`; imports should support dry-run reporting before apply.
- Проверка access-pack policy: `AccessPackPolicy` should accept only manual/private config-KV access packs, reject raw secrets/tokens and require operator review for scoped grants.
- Проверка rollout policy: `php artisan access:rollout-policy <profile> --json` should return `valid=true`, no errors and a machine-readable required-smoke list for the selected deployment profile.
- Проверка rollout smoke: `php artisan access:rollout-smoke <profile> --json` should pass `scope-denied-403`, `rate-limit-429`, durable audit write and audit payload sanitation using disposable data and cleanup.
- Проверка resolver catalog: `php artisan access:resolver-catalog --json` should list built-in `owner` and package-defined `participant`, `editor`, `organization_member`; downstream packages must add resolver smoke before using custom targets.
- Проверка explain-view: `/admin/access-explain` should render after login, show `allowed` or `denied`, decision reason, selected operation and audit-safe `AccessDecision::explain()` JSON.
- Проверка sessionless API-token: normal `access.token` API-key flow should not start a web session.
- Проверка installed-route API smoke: `php artisan access:api-smoke --url=<local-larena-url> --json` should pass with missing-token `401`, disposable-token `200` or allowed `403`, no `Set-Cookie`, cleanup done and no raw token output.
- Проверка custom resolver: package-defined `AccessGrantTargetResolver` should match virtual targets only when both target and resource policy match.
- Проверка admin UX baseline: `/admin/access-grants` route and `AccessGrantEntityConfig` must be guarded by view/create/edit/delete permissions; `/admin/access-audit-log` and `AccessAuditLogEntityConfig` must be read-only and guarded by `access.view_audit_logs`.
- Visual browser smoke по `/login`, `/admin`, `/admin/access`, `/admin/group`, `/admin/users`, `/admin/access-operations`, `/admin/access-operation-values`, `/admin/access-grants`, `/admin/access-audit-log`, `/admin/access-explain`, `/admin/key-api`.
- Полный прогон `checklists/access-checklist.md`.
- `php artisan larena:validate-packages --path=/Users/rim/Documents/GitHub/larena-access --strict`.
