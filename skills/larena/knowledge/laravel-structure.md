# Структура Laravel приложения

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
- Перед правками в конкретном пакете загружай его паспорт из `knowledge/modules/*`.
