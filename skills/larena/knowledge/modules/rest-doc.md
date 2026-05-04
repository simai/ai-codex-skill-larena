# Пакет `larena/rest_doc` (паспорт)

## Роль
- OpenAPI/Swagger документация для `larena/rest`.
- Безопасная модель документации: публичный placeholder без paths и защищённая permission-filtered схема для авторизованного API-токена.

## Ключевые точки
- Feature-тесты:
  - `packages/rest_doc/tests/Feature/SwaggerEndpointsTest.php`
  - `packages/rest_doc/tests/Feature/SwaggerTryItOutTest.php`
- Совместимость схем/paths с `simai/rest`.

## Инварианты
- Публичный `/api-docs/swagger.json` не должен раскрывать защищенные paths.
- Полная схема должна отдаваться через защищённый `/api/v1/rest-doc/swagger.json` с `access.token` и фильтрацией по текущим правам.
- Swagger endpoints должны стабильно отдавать валидный контракт.
- Try-it-out параметры и схемы должны соответствовать реальным endpoint-ам.
- Runtime-рендер без внешних CDN/жестких внешних URL.
- Статический файл `public/api-docs/swagger.json` не должен обходить Laravel route; при smoke проверяй его отсутствие или безопасное содержимое.

## Типовые риски
- Утечка полной API-схемы через старый статический `public/api-docs/swagger.json`.
- Ломка try-it-out из-за рассинхронизации параметров.
- Пустые/битые `paths` после изменения генерации.
- CORS/доступность swagger-endpoints в защищенных контурах.

## Обязательные проверки
- `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerEndpointsTest.php`
- `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerTryItOutTest.php`
- `php artisan route:list --path=api-docs/swagger.json`
- `php artisan route:list --path=api/v1/rest-doc/swagger.json`
- Ручной smoke `paths` + пример try-it-out вызова.
