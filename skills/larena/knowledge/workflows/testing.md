# Тестирование

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../../references/canonical-package-portfolio.md).

## Какие входные данные собрать
- Область изменения и уровень риска.
- Нужный уровень покрытия (unit/feature/integration).
- Ограничения окружения (DB, queue, cache).

## Планирование тестов
1. Сопоставь критерии приемки с тест-кейсами.
2. Выбери минимальный надежный набор команд.
3. Добавь integration/regression кейсы при межпакетных изменениях.
4. Для багфикса добавь тест, который воспроизводит дефект.
5. Для прав доступа добавь минимум один негативный тест.

## Порядок запуска
1. Структурный гейт: `composer run validate:repo`
2. Гейт стиля: `composer run lint:changed`
3. Таргетные тесты: `vendor/bin/phpunit packages/<module>/tests`
4. Расширенная регрессия (если нужна): `vendor/bin/phpunit --testsuite=packages`

## Что отдать в результате
- Раздел `QA Report` (`templates/artifacts/qa-report.md`).
- Раздел `Regression Checklist` (`templates/artifacts/regression-checklist.md`).
- Точный список команд с pass/fail статусом.
- Явный список новых/обновленных тестов.

## Проверки
- Тесты воспроизводимы.
- Ассерты покрывают измененное поведение.
- Нет скрытых падений и пропуска критичных сценариев.
- Тестовая база расширена при изменении поведения (не только адаптация старых тестов).
