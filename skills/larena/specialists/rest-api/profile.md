# REST API

Owns Larena REST Runner, OpenAPI/Swagger, API method metadata, token access and API safety.

## Load When

- task touches `larena/rest`, `larena/rest-doc`, Swagger/OpenAPI, `/api/v1/run`, token scopes or external API contracts.

## Required Knowledge

- [knowledge-packs/rest-safety.md](../../knowledge-packs/rest-safety.md)
- [knowledge-packs/ai-agent-service-architecture.md](../../knowledge-packs/ai-agent-service-architecture.md)
- [knowledge-packs/session-safe-background-enrichment.md](../../knowledge-packs/session-safe-background-enrichment.md)
- [knowledge/modules/rest.md](../../knowledge/modules/rest.md)
- [knowledge/modules/rest-doc.md](../../knowledge/modules/rest-doc.md)

## Gatekeeper Rules

- `class@method` is not automatically a public API method.
- Production `/run` must be explicit, allowlisted/registered, ACL-aware and audited.
- Swagger/OpenAPI must not expose unavailable or dangerous methods for the current token/rights.
- REST metadata should make safe operations discoverable for service-to-service and AI-agent use.
- Breaking API changes need upgrade notes and tests.
- Enrichment/preview/tool APIs must declare session mode, rate limits, queue/circuit-breaker policy and external network policy in `module.yaml`; arbitrary URL crawling or synchronous external fetch from user requests is rejected.
