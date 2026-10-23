# Знания навыка larena — единый слой

> Источник: этот каталог; состав пакетов — larena-specs и larena `composer.json` · Проверено: 2026-10-23 · Версия: ai-skill-larena (перенос слоёв), larena-specs a19a9f10a, larena bce7b637

До 2026-10-23 знания лежали в трёх местах: `knowledge/`, `knowledge-packs/`,
`modules/`. Теперь всё в `knowledge/`; содержимое перенесено без потерь
(`git log --follow` показывает историю). Имя из `knowledge_packs` в
`activities/*.json` — это файл `knowledge/<имя>.md`.

Сначала факты, потом метод: состав пакетов и версии — только из
[../references/canonical-package-portfolio.md](../references/canonical-package-portfolio.md)
и из самих источников. Файлы с пометкой «справка эпохи SIMAI Laravel»
описывают старые пакеты `simai/*` — метод годится, имена нет.

## Платформа Larena (актуальные стандарты)

- Состав и карта пакетов: [package-map.md](./package-map.md)
- Архитектура продукта: [product-architecture.md](./product-architecture.md),
  [core-platform.md](./core-platform.md), [admin-platform.md](./admin-platform.md),
  [access-platform.md](./access-platform.md), [search-platform.md](./search-platform.md)
- Настройки, хранилище, свойства, layout: [settings-storage-props-layout.md](./settings-storage-props-layout.md),
  каталог настроек по уровням и раздел «Хранилище»: [settings-catalog-and-storage-admin.md](./settings-catalog-and-storage-admin.md)
- Фронтенд и компоненты админки (`larena/ui`, набор `larena`): [larena-ui-components.md](./larena-ui-components.md),
  слои `/simai` ↔ Larena: [simai-layer-dna.md](./simai-layer-dna.md)
- Обновления и регистрация: [update-registration.md](./update-registration.md)
- SitePack: [sitepack-bridge.md](./sitepack-bridge.md); Docara: [docara-proof.md](./docara-proof.md)
- REST: [rest-safety.md](./rest-safety.md); ИИ-сервисы: [ai-agent-service-architecture.md](./ai-agent-service-architecture.md)
- Локализация: [localization.md](./localization.md); UX-контракт: [ux-implementation-contract.md](./ux-implementation-contract.md)
- Хостинг и фоновые задачи: [ordinary-hosting-scheduler.md](./ordinary-hosting-scheduler.md),
  [session-safe-background-enrichment.md](./session-safe-background-enrichment.md)

## Стандарты пакета

[module-yaml-standard.md](./module-yaml-standard.md),
[package-naming-standard.md](./package-naming-standard.md),
[package-repository-structure.md](./package-repository-structure.md),
[package-pre-codegen-repository-preparation.md](./package-pre-codegen-repository-preparation.md),
[package-tz-standard.md](./package-tz-standard.md),
[package-completion-standard.md](./package-completion-standard.md),
[feature-graph.md](./feature-graph.md),
[legacy-detection-patterns.md](./legacy-detection-patterns.md).

## Процесс работы

[larena-goal-execution-profile.md](./larena-goal-execution-profile.md),
[developer-feedback-intake-protocol.md](./developer-feedback-intake-protocol.md),
[deployment-ops.md](./deployment-ops.md) (продвижение пакета Workspace → Root),
[documentation.md](./documentation.md) (где живут документы),
[work-scenarios.md](./work-scenarios.md) → сценарии в [workflows/](./workflows/)
(api, new-feature, project-changes, data-migrations, jobs-queues,
auth-authorization, performance, testing, documentation, release).

## Паспорта пакетов

[packages/](./packages/): admin, access, rest, lang, docara; `docara-core`,
`docara-admin`, `rest-doc` — архивные идентичности.

## Справка эпохи SIMAI Laravel

- Общий Laravel с поправками на старые `simai/*`: [laravel/](./laravel/).
  Общая разработка на Laravel — у `$dev`; здесь держим только то, что нужно
  для старых проектов и миграции на `larena/*`.
- [simai-package-rules.md](./simai-package-rules.md), [quickstart.md](./quickstart.md),
  [access-control.md](./access-control.md), [auth-authorization.md](./auth-authorization.md),
  [testing.md](./testing.md).
