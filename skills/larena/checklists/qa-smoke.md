# Чеклист дымового тестирования (Laravel монорепа)

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../references/canonical-package-portfolio.md).

- [ ] `composer run validate:repo` прошел
- [ ] `composer run lint:changed` (или `composer run lint`) прошел
- [ ] Таргетные тесты пакета прошли (`vendor/bin/phpunit packages/<module>/tests`)
- [ ] Межмодульные тесты запущены при интеграционном риске (`vendor/bin/phpunit --testsuite=packages`)
- [ ] Изменения поведения отражены в `SPEC.md` и `CHANGELOG.md`
- [ ] Раздел `Migration Notes` добавлен (`No changes`, если неприменимо)
- [ ] Для `larena/rest` пройдены package-owned OpenAPI tests paths/params/access
- [ ] Нет новых внешних CDN/сторонних URL в Blade/JS/CSS
- [ ] Для UI есть локализация минимум `ru` и `en` с паритетом ключей
- [ ] Для новых модулей обеспечен install-flow через `simai:install`
- [ ] Для access-задач заполнен `Access Matrix` и пройден `checklists/access-checklist.md`
