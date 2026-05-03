# Аутентификация и авторизация

## Когда использовать
- Реализация или доработка аутентификации.
- Доработка ролей, прав, политик доступа.
- Hardening существующего доступа после инцидентов/аудита.

## Какие входные данные собрать
- Модель пользователя, роли и источники прав.
- Требования к сессиям, токенам, срокам жизни.
- Политики доступа по действиям.
- Инвентаризацию маршрутов (API/UI/CRUD) и ожидаемые middleware.
- `config/simai_<module>.php` (`operations`, `accesses`, `access_levels`).
- `EntityConfig`/ability map для сущностей.

## Контрактная подготовка
1. Зафиксируй `Acceptance Criteria` и ожидаемые HTTP-коды (`401/403/2xx`).
2. Сформируй `Access Matrix` по шаблону `templates/artifacts/access-matrix.md`.
3. Определи тестовый набор (feature + негативные access-сценарии).
4. Зафиксируй `Do Not Touch` (нерелевантные модули, сторонние зависимости, CDN).
5. Зафиксируй риски и rollback (revert, откат конфига операций, rollback токен-правил).

## Порядок выполнения
1. Сверь текущую карту маршрутов с моделью доступа (`access`, `access.token`, `access.entity`).
2. Нормализуй operation-коды и mapping в `config/simai_<module>.php`.
3. Для CRUD/Entity действий используй `access.entity` + `EntityConfig` ability map.
4. Для API-токенов используй `access.token` и явную операцию/ability.
5. Добавляй policy/gate только как дополнение к middleware-контролю, не замену.
6. Добавь тесты для каждого защищенного action: `401`, `403`, `2xx`, custom-action.
7. Синхронизируй `SPEC.md` и `CHANGELOG.md`, если изменилось поведение доступа.

## Что отдать в результате
- План.
- `Access Matrix` (route -> middleware -> operation/ability -> expected status).
- Список патчей.
- Чеклист проверок (`checklists/access-checklist.md` + релевантные smoke/API).
- `QA Report` с перечнем access-тестов.
- Релизные заметки при изменении поведения.

## Проверки
- Нет bypass-кейсов без явного и обоснованного исключения.
- Все защищенные маршруты есть в `Access Matrix`.
- `checklists/access-checklist.md` пройден полностью.
- Запреты подтверждены негативными тестами `401/403`.
