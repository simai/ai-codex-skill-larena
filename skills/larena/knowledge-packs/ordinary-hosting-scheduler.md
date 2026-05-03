# Ordinary Hosting Scheduler

Larena must work on ordinary hosting where long-running queue workers may be unavailable.

For platform background work, prefer designs that can run with a bounded tick model:

- DB-backed `JobStore`;
- dispatcher that executes only ready jobs within a time/count budget;
- command such as `simai:tick`;
- cron mode when cron exists;
- sub-ticks inside a minute when useful;
- hit fallback with strict lock and rate limit when cron is absent;
- retry/backoff with jitter;
- job attempt log with status, error, duration, worker id and payload hash;
- queue metrics such as length, wait time, success/failure rate and throughput;
- admin visibility with ACL for requeue/cancel/run-now actions.

This matters for AI-agent/service architecture because update tasks, import/export, indexing, storage MV refresh, API jobs, webhooks and cross-service operations need reliable background execution without assuming managed infrastructure.

When evaluating packages, flag any required always-on worker as a hosting compatibility risk unless there is a documented fallback.
