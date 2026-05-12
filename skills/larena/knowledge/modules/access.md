# Пакет `larena/access` (паспорт)

## Роль
- Единая модель прав доступа, middleware и operation-коды для пакетов Larena.
- `simai/access` допускается только как Composer compatibility alias.

## Текущий статус
- Completion level: `L4 partial`.
- Каноническая ДНК: `simai/larena/docs/developer/dna/access-dna.md`.
- Пакетные документы: `docs/developer/dna/access-dna.md`, `docs/developer/access-dna-compliance.md`, `docs/developer/architecture.md`, `docs/developer/ai-contract.md`, `docs/developer/package-status.md`.
- Текущая реализация полезна как compatibility layer: access profiles, operations, operation values, user/group bindings, middleware, API keys.
- Первый explainable decision-layer реализован: `AccessValue`, `AccessContext`, `AccessDecision`, `AccessControl::decide()` и `AccessChecker::decide()`.
- Grants/context baseline реализован без миграций: `AccessActorType`, `AccessScope`, `AccessResource`, `AccessGrantTarget`, `AccessGrantTargetResolver`.
- Security/operations baseline реализован: `AccessTokenScope`, `AccessAuditEvent`, policy docs, negative tests for missing token and unsafe bypass config.
- L4 demonstrator baseline описан: decision explain, missing grant, group grant, token safety, installed admin/API smoke.
- Installed-site HTTP and visual browser smoke по `larena.test` прошёл для main admin access pages. Browser Use в текущей сессии был недоступен, поэтому визуальный smoke выполнен через CLI Playwright fallback.
- Package-local `access:doctor` реализован и проверен на `larena.test`: 48 checks, 0 warnings после token-scope, rate-limit, durable-audit, scoped-grant, cache и SitePack baseline. Команда read-only, не выводит секреты и проверяет config, tables, token-scope/scoped-grant/audit storage, rate-limit profiles, cache/SitePack services, middleware, routes, contracts и bypass-token safety.
- Token-scope storage baseline реализован: `sf_access_api_key.scopes`, `AccessTokenScopePolicy`, config-gated middleware enforcement через `ACCESS_TOKEN_SCOPE_ENFORCEMENT`. Enforcement выключен по умолчанию для совместимости.
- API-key scope assignment baseline реализован: `ApiKeyEntityConfig` exposes `scopes` as form/filter/writable CRUD metadata; generic CRUD stores masked `key` plus Laravel `hashed_key`, and runtime validation still accepts legacy SHA-256 hashes for compatibility.
- Audit dispatcher baseline реализован: `AccessAuditDispatcher` emits `AccessAuditRecorded` Laravel events for token middleware decisions; payload sanitation strips raw tokens, authorization headers, hashed keys, passwords and secrets.
- Durable audit sink baseline реализован: `sf_access_audit_log`, `AccessAuditLog`, `ACCESS_AUDIT_SINK=event|database|both|off`, `ACCESS_AUDIT_FAIL_OPEN=true|false`. Default sink remains `event` for compatibility; `database`/`both` writes sanitized payloads.
- Token rate-limit baseline реализован: `AccessRateLimitPolicy` wires `access.token` to Laravel `RateLimiter`, config-gated through `ACCESS_TOKEN_RATE_LIMITS_ENABLED`, with named profiles (`admin-default`, `admin-sensitive`, `api-sensitive`, `tool-sensitive`, `internal-service`). Limit exceeded returns `429 rate_limited` with `Retry-After` and emits sanitized `access.token.rate_limited`.
- Scoped grant storage baseline реализован через RFC 0001: `sf_access_grant`, `AccessGrant`, `AccessScopedGrantStore`, `AccessGrantResolverRegistry`, `ResolvedScopedGrant`, `ACCESS_SCOPED_GRANTS_ENABLED=false` by default. When enabled, `AccessControl::decide()` checks scoped grants before legacy user/group fallback and explains `details.grant.source=scoped_grant`.
- Access cache baseline реализован: `AccessCache` uses versioned cache keys for `hasAccess()` and `isUserInGroup()` compatibility helpers. Eloquent hooks invalidate cache versions on access profile, operation, user group, user and scoped grant save/delete. Direct SQL writes and low-level pivot-table changes still require explicit `AccessCache::invalidateAll()`, `invalidateUser()` or `invalidateGroup()`.
- Access SitePack baseline реализован: `AccessSitePackMapper` exports/imports operations (`larena.access.operations`), profiles (`larena.access.profiles`) and scoped grants (`larena.access.grants`) as config-KV. Imports are dry-run capable, `applyPolicy=manual`, and profiles bind operations by stable operation code instead of local database ids.
- Sessionless API-token smoke реализован: normal `access.token` API-key flow does not start a web session; bypass-token flow remains special/internal and requires explicit `ACCESS_BYPASS_USER_ID > 0`.
- Custom resolver smoke реализован: `AccessGrantResolverRegistry` can register package-defined resolvers for virtual targets such as `participant`; production resolver catalog remains future work.
- Visual smoke note: access pages render, but legacy update/upserv asset URLs under `/vendor/larena/upserv/public/...` return 404. Это не блокер `larena/access`, но должно уйти в update/upserv cleanup batch.
- До полноценной Larena Access DNA не хватает scoped grant admin UX, operator audit UI, installed-route API smoke, marketplace/update-server access-pack install policy and production virtual-target resolver catalog.

## Ключевые точки
- Сервисы: `AccessChecker`, `AccessManagement`, `AccessControl`, `AccessTokenScopePolicy`, `AccessAuditDispatcher`, `AccessCache`, `AccessRateLimitPolicy`, `AccessScopedGrantStore`, `AccessSitePackMapper`, `AccessGrantResolverRegistry`, `ApiKeyManager`.
- Events: `AccessAuditRecorded`.
- Durable audit model: `AccessAuditLog` over `sf_access_audit_log`.
- Scoped grant model: `AccessGrant` over `sf_access_grant`.
- Decision-layer: `AccessValue`, `AccessContext`, `AccessDecision`.
- Grants/context baseline: `AccessActorType`, `AccessScope`, `AccessResource`, `AccessGrantTarget`, `AccessGrantTargetResolver`.
- Security/operations baseline: `AccessTokenScope`, `AccessAuditEvent`.
- Middleware: `access`, `access.token`, `access.entity`.
- Контракт проверки entity-прав: `EntityAbilityChecker`.
- Runtime diagnostics: `php artisan access:doctor`, `php artisan access:doctor --json`.
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
1. Для update/upserv отдельно почистить legacy asset URLs, найденные visual smoke.
2. Добавить operator audit review UI и scoped grant admin UX, когда `larena/admin` CRUD patterns стабилизируются.
3. Добавить marketplace/update-server install policy для access packs.
4. Добавить installed-route API smoke и production virtual-target resolver catalog.

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
- Проверка sessionless API-token: normal `access.token` API-key flow should not start a web session.
- Проверка custom resolver: package-defined `AccessGrantTargetResolver` should match virtual targets only when both target and resource policy match.
- Visual browser smoke по `/login`, `/admin`, `/admin/access`, `/admin/group`, `/admin/users`, `/admin/access-operations`, `/admin/access-operation-values`, `/admin/key-api`.
- Полный прогон `checklists/access-checklist.md`.
- `php artisan larena:validate-packages --path=/Users/rim/Documents/GitHub/larena-access --strict`.
