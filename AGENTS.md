# AGENTS.md

## Larena Skill Routing

Работай на русском, если пользователь не переключился на другой язык.

Этот репозиторий содержит SIMAI skill `larena`. `$larena` остаётся владельцем
Larena-смысла: Laravel CMS/application platform, Larena packages, modular
admin, installer/update flows, registration/licensing, SitePack bridge, Docara
product proof, REST/API safety, settings/storage/props/layout/search,
migrations, release readiness and QA.

`GrowGraph` используется как companion layer для структуры, связей,
adoption/readiness, semantic preservation, effectiveness и federation
contracts. Он не заменяет `SKILL.md`, `kernel/`, `rules/`, `activities/`,
`specialists/`, `knowledge-packs/`, `knowledge/`, `modules/`, `quality/` и
templates.

## GrowGraph Rules

- Не считать repo-local GrowGraph migration успешной только из-за валидного
  JSON.
- Не переписывать `skills/larena/SKILL.md` массово из generated artifacts.
- Generated candidates из `graph/generated/` не являются canonical truth.
- Larena domain ownership stays with `$larena`; `$graph` owns graph structure
  and gates only.
- Do not collapse Larena into generic Laravel, Bitrix, SF5 or Docara ownership;
  use companion contracts instead.
- Canonical changes in `graph/specs/` require an apply plan, validation and a
  rollback path.
- If semantic preservation, effectiveness, federation export or integration
  review is missing, do not claim `GGA9` or graph-first repository migration.

## Required Gate

Before claiming GrowGraph integration for this repository, run:

```bash
python3 scripts/growgraph_contract_gate.py
```

The GitHub workflow also runs this gate after ordinary repository checks.

## Current Repo-Local GrowGraph Scope

Current migration scope:

```text
skill:larena
```

Canonical repo-local graph root:

```text
graph/
```

Current GrowGraph artifacts:

```text
graph/source/growgraph/seeds/
graph/generated/growgraph/
graph/federation/exports/
```

This repository is allowed to export a bounded federation contract after the
semantic and effectiveness gates pass.
