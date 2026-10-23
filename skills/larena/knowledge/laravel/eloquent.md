# Модели Eloquent

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../../references/canonical-package-portfolio.md).

## Базовые правила
- Явно определяй связи, ключи и casts.
- Используй eager loading для предотвращения N+1.
- Не перегружай модели тяжелой бизнес-логикой.
- Повторяющиеся фильтры оформляй в scopes/query objects.

## Simai-специфика
- Для CRUD-сущностей синхронизируй Eloquent-модель и EntityConfig.
- Ограничивай writable/allowed поля, не делай permissive mass-assignment.
- Для Docara/иерархий учитывай canonical keys (`version/locale/parent/slug`) и уникальности.

## Типовые риски
- Скрытые N+1 на admin-списках.
- Неверные каскадные удаления или soft-delete семантика.
- Рассинхрон сортировки/фильтров между query и EntityConfig.

## Обязательные проверки
- Feature smoke на list/show/create/update/delete.
- Query-проверка hot-path сценариев.
- Тесты на уникальные ограничения и конфликтные кейсы.
