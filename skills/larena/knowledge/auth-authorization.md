# Аутентификация и авторизация

## Базовые правила
- Для API применяй `access.token`, для CRUD — `access.entity`/EntityConfig map.
- Для статических operation-проверок используй `access:<operation>`.
- Не оставляй endpoint без явной проверки доступа.
- По умолчанию применяй принцип минимально необходимых прав.
- Для access-задачи всегда формируй `Access Matrix` и проверяй ее тестами.
- Для Auth/2FA задач всегда проверяй фактическое владение маршрутом `POST /login` через `php artisan route:list --path=login`: `larena/two-fa` может оборачивать или переопределять login flow, и это должно быть явной частью контракта, а не случайной коллизией маршрутов.

## Практика для Simai
- Операции/доступы описывай в `config/simai_<module>.php`.
- Не размазывай operation-коды хардкодом по контроллерам.
- Для новых действий синхронизируй mapping в EntityConfig (`create/read/update/delete/status/custom`).
- Для API/CRUD используй route-level middleware как primary guardrail, не только проверки внутри метода.

## Минимальный workflow hardening
1. Сними инвентарь защищенных маршрутов (UI/API/CRUD).
2. Построй `Access Matrix` через `templates/artifacts/access-matrix.md`.
3. Сверь operation/ability с `config/simai_<module>.php` и `EntityConfig`.
4. Добавь feature-тесты `401/403/2xx` на каждый критичный action.
5. Прогони `checklists/access-checklist.md` и зафиксируй доказательства в `QA Report`.

## Типовые риски
- Несоответствие operation-кодов в конфиге и middleware.
- Пропуск негативных сценариев (неавторизованный/без прав).
- Случайный bypass при кастомных middleware цепочках.
- Расхождение route-level доступа и policy/gate условий.
- Неявная коллизия `larena/auth` и `larena/two-fa` вокруг `POST /login`: если 2FA включена, auth smoke должен подтверждать не только наличие `/login`, но и корректный handoff к OTP challenge.

## Обязательные проверки
- Feature-тесты `401`/`403` на критичных маршрутах.
- Проверка happy path + forbidden path для create/update/delete.
- Проверка доступа на custom CRUD-экшены.
- Проверка отсутствия endpoint-ов без доступа в `Access Matrix`.
- Для stateful auth/security пакетов: `route:list --path=login`, `route:list --path=two-factor`, logout/session smoke и явная запись, кто владеет `POST /login` в текущей сборке.
