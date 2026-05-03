# Пакет `simai/rest` (паспорт)

## Роль
- REST-слой и генерация/поддержка Swagger-метаданных для API.

## Ключевые точки
- Swagger unit-тесты: `packages/rest/tests/Unit/SwaggerDocServiceTest.php`.
- Контракты endpoint-ов должны быть согласованы с `rest_doc`.
- API доступы через `access.token`/`simai/access`.

## Инварианты
- Любое изменение API сопровождается обновлением контрактов и тестов.
- Формат ошибок и статусов единообразен.
- Не использовать внешние CDN в runtime-документации API.

## Типовые риски
- Расхождение фактического API и Swagger-описания.
- Неполное покрытие validation/authorization веток.
- Breaking changes без Upgrade Notes.

## Обязательные проверки
- `vendor/bin/phpunit packages/rest/tests/Unit/SwaggerDocServiceTest.php`
- Таргетные feature/unit тесты измененного API.
- Негативные тесты `401/403` и validation errors.
