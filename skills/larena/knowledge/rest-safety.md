# REST Safety

Current conceptual endpoint: `/api/v1/run/{module}/{class}/{method}`.

## Core Rule

`class@method` is not automatically an API method.

A `200` response only proves that code executed. It does not prove that the operation was safe.

Strategic role: dynamic REST is useful because Larena is service-oriented and AI-agent-ready. It can expose controlled internal capabilities to other services, external clients and AI tools. This must strengthen interoperability without turning every internal PHP method into a public operation.

## Preferred Production Models

Allowed safe directions:

- strict registered operations only;
- SimaiCrud/standard operation contracts only;
- explicit method declaration/attributes that generate API metadata;
- hybrid platform-token mode only with deny-by-default, allowlist, permissions, confirmation, audit and limits.
- separation between internal API, service-to-service API, public external API and AI-agent tool API.
- public REST resources by whitelist, with `/run` treated as internal/service/agent infrastructure unless explicitly hardened and approved.

Unsafe direction:

- arbitrary public method runner in production.

## API Operation Contract

When designing Larena REST/API, use operation contracts rather than exposing PHP methods directly.

Preferred package-local structure:

```text
module.yaml
api.yaml
access.yaml
```

- no REST/API operations -> `api.yaml` is not required;
- one or more REST/API operations -> `api.yaml` is required;
- `api.yaml` is the source for public/internal API operation metadata: route, params, handler, auth mode, execution policy, response, rate limit, cache/queue/audit policy.
- `access.yaml` is the source for permission semantics: operation key, resource, access values, target providers, resolver/query scope and explain behavior.
- `module.yaml.api_operations` may summarize or link to API contracts, but must not be the source of truth.
- REST operation keys and access operation keys should be linked and often identical, for example `docara.page.update`, but REST and access contracts must stay conceptually separate.

For list/search/export, access must return or require an access-aware query scope. Do not allow a broad REST query followed by ad hoc filtering in the controller, AI tool or client.

## Swagger/OpenAPI

Swagger should be token-aware and ACL-aware:

- show only methods available for current token/rights;
- include risk/confirmation conditions where needed;
- stay synchronized with actual route/method metadata;
- include tests for 401/403/validation paths.
- describe operation purpose, inputs, outputs, side effects, permissions and audit behavior so humans and AI agents can choose safe actions.

Useful implementation targets from Larena backlog:

- unified API error contract (`error.code`, `error.message`, `error.details`, HTTP status map);
- MethodInfoService as source metadata for OpenAPI generation;
- tests that Swagger includes only published/allowed operations;
- audit of `/run` calls: actor/token, method, params policy, result/error, duration and correlation id.
