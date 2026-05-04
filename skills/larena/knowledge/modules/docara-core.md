# Пакет `larena/docara-core` (паспорт)

## Роль
- Free/public runtime слой Docara: публичный docs runtime, источники документов, локальные assets, file/DB reads.
- Должен работать без `larena/docara-admin`.
- Legacy Composer alias `simai/docara-core` может встречаться в старых материалах, но новые документы и решения используют `larena/docara-core`.

## Ключевые точки
- Источники docs: `resources/docs/{version}/{locale}`.
- Публичные assets: `resources/public/*`, `PublicAssetsInstaller`.
- Роуты docs/search/assets: `routes/web.php`.
- Поддержка версий/локалей: `DocaraVersionResolver`, locale helpers.

## Инварианты
- Runtime assets должны быть локальными (без CDN зависимостей).
- DB/File режимы docs должны работать консистентно.
- Маршруты `/docs/{version}/{locale}` и `search-index_{locale}.json` стабильны.
- Core не владеет editor/revisions/rollback/sync UI; это граница `larena/docara-admin`.
- Не добавляй ad hoc коммерческую проверку в Core: free/runtime boundary фиксируется metadata/docs, entitlement позже идет через update/registration.

## Типовые риски
- `404` на `/vendor/docara/distr/*` после релиза.
- Расхождение между seed docs и runtime DB-import.
- Ломка версионного переключателя при нестандартном `source_path`.

## Обязательные проверки
- `vendor/bin/phpunit packages/docara-core/tests`
- Smoke: `/docs/<version>/<locale>`, `/search-index_<locale>.json`, `/vendor/docara/...`.
- В starter: `php artisan larena:doctor --docara`.
- Проверка синка docs при релизе:
  - `packages/docara-core/resources/docs`
  - `../laravel.docara-core/resources/docs`
