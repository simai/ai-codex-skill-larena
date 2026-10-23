# Стандарты кодирования (Laravel)

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../../references/canonical-package-portfolio.md).

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
