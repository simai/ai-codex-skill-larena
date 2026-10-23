# Миграции и сиды

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../../references/canonical-package-portfolio.md).

## Базовые правила
- Делай миграции идемпотентными и повторяемыми.
- Разделяй schema и data migration, где это возможно.
- Не выполняй destructive изменения без подтвержденного rollback-плана.
- Всегда описывай rollback и post-check шаги.

## Simai-специфика
- Учитывай `simai:install` поток: миграции должны быть безопасны для clean install.
- Для module config seeding используй upsert-подход.
- Для Docara/access учитывай cross-db особенности (sqlite/mysql) и индексные ограничения.

## Типовые риски
- Падение install на чистой БД.
- Необратимые изменения данных без backup/backfill.
- Уникальные конфликты при импорте/merge сценариях.

## Обязательные проверки
- `php artisan migrate --force` на чистой БД.
- `php artisan migrate:rollback` (или проверяемый rollback сценарий).
- Тест/смоук на консистентность данных после миграции.
