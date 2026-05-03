# Пакет `simai/docara-admin` (паспорт)

## Роль
- Админ-контур Docara: editor, import/sync, revision flows, CRUD для страниц.

## Ключевые точки
- Консольные команды: install/sync/import Docara.
- Сервисы import pipeline: planner, duplicate resolver, revision support.
- Админ-роуты и UI-контур страниц/редактора.
- Интеграция с `simai/admin` (CRUD/route macros) и `simai/access`.

## Инварианты
- Install/sync flow должен быть идемпотентным и безопасным для повторного запуска.
- Editor/revision сценарии должны сохранять консистентность version/locale/path.
- Admin UI не должен зависеть от внешних CDN.

## Типовые риски
- Конфликты уникальности при dedupe/reparent в импорте.
- Регрессии rollback/revisions semantics.
- Нарушение совместимости с `simai/admin` route macros.

## Обязательные проверки
- `vendor/bin/phpunit packages/docara-admin/tests`
- Smoke: `/admin/docara/pages`, create/edit/rollback/import flows.
- Для релизов Docara: обновить `docs/DOCARA_ISSUE_LOG.md` и `docs/DOCARA_DEVELOPMENT_LOG.md`.
