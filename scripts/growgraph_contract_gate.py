#!/usr/bin/env python3
"""Validate the repo-local GrowGraph integration contract for larena."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_ARTIFACTS = {
    "semantic": Path(
        "graph/generated/growgraph/semantic-preservation/"
        "larena-repo-local-semantic-review-20260529/semantic-preservation-verdict.json"
    ),
    "effectiveness": Path(
        "graph/generated/growgraph/effectiveness-reports/"
        "larena-repo-local-effectiveness-20260529/effectiveness-report.json"
    ),
    "adoption": Path(
        "graph/generated/growgraph/adoption-reports/"
        "larena-repo-local-adoption-gga9-active-gate-20260529/growgraph-adoption-report.json"
    ),
    "federation": Path(
        "graph/federation/exports/larena-repo-local-federation-export-20260529/federation-export.json"
    ),
    "integration": Path(
        "graph/generated/growgraph/integration-reviews/"
        "larena-repo-local-integration-review-active-gate-20260529/growgraph-integration-review.json"
    ),
}


def load_json(ref: Path) -> dict:
    path = ROOT / ref
    if not path.exists():
        raise FileNotFoundError(str(ref))
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    blockers: list[str] = []
    artifacts: dict[str, dict] = {}

    for name, ref in REQUIRED_ARTIFACTS.items():
        try:
            artifacts[name] = load_json(ref)
        except Exception as exc:  # noqa: BLE001 - gate must report all blockers.
            blockers.append(f"{name}: {exc}")

    semantic = artifacts.get("semantic", {})
    if semantic.get("verdict") not in {"pass", "pass_with_notes"}:
        blockers.append("semantic preservation did not pass")

    effectiveness = artifacts.get("effectiveness", {})
    if effectiveness.get("verdict") != "improved":
        blockers.append("effectiveness verdict is not improved")

    adoption = artifacts.get("adoption", {})
    if adoption.get("adoption_level") != 9:
        blockers.append("adoption level is not GGA9")

    federation = artifacts.get("federation", {})
    if (
        federation.get("protocol_version") != "1.0.0"
        or federation.get("manifest", {}).get("graph_type") != "growgraph_skill_pilot"
    ):
        blockers.append("federation export is missing or invalid")

    integration = artifacts.get("integration", {})
    if integration.get("integration_allowed") is not True:
        blockers.append("integration review is not allowed")

    result = {
        "operation_id": "larena.growgraph-contract-gate",
        "status": "blocked" if blockers else "success",
        "blockers": blockers,
        "checked_artifacts": {name: str(ref) for name, ref in REQUIRED_ARTIFACTS.items()},
        "canonical_write_allowed": False,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if blockers else 0


if __name__ == "__main__":
    sys.exit(main())
