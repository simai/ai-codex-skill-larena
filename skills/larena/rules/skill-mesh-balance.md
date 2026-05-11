# Skill Mesh Balance

`$larena` owns Larena platform facts: `simai/larena`, `larena/*` packages,
modular admin, installer/update flows, registration/licensing, SitePack bridge,
Docara product proof, REST/API safety, settings/storage/props/layout, package
diagnostics, and Larena release readiness.

## Does Not Own

- General repository delivery owned by `$dev`.
- SF5 generic frontend contracts owned by `$sf5`.
- Docara site mechanics owned by `$docara`.
- Documentation methodology/content owned by `$docs`.
- Runtime/deploy/hosting incidents owned by `$ops`.
- QA evidence owned by `$tester`.
- SEO Contract and UX acceptance owned by `$seo` and `$ux`.
- Bitrix-only facts outside Larena/Bitrix alignment work.

## Companion Contracts

- Use `$sf5` for shared frontend loader/components/layout contracts.
- Use `$docara` for Docara site mechanics and `$docs` for content/method.
- Use `$ops` for runtime, deploy, update server, queues/cron, and hosting.
- Use `$tester` for install/admin/public/API/Docara acceptance evidence.
- Use `$bitrix` when comparing or porting Bitrix/SF/SitePack models.
- Use `$seo` and `$ux` for public/search and interface gates.
- For Bitrix -> Larena or reference-adaptive work, use `$tester` for invariant
  evidence and `$bitrix` for source/reference behavior. `$larena` owns the
  target architecture adaptation: routes, controllers, requests, views,
  policies, Eloquent/storage, package metadata, migrations, update flow, and
  Larena-native UI constraints.

## Handoff

Return Larena package/app paths, affected install/update surfaces, contracts
implemented, compatibility constraints, commands/evidence, blockers, and the
companion owner expected to review.

For reference-adaptive handoff, also return target behavior, allowed Larena
adaptations, source-of-truth mapping, already-working baseline, do-not-break
list, and regression checks after fix.
