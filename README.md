# ai-skill-larena

Репозиторий skill `$larena` для Larena как SIMAI Laravel CMS/application
platform.

Runtime skill находится в:

```text
skills/larena/
```

## Mirai Graph

Репозиторий содержит repo-local Mirai Graph companion layer:

```text
mirai/graph/source/mirai-graph/      seeds, migration notes, review inputs
mirai/graph/generated/mirai-graph/   adoption, semantic, effectiveness, gate reports
mirai/graph/federation/exports/    bounded federation exports
```

Проверка локального Mirai Graph-контракта:

```bash
python3 scripts/mirai_graph_contract_gate.py
```

## Обслуживание

- Новые рабочие заметки и raw source держите в ignored `source/`.
- Новые устойчивые правила добавляйте в самое узкое место внутри
  `skills/larena/`, а не раздувайте `SKILL.md`.
- Реальные доступы, production exports и клиентские raw данные не коммитятся.
