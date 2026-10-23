# Чеклист прав доступа

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../references/canonical-package-portfolio.md).

- [ ] Есть инвентарь защищенных маршрутов (UI/API/CRUD) и он актуален
- [ ] Для каждого маршрута определен middleware: `access` / `access.token` / `access.entity`
- [ ] Для каждого маршрута определен operation-code или entity ability
- [ ] Operation-коды объявлены в `config/simai_<module>.php` и не хардкодятся хаотично
- [ ] Для SimaiCrud действий настроен ability map в `EntityConfig`
- [ ] На каждый критичный action есть тест `401` (unauthorized)
- [ ] На каждый критичный action есть тест `403` (forbidden)
- [ ] На каждый критичный action есть тест успешного доступа (`2xx`)
- [ ] Для custom action есть отдельные позитивный и негативный тесты
- [ ] Любые bypass-правила (service token/impersonation) задокументированы и покрыты тестом
- [ ] `Access Matrix` заполнен и приложен к отчету
