# Admin Platform

Target model: `Admin Kernel + Module Extensions`.

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
- Long-running admin operations should use `AdminBatch`, queues or commands with progress/failure diagnostics.
- Route ownership, plugin health and admin smoke commands are release gates for packages that contribute admin routes/UI.

## Current Core Package Gaps To Watch

- Final package contribution manifest is not yet fully connected to `module.yaml` capability metadata.
- AI-readable admin capabilities and safe admin tool metadata are not finalized.
- Production defaults for access fail-open, demo showcase and plugin boot policy require environment-aware decisions.

Developer demonstrator target: show registered areas/slots and allow adding sample contribution data into an area.
