# Релиз модуля

## Когда использовать
- Нужна публикация изменений пакета из монорепы в выделенный repo модуля.
- Нужен новый tag пакета и обновление зависимости в `bitrix-update`.

## Какие входные данные собрать
- Имя модуля (`packages/<module>`).
- Путь к выделенному repo (`../laravel.<module>` или явный путь).
- Целевой tag (`x.y.z`) или правило автоинкремента.
- Нужно ли обновлять `bitrix-update` и в каком проекте.

## Контрактная подготовка
1. Зафиксируй scope релиза (какие пакеты входят, какие исключены).
2. Зафиксируй `Do Not Touch` (обязательно: не включать `packages/rest`).
3. Зафиксируй checks до публикации (lint/tests/smoke).
4. Зафиксируй rollback (git revert + composer require на предыдущий tag).

## Порядок выполнения
1. Подготовь monorepo commit/push (исключая `packages/rest`).
2. Синхронизируй `packages/<module>` в выделенный repo и сделай commit/push.
3. Создай и запушь новый tag в выделенном repo.
4. Обнови `bitrix-update` (`composer require/update`) до нового tag и зафиксируй точный вывод.
5. Для `docara-core` синхронизируй docs:
   - `packages/docara-core/resources/docs`
   - `../laravel.docara-core/resources/docs`
6. Для Docara задач синхронизируй:
   - `docs/DOCARA_ISSUE_LOG.md`
   - `docs/DOCARA_DEVELOPMENT_LOG.md`

## Что отдать в результате
- Monorepo branch + commit hash.
- Module repo branch + commit hash + tag.
- Точный результат `composer require/update` в `bitrix-update`.
- `Migration Notes` / `Upgrade Notes` при необходимости.
- Обновленные Docara-логи (если релиз касается Docara).

## Проверки
- Релизный чеклист пройден (`checklists/release-checklist.md`).
- Поведение пакета валидировано тестами и smoke-проверками.
- В отчете есть явные rollback-команды.
