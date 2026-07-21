# Пример: релизные заметки по API

## Добавлено
- `GET /api/orders/{id}` — получение заказа по `id`.
- `POST /api/orders` — создание заказа.

## Изменено
- Ответ `GET /api/orders/{id}` дополнен полями `status` и `total`.
- Для защищенных endpoint-ов включена проверка `access.token`.

## Совместимость
- Ломающих изменений нет.
- Требуется обновить swagger-контракт и клиентские DTO при использовании новых полей.

## Проверки
- `vendor/bin/phpunit packages/rest/tests/Unit/OpenApiGeneratorTest.php`
- `vendor/bin/phpunit packages/rest/tests/Unit/PackageApiContractLoaderTest.php`
- `vendor/bin/phpunit packages/rest/tests/Unit/AdminApiRuntimeTest.php`
