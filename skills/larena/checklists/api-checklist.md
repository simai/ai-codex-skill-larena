# Чеклист API

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../references/canonical-package-portfolio.md).

- [ ] Контракт ответа задокументирован
- [ ] HTTP-статусы корректны
- [ ] Ошибки в едином формате
- [ ] Аутентификация и авторизация проверены
- [ ] Для защищенных маршрутов применен `access.token`/`simai/access`
- [ ] На каждый защищенный endpoint есть тесты `401` (unauthorized), `403` (forbidden), `2xx` (allowed)
- [ ] Для custom action есть отдельные негативный и позитивный тесты доступа
- [ ] `Access Matrix` заполнен и синхронизирован с маршрутами/конфигом операций
- [ ] Нет внешних CDN/сторонних URL в API-документации
