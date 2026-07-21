# Example: promote one canonical package revision

This example replaces the retired monorepo-to-`laravel.<module>` publishing
flow. Do not copy a package into a second repository or update `bitrix-update`.

## Goal

Promote one accepted Workspace package revision into the Root distribution
without changing unrelated packages.

## Procedure

1. Record the package key, current revision, candidate revision, affected
   contracts and rollback revision.
2. Run package validation, lint, analysis and tests in
   `larena-workspace/packages/<slug>`.
3. Commit and push the package repository without rewriting history.
4. Update the exact package reference, Composer lock and release manifest in
   Root.
5. Run the complete Root acceptance matrix and preserve its evidence.
6. Update Specs only when the product contract changed.
7. Create a tag/release only when that separate action is explicitly scoped and
   all release gates pass.

## Evidence

- package key, branch and exact commit;
- Root branch, lock/manifest commit and acceptance evidence;
- Specs revision when applicable;
- migration/upgrade notes and tested rollback;
- proof that no retired package identity entered the resolved dependency graph.
