# Пакет `larena/admin` (паспорт)

## Роль
- Core modular admin platform: базовый admin UI слой, CRUD-макросы, рендер payload/meta/ui, plugin/extension registries, batches, audit and diagnostics.
- Legacy Composer alias `simai/admin` может встречаться в старых материалах, но новые Larena-facing документы и решения используют `larena/admin`.

## Ключевые точки
- Установка: `simai:install` (`packages/admin/src/Commands/InstallSimai.php`).
- Роут-макросы: `Route::simaiCrud`, `Route::simaiApiCrud`, `Route::simaiDualCrud`.
- Регистраторы: `SimaiUiCrudRegistrar`, `SimaiApiCrudRegistrar`.
- Рендер: `SimaiResponder`, `UiDriverRegistry`, `admin::layouts.*`, `admin::crud.*`.
- Extension contracts: plugin, menu, table, field, widget, page, block, cell, bulk action.
- Diagnostics: `simai:admin:routes:check`, `simai:admin:plugins:health`, `simai:admin:smoke`, `simai:admin:e2e:smoke`.

## Инварианты
- `simai:install` должен оставаться оркестратором установки всех `simai:install-*`.
- CRUD должен идти через EntityConfig + `access.entity`.
- UI расширения (виджеты/шаблоны) должны быть совместимы со стилем `simai/admin`.
- Host projects and product packages must not edit/copy `vendor/larena/admin`; extend through typed contracts, config, routes or separate Composer packages.
- Admin core must not contain monetization/entitlement policy.
- Long admin operations should use `AdminBatch`, queue/command flows and diagnostics, not long blocking web requests.
- New package admin contributions should be permission/context-aware and later mapped into `module.yaml` capability metadata.

## Типовые риски
- Коллизии маршрутов `/{id}` и статических сегментов (`create`, `reorder`).
- Ломка fallback-рендера при изменении presets/drivers.
- Несовместимость route names для batch/UI действий.
- Production defaults requiring review: `SIMAI_ADMIN_ACCESS_FAIL_OPEN`, `SIMAI_ADMIN_DEMO_ENABLED`, plugin boot error policy.
- Historical docs/examples may still use `simai/admin` naming.
- Deep audit 2026-05-13: current package status is L4-ready with conditions; development debug logs must go through `AdminDevelopmentLogger` and active compatibility surfaces are registered centrally.

## Обязательные проверки
- `vendor/bin/phpunit packages/admin/tests`
- Проверка `simai:install` на чистой БД.
- Smoke по UI CRUD (index/create/edit/show) и `access.entity`.
- In starter: `php artisan simai:admin:routes:check`
- In starter: `php artisan simai:admin:plugins:health --strict`
- In starter: `php artisan simai:admin:smoke --strict-plugins`
- In starter: `php artisan simai:admin:e2e:smoke --strict-plugins`
- Source audit: verify no ungated `Log::debug` remains outside `AdminDevelopmentLogger`.
