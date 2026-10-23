# Canonical Larena Package Portfolio

> Источник: larena-specs `specs/registry.json`, larena `composer.json` / `composer.distribution.json` / `composer.lock`, larena-workspace `packages/` · Проверено: 2026-10-23 · Версия: larena-specs a19a9f10a, larena bce7b637, larena-workspace 0e1932e

This reference supersedes historical package lists embedded in older Larena
knowledge. Verify it against the current project before making a readiness or
release claim: the portfolio changes every few weeks.

## Как перепроверить (одна команда на источник)

```bash
# портфель: число и статусы пакетов в Specs
python3 -c "import json;p=json.load(open('specs/registry.json'))['packages'];print(len(p));print(sorted(x['slug'] for x in p))"   # в larena-specs
# сборка: пакеты larena/* в Root (require + require-dev)
python3 -c "import json;d=json.load(open('composer.json'));print(sorted(k for k in {**d['require'],**d.get('require-dev',{})} if k.startswith('larena/')))"   # в larena
```

## Состояние на 2026-10-23

Platform: Laravel `^13.8` (lock: `laravel/framework` v13.22.0), PHP `^8.3`.
Root identity: `simai/larena`.

**Portfolio (Specs): 44 unique `larena/*` packages** — 31 `pilot`, 13 `draft`.
New since the July baseline: `larena/security`, `larena/telephony` (both
`draft`).

Draft 13:

```text
ai ai-provider chat secret security telephony visibility workflow
workflow-amocrm workflow-bitrix24 workflow-email workflow-github workflow-messenger
```

**Assembly (Root Composer): 26 packages**, all pinned in `composer.lock`;
`composer.distribution.json` carries the same 26. In `composer.json` eight are
in `require` (admin auth dataview layout monitoring notification storage ui),
eighteen in `require-dev`.

```text
access admin audit auth backup cockpit core dataview file-manager filesystem
lang layout licensing link monitoring notification property queue rest
scheduler search secret setting storage ui update
```

Changes against July: `monitoring`, `notification`, `queue`, `scheduler`,
`secret` joined the assembly (`secret` — with field encryption, 2026-10);
`content` and `docara` are no longer in it.

**Workspace-only: 18 packages**

```text
ai ai-provider automation chat content docara mcp security telephony
update-client update-registration visibility workflow workflow-amocrm
workflow-bitrix24 workflow-email workflow-github workflow-messenger
```

`larena/content` is retired by owner decision (2026-09-23, recorded in its
Specs DNA): it must not create base records, revisions, site structure or
publication state — `larena/storage` owns them. Keep `content` only as a
compatibility/migration reference.

### Known lag between sources

- larena `README.md` still says 25 runtime packages of 42;
- `release/developer-alpha-manifest.json` (release `update-safety-center-2026-08-02`)
  says portfolio 40, assembly 26, workspace-only 14;
- Specs say 44. Per the authority order below, Specs and Composer win; report
  the lag instead of copying any of these numbers into a readiness claim.

This partition is membership evidence, not a production-readiness or
all-packages-readiness claim. Root itself states it is not production-ready.

## MFA ownership

`larena/auth` is the sole package owner of authentication methods, sessions,
MFA/TOTP, recovery codes, challenges and assurance state. Root may provide a
Laravel adapter for an Auth-owned cryptographic secret-protection contract; it
does not create another domain owner.

`larena/two-fa` and the local alias `larena-2fa` are retired. They may appear in
historical changelog, recovery bundle, migration evidence or a deliberately
bounded legacy service compatibility record only. Never add either identity to
Specs, Workspace packages, Root requirements, Composer lock, a new worktree or
a new product track.

## Other retired identities

Split `larena/docara-core` / `larena/docara-admin`, `larena/rest-doc`,
`larena/rest_doc`, `larena/logs`, `larena/upserv` and (since 2026-09-23)
`larena/content` are not current ownership targets. Preserve old names only
where a tested compatibility or archive contract explicitly requires them; use
`larena/docara`, `larena/rest`, `larena/audit`, `larena/update` and
`larena/storage` for current ownership.

## Authority order

For a live Larena project, use this order:

1. current `larena-specs` registry and package contracts;
2. current `larena-workspace` package inventory;
3. current Root Composer files/lock and release manifest for the assembled subset;
4. this reference as a durable owner-skill baseline;
5. older knowledge/changelog only as migration context.
