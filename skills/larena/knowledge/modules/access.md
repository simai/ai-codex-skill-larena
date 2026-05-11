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
- Installed-site HTTP smoke по `larena.test` прошёл для main admin access pages; визуальный browser evidence ещё нужен, если Browser Use доступен.
- Package-local `access:doctor` реализован и проверен на `larena.test`: 35 checks, 0 warnings. Команда read-only, не выводит секреты и проверяет config, tables, middleware, routes, contracts и bypass-token safety.
- До полноценной Larena Access DNA не хватает runtime token-scope storage, audit dispatcher, rate-limit wiring, runtime resolver registry, scoped grant storage and cache invalidation.

## Ключевые точки
- Сервисы: `AccessChecker`, `AccessManagement`, `AccessControl`.
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
1. Провести визуальный browser smoke на установленном Larena site по `docs/developer/demonstrator.md`, когда Browser Use доступен.
2. Позже отдельно внедрять runtime token-scope storage, audit dispatcher and rate-limit wiring.

Не начинать с переименования `sf_access_*` таблиц или крупных миграций. Следующий слой должен закрывать security/operations, а runtime resolver registry и новое grant storage делать только после RFC.

## Типовые риски
- Разнобой operation-кодов между конфигом и кодом.
- Утечки доступа из-за обхода middleware.
- Неправильная обработка bypass token и impersonation.
- API keys без scopes/audit/rate limits дают слишком широкий контур для внешних клиентов и AI/MCP.
- Root/bypass policy без тестов может создать неявный супердоступ.

## Обязательные проверки
- Негативные тесты `401/403` для критичных действий.
- Проверки `access.entity` для `store/update/destroy/status`.
- Проверка корректного поведения токенов и срока действия ключей.
- `php artisan access:doctor` после install/update пакета; нормальный baseline: exit code `0`, `PASS`, no secrets, JSON mode пригоден для CI.
- Полный прогон `checklists/access-checklist.md`.
- `php artisan larena:validate-packages --path=/Users/rim/Documents/GitHub/larena-access --strict`.
