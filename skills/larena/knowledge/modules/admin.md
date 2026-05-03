# Пакет `simai/admin` (паспорт)

## Роль
- Базовый admin UI слой, CRUD-макросы и рендер payload/meta/ui.

## Ключевые точки
- Установка: `simai:install` (`packages/admin/src/Commands/InstallSimai.php`).
- Роут-макросы: `Route::simaiCrud`, `Route::simaiApiCrud`, `Route::simaiDualCrud`.
- Регистраторы: `SimaiUiCrudRegistrar`, `SimaiApiCrudRegistrar`.
- Рендер: `SimaiResponder`, `UiDriverRegistry`, `admin::layouts.*`, `admin::crud.*`.

## Инварианты
- `simai:install` должен оставаться оркестратором установки всех `simai:install-*`.
- CRUD должен идти через EntityConfig + `access.entity`.
- UI расширения (виджеты/шаблоны) должны быть совместимы со стилем `simai/admin`.

## Типовые риски
- Коллизии маршрутов `/{id}` и статических сегментов (`create`, `reorder`).
- Ломка fallback-рендера при изменении presets/drivers.
- Несовместимость route names для batch/UI действий.

## Обязательные проверки
- `vendor/bin/phpunit packages/admin/tests`
- Проверка `simai:install` на чистой БД.
- Smoke по UI CRUD (index/create/edit/show) и `access.entity`.
