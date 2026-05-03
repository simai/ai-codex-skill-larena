# Стандарты кодирования (Laravel)

## Общие правила
- Соблюдай стиль и форматирование проекта (`lint:changed`/`lint`).
- Используй предметные имена классов/методов и явные контракты.
- Избегай магических строк, неявных зависимостей и скрытых side-effects.

## Структурные правила
- Тонкие контроллеры, бизнес-логика в сервисах/доменных слоях.
- Валидация через FormRequest, сериализация через Resource/DTO-подход.
- Доступ к env только через `config/*`.

## Simai-специфика
- UI строки не хардкодить: использовать `resources/lang/ru|en`.
- CRUD-поток через `simaiCrud/simaiApiCrud` + EntityConfig.
- Доступы через `simai/access` (operation-коды в конфиге модуля).

## Минимальный quality gate
- `composer run validate:repo`
- `composer run lint:changed`
- `vendor/bin/phpunit packages/<module>/tests`
