# Larena UI And Admin Components

> Источник: simai/larena-ui `README.md`, simai/ui-admin `README.md`, larena `git log` · Проверено: 2026-10-23 · Версия: larena-ui 51cf18f, ui-admin 3326a35, larena bce7b637

Where Larena's frontend comes from and who owns which side. The source moved
twice in October 2026 — re-check before naming a repository.

## Two parts

| Part | What | Where |
| --- | --- | --- |
| `larena/ui` (Composer package) | `SmartRegistry` with ten canonical manifests (`ui.button`, `ui.input`, `ui.textarea`, `ui.checkbox`, `ui.dropdown`, `ui.dataview`, `ui.pagination`, `ui.badge`, `ui.alert`, `ui.modal`), `Smart::render(...)`, asset activation via `core.assets`, catalog projections for people and AI | repository `simai/larena-ui` |
| component package `larena` (admin kit) | admin Smart components `sf-table`, `sf-data-view`, `sf-property-view`, `sf-admin-menu` | source: `simai/ui-pro` (since 2026-10-23); before — `simai/ui-admin` (2026-10-22), before that `simai/larena-ui/components` |

Built kit archives (`package-larena.tar` with sha256 and receipt) are still
published as releases of `simai/larena-ui`; Larena's installer and checks
fetch them there. `simai/ui-admin` stays the reference host and polygon
(mock API, seeded records of every property type) on which the components are
tried.

## How Root pins it

- Root pins a Framework pair: a Framework build id (`ui-…`) plus a kit id
  (`larena-…`); commits read "Pin the admin kit larena-<id> over ui-<id>".
- The frontend runtime lock pins packages by name; install, update and sealing
  refuse a runtime whose lock does not cover every declared component set.
- Kits carry SPDX licence expressions; the admin kit is included in Larena's
  licence (PolyForm terms apply outside Larena).

## Ownership

- `$framework` — Framework core, components, kit build and release, docs at
  ui.simai.io.
- `$larena` — host side: ports (data view, property view), lookup sources,
  rights, refusal messages, what the admin shows; Root pins and gates.
- `$designer` / `$ux` — visual QA and screen structure.

Licensing and source-repository choices are owner decisions; record them, do
not infer them from a commit.
