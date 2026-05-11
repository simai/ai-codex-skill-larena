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
- Package-local `access:doctor` реализован и проверен на `larena.test`: 38 checks, 0 warnings после token-scope и rate-limit baseline. Команда read-only, не выводит секреты и проверяет config, tables, token-scope storage, rate-limit profiles, middleware, routes, contracts и bypass-token safety.
- Token-scope storage baseline реализован: `sf_access_api_key.scopes`, `AccessTokenScopePolicy`, config-gated middleware enforcement через `ACCESS_TOKEN_SCOPE_ENFORCEMENT`. Enforcement выключен по умолчанию для совместимости.
- Audit dispatcher baseline реализован: `AccessAuditDispatcher` emits `AccessAuditRecorded` Laravel events for token middleware decisions; payload sanitation strips raw tokens, authorization headers, hashed keys, passwords and secrets. Durable audit storage ещё не реализовано.
- Token rate-limit baseline реализован: `AccessRateLimitPolicy` wires `access.token` to Laravel `RateLimiter`, config-gated through `ACCESS_TOKEN_RATE_LIMITS_ENABLED`, with named profiles (`admin-default`, `admin-sensitive`, `api-sensitive`, `tool-sensitive`, `internal-service`). Limit exceeded returns `429 rate_limited` with `Retry-After` and emits sanitized `access.token.rate_limited`.
- Visual smoke note: access pages render, but legacy update/upserv asset URLs under `/vendor/larena/upserv/public/...` return 404. Это не блокер `larena/access`, но должно уйти в update/upserv cleanup batch.
- До полноценной Larena Access DNA не хватает durable audit storage, admin/API scope assignment UI, runtime resolver registry, scoped grant storage and cache invalidation.

## Ключевые точки
- Сервисы: `AccessChecker`, `AccessManagement`, `AccessControl`, `AccessTokenScopePolicy`, `AccessAuditDispatcher`, `AccessRateLimitPolicy`.
- Events: `AccessAuditRecorded`.
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
1. Позже отдельно внедрять durable audit storage или configurable audit sink.
2. Добавить admin/API UI для назначения scopes API-ключам до включения enforcement на реальных установках.
3. Для update/upserv отдельно почистить legacy asset URLs, найденные visual smoke.

Не начинать с переименования `sf_access_*` таблиц или крупных миграций. Следующий слой должен закрывать security/operations, а runtime resolver registry и новое grant storage делать только после RFC.

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
- Проверка token rate limits: when `ACCESS_TOKEN_RATE_LIMITS_ENABLED=true`, excessive token requests return `429 rate_limited`, include `Retry-After`, and dispatch `access.token.rate_limited` without raw token or hashed key in payload.
- Visual browser smoke по `/login`, `/admin`, `/admin/access`, `/admin/group`, `/admin/users`, `/admin/access-operations`, `/admin/access-operation-values`, `/admin/key-api`.
- Полный прогон `checklists/access-checklist.md`.
- `php artisan larena:validate-packages --path=/Users/rim/Documents/GitHub/larena-access --strict`.
