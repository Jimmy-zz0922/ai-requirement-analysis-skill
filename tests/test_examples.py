from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "real-estate-output.json"
VALIDATOR = ROOT / "scripts" / "validate_output.py"
EXPORTER = ROOT / "scripts" / "export_csv.py"


class SkillExamplesTest(unittest.TestCase):
    def test_example_validates(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(EXAMPLE)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)

    def test_example_exports_two_cards(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "requirements.csv"
            result = subprocess.run(
                [sys.executable, str(EXPORTER), str(EXAMPLE), str(output)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
            with output.open("r", encoding="utf-8-sig", newline="") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["requirement_id"], "REQ-001")


if __name__ == "__main__":
    unittest.main()
