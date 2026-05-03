# Контур прав доступа (Simai)

## Цель
Сделать проверки доступа предсказуемыми и проверяемыми для UI/API/CRUD сценариев.

## Единая модель
- Статические операции: `access:<operation_code>`.
- API-токены: `access.token[:operation_code]`.
- Entity-aware действия: `access.entity:<EntityConfigClass>,<ability>[,<routeParam>]`.
- Источник operation-кодов: `config/simai_<module>.php` (`operations`, `accesses`, `access_levels`).

## Привязка маршрутов к проверкам
- API endpoint:
  - middleware: `['api', 'access.token']`
  - операция: через operation-code или entity-ability.
- UI/CRUD endpoint:
  - middleware: `access.entity` через регистраторы `simaiCrud/simaiApiCrud`.
  - ability: `index/show/store/update/destroy/status/reorder/custom`.

## Конвенция operation-code
- Формат: `<module>.<entity>.<action>` (например, `docara.pages.update`).
- Код должен быть стабильным и человекочитаемым.
- Не допускается дублирование одного и того же кода с разной семантикой.

## Минимум тестов на каждый защищенный action
1. `unauthorized` (`401`) для отсутствующего/некорректного токена.
2. `forbidden` (`403`) для пользователя без нужного права.
3. `allowed` (`2xx`) для пользователя/токена с нужным правом.
4. Для custom action: отдельный негативный и позитивный тест.

## Антипаттерны
- Проверять права только в контроллере без middleware.
- Хардкод operation-кодов в нескольких местах без конфига.
- Отсутствие негативных тестов (есть только happy path).
- Непрозрачные bypass-правила без audit-логов.

## Артефакт для задач
- Обязательно формируй `Access Matrix` по шаблону:
  - `templates/artifacts/access-matrix.md`
- Перед завершением задачи проходи:
  - `checklists/access-checklist.md`
