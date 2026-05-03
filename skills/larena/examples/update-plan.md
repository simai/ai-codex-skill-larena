# Пример: план доработки

## Scope
- Добавить новое поле в сущность заказа и отдать его в API/admin.

## Acceptance Criteria
1. Поле сохраняется и возвращается в API.
2. Поле доступно в admin CRUD форме.
3. Доступы и валидация не нарушены.
4. Для защищенных действий обновлена `Access Matrix`.

## Checks/Tests
1. Миграции и rollback.
2. Feature-тесты API (happy path + validation + unauthorized/forbidden).
3. CRUD smoke в admin.
4. Проверка `checklists/access-checklist.md`.

## Do Not Touch
1. Не менять unrelated модули.
2. Не добавлять внешние CDN/URL.
3. Не изменять `packages/rest` без отдельного scope.

## Risks/Rollback
1. Риск рассинхрона API и Swagger.
2. Rollback: revert commit + откат миграции + возврат предыдущего package tag при релизе.
