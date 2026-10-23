# Рабочие сценарии

Используй эту карту маршрутизации, чтобы выбрать минимальный и безопасный workflow.

## Маршрутизация сценариев
- Новое поведение или расширение домена:
  - Загрузи `knowledge/workflows/new-feature.md`
  - Требуй полный контракт (`AC`, checks, `Do Not Touch`, risks, rollback)
- Локальный багфикс или рефакторинг:
  - Загрузи `knowledge/workflows/project-changes.md`
  - Держи минимальный патч и жесткий scope
- API или контрактные изменения:
  - Загрузи `knowledge/workflows/api.md`
  - Включи контракт endpoint-ов и Swagger-проверки
- Изменения схемы или данных:
  - Загрузи `knowledge/workflows/data-migrations.md`
  - Всегда формируй Migration Notes
- Async/event обработка:
  - Загрузи `knowledge/workflows/jobs-queues.md`
  - Обеспечь идемпотентность и обработку retry
- Изменения auth/access:
  - Загрузи `knowledge/workflows/auth-authorization.md`
  - Загрузи `knowledge/access-control.md`
  - Сформируй `Access Matrix` и пройди `checklists/access-checklist.md`
  - Обеспечь проверки permission и негативные тесты
- Performance-оптимизация:
  - Загрузи `knowledge/workflows/performance.md`
  - Покажи измеримый результат до и после
- Итерация, сфокусированная на тестах:
  - Загрузи `knowledge/workflows/testing.md`
  - Сформируй QA Report и regression checklist
- Документационная задача:
  - Загрузи `knowledge/workflows/documentation.md`
  - Используй шаблоны из `templates/wiki/*`
- Release of a canonical Workspace package into the Root distribution:
  - Загрузи `knowledge/workflows/release.md`
  - Загрузи `knowledge/deployment-ops.md`
  - Pin the accepted package revision in Root and run the Root acceptance gate
- Работа в конкретном пакете:
  - Загрузи паспорт модуля из `knowledge/packages/*` (например, `admin.md`, `access.md`, `docara.md`)
  - Проверь инварианты/риски до внесения правок

## Проектные ограничения
- Сначала прочитай `playbook/00_ROUTER.md`, `playbook/01_CORE.md`, `playbook/15_ITERATION_PROTOCOL.md`.
- Обновляй `SPEC.md` и `CHANGELOG.md` при изменении поведения.
- Запускай релевантные verification gates до завершения задачи.
