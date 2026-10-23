# Modular Admin

Owns `larena-admin`, CRUD, admin extension model, slots, contributions, manifests, widgets and developer/admin UX.

## Load When

- task touches admin pages, CRUD, navigation registry, route macros (SIMAI-era: `EntityConfig`), widgets, menus, dashboard, settings UI or admin module architecture;
- implementing or reviewing modular admin extension points;
- building admin demonstrators.

## Required Knowledge

- [knowledge/admin-platform.md](../../knowledge/admin-platform.md)
- [knowledge/packages/admin.md](../../knowledge/packages/admin.md)

## Gatekeeper Rules

- Admin is infrastructure core, not the place for monetization policy.
- Prefer typed extension points, slots and contributions over raw HTML or ad hoc Blade injection.
- Disabled modules must publish no admin contributions.
- Contributions must be permission/context-aware.
- Preserve access-aware admin routes and package-owned navigation descriptors; `EntityConfig` and `simaiCrud` macros are SIMAI-era (absent in current `larena/*` packages, checked 2026-10-23) and apply only to old projects.
