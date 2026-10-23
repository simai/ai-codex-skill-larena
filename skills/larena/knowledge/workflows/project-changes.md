# Изменения в проекте (минимальный патч)

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../../references/canonical-package-portfolio.md).

## Какие входные данные собрать
- Целевой пакет или модуль и точные зоны правок.
- Ожидаемое поведение до и после.
- Ограничения по версиям Laravel/PHP.
- Границы задачи и явный out-of-scope.
- Инварианты модуля из `knowledge/packages/*` (если есть).

## Контрактная подготовка
1. Запиши критерии приемки.
2. Определи проверки и тесты (сначала таргетно, затем шире при необходимости).
3. Зафиксируй список `Do Not Touch`.
4. Зафиксируй риски и путь rollback.
5. Если это клиентская доработка в `client-*` репозитории, используй стандарт
   `repo://ai-skill-teamlead/docs/standards/client-project-repository-standard.md`:
   `project/files/` зеркалит корень Larena/Laravel приложения, `project/migrations/`
   хранит одноразовые backfill/repair операции, `deploy/` хранит backup/deploy/
   smoke/rollback, а `source/` остается ignored рабочим слоем.

## Порядок выполнения
1. Прочитай текущее поведение в коде и `SPEC.md`.
2. Внеси минимальный локализованный патч.
3. Сохрани архитектурные и зависимостные границы.
4. Не нарушай правила мультиязычности, доступов и install-flow.
5. Не добавляй CDN и внешние URL в пакетные шаблоны/скрипты.
6. Если затронут доступ, обнови `Access Matrix` и пройди `checklists/access-checklist.md`.
7. Обнови документацию при изменении поведения (`SPEC.md`, `CHANGELOG.md`).
8. Добавь регрессионные тесты для багфиксов.

## Что отдать в результате
- Краткий план.
- Список патчей по затронутым файлам.
- Чеклист с pass/fail доказательствами.
- `Access Matrix` (для access/auth изменений).
- `Migration Notes` (`No changes`, если неприменимо).
- Релизные заметки или фрагмент changelog при релизном контексте.

## Проверки
- `composer run validate:repo`
- `composer run lint:changed` (или `composer run lint`)
- `vendor/bin/phpunit packages/<module>/tests`
- `vendor/bin/phpunit --testsuite=packages` при интеграционном риске

## Ограничители
- Не расширяй scope без подтверждения.
- Не добавляй зависимости без подтверждения.
- Не редактируй нерелевантные модули.
