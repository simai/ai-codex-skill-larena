# Пример: Access Hardening Plan

## Scope
- Выравнивание прав доступа для CRUD `docara pages` и API операций публикации.

## Acceptance Criteria
1. Все защищенные маршруты покрыты `access.entity` или `access.token`.
2. Операции синхронизированы с `config/simai_docara.php`.
3. Для каждого критичного action есть тесты `401/403/2xx`.
4. Сформирован `Access Matrix` и пройден `access-checklist`.

## Checks/Tests
1. `vendor/bin/phpunit packages/docara/tests --filter='Access|Denied|Audit'`
2. `vendor/bin/phpunit packages/access/tests`
3. `composer run validate:repo`

## Do Not Touch
1. Не менять контракты `packages/rest` без отдельного scope.
2. Не добавлять новые внешние зависимости.
3. Не менять UI-шаблоны вне задач по доступам.

## Risks/Rollback
1. Риск ложных `403` из-за ошибочного operation-code mapping.
2. Rollback: revert commit + возврат предыдущего `config/simai_docara.php`.
