# QA Validation

Owns tests, static checks, install smoke, admin/browser smoke, release gates and evidence.

## Load When

- any implementation task;
- diagnostics that need a readiness verdict;
- release, install, update, admin or public product flows.

## Required Knowledge

- [kernel/output-contract.md](../../kernel/output-contract.md)
- [checklists/qa-smoke.md](../../checklists/qa-smoke.md)
- [checklists/release-checklist.md](../../checklists/release-checklist.md)

## Gatekeeper Rules

- Run the narrowest meaningful checks first, then broader checks when integration risk exists.
- If checks cannot run, state exact blocker and provide closest static verification.
- User-facing admin/public UI changes need browser smoke when a runnable target exists.
- Behavior fixes should include regression tests where feasible.
