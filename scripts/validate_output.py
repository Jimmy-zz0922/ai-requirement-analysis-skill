#!/usr/bin/env python3
"""Validate an AI requirement-analysis JSON output against the bundled schema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit(
        "Missing dependency 'jsonschema'. Run: python -m pip install -r requirements.txt"
    ) from exc


def load_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as exc:
        raise SystemExit(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def validate(data_path: Path, schema_path: Path) -> list[str]:
    data = load_json(data_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        location = "$"
        for part in error.absolute_path:
            location += f"[{part}]" if isinstance(part, int) else f".{part}"
        errors.append(f"{location}: {error.message}")
    return errors


def main() -> int:
    default_schema = Path(__file__).resolve().parents[1] / "schemas" / "requirement-analysis.schema.json"

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data", type=Path, help="JSON output to validate")
    parser.add_argument("--schema", type=Path, default=default_schema, help="Schema path")
    args = parser.parse_args()

    errors = validate(args.data, args.schema)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for item in errors:
            print(f"- {item}", file=sys.stderr)
        return 1

    print(f"Validation passed: {args.data}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
