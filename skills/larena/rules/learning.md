# Learning

When a reusable Larena lesson appears, store it at the narrowest useful level:

- product/platform invariant -> `kernel/` or `knowledge-packs/product-architecture.md`;
- routing or workflow rule -> `rules/` or `activities/`;
- package implementation detail -> `knowledge/modules/*` or a package-specific knowledge pack;
- admin/update/SitePack/REST/settings rule -> the matching specialist or knowledge pack;
- one-off project fact -> project repo `source/memory/`, not this skill.

Do not put secrets, raw logs, raw chat exports, temporary credentials, or unverified plans into the skill.

After editing the skill, verify:

- `SKILL.md` frontmatter still names `larena`;
- references point to existing files;
- `agents/openai.yaml` default prompt mentions `$larena`;
- the installed symlink points to this repository.
