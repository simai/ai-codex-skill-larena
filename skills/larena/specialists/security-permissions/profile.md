# Security Permissions

Owns auth, access, 2FA, tokens, license checks, admin guards, secret handling and unsafe API boundaries.

## Load When

- task touches auth, access, 2FA, tokens, API scopes, admin permissions, file delivery, license checks or security-sensitive REST/update behavior.

## Required Knowledge

- [kernel/non-negotiables.md](../../kernel/non-negotiables.md)
- [knowledge/access-control.md](../../knowledge/access-control.md)
- [knowledge/auth-authorization.md](../../knowledge/auth-authorization.md)
- [knowledge-packs/access-platform.md](../../knowledge-packs/access-platform.md)
- [knowledge-packs/session-safe-background-enrichment.md](../../knowledge-packs/session-safe-background-enrichment.md)
- [checklists/access-checklist.md](../../checklists/access-checklist.md)

## Gatekeeper Rules

- Do not put secrets in docs, skill knowledge, frontend payloads or logs.
- Use Larena access package as the central permission source where applicable.
- File/update delivery must avoid direct unsafe paths and executable upload dirs.
- REST and update actions must be auditable and deny-by-default for risky operations.
- Background, preview, polling, diagnostics and AI-tool endpoints must not use session-write flows. Require explicit session mode and fail release gates when read-only/sessionless endpoints write to session.
