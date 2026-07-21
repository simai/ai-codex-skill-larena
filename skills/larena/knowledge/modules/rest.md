# Пакет `larena/rest` (паспорт)

## Роль
- REST Runner, API discovery, controlled method invocation and API capability boundary for Larena.

## Ключевые точки
- OpenAPI unit/runtime tests live under `packages/rest/tests` and must exercise
  the same registry used for execution.
- Endpoint and OpenAPI contracts are both owned by `larena/rest`; do not route
  documentation work to the retired `rest_doc` identity.
- API доступы через `access.token`/`simai/access`.

## Инварианты
- Любое изменение API сопровождается обновлением контрактов и тестов.
- Формат ошибок и статусов единообразен.
- Не использовать внешние CDN в runtime-документации API.
- `/api/v1/run` не является автоматическим публичным доступом к `class@method`: метод должен быть discoverable, ACL-aware, bounded and auditable.
- `scope=all` должен считаться повышенным риском; для public/agent exposure требуются явный allowlist, rate limits, audit и timeout/queue policy.

## Типовые риски
- Расхождение фактического API и Swagger-описания.
- Неполное покрытие validation/authorization веток.
- Breaking changes без Upgrade Notes.

## Обязательные проверки
- `vendor/bin/phpunit packages/rest/tests`
- Таргетные feature/unit тесты измененного API.
- Негативные тесты `401/403` и validation errors.
