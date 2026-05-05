# UX Implementation Contract

Use this pack when `$larena` implements or reviews an interface designed by `$ux`.

## Rule

Map UX decisions to Larena surfaces before writing UI code. `$ux` defines the scenario and usability contract; `$larena` maps it to package boundaries, routes, views, admin extension points, settings/storage/props/layout persistence, and Laravel runtime constraints.

## Required Mapping

- `Surface`: modular admin page, package settings screen, install/update UI, registration/licensing UI, Docara editor/docs UI, public/admin page, or API-adjacent status screen.
- `Package boundary`: entry app vs `larena/*` package.
- `Route/controller/view`: route name, controller/action, view/component owner, middleware/permission boundary.
- `Data`: fields, validation, persistence target, defaults, reset behavior, props/layout contract.
- `Actions`: save/apply/cancel/reset, install/update/retry, publish/preview/rollback, destructive confirmation.
- `States`: idle, empty, loading/running, diagnostic, validation error, runtime error, success, disabled.
- `Copy`: localization keys, action labels, errors, success messages.
- `Acceptance`: browser/admin scenarios and `$tester` usability gate points.

## Defaults

- Modular admin screens must fit Larena admin navigation and extension slots.
- Settings screens must state where values persist and how defaults/reset work.
- Install/update UI must expose diagnostic, error, retry, and success states.
- Docara UI must account for tree navigation, create/edit/save, preview, revisions, rollback, denial, and cleanup.

## Output Back To `$ux`

If Larena package boundaries change the design, report:

```markdown
UX deviation:
Package/runtime reason:
Alternative:
Retest point:
```
