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
- the change states which product goal it serves: self-install, update safety, admin UX, SitePack portability, Docara proof, AI readiness, marketplace ecosystem, or Bitrix/SF5 continuity;
- free/paid/core/pro/internal boundaries are explicit when product capability or package distribution is affected;
- update/registration boundaries are respected;
- SitePack standard and platform adapter responsibilities are separated;
- admin, REST, access and install flows are not weakened;
- machine-readable package/service metadata remains present or is introduced when needed;
- required verification is run or explicitly impossible;
- durable knowledge/docs are updated when stable rules were learned.
