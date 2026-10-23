# Структура Laravel приложения

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../../references/canonical-package-portfolio.md).

## Основные директории
- `app/` — логика приложения (Models, Services, Jobs)
- `routes/` — web/api маршруты
- `database/` — миграции, seeders, factories
- `resources/` — views, локализация, assets
- `config/` — конфиги
- `tests/` — тесты

## Структура пакета в этой монорепе
- `packages/<module>/src` — код пакета
- `packages/<module>/config` — конфиги, включая `simai_<module>.php`
- `packages/<module>/resources` — views/lang/assets/docs (по модулю)
- `packages/<module>/tests` — unit/feature/integration тесты пакета
- `packages/<module>/SPEC.md`, `CHANGELOG.md`, `module.yaml` — контракт и история

## Примечания
- Следуй локальным конвенциям проекта и module boundaries.
- Не создавай лишние слои без необходимости.
- Перед правками в конкретном пакете загружай его паспорт из `knowledge/packages/*`.
