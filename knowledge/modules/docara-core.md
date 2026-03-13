# Пакет `simai/docara-core` (паспорт)

## Роль
- Ядро Docara: публичный docs runtime, источники документов, bootstrap/sync для DB mode.

## Ключевые точки
- Источники docs: `resources/docs/{version}/{locale}`.
- Публичные assets: `resources/public/*`, `PublicAssetsInstaller`.
- Роуты docs/search/assets: `routes/web.php`.
- Поддержка версий/локалей: `DocaraVersionResolver`, locale helpers.

## Инварианты
- Runtime assets должны быть локальными (без CDN зависимостей).
- DB/File режимы docs должны работать консистентно.
- Маршруты `/docs/{version}/{locale}` и `search-index_{locale}.json` стабильны.

## Типовые риски
- `404` на `/vendor/docara/distr/*` после релиза.
- Расхождение между seed docs и runtime DB-import.
- Ломка версионного переключателя при нестандартном `source_path`.

## Обязательные проверки
- `vendor/bin/phpunit packages/docara-core/tests`
- Smoke: `/docs/<version>/<locale>`, `/search-index_<locale>.json`, `/vendor/docara/...`.
- Проверка синка docs при релизе:
  - `packages/docara-core/resources/docs`
  - `../laravel.docara-core/resources/docs`
