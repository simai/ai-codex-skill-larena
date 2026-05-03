# Modular Admin

Owns `larena-admin`, CRUD, admin extension model, slots, contributions, manifests, widgets and developer/admin UX.

## Load When

- task touches admin pages, CRUD, `EntityConfig`, route macros, widgets, menus, dashboard, settings UI or admin module architecture;
- implementing or reviewing modular admin extension points;
- building admin demonstrators.

## Required Knowledge

- [knowledge-packs/admin-platform.md](../../knowledge-packs/admin-platform.md)
- [knowledge/modules/admin.md](../../knowledge/modules/admin.md)

## Gatekeeper Rules

- Admin is infrastructure core, not the place for monetization policy.
- Prefer typed extension points, slots and contributions over raw HTML or ad hoc Blade injection.
- Disabled modules must publish no admin contributions.
- Contributions must be permission/context-aware.
- Preserve CRUD through `EntityConfig` and access-aware route macros when applicable.
