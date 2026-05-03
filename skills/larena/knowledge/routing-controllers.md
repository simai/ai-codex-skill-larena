# Маршруты и контроллеры

## Общие правила
- Группируй маршруты по доменным зонам и контекстам доступа.
- Применяй `FormRequest`/валидационные слои на входе.
- Держи контроллеры тонкими, бизнес-логику выноси в сервисы.
- Не смешивай API и UI поведение в одном route-контракте без явной причины.

## Правила SimaiCrud (обязательно для CRUD)
- Для UI CRUD используй `Route::simaiCrud(...)`.
- Для API CRUD используй `Route::simaiApiCrud(...)`.
- Если нужна dual-схема, используй `Route::simaiDualCrud(...)`.

## Настройка регистратора
- Явно задавай:
  - `->param('id')` (или другое имя ключа);
  - `->only([...])` / `->except([...])`;
  - `->extras([...])` для доп. действий;
  - `->names(['api' => '...', 'ui' => '...'])` для предсказуемых имен;
  - `->middleware(['api' => [...], 'ui' => [...], 'any' => [...]])`;
  - `->register()`.
- Для UI-регистратора учитывай where-паттерны:
  - id должен быть ограничен (по умолчанию numeric), чтобы `/create` не матчился как `{id}`;
  - custom slug должен иметь отдельный безопасный pattern.

## Доступы в маршрутах
- Для API-групп используй `['api', 'access.token']`.
- Для entity-действий полагайся на `access.entity:<EntityConfigClass>,<ability>[,<routeParam>]`.
- Проверки доступа должны опираться на `EntityConfig` и operation-коды из module config.

## EntityConfig и custom routes
- Определяй capability map (`create/read/update/delete/status/custom`) централизованно в EntityConfig.
- Для кастомных действий используй `customRoutes()` конфигурации и явные verbs/channels/middleware.
- Не создавай permissive-роуты; ограничивай действия и параметры.

## Контроллерный слой
- CRUD-контроллеры должны работать через общий контракт payload/meta/ui.
- Для админского HTML-рендера используй responder-поток `SimaiResponder`/`AdminResponder`.
- Шаблоны и пресеты выбирай через текущую архитектуру UI drivers, без дублирования layout-логики.
