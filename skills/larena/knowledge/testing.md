# Тестирование

## Цель
Подтвердить изменение поведения воспроизводимыми тестами и не допустить регрессий в install/access/admin-flow.

## Матрица тестов
- `Unit`: изолированная бизнес-логика, маппинги, value objects, policy helpers.
- `Feature`: endpoint-и, CRUD сценарии, валидация, middleware, рендер.
- `Integration` (по риску): межпакетные сценарии, особенно при изменении install/access/admin.

## Обязательные правила
- Для багфикса добавляй regression test, который падает без фикса.
- Для прав доступа добавляй минимум один негативный кейс (`401`/`403`) на каждое критичное действие.
- Для новых API проверяй:
  - контракт ответа;
  - валидацию;
  - авторизацию (`access.token` / `access.entity`).
- Для CRUD в admin проверяй минимум:
  - list/show/create/edit happy path;
  - ограничения по полям/валидации;
  - запрет неразрешенных действий.

## Тесты для install-flow
- При добавлении нового модуля/команды `simai:install-<module>` проверяй:
  - идемпотентный повторный запуск;
  - отсутствие интерактива;
  - корректную обработку `config/simai_<module>.php`.
- При изменениях в `simai:install`-совместимости добавляй smoke/integration проверки загрузки модуля.

## Тесты для мультиязычности
- Проверяй наличие минимум `ru`/`en` ключей для новых UI текстов.
- Не принимай изменения, где новые UI строки добавлены только в один язык.

## Рекомендуемый набор запусков
1. `composer run validate:repo`
2. `composer run lint:changed` (или `composer run lint`)
3. `vendor/bin/phpunit packages/<module>/tests`
4. `vendor/bin/phpunit --testsuite=packages` при интеграционном риске

## Обязательные Swagger-проверки (`rest` / `rest_doc`)
- `vendor/bin/phpunit packages/rest/tests/Unit/SwaggerDocServiceTest.php`
- `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerEndpointsTest.php`
- `vendor/bin/phpunit packages/rest_doc/tests/Feature/SwaggerTryItOutTest.php`
