#!/usr/bin/env python3
"""Local executable assurance for one SIMAI owner-skill technology contract."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any


SCRIPT = Path(__file__).resolve()
SKILL_DIR = SCRIPT.parents[1]
SKILL = SKILL_DIR.name
REPO = SCRIPT.parents[3]
CONTRACT_REL = Path(
    "graph/generated/mirai-graph/federation-runtime/contracts/owner-skill-contracts.json"
)


def graph_repo_path(explicit: str) -> Path:
    candidates = [
        Path(explicit).expanduser() if explicit else None,
        Path(os.environ["SIMAI_GRAPH_REPO"]).expanduser() if os.environ.get("SIMAI_GRAPH_REPO") else None,
        REPO.parent / "ai-codex-skill-graph",
    ]
    return next((path.resolve() for path in candidates if path and path.exists()), Path(""))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph-repo", default="")
    args = parser.parse_args()
    blockers: list[str] = []
    skill_md = SKILL_DIR / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8", errors="ignore") if skill_md.exists() else ""
    if not skill_md.exists():
        blockers.append("skill_entrypoint_missing")
    if "## Mirai Graph Runtime Entry" not in text:
        blockers.append("mirai_graph_runtime_entry_missing")
    if not (REPO / "graph").exists():
        blockers.append("local_graph_missing")
    linked_refs = []
    for match in re.finditer(r"\[[^\]]+\]\((\./[^)#]+)(?:#[^)]+)?\)", text):
        ref = (SKILL_DIR / match.group(1)).resolve()
        linked_refs.append(str(ref.relative_to(REPO)) if ref.exists() else match.group(1))
        if not ref.is_file():
            blockers.append(f"direct_method_ref_missing:{match.group(1)}")
    graph_repo = graph_repo_path(args.graph_repo)
    contract_path = graph_repo / CONTRACT_REL if graph_repo else Path("")
    owner_contract: dict[str, Any] = {}
    if not contract_path.is_file():
        blockers.append("federation_owner_contract_package_missing")
    else:
        try:
            package = json.loads(contract_path.read_text(encoding="utf-8"))
            owner_contract = next(
                (item for item in package.get("contracts") or [] if item.get("skill_id") == SKILL),
                {},
            )
        except (OSError, json.JSONDecodeError) as exc:
            blockers.append(f"federation_owner_contract_unreadable:{exc}")
    if not owner_contract:
        blockers.append("owner_contract_missing")
    elif not owner_contract.get("process_contracts"):
        blockers.append("owner_process_contract_missing")
    fallback = owner_contract.get("fallback_contract") or {}
    if owner_contract and (
        fallback.get("silent_merge_allowed") is not False
        or fallback.get("uncontracted_hardcoded_fallback_allowed") is not False
    ):
        blockers.append("fail_closed_fallback_contract_missing")
    result = {
        "schema_version": "1.0.0",
        "operation_id": "simai.owner_skill.technology_contract_smoke",
        "skill": SKILL,
        "status": "fail" if blockers else "success",
        "runtime_entry": bool("## Mirai Graph Runtime Entry" in text),
        "direct_method_refs_checked": len(linked_refs),
        "owner_contract_id": owner_contract.get("contract_id"),
        "owner_process_contract_count": len(owner_contract.get("process_contracts") or []),
        "blockers": list(dict.fromkeys(blockers)),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())

