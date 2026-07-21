# Деплой и эксплуатация

## Базовые рекомендации
- Проверяй миграции на staging.
- Делай безопасный rollout с контролируемым scope.
- Всегда имей проверяемый rollback-план.

## Canonical package promotion

Larena uses three authoritative contours:

1. `larena-specs` for product and package contracts;
2. `larena-workspace/packages/<slug>` for the canonical package source;
3. Root `larena` for distribution, exact dependency revisions and acceptance.

Do not publish by copying a Workspace package into a second top-level
`laravel.<module>` repository. Do not route Larena releases through
`bitrix-update`. Old commands that did so are historical evidence only.

For a package promotion:

1. gate and validate the package in its canonical Workspace checkout;
2. commit and push the exact package revision without history rewrite;
3. update Root Composer lock and release manifest to that same revision;
4. run the full Root acceptance matrix and retain evidence;
5. update Specs only when the product contract changed;
6. tag or release only under an explicit release gate;
7. keep a tested rollback to the previous Root lock/manifest.

For Docara, package documentation stays in `packages/docara`; cross-package
contracts stay in Specs. Never synchronize to retired `docara-core` or
`docara-admin` repositories.

## Релизные данные, которые нужно зафиксировать
- Package repository commit hash and branch.
- Root lock/manifest commit and full acceptance evidence.
- Specs revision when the product contract changed.
- Optional tag/release receipt and tested rollback.

## Минимальный релизный чеклист
- Используй `checklists/release-checklist.md`.

## Клиентские репозитории `client-*`

Когда Larena/Laravel доработка выполняется в клиентском репозитории `client-*`,
это проектная поставка, а не выпуск reusable package по умолчанию. Используй
общий стандарт:

`/Users/rim/Documents/GitHub/ai-codex-skill-teamlead/docs/client-project-repository-standard.md`

Правила:

- `project/files/` зеркалит корень приложения: `app/`, `routes/`,
  `resources/`, `config/`, `database/migrations/`, если эти файлы являются
  частью поставки;
- `project/migrations/` хранит одноразовые backfill/repair скрипты и операции,
  которые не должны становиться частью обычного Laravel migration lifecycle;
- `deploy/` хранит inventory, backup, deploy, smoke, rollback, cache clear,
  `composer dump-autoload`, frontend build/sync и artisan-команды;
- `docs/` фиксирует архитектуру, deploy, rollback, operations и handoff;
- `source/` остается ignored для intake, evidence, logs, raw client materials и
  временных отчетов.

Если проектная доработка стала reusable package, вынеси core в отдельный
пакетный репозиторий, а в `client-*` оставь adapter/config/migrations/deploy.
