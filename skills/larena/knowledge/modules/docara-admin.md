# Пакет `larena/docara-admin` (паспорт)

## Роль
- Pro/admin слой Docara: editor, import/sync, revision flows, rollback, CRUD для страниц.
- Работает поверх free runtime `larena/docara-core`.
- Legacy Composer alias `simai/docara-admin` может встречаться в старых материалах, но новые документы и решения используют `larena/docara-admin`.

## Ключевые точки
- Консольные команды: install/sync/import Docara.
- Сервисы import pipeline: planner, duplicate resolver, revision support.
- Админ-роуты и UI-контур страниц/редактора.
- Интеграция с `simai/admin` (CRUD/route macros) и `simai/access`.

## Инварианты
- Install/sync flow должен быть идемпотентным и безопасным для повторного запуска.
- Editor/revision сценарии должны сохранять консистентность version/locale/path.
- Admin UI не должен зависеть от внешних CDN.
- Docara Admin является paid/Pro layer; не смешивай его с бесплатным public runtime.
- Не внедряй ad hoc entitlement в пакете до update/registration flow; границу фиксируй через metadata/docs и будущий update-server contract.
- Heavy sync/import не должен выполняться как долгий пользовательский web request; нужен dry-run, batch/queue/backpressure и диагностируемый результат.

## Типовые риски
- Конфликты уникальности при dedupe/reparent в импорте.
- Регрессии rollback/revisions semantics.
- Нарушение совместимости с `simai/admin` route macros.

## Обязательные проверки
- `vendor/bin/phpunit packages/docara-admin/tests`
- Smoke: `/admin/docara/pages`, create/edit/rollback/import flows.
- В starter: `php artisan docara:sync --dry-run`, `php artisan larena:doctor --docara`.
- Для релизов Docara: обновить `docs/DOCARA_ISSUE_LOG.md` и `docs/DOCARA_DEVELOPMENT_LOG.md`.
