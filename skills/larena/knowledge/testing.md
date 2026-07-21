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

## Package-local PHPUnit harness

Для отдельных `larena/*` package-репозиториев тесты должны запускаться из самого пакета, а не только из starter-приложения.

Минимальный стандарт:

- `phpunit.xml` в корне пакета;
- `composer.json` содержит `require-dev` для `phpunit/phpunit`, `orchestra/testbench` и тестовых Larena-интеграций;
- `composer.json` содержит `autoload-dev` для `Simai\\<Package>\\Tests\\`;
- если пакетные тесты зависят от приватных Larena-пакетов, добавь VCS repositories для этих пакетов или документированный shared-vendor fallback;
- `tests/bootstrap.php` может подключать локальный `vendor/autoload.php` или shared starter `vendor/autoload.php`, но должен грузить локальный `src/` и `tests/` из package checkout;
- тестовые stubs/fixtures должны жить под `tests/Fixtures/` и не зависеть от приложения пользователя;
- `.gitignore` должен исключать `vendor/`, `.phpunit.cache/` и `composer.lock`, если lock-файл не является осознанной частью package workflow.

Проверочный минимум перед коммитом:

```bash
composer validate --no-check-publish
find src config database routes resources tests -name '*.php' -print0 | xargs -0 -n1 php -l
vendor/bin/phpunit
php artisan larena:validate-packages --path=/path/to/package --strict
```

## Required OpenAPI checks (`larena/rest`)

- `vendor/bin/phpunit packages/rest/tests/Unit/OpenApiGeneratorTest.php`
- `vendor/bin/phpunit packages/rest/tests/Unit/PackageApiContractLoaderTest.php`
- `vendor/bin/phpunit packages/rest/tests/Unit/AdminApiRuntimeTest.php`

The current REST package owns both execution and documentation contracts.
