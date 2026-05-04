# Update Registration

Owns update server, registration server, licensing, product channels, installers, update artifacts and entitlement checks.

## Load When

- task touches `larena-update`, `larena-upserv`, `larena-update-registration`, licensing, product delivery, update archives or installer scripts;
- comparing Bitrix update flow with future Larena update flow;
- planning free/paid/internal package delivery.

## Required Knowledge

- [knowledge-packs/update-registration.md](../../knowledge-packs/update-registration.md)
- [knowledge-packs/product-architecture.md](../../knowledge-packs/product-architecture.md)

## Gatekeeper Rules

- `larena-update` is the canonical update server.
- `larena-upserv` is legacy alias/historical naming for the update server. New Composer/manifests/docs should use `larena/update`; keep `larena/upserv` only as compatibility alias where needed.
- `larena-update-registration` is closed-contour registration/licensing server.
- Users should not talk directly to registration server.
- Serve update files through controlled delivery, not public filesystem paths.
- Keep upload/temp storage non-executable and clean stale temp files.
