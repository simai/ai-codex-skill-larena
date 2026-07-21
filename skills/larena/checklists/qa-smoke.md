# Чеклист дымового тестирования (Laravel монорепа)

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
