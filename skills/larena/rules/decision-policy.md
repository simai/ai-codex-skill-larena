# Decision Policy

Coordinator decisions:

- `APPROVED`: requirements and verification are sufficient.
- `APPROVED_WITH_CONDITIONS`: acceptable if listed conditions are handled.
- `NEEDS_REVISION`: direction is valid, but missing work or risk blocks acceptance.
- `REJECTED`: violates Larena non-negotiables or product architecture.
- `BLOCKED`: missing access, source, runtime, or irreversible choice.

Before approving, check:

- product DNA and non-negotiables are respected;
- selected scope matches Larena phase and repository;
- the change states which product goal it serves: self-install, update safety, admin UX, SitePack portability, Docara proof, AI readiness, marketplace ecosystem, or Bitrix/SIMAI Framework continuity;
- free/paid/core/pro/internal boundaries are explicit when product capability or package distribution is affected;
- update/registration boundaries are respected;
- SitePack standard and platform adapter responsibilities are separated;
- admin, REST, access and install flows are not weakened;
- machine-readable package/service metadata remains present or is introduced when needed;
- required verification is run or explicitly impossible;
- durable knowledge/docs are updated when stable rules were learned.

## Coordinator Duties

1. Keep the task inside the current Larena phase and stated repository.
2. Choose the smallest sufficient specialist set.
3. Separate product direction from current implementation findings; treat
   mismatches in current packages as diagnostic findings, not automatic
   direction changes.
4. Keep update/registration security boundaries explicit.
5. Preserve SitePack as portable transport with separate platform adapters.
6. Require install, migration, release, rollback and QA artifacts when the
   selected activity demands them.
7. Update durable knowledge in repo `source/` or this skill when a stable
   reusable rule is learned (see [learning.md](./learning.md)).

For non-trivial review or architecture work collect compact specialist
assessments with
[../quality/specialist-assessment-template.md](../quality/specialist-assessment-template.md),
close with
[../quality/coordinator-gate-template.md](../quality/coordinator-gate-template.md)
and use
[../quality/release-readiness-template.md](../quality/release-readiness-template.md)
for release decisions.
