# GrowGraph Contract Gate

This repository exposes a bounded GrowGraph companion layer for
`skill:larena`.

Before claiming repo-local `GGA9 federation_integrated`, run:

```bash
python3 scripts/growgraph_contract_gate.py
```

The gate checks:

- semantic preservation passed;
- effectiveness verdict is `improved`;
- final adoption report is `GGA9`;
- federation export uses protocol `1.0.0` and `growgraph_skill_pilot`;
- integration review allows the AGENTS/hook/CI integration.

Canonical writes remain disabled until a separate graph-first source-of-truth
migration is accepted.
