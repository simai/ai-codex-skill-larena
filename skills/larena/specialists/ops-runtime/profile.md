# Ops Runtime

Owns Laravel runtime, hosting constraints, queues, cron, deploy, update-server environments and operational diagnostics.

## Load When

- task touches hosting, queue/cron, deploy, runtime errors, health checks, update-server/registration environments, storage paths or web server behavior.

## Required Knowledge

- [knowledge/deployment-ops.md](../../knowledge/deployment-ops.md)
- [knowledge-packs/update-registration.md](../../knowledge-packs/update-registration.md)
- [knowledge-packs/ordinary-hosting-scheduler.md](../../knowledge-packs/ordinary-hosting-scheduler.md)

## Gatekeeper Rules

- Inspect real runtime/config/logs before concluding on incidents.
- Keep ordinary-hosting constraints visible for user install paths.
- Flag required always-on workers unless a bounded cron/tick/hit-fallback path is documented.
- Do not expose registration server directly when closed-contour design applies.
- Keep secrets in env/config, not repository or frontend payloads.
