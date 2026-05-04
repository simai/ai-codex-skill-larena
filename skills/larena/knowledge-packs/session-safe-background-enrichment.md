# Session-Safe Background Enrichment

Use this pack when work touches link preview, URL unfurling, attachment preview, imports from URLs, AI-agent context gathering, crawling, thumbnail generation, external fetches, admin widgets with many AJAX requests, long-running read-only endpoints, queues, session policy, diagnostics or package manifests for such behavior.

## Canonical Source

In `simai/larena`:

- `docs/developer/rfc/0002-session-safe-background-enrichment.md`
- `docs/developer/module-yaml-schema.md`
- `docs/developer/schemas/module.schema.json`

## Threat Class

Auxiliary features must not saturate the shared web worker pool or hold/wait on user sessions.

Risk pattern:

- background/AJAX request runs as user web request;
- request opens or writes user session;
- external URL/internal crawl/long operation blocks worker;
- many parallel requests fan out from one page/user;
- no queue isolation, limits, circuit breaker or diagnostics;
- CMS appears frozen even though the trigger was "just preview/enrichment".

## Larena Principles

- Background/enrichment endpoints are sessionless by default.
- Read-only identity should use actor snapshots, signed internal requests, first-party API tokens or capability-scoped tokens, not session-write web flows.
- Preview/enrichment/external fetch/AI context gathering is async by default.
- Heavy auxiliary work uses separate bounded queues.
- External fetch is denied by default until policy is configured.
- UI must degrade with placeholder/pending/failed states.
- No preview/enrichment feature may be required for primary page/admin rendering.

## Required Components

Expected architecture:

- `LinkPreviewService`
- `PreviewJob`
- `PreviewCache`
- `ExternalFetchClient`
- `InternalEntityPreviewResolver`
- `FeatureCircuitBreaker`
- `RateLimitPolicy`
- `PackageCapabilityManifest`
- `DiagnosticsDashboard`

## Default Limits

Baseline defaults for Core:

- preview request cache miss response target: <= 150 ms;
- external connect timeout: 500 ms;
- external total timeout: 2 s;
- max redirects: 3;
- max response body: 512 KB;
- max preview jobs per request: 5;
- max links per entity/comment: 20;
- success cache TTL: 7 days;
- failure cache TTL: 1 hour;
- in-flight lock TTL: 60 s;
- preview queue concurrency: 1-2 workers on shared/VPS hosting;
- job timeout: 10 s;
- attempts: 2;
- backoff: `[30, 300]`.

## Session Modes

Package endpoints should declare one of:

- `stateful`
- `readonly-auth`
- `sessionless`
- `signed-internal`
- `capability-token`

Background, preview, polling, diagnostics, AI-tool and enrichment endpoints should not be `stateful` unless there is a specific user-facing session-write reason.

## Manifest Requirements

Packages that add endpoints/jobs/background enrichment must declare:

- `endpoints[].session_mode`
- `queues`
- `rate_limits`
- `external_network`
- `api_operations`
- `permissions`
- `audit`
- `health_checks`
- `operational_risks`
- `rollback`

The validator/schema should fail strict release gates when high-risk packages omit these policies.

## Never Do This

- Never fetch external URLs inside a normal user web request.
- Never use session middleware for background enrichment endpoints.
- Never let preview/unfurling hold or wait on user session lock.
- Never crawl internal Larena pages through HTTP to generate previews.
- Never send user cookies/session headers to external fetches.
- Never allow arbitrary URL crawling by AI agents.
- Never dispatch unbounded jobs from one page/comment/entity.
- Never run preview jobs on the same pool as auth/admin critical work without limits.
- Never let UI depend on preview completion to render the main page.

## Release Gates

Required checks for preview/enrichment packages:

- one page with 100 links does not dispatch more than allowed preview jobs;
- slow external URL does not block web workers;
- pending preview renders placeholder;
- repeated URL deduplicates into one in-flight job;
- disabled preview does not break UI;
- package without manifest session policy fails strict validator;
- endpoint writing session in read-only/sessionless mode fails test;
- external fetch without policy is rejected;
- SSRF targets are rejected;
- circuit breaker open state prevents new work;
- preview queue saturation does not affect login/admin/public rendering.
