# Larena Goal Execution Profile

Use this profile when Larena work is requested as a goal, milestone, or
autonomous multi-batch delivery.

`teamlead` owns the universal goal execution standard. `larena` applies it to
Larena platform development through package specs, implementation planning,
launch records, evidence, metrics, runtime/security gates and package DNA.

## Hierarchy

```text
goal -> milestone -> batch -> checkpoint -> evidence -> Kaizen
```

## Larena Goal Examples

- make the entry app installable for the first guarded developer preview;
- complete the runtime/security cluster to developer-testable state;
- prepare a package cluster for first coding batch;
- produce human TZ and graph feedback loop for a package cluster;
- move a package repository from legacy reset to ready-to-code;
- close a guarded install/update/runtime milestone.

## Required Goal Fields

Every Larena goal must name:

- target surface: specs, workspace, entry app, package repo, update server,
  registration server, SitePack, Docara, runtime, or QA;
- parent Larena trajectory, for example production launch, developer preview,
  package cluster readiness, or install/update readiness;
- `Done When`;
- packages/clusters in scope;
- non-goals;
- required launch records or proof that no coding launch is involved;
- package DNA and graph/spec refs;
- metrics/evidence outputs;
- human checkpoints.

## Milestone Rules

Larena milestones should map to product-meaningful control points, not only
small commits:

- repository prepared;
- launch record ready;
- interface skeleton done;
- smoke integrated;
- evidence accepted;
- developer-testable preview;
- guarded runtime mutation ready;
- release candidate.

## Batch Rules

Larena batches must stay inside:

- package ownership boundaries;
- allowed files from launch records;
- package DNA;
- graph/spec source of truth;
- evidence and graph-sync proposal boundaries;
- runtime/security gates.

Do not start or continue package coding from a human Markdown plan alone.
Coding requires the relevant process contract and launch record.

## Human Checkpoints

Ask for a human checkpoint when:

- architecture direction changes;
- runtime/live/destructive approval is required;
- developer/user testing is the next meaningful product signal;
- package ownership is ambiguous;
- graph/spec update would change canonical platform behavior.

Otherwise continue the next safe batch automatically.

