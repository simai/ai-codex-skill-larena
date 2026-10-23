# Валидация, Request и Resource

> Статус: справка эпохи SIMAI Laravel (пакеты `simai/*`, до `larena/*`). Сверка 2026-10-23: `simaiCrud`, `simai:install`, `EntityConfig`, `config/simai_<module>.php` в текущих пакетах larena-workspace не найдены; текущие имена — команды `larena:*`, конфиги `config/larena-<package>.php`. Метод годится, имена и пути — только для старых проектов и миграции; текущий состав пакетов — [canonical-package-portfolio](../../references/canonical-package-portfolio.md).

## Базовые правила
- Валидацию выполняй через FormRequest/валидаторы, не в контроллере.
- Нормализуй входные данные до бизнес-слоя.
- Держи единый формат ошибок для API.
- Ответы сериализуй через Resources/DTO, а не сырой массив из модели.

## Simai-специфика
- Для CRUD операций синхронизируй validation-правила с EntityConfig writable/fields.
- Для custom CRUD actions задавай отдельные правила валидации.
- Учитывай `ru/en` локализацию пользовательских сообщений об ошибках.

## Типовые риски
- Расхождение валидации UI и API контуров.
- Избыточно permissive payload, который обходит ограничения модели.
- Нестабильные error-payload структуры в разных endpoint-ах.

## Обязательные проверки
- Тесты на validation success/fail для каждого измененного endpoint-а.
- Проверка формата error payload.
- Проверка forbidden/unauthorized веток вместе с validation.
