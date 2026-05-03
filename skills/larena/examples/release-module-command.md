# Пример: команда релиза одного модуля

## Цель
Сделать релиз одного пакета через монорепу и выделенный репозиторий модуля с новым тегом.

## Команда
```bash
# сначала проверка плана
tools/release_module.sh \
  --module docara-core \
  --repo ../laravel.docara-core \
  --tag 1.0.54 \
  --bitrix-update-path ../bitrix-update \
  --composer-package simai/docara-core \
  --dry-run

# потом фактический запуск
tools/release_module.sh \
  --module docara-core \
  --repo ../laravel.docara-core \
  --mono-branch main \
  --module-branch master \
  --mono-commit "chore(release): sync docara-core from monorepo" \
  --module-commit "chore(release): publish docara-core" \
  --tag 1.0.54 \
  --sync-docara-docs yes \
  --bitrix-update-path ../bitrix-update \
  --composer-package simai/docara-core \
  --bitrix-branch master \
  --bitrix-commit "chore(release): bump simai/docara-core to 1.0.54"
```

## Что делает команда
1. Делает commit+push в монорепу (исключая `packages/rest`).
2. Копирует `packages/docara-core/*` в `../laravel.docara-core/*`.
3. Синхронизирует docs:
   - `packages/docara-core/resources/docs`
   - `../laravel.docara-core/resources/docs`
4. Делает commit+push в `../laravel.docara-core`.
5. Создаёт и пушит tag `1.0.54`.
6. Выполняет `composer require simai/docara-core:1.0.54 -W --no-interaction` в `bitrix-update`.

## Что зафиксировать после
- Monorepo commit hash и branch.
- Commit и tag в `laravel.docara-core`.
- Результат обновления `bitrix-update` (`composer require simai/docara-core:1.0.54 -W` или `composer update ...`).
- Обновление `docs/DOCARA_ISSUE_LOG.md` и `docs/DOCARA_DEVELOPMENT_LOG.md`.
