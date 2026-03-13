# Деплой и эксплуатация

## Базовые рекомендации
- Проверяй миграции на staging.
- Делай безопасный rollout с контролируемым scope.
- Всегда имей проверяемый rollback-план.

## Вариант релизной команды (монорепа -> репозиторий модуля -> тег)

Используй скрипт:
- `tools/release_module.sh`

Он выполняет:
1. commit/push в монорепу в пределах релизного scope (всегда исключает `packages/rest`);
2. синхронизацию `packages/<module>/` в выделенный репозиторий модуля (`../laravel.<module>` по умолчанию);
3. commit/push в репозиторий модуля;
4. создание и push тега (по умолчанию следующий patch от последнего тега);
5. опциональное обновление `bitrix-update` до нового тега пакета.

Пример (автотег от последнего):
```bash
tools/release_module.sh \
  --module docara-core \
  --mono-branch main \
  --module-branch master \
  --mono-commit "chore(release): docara-core monorepo sync" \
  --module-commit "chore(release): docara-core 1.0.x" \
  --bitrix-update-path ../bitrix-update
```

Пример (явный тег):
```bash
tools/release_module.sh \
  --module docara-core \
  --repo ../laravel.docara-core \
  --tag 1.0.54 \
  --bitrix-update-path ../bitrix-update \
  --composer-package simai/docara-core
```

## Безопасный режим
- Перед запуском используй:
  - `tools/release_module.sh --module <module> --dry-run`
- Скрипт проверяет scope изменений в монорепе.
- Если есть нерелевантные изменения, релиз блокируется.
- Для осознанного обхода блокировки используй:
  - `--allow-unrelated`

## Docara: обязательный синк документации после релиза

После релиза `docara-core` синхронизируй docs в выделенном репозитории:
- источник в монорепе: `packages/docara-core/resources/docs`
- целевой путь: `../laravel.docara-core/resources/docs`

В скрипте это делается автоматически для `--module docara-core` (`--sync-docara-docs auto`).
Для принудительного режима используй:
- `--sync-docara-docs yes`

## Релизные данные, которые нужно зафиксировать
- Monorepo commit hash + branch.
- Module repo commit hash + tag.
- Результат обновления зависимостей в `bitrix-update` (точный вывод `composer update/require`).
- Для Docara-задач: синхронизация `docs/DOCARA_ISSUE_LOG.md` и `docs/DOCARA_DEVELOPMENT_LOG.md`.

## Минимальный релизный чеклист
- Используй `checklists/release-checklist.md`.
