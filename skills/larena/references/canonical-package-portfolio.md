# Canonical Larena Package Portfolio

This reference supersedes historical package lists embedded in older Larena
knowledge. Verify it against the current project before making a readiness or
release claim.

## 2026-07 accepted boundary

Project evidence:

- Specs revision `0777e336e9d09221cdc8da69aeff202b118bea3e`;
- Workspace revision `4eef7cb29f76056efefcb92a6e51a51127fbdec1`;
- Root evidence revision `9c2c94dec3631d1af1330df831e74cf3f83a6c26`;
- accepted Root content `46b9d29ca3cbeaf7bb190e267efd4430cdbe259e`.

The portfolio contains 42 unique `larena/*` packages. The accepted runnable
assembly pins 23 exact package revisions; 19 packages remain workspace-only.
This partition is membership evidence, not a production-readiness or
all-packages-readiness claim.

Runnable 23:

```text
access admin audit auth backup cockpit content core dataview docara
file-manager filesystem lang layout licensing link property rest search
setting storage ui update
```

Workspace-only 19:

```text
ai ai-provider automation chat mcp monitoring notification queue scheduler
secret update-client update-registration visibility workflow workflow-amocrm
workflow-bitrix24 workflow-email workflow-github workflow-messenger
```

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
`larena/rest_doc`, `larena/logs` and `larena/upserv` are not current portfolio
members. Preserve old names only where a tested compatibility or archive
contract explicitly requires them; use `larena/docara`, `larena/rest`,
`larena/audit` and `larena/update` for current ownership.

## Authority order

For a live Larena project, use this order:

1. current `larena-specs` registry and package contracts;
2. current `larena-workspace` package/profile inventory;
3. current Root release manifest and Composer lock for the runnable subset;
4. this reference as a durable owner-skill baseline;
5. older knowledge/changelog only as migration context.
