# Модели Eloquent

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
