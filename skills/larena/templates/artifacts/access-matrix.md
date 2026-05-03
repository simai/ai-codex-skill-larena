# Матрица доступа (Access Matrix)

## Контекст (Context)
- Модуль (Module):
- Область (Scope):
- Версия/ветка (Version/Branch):

## Route -> Access mapping
| Маршрут (Route) | Тип (Type: UI/API/CRUD) | Middleware | Операция/Ability (Operation/Ability) | Роли/Токен (Roles/Token) | Ожидаемый статус (Expected Status) |
|---|---|---|---|---|---|
| `GET /...` | API | `access.token` | `module.entity.read` | `manager` | `200` |
| `POST /...` | CRUD | `access.entity` | `store` | `admin` | `201` |

## Негативные сценарии (Negative Scenarios)
| Маршрут (Route) | Без токена/сессии (Unauthorized) | Без права (Forbidden) | Тест-кейс (Test Case) |
|---|---|---|---|
| `POST /...` | `401` | `403` | `Feature\\...Test::test_store_access` |

## Особые правила (Special Rules)
- Bypass/impersonation правила:
- Ограничения на custom actions:
- Откат (Rollback) для access-конфига:
