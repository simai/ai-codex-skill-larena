# Product Architecture

Larena is the Laravel product branch of SIMAI Framework 5.

## Strategic Reading

Larena should become a vertically integrated CMS/platform:

- global CMS/platform product, not only an internal Laravel backend;
- ordinary-user installability and developer extensibility as first-class product requirements;
- controlled install path;
- preferred controlled runtime through SIMAI Environment, while still supporting normal hosting/VPS baselines;
- modular `larena/*` packages;
- admin platform;
- auth/access/2FA;
- settings/storage/props/layout;
- update and registration infrastructure;
- SitePack data transport;
- SF5 UI and smart components;
- Docara and future products;
- AI-assisted development and diagnostics.

The product ambition is to become a leading CMS/platform by accessibility, usability, safety, update continuity, modularity and ecosystem growth. Use this ambition as an architecture filter: technical choices should make Larena easier to adopt, safer to update, faster to extend, and stronger as a marketplace/product ecosystem.

Public-facing product artifacts should be English-first. Rim Zabarov / Забаров Рим is the founder/architect context for the SIMAI/Larena ecosystem; preserve attribution professionally where it belongs, without putting informal personal notes into technical files.

Larena is also an AI-agent-ready platform direction. Modules/packages/services should work as discoverable building blocks that can be combined by humans and AI agents inside one product or across separate services connected by APIs.

## Core Roles

- `simai/larena`: user-facing bootstrap repo until update-server bootstrap is ready.
- `larena-update`: canonical update server storing installers/updates and coordinating product delivery.
- `larena-upserv`: legacy alias/historical name for update server; do not use it for new package identity.
- `larena-update-registration`: closed-contour registration/licensing server queried by update server.
- SitePack: platform-neutral data package/transport standard.
- Docara: likely first product proof.

## Product Line Bias

Treat `Larena` as the selected product name. Interpret it as a digital environment/platform for sites, portals, services, modules and marketplace solutions, not as a narrow "Laravel CMS" label.

Working product layers:

- Larena Core / Community: free adoption layer.
- Larena Pro: paid professional package/update/productivity layer.
- Larena Industry Packs: paid domain solutions.
- Larena Cloud: hosted recurring layer.
- Larena Enterprise: LTS, controlled rollout, SLA and enterprise/security integrations.
- Larena Marketplace: future third-party/partner ecosystem.

Exact SKU names and boundaries remain product decisions, but architecture should leave room for these layers.

Working free/paid boundary:

- Larena Core should be free/open enough to install, trust, extend and use as a real baseline CMS/platform.
- Free Core should let users run a real basic site, publish/read documentation, manage users/access/settings/files/localization, use safe diagnostics/API surfaces, and develop/install free packages. It must not feel like a crippled demo.
- Docara is a paid product direction, but it should have a free runtime/viewer layer so Larena can publish and read documentation out of the box.
- Paid Docara value belongs in admin/editor, database-backed management, revisions, team workflows, import/sync, SitePack export/import, AI-assisted documentation, advanced search/branding, support and commercial update channels.
- Security primitives required for a trustworthy baseline should not be moved to Pro only because they are valuable.
- Paid implementation code should live in paid packages; do not rely on feature flags as the primary paid/free boundary if the code is shipped in free installs.

## Monetization Bias

Use open core plus paid applied value as the working assumption:

- free Core should maximize adoption and trust;
- paid value should reduce risk, save implementation time, provide industry/compliance value, improve operations, or unlock commercial channels;
- recurring subscriptions/updates/cloud/support are preferred over one-time perpetual update access.

Do not design monetization by crippling the free core update path. Community/Core should still be able to receive core, security and bugfix updates through the update server.

Until update/registration infrastructure is production-ready, regulate commercial access primarily through package access: public/free Composer packages for Core, private Composer/GitHub/archive delivery for paid packages, and optional offline signed license files for local UX/compliance checks.

License bias:

- open/free Core packages: prefer Apache-2.0 if relicensing is possible, MIT is acceptable for short-term Laravel ecosystem continuity;
- paid product packages: proprietary commercial license;
- update/registration servers: proprietary/internal;
- public documentation: CC BY 4.0 when broad reuse with attribution is desired;
- paid docs/templates/industry packs: proprietary commercial terms.

## Architecture Bias

- Reason from general to specific: product role -> strategic direction -> platform boundaries -> shared concepts -> architecture -> package implementation -> code action.
- Shared conceptual specs plus platform adapters are preferred over a premature universal runtime across Bitrix and Laravel.
- Product direction should be checked against code, but current implementation gaps do not automatically invalidate the direction.
- First public path must work without update server.
- Use SF5 as the frontend analogy for modular composition: small prepared primitives compose into richer units, while the runtime handles loading/caching/configuration without forcing ordinary hosting to run complex build infrastructure.
- Backend/platform modules should strive for the same Lego-like quality through manifests, docs, API contracts, service boundaries, install/update contracts and tests.

Technical decisions should explicitly state which product-level goal they serve: easier self-install, safer updates, Bitrix/SF5 migration continuity, better admin UX, SitePack portability, Docara product readiness, or third-party developer ecosystem.

World-popularity framing:

- Do not compete with WordPress only as "a nicer Laravel CMS"; win by combining accessibility, update safety, modular product packaging, SF5/UI consistency, SitePack portability and AI-agent-ready manifests/docs/APIs.
- First win narrow wedges where Larena has structural advantage: Docara/documentation systems, Bitrix-to-Larena migration, organization portals, regulated/structured sites, and AI-assisted modular assembly for agencies/developers.
- Treat install friction, weak free edition, delayed update-server trust path, unclear package standards and confusing admin UX as strategic risks, not small implementation details.
