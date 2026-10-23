# Чеклист миграций

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../references/canonical-package-portfolio.md).

- [ ] Миграции идемпотентны
- [ ] Rollback возможен
- [ ] Индексы и уникальность учтены
- [ ] План backfill определен
- [ ] Миграции безопасны для `simai:install` сценария
