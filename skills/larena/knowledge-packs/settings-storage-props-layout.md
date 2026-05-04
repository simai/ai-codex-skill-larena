# Settings Storage Props Layout

Larena should align with Bitrix/SF5 concepts while staying Laravel-native.

## Settings

Reference direction from Bitrix `simai.main`:

- schema;
- value;
- history;
- pending;
- scoped resolver;
- facade API;
- import/export;
- explainable direct vs resolved values.

Larena question: evolve `larena/setting` toward this model or split lower-level platform settings package.

## Universal Properties

Bitrix `simai.property` is a reference for reusable property controls in view/edit/filter contexts.

Observed types include:

- entity;
- URL;
- file;
- color;
- checkbox;
- sort;
- link;
- phone;
- map.

Larena should separate property storage, UI render/edit/filter contracts and CRUD integration.

Current `larena/props` is a file-based property type/template package, not the final universal property value model. It ships JSON definitions, translations and Blade templates and exposes admin template editing/import/export.

When inspecting or extending `larena/props`, require an explicit safety gate before functional growth:

- do not treat submitted translation/template content as safe executable code;
- replace or gate `eval()`-style parsing;
- restrict template save paths to approved roots;
- harden ZIP import with canonical path checks and extension allowlists;
- protect admin routes with explicit `larena/access` operations, not only generic `auth`;
- add audit/rollback for executable Blade template edits;
- keep SitePack mapping separate until property schema and entity-bound values are accepted.

## Storage

Storage 2.0 reference:

- storage registry metadata, not arbitrary user-data table;
- stable `code`;
- active/sort;
- MV profile;
- encryption flag;
- element-level ACL flag;
- logging flag;
- `settings_json`;
- audit fields.

Compare with Larena filesystem/assets and SitePack SHA-256 blob conventions.

## Layout

Reference model: `Atomic Block -> Section -> Page`.

Larena page builder should map:

- data provider;
- view;
- renderer;
- SF5 components/smart components;
- machine-readable specs for editor/developer/AI workflows.
