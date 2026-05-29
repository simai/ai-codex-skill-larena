# ai-codex-skill-larena

Репозиторий skill `$larena` для Larena как SIMAI Laravel CMS/application
platform.

Runtime skill находится в:

```text
skills/larena/
```

## GrowGraph

Репозиторий содержит repo-local GrowGraph companion layer:

```text
graph/source/growgraph/      seeds, migration notes, review inputs
graph/generated/growgraph/   adoption, semantic, effectiveness, gate reports
graph/federation/exports/    bounded federation exports
```

Проверка локального GrowGraph-контракта:

```bash
python3 scripts/growgraph_contract_gate.py
```

## Обслуживание

- Новые рабочие заметки и raw source держите в ignored `source/`.
- Новые устойчивые правила добавляйте в самое узкое место внутри
  `skills/larena/`, а не раздувайте `SKILL.md`.
- Реальные доступы, production exports и клиентские raw данные не коммитятся.
