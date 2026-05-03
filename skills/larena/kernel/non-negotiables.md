# Non-Negotiables

- Keep incoming source materials, research, and handoff notes in repository `source/` unless a narrower project rule exists.
- Do not copy raw secrets from `source/input`, chat exports, operational notes or `.env` files into skill knowledge, docs or answers.
- Do not assume update server availability for the current `simai/larena` user install path.
- Do not expose arbitrary REST class/method execution as production public API without explicit registration, allowlist, ACL, audit and risk controls.
- Do not hardwire licensing or monetization logic into `larena-admin` core.
- Do not make Larena Free/Core a crippled demo; it must remain useful enough for real adoption, trust, learning and basic production scenarios.
- Do not move baseline safety/security/trust features into paid products only.
- Do not ship paid implementation code inside free packages and rely on feature flags as the primary commercial boundary.
- Do not collapse SitePack standard and platform adapter responsibilities.
- Do not add CDN or hardcoded external services to package runtime templates; use config/env contracts and safe fallback.
- Preserve localization parity for public/admin UI strings where package conventions require `ru` and `en`.
- Prefer idempotent install/update commands and explicit rollback/migration notes.
- Treat developer/package docs that still say `simai/*` as stale until verified against current `larena/*` package naming.
- Do not approve official packages that lack machine-checkable metadata, install/update behavior, documentation and a smoke/health check path.
- Do not let local package convenience override Larena product DNA, modularity, update safety, SitePack portability, API safety, Docara product proof or AI-agent readability.
