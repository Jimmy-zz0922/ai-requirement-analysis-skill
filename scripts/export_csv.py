#!/usr/bin/env python3
"""Export requirement cards from validated JSON to a flat UTF-8 CSV file."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from validate_output import validate


COLUMNS = [
    "requirement_id", "title", "user_role", "business_stage", "scenario",
    "user_goal", "pain_point", "problem_type", "root_cause", "business_impact",
    "ai_fit", "ai_capabilities", "product_form", "product_description",
    "alternative_non_ai", "data_dependencies", "system_dependencies",
    "human_review_points", "risks", "priority", "confidence",
    "validation_status", "evidence_refs", "open_questions"
]


def join_list(value: list[str]) -> str:
    return "；".join(value)


def flatten(card: dict) -> dict:
    ai = card["ai_assessment"]
    proposal = card["product_proposal"]
    evidence_refs = [
        f'{e["source_id"]}@{e["locator"]}' for e in card["evidence"]
    ]
    return {
        "requirement_id": card["requirement_id"],
        "title": card["title"],
        "user_role": card["user_role"],
        "business_stage": card["business_stage"],
        "scenario": card["scenario"],
        "user_goal": card["user_goal"],
        "pain_point": card["pain_point"],
        "problem_type": card["problem_type"],
        "root_cause": card["root_cause"],
        "business_impact": card["business_impact"],
        "ai_fit": ai["fit"],
        "ai_capabilities": join_list(ai["capabilities"]),
        "product_form": proposal["form"],
        "product_description": proposal["description"],
        "alternative_non_ai": proposal["alternative_non_ai"],
        "data_dependencies": join_list(ai["data_dependencies"]),
        "system_dependencies": join_list(ai["system_dependencies"]),
        "human_review_points": join_list(ai["human_review_points"]),
        "risks": join_list(ai["risks"]),
        "priority": card["priority"],
        "confidence": card["confidence"],
        "validation_status": card["validation_status"],
        "evidence_refs": join_list(evidence_refs),
        "open_questions": join_list(card["open_questions"]),
    }


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    default_schema = repo_root / "schemas" / "requirement-analysis.schema.json"

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--schema", type=Path, default=default_schema)
    args = parser.parse_args()

    errors = validate(args.data, args.schema)
    if errors:
        for item in errors:
            print(f"ERROR: {item}")
        return 1

    with args.data.open("r", encoding="utf-8") as f:
        data = json.load(f)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for card in data["requirement_cards"]:
            writer.writerow(flatten(card))

    print(f"Exported {len(data['requirement_cards'])} card(s): {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
