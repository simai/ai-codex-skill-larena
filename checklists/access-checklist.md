# Чеклист прав доступа

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
