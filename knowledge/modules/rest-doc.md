# Пакет `simai/rest_doc` (паспорт)

## Роль
- Публичные endpoints документации Swagger и сценарии try-it-out.

## Ключевые точки
- Feature-тесты:
  - `packages/rest_doc/tests/Feature/SwaggerEndpointsTest.php`
  - `packages/rest_doc/tests/Feature/SwaggerTryItOutTest.php`
- Совместимость схем/paths с `simai/rest`.

## Инварианты
- Swagger endpoints должны стабильно отдавать валидный контракт.
- Try-it-out параметры и схемы должны соответствовать реальным endpoint-ам.
- Runtime-рендер без внешних CDN/жестких внешних URL.

## Типовые риски
- Ломка try-it-out из-за рассинхронизации параметров.
- Пустые/битые `paths` после изменения генерации.
- CORS/доступность swagger-endpoints в защищенных контурах.

## Обязательные проверки
- `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerEndpointsTest.php`
- `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerTryItOutTest.php`
- Ручной smoke `paths` + пример try-it-out вызова.
