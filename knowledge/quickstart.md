# Быстрый старт (Laravel + Simai)

## Цель
Быстро и безопасно войти в контекст пакета, не ломая install-flow, доступы и админ-интерфейс.

## Шаг 1. Вход в контекст
1. Прочитай `playbook/00_ROUTER.md` и `playbook/01_CORE.md`.
2. Определи целевой пакет в `packages/<module>`.
3. Открой обязательные документы пакета:
   - `packages/<module>/SPEC.md`
   - `packages/<module>/CHANGELOG.md`
   - `packages/<module>/module.yaml`

## Шаг 2. Быстрая архитектурная проверка
1. Проверь сервис-провайдер пакета (`src/Providers/*ServiceProvider.php`):
   - регистрации маршрутов, переводов, миграций, команд.
2. Найди `config/simai_<module>.php` и проверь наличие секций:
   - `module_info`
   - `menu`
   - `access_levels` (если нужно)
   - `accesses`
   - `operations`
3. Проверь установку пакета:
   - есть ли команда `simai:install-<module>`;
   - идемпотентна ли команда;
   - не требует ли интерактива.

## Шаг 3. Проверка интеграции с admin/access
1. Для CRUD убедись, что используются `Route::simaiCrud(...)` и/или `Route::simaiApiCrud(...)`.
2. Проверь доступы:
   - API: `access.token`;
   - CRUD actions: `access.entity` + `EntityConfig`.
3. Для админ-страниц проверь использование `admin::layouts.*` и `admin::crud.*`.
4. Если добавлены виджеты/шаблоны, проверь переиспользуемость и совместимость с текущими пресетами UI.

## Шаг 4. Базовый quality-scan до правок
1. Локализация: `resources/lang/ru` и `resources/lang/en`, паритет ключей.
2. Безопасность install UX: минимум команд (`composer require` + `php artisan simai:install`).
3. Отсутствие внешних CDN/жестких URL в Blade/JS/CSS.
4. Наличие тестов и возможность добавить regression coverage под изменения.

## Шаг 5. Базовый набор команд для старта
- `composer run validate:repo`
- `composer run lint:changed` (или `composer run lint`)
- `vendor/bin/phpunit packages/<module>/tests`
