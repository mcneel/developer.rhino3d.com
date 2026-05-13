#!/usr/bin/env python3
"""Syntax-check every ```python and ```py block in content/en/samples/**/index.md.

Python 3 only. Uses ast.parse, so this catches syntax errors but not
missing names or API mismatches.
"""
import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SAMPLES = ROOT / "content" / "en" / "samples"
FENCE = re.compile(r"```(?:python|py)\s*\n(.*?)```", re.DOTALL)


def check_file(md_path: Path) -> list[str]:
    text = md_path.read_text(encoding="utf-8")
    errors = []
    for i, match in enumerate(FENCE.finditer(text), start=1):
        block = match.group(1)
        md_line = text.count("\n", 0, match.start(1)) + 1
        try:
            ast.parse(block, filename=str(md_path))
        except SyntaxError as e:
            file_line = md_line + (e.lineno or 1) - 1
            errors.append(
                f"{md_path.relative_to(ROOT)}:{file_line}: block #{i}: {e.msg}"
            )
    return errors


def main() -> int:
    md_files = sorted(SAMPLES.rglob("index.md"))
    all_errors: list[str] = []
    checked = 0
    for md in md_files:
        if not FENCE.search(md.read_text(encoding="utf-8")):
            continue
        checked += 1
        all_errors.extend(check_file(md))

    print(f"Checked {checked} markdown files containing Python blocks.")
    if all_errors:
        print(f"\nFound {len(all_errors)} syntax error(s):\n")
        for err in all_errors:
            print(f"  {err}")
        return 1
    print("All Python blocks parsed cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
