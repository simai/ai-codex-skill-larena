# Admin Platform

Target model: `Admin Kernel + Module Extensions`.

Canonical DNA:

- `simai/larena/docs/developer/dna/admin-dna.md`
- `simai/larena/docs/developer/dna/layout-dna.md`

`larena/admin` is the object-based admin interface platform, not a collection of hardcoded Blade screens. Packages extend it through governed areas, slots, contributions, renderers, context and manifest metadata.

Contract rule:

- `module.yaml.admin` is a package summary/link layer.
- Simple packages may declare a small menu/page summary in `module.yaml.admin`.
- Complex package UI should use `admin.yaml` as the source contract for areas, slots, contributions, renderers, actions and diagnostics.
- Security Admin UX is a specialized security/runtime surface that uses the common admin contribution model; it is not a separate generic admin generator.
- Third-party packages must extend admin through `larena/admin` contributions, never by editing admin shell/templates directly.

Future `larena/layout` shares the same composition philosophy but owns public/content page composition: pages, sections, atomic blocks, data providers, renderers and editor schemas. The admin may host the layout editor, but the page/layout model must remain a separate package domain.

## Core Terms

- Package: Composer package.
- Module: logical installed/managed unit known by admin runtime.
- Extension Point: named place where modules can contribute UI/behavior.
- Slot: concrete placement inside an extension point.
- Contribution: module-owned item added into a slot.
- Renderer: renders a contribution type.
- Context: runtime data for visibility, permissions and rendering.
- Manifest: module-declared metadata and contributions.

## Module Statuses

- `discovered`
- `installed`
- `enabled`
- `disabled`
- `upgrading`
- `broken`
- `removed`

## Extension Points And Slots

Examples:

- navigation;
- dashboard;
- profile;
- resource-page;
- settings;
- widget-area;
- action-area.

Example slots:

- `layout.sidebar.start`
- `dashboard.widgets.main`
- `profile.preferences`
- `resource.posts.form.sidebar`

## Contribution Types

- `NavGroup`
- `NavItem`
- `ProfileSection`
- `PageBlock`
- `Widget`
- `Action`
- `PageTab`
- `FormField`
- `Text`
- `Link`
- `BladeView`
- `Component`
- restricted `Html`

## Invariants

- A contribution belongs to one module and one slot.
- Disabled modules publish no contributions.
- Visibility is permission/context-aware.
- Raw HTML is not a normal extension mechanism.
- Admin core must not hardwire paid/free product logic.
- Host projects and product packages must not edit or copy `vendor/larena/admin` source. Extensions go through typed contracts, project config/routes, or separate Composer packages.
- Long-running admin operations should use `AdminBatch`, queues or commands with progress/failure diagnostics. Never treat a `202 Accepted`, `batch_id` or `async: true` label as proof of isolation: verify that heavy work is dispatched to a real queue/job and not executed inside the web request.
- Generic admin bulk actions are bounded sync by default. If `async: true` is present without a real queue/job payload, the package should fail closed or require an explicit `sync=true` fallback; it must not silently run fake async in the HTTP request.
- Route ownership, plugin health and admin smoke commands are release gates for packages that contribute admin routes/UI.
- Admin packages must publish every asset referenced by shared layouts. Even harmless missing `/simai/admin/*` assets, such as a favicon, create browser noise and can mask real admin errors during smoke checks.
- Current favicon baseline is `/simai/admin/images/favicon.ico`; do not reference `/simai/admin/images/favicon.png` unless the package ships that file.
- Development/debug logs in admin CRUD, validators or renderers must be gated by package config and should use a package-specific channel. The current baseline is `AdminDevelopmentLogger` with `simai_admin.development_logs.*`, disabled by default.
- Package-local admin tests should use a stable bootstrap/harness that resolves
  sibling Larena packages from the exact active Workspace profile. Do not add
  retired naming aliases such as `larena-2fa`; MFA tests resolve canonical
  `larena/auth`. Avoid one-off temporary bootstrap files as the only path to
  full-suite execution.
- Treat `simai/admin`, `Simai\Admin`, `simai_admin`, `/simai/admin`, legacy plugin API, access code aliases and the fail-open bootstrap switch as explicit compatibility surfaces. They must be tracked in `docs/developer/legacy/registry.json` and not removed during routine L4 standardization.

## Security Admin UX

When designing or auditing admin surfaces for `auth`, `access`, `audit`, `rest`, `mcp`, settings/security policy, update/licensing capabilities or package exposure, use the Security Admin UX contract from `simai/larena/docs/developer/admin/security-admin-ux-tz.md`.

Security UI must not expose the operator to a raw table of hundreds of scopes as the primary model. The first UX layer should be:

```text
EntryObject / access target
  -> package
  -> profile or preset
  -> operation overrides only when needed
  -> effective preview
  -> explain
  -> audit trail
```

Security admin actions must follow the runtime lifecycle:

```text
admin intent
  -> contribution/action metadata
  -> auth EntryObject
  -> token/session/channel constraints
  -> access operation check
  -> safety warning/fresh auth if needed
  -> backend action
  -> audit event
  -> explain/result state
```

Do not treat hidden UI as a security boundary. Every security write action must repeat backend permission checks and produce audit where required.

## Current Core Package Gaps To Watch

- Final package contribution manifest is not yet fully connected to `module.yaml` capability metadata.
- AI-readable admin capabilities and safe admin tool metadata are not finalized.
- Production defaults for access fail-open, demo showcase and plugin boot policy require environment-aware decisions.

Developer demonstrator target: show registered areas/slots and allow adding sample contribution data into an area.
