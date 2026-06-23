# Larena Developer Feedback Intake Protocol

Use this protocol whenever the user gives Larena developer feedback, review
findings, retest results, architecture notes or handoff recommendations.

Do not treat developer feedback as a ready canonical change. Treat it as review
input that must pass through controlled intake.

## Required Flow

```text
feedback file or message
-> intake report
-> finding classification
-> impact analysis
-> outcome decision
-> fix / guardrail / docs / defer / reject
-> Larena validation
-> Kaizen/process learning
```

## Finding Types

- `real_bug`;
- `architecture_drift`;
- `ux_dx_problem`;
- `developer_preview_limitation`;
- `already_covered_but_unclear`;
- `future_track_proposal`;
- `false_positive_or_stale`.

## Outcomes

- `accepted_fix_now`;
- `accepted_guardrail_now`;
- `accepted_docs_clarification`;
- `defer_to_next_track`;
- `reject_not_applicable`;
- `needs_user_decision`.

## Larena-Specific Impact Check

For each finding, check whether it affects:

- current developer-preview behavior;
- next track launch readiness;
- Larena graph/spec/DNA alignment;
- package ownership boundary;
- security/runtime safety;
- documentation or cockpit clarity;
- validators, metrics, launch records or evidence.

## Recurrence Prevention

Every current and applicable developer finding must have a prevention outcome,
not only a local code outcome. Accepted findings must answer what prevents
recurrence:

- validator/test added or updated;
- cockpit metric added or updated;
- docs or standard clarified;
- graph/process contract updated;
- launch-record rule added;
- deferred trigger recorded;
- not required with reason.

If a finding is systemic, a code patch alone is not sufficient. If prevention
is not required, record why the finding is isolated, already covered, stale or
not safely preventable in the current track.

## Required Artifacts

Use the project-local protocol when available:

```text
graph/specs/processes/larena-developer-feedback-intake-protocol.json
docs/project-management/templates/developer-feedback-intake.md
docs/project-management/templates/developer-feedback-intake.json
scripts/validate-developer-feedback-intake.php
```

For active feedback processing, create:

```text
source/workflow/YYYY-MM-DD-developer-feedback-intake.md
docs/project-management/reports/YYYY-MM-DD-developer-feedback-intake.md
docs/project-management/reports/YYYY-MM-DD-developer-feedback-intake.json
```

## Validation

Run the narrow gate first:

```bash
composer validate:developer-feedback-intake
```

Then run the relevant Larena gates, usually:

```bash
composer quality:full
git diff --check
```

## Stop Conditions

Stop and ask for a decision if:

- the fix would require production runtime, destructive data mutation or release
  readiness approval;
- ownership boundary is unclear;
- the finding requires product direction;
- there is no safe evidence path;
- solving it would expand the current goal beyond its Done When.
