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
- До полноценной Larena Access DNA не хватает token scopes, audit, rate limits, runtime resolver registry, scoped grant storage and cache invalidation.

## Ключевые точки
- Сервисы: `AccessChecker`, `AccessManagement`, `AccessControl`.
- Decision-layer: `AccessValue`, `AccessContext`, `AccessDecision`.
- Grants/context baseline: `AccessActorType`, `AccessScope`, `AccessResource`, `AccessGrantTarget`, `AccessGrantTargetResolver`.
- Middleware: `access`, `access.token`, `access.entity`.
- Контракт проверки entity-прав: `EntityAbilityChecker`.
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

## Архитектурные правила интеграции
1. При добавлении нового модуля сначала опиши операции в `config/simai_<module>.php`.
2. Привяжи маршруты к `access.token`/`access.entity` на уровне routing, а не только в контроллере.
3. Для SimaiCrud действия должны иметь явный ability map в `EntityConfig`.
4. Любой bypass (service token/impersonation) должен быть задокументирован и покрыт тестами.
5. При изменении модели доступа обновляй `SPEC.md`, `CHANGELOG.md` и `Access Matrix`.

## Ближайший безопасный батч
1. Подготовить token scopes и audit RFC до REST/MCP/AI exposure.
2. Описать root/bypass production policy и добавить негативные тесты.
3. Добавить rate-limit policy для access-sensitive endpoints.
4. Добавить cache invalidation hooks для grants, operations и group membership.

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
- Полный прогон `checklists/access-checklist.md`.
- `php artisan larena:validate-packages --path=/Users/rim/Documents/GitHub/larena-access --strict`.
