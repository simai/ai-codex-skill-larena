# Изменения API

## Какие входные данные собрать
- Список endpoint-ов и их владельцев (module/class/method).
- Контракт запроса/ответа и коды статусов.
- Требования по аутентификации и авторизации.
- Ожидания по обратной совместимости.

## Контрактная подготовка
1. Запиши критерии приемки для каждого endpoint-а.
2. Составь план тестов (happy path, validation, unauthorized, forbidden).
3. Зафиксируй границы `Do Not Touch`.
4. Зафиксируй риски и rollback.

## Порядок выполнения
1. Минимально обнови routes/controllers/requests/resources.
2. Для защищенных endpoint-ов применяй `access.token` и единый доступ через `simai/access`.
3. Сохрани единый формат ошибок и статусов.
4. Проверь явность permission/middleware/operation codes.
5. Обнови API docs и changelog/spec при изменении поведения.
6. Не добавляй внешние CDN/сторонние URL для API-документации и UI.

## Что отдать в результате
- План и список патчей.
- Результаты API-чеклиста.
- Регрессионный чеклист по затронутым endpoint-ам.
- Релизные заметки или фрагмент changelog.

## API-проверки
- Контракт задокументирован и стабилен.
- HTTP-статусы корректны.
- Формат ошибок единообразный.
- Аутентификация и авторизация применяются принудительно.

## Swagger-проверки (`rest` / `rest_doc`)
- `vendor/bin/phpunit packages/rest/tests/Unit/SwaggerDocServiceTest.php`
- `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerEndpointsTest.php`
- `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerTryItOutTest.php`
- Проверь генерацию `paths` и схемы аргументов для try-it-out сценариев.
