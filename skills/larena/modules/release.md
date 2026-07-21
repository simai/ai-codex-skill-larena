# Релиз модуля

## Когда использовать
- Нужна публикация канонического `larena/*` пакета из Workspace.
- Нужно обновить exact revision в Root distribution и согласовать Specs.

## Какие входные данные собрать
- Канонический package key и checkout под `larena-workspace/packages/<slug>`.
- Принятая package revision и целевая release/version policy.
- Root manifest/Composer lock и связанные Specs contracts.

## Контрактная подготовка
1. Зафиксируй scope релиза и точные package revisions.
2. Зафиксируй `Do Not Touch` по незатронутым пакетам и runtime.
3. Зафиксируй checks до публикации (lint/tests/integration/smoke).
4. Зафиксируй rollback к предыдущему Root lock/manifest.

## Порядок выполнения
1. Validate and commit the owning package repository in Workspace.
2. Push the accepted package revision without rewriting history.
3. Update the Root exact revision, Composer lock and release manifest.
4. Run the full Root acceptance matrix and preserve evidence.
5. Update Specs only when the product contract changed.
6. Tag/release only after explicit release scope and readiness gate.

## Что отдать в результате
- Package branch + exact commit hash and optional approved tag.
- Root branch, lock/manifest commit and acceptance evidence.
- Specs revision when the contract changed.
- `Migration Notes` / `Upgrade Notes` при необходимости.
- Обновленные Docara-логи (если релиз касается Docara).

## Проверки
- Релизный чеклист пройден (`checklists/release-checklist.md`).
- Поведение пакета валидировано тестами и smoke-проверками.
- В отчете есть явные rollback-команды.
