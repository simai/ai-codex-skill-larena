---
name: laravel
description: Разрабатывай и поддерживай пакеты Simai Laravel монорепы в `packages/*` с контрактным подходом, строгим контролем границ задачи и воспроизводимыми проверками. Используй скилл для фич, багфиксов, API и Swagger изменений, миграций, auth/access, очередей, производительности, тестов и документации, когда задача должна следовать playbook (`playbook/00_ROUTER.md`, `playbook/01_CORE.md`, `playbook/15_ITERATION_PROTOCOL.md`), обновлять `SPEC.md` и `CHANGELOG.md` при изменении поведения и проходить quality gates (`composer run validate:repo`, lint и релевантные PHPUnit-наборы).
---

# Выполнение задач в Laravel монорепе

## 1) Сначала зафиксируй проектный контекст
- Прочитай `playbook/00_ROUTER.md` и `playbook/01_CORE.md` до планирования и правок.
- Соблюдай разделение фаз из `playbook/15_ITERATION_PROTOCOL.md`.
- Загружай только нужные материалы из скилла (не подгружай сразу весь `knowledge/*`).
- Перед правками прочитай контракты модуля:
  - `packages/<module>/SPEC.md`
  - `packages/<module>/module.yaml`
  - `packages/<module>/CHANGELOG.md`
- Сверься с общими документами:
  - `docs/ARCHITECTURE.md`
  - `docs/AI_WORKFLOW.md`
  - `docs/DEPENDENCIES.md`
- Перед созданием/привязкой нового модуля обязательно прочитай:
  - `knowledge/simai-package-rules.md`
  - `examples/new-module-bootstrap.md`

## 2) Маршрутизируй задачу в нужный модуль
- Для новой функциональности используй `modules/new-feature.md`.
- Для локальных багфиксов/рефакторинга используй `modules/project-changes.md`.
- Для REST/Swagger контрактов используй `modules/api.md`.
- Для схемы/данных используй `modules/data-migrations.md`.
- Для async/events используй `modules/jobs-queues.md`.
- Для guard/policy/permissions используй `modules/auth-authorization.md`.
- Для query/cache/perf задач используй `modules/performance.md`.
- Для стратегии тестирования и QA используй `modules/testing.md`.
- Для runbook/ADR/доков используй `modules/documentation.md`.
- Для релизов/публикации используй `modules/release.md`.

## 3) Построй контракт до кода
- Зафиксируй границы задачи (scope и out-of-scope).
- Сформулируй проверяемые критерии приемки.
- Определи проверки и тесты до реализации.
- Явно укажи границы `Do Not Touch`.
- Зафиксируй риски и стратегию rollback.
- Держи патч минимальным и локализованным.

## 4) Соблюдай инварианты монорепы при реализации
- Не выдумывай структуру пакетов и зависимости.
- Не добавляй новые зависимости без явного согласования.
- При изменении поведения обновляй документацию поведения:
  - `SPEC.md`
  - `CHANGELOG.md`
- Держи межпакетные связи явными и согласованными с `module.yaml`.
- Если меняется `module.yaml`, перегенерируй карту зависимостей: `composer run deps:generate`.
- Если затронуты Docara-пакеты, синхронизируй оба лога:
  - `docs/DOCARA_ISSUE_LOG.md`
  - `docs/DOCARA_DEVELOPMENT_LOG.md`

## 4.1) Специальные правила Simai (обязательно)
- Локализация пакетов:
  - Поддерживай минимум `ru` и `en` в `resources/lang/*` с одинаковыми ключами.
  - Не оставляй хардкод UI-строк в PHP/Blade.
- Архитектура прав доступа:
  - Используй `simai/access` как единый источник прав.
  - Для API используй `access.token`, для CRUD маршрутов — `access.entity`/`EntityConfig` abilities.
  - Операции и уровни доступа описывай в `config/simai_<module>.php` (`operations`, `accesses`, `access_levels`).
  - Для access-задач обязательно формируй `Access Matrix` и проходи `checklists/access-checklist.md`.
- Установка с минимумом команд:
  - Целевой UX: `composer require simai/<module>` + `php artisan simai:install`.
  - Для нового пакета добавляй `simai:install-<module>` (идемпотентную, без интерактива) и регистрируй её в провайдере.
  - Поддерживай автоподхват `simai:install` через префикс `simai:install-` и `config/simai_*.php`.
- Admin CRUD и страницы:
  - Используй `Route::simaiCrud(...)`/`Route::simaiApiCrud(...)` и `EntityConfig` как базовый путь.
  - Для админ-страниц используй тему `admin::layouts.*`, CRUD шаблоны `admin::crud.*`, и UI presets/drivers.
  - Новые виджеты/шаблоны добавляй осознанно в `simai/admin`-совместимом стиле и документируй.
- Внешние зависимости и CDN:
  - Не добавляй CDN/внешние script/style ссылки в пакетные Blade/JS/CSS.
  - Не добавляй жестко прошитые внешние сервисы; интеграции только через явный config/env контракт и с безопасным fallback.
- Логи и учет изменений:
  - Логируй ключевые бизнес- и системные операции без секретов/PII.
  - Всегда фиксируй изменения в `CHANGELOG.md`; для сложных случаев добавляй runbook/ADR.
- Тестирование:
  - Любое поведенческое изменение должно иметь новые/обновленные тесты.
  - Для багфикса обязательно добавляй регрессионный тест, который падает без фикса.

## 5) Выполняй верификационные гейты
Запускай релевантные команды по области задачи, но сохраняй воспроизводимость проверок:

- Базовый структурный гейт:
  - `composer run validate:repo`
- Гейт форматирования:
  - `composer run lint:changed` (или `composer run lint` при необходимости)
- Тестовый гейт (по уровню риска):
  - Сначала таргетные тесты пакета: `vendor/bin/phpunit packages/<module>/tests`
  - При интеграционном риске: `vendor/bin/phpunit --testsuite=packages`
- API/Swagger гейт для `rest` или `rest_doc`:
  - `vendor/bin/phpunit packages/rest/tests/Unit/SwaggerDocServiceTest.php`
  - `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerEndpointsTest.php`
  - `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerTryItOutTest.php`
- Access гейт (для auth/access и защищенных endpoint-ов):
  - `checklists/access-checklist.md`
  - Набор feature-тестов `401/403/2xx` по измененным маршрутам
- Релизный гейт (для publish-задач):
  - `checklists/release-checklist.md`
  - `tools/release_module.sh --module <module> --dry-run`

## 6) Формируй обязательные артефакты в ответе
- Всегда давай: краткий план, список патчей, результаты проверок.
- Всегда добавляй раздел `Migration Notes` (`No changes`, если неприменимо).
- Добавляй раздел `Upgrade Notes`, если менялись поведение/config/contracts.
- Добавляй релизный фрагмент: `Release Notes` или `Changelog Fragment`.
- Для тесто-центричных задач добавляй раздел `QA Report`.
- Для access/auth задач добавляй `Access Matrix` (route -> middleware -> operation/ability -> expected status).
- Используй шаблоны из `templates/artifacts/*`.

## 7) Избегай типовых ошибок
- Не пропускай контрактный этап.
- Не смешивай discovery/review/tasking в одном ответе.
- Не расширяй scope побочными изменениями.
- Не оставляй изменения поведения без обновления документации.
- Не закрывай задачу без явных тестовых доказательств.

## Референсы для загрузки по необходимости
- `knowledge/simai-package-rules.md`
- `knowledge/quickstart.md`
- `knowledge/laravel-structure.md`
- `knowledge/laravel-development.md`
- `knowledge/routing-controllers.md`
- `knowledge/eloquent.md`
- `knowledge/validation-requests.md`
- `knowledge/migrations.md`
- `knowledge/auth-authorization.md`
- `knowledge/access-control.md`
- `knowledge/queues-events.md`
- `knowledge/caching-performance.md`
- `knowledge/testing.md`
- `knowledge/deployment-ops.md`
- `knowledge/documentation.md`
- `knowledge/coding-standards.md`
- `knowledge/modules/admin.md`
- `knowledge/modules/access.md`
- `knowledge/modules/rest.md`
- `knowledge/modules/rest-doc.md`
- `knowledge/modules/docara-core.md`
- `knowledge/modules/docara-admin.md`
- `checklists/access-checklist.md`
- `templates/artifacts/access-matrix.md`
- `examples/access-hardening-plan.md`
- `examples/new-module-bootstrap.md`
- `examples/release-module-command.md`
