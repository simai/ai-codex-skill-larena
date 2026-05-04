# Пакет `larena/rest` (паспорт)

## Роль
- REST Runner, API discovery, controlled method invocation and API capability boundary for Larena.

## Ключевые точки
- Swagger unit-тесты: `packages/rest/tests/Unit/SwaggerDocServiceTest.php`.
- Контракты endpoint-ов должны быть согласованы с `rest_doc`.
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
- `vendor/bin/phpunit packages/rest/tests/Unit/SwaggerDocServiceTest.php`
- Таргетные feature/unit тесты измененного API.
- Негативные тесты `401/403` и validation errors.
