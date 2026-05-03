# Routing

Choose the smallest sufficient specialist set.

## Work Type Routing

- Entry install/readiness: `package-installer` + `qa-validation`; add `ops-runtime` for host/runtime issues.
- Package diagnostics: `platform-architect` + relevant surface specialist + `qa-validation`.
- New package/module: `platform-architect` + `package-installer` + `security-permissions` + `qa-validation`.
- Modular admin: `modular-admin` + `security-permissions` + `qa-validation`; add `sf5-integration` for layout/components.
- Update server or registration: `update-registration` + `security-permissions` + `ops-runtime` + `qa-validation`.
- SitePack import/export/bridge: `sitepack-bridge` + `data-settings-props`; add `docara-product` for Docara data.
- SF5 runtime/layout: `sf5-integration` + `platform-architect`; add `data-settings-props` for page/layout data.
- REST/OpenAPI: `rest-api` + `security-permissions` + `qa-validation`.
- AI-agent/service architecture, service discovery or module capability manifests: `platform-architect` + `rest-api` + `documentation-learning`; add `security-permissions` when operations can mutate data or cross trust boundaries.
- Settings/storage/props/layout: `data-settings-props` + `platform-architect` + `qa-validation`.
- Docara product proof: `docara-product` + `package-installer` + `qa-validation`; add `sitepack-bridge` for import/export.
- Documentation/skill learning: `documentation-learning`; add domain specialist for subject correctness.
- Deploy/runtime/queues/cron: `ops-runtime` + `qa-validation`; add `package-installer` if install code changes.
- Shared-hosting scheduler/tick/hit-fallback: `ops-runtime` + `rest-api` + `qa-validation`.

## Conflict Rule

If routing selects more than five specialists, split into stages and keep only the current stage active.
