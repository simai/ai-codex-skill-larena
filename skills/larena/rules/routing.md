# Routing

Choose the smallest sufficient specialist set.

## Work Type Routing

- Entry install/readiness: `package-installer` + `qa-validation`; add `ops-runtime` for host/runtime issues.
- Package diagnostics: `platform-architect` + relevant surface specialist + `qa-validation`.
- New package/module: `platform-architect` + `package-installer` + `security-permissions` + `qa-validation`.
- Modular admin: `modular-admin` + `security-permissions` + `qa-validation`; add `framework-integration` for layout/components.
- Update server or registration: `update-registration` + `security-permissions` + `ops-runtime` + `qa-validation`.
- SitePack import/export/bridge: `sitepack-bridge` + `data-settings-props`; add `docara-product` for Docara data.
- SIMAI Framework runtime/layout, `larena/ui`, admin component kit: `framework-integration` + `platform-architect`; add `data-settings-props` for page/layout data. Component fixes themselves go to `$framework`.
- REST/OpenAPI: `rest-api` + `security-permissions` + `qa-validation`.
- AI-agent/service architecture, service discovery or module capability manifests: `platform-architect` + `rest-api` + `documentation-learning`; add `security-permissions` when operations can mutate data or cross trust boundaries.
- Settings/storage/props/layout: `data-settings-props` + `platform-architect` + `qa-validation`.
- Docara product proof: `docara-product` + `package-installer` + `qa-validation`; add `sitepack-bridge` for import/export.
- Documentation/skill learning: `documentation-learning`; add domain specialist for subject correctness.
- Deploy/runtime/queues/cron: `ops-runtime` + `qa-validation`; add `package-installer` if install code changes.
- Shared-hosting scheduler/tick/hit-fallback: `ops-runtime` + `rest-api` + `qa-validation`.

## Conflict Rule

If routing selects more than five specialists, split into stages and keep only the current stage active.

## Activity Fallback

Use [../activities/activity-registry.json](../activities/activity-registry.json)
as the first routing layer. If no activity matches, create a temporary activity
with `activity_id`, `title`, `triggers`, `required_specialists`,
`optional_specialists`, `knowledge_packs`, `required_gates` and
`required_outputs`.

## Load Discipline

Load only the selected specialist profiles
([../references/specialist-roster.md](../references/specialist-roster.md)) and
the knowledge packs they reference. Do not load every reference file.
An activity's `knowledge_packs` name resolves to `knowledge/<name>.md`; the
index of the single knowledge layer is [../knowledge/README.md](../knowledge/README.md).

For simple edits, one primary specialist plus `qa-validation` is enough. For
install/update, licensing, SitePack, REST safety, admin architecture or product
proof work, use explicit gatekeepers.
