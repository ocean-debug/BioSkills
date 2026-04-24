from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from _common import VALID_OS_VALUES, parse_frontmatter


REQUIRED_SECTIONS = [
    "## Purpose / When To Use",
    "## Inputs / Outputs",
    "## Decision Rules",
    "## Execution Path",
    "## QC / Validation Checkpoints",
    "## Failure Handling / When To Ask The User",
    "## Related Skills",
]


def validate_skill_dir(skill_dir: Path) -> tuple[bool, str]:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    text = skill_md.read_text(encoding="utf-8", errors="replace")
    frontmatter = parse_frontmatter(text)
    if not frontmatter:
        return False, "Invalid or missing YAML frontmatter"

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not re.match(r"^[a-z0-9-]+$", name):
        return False, "Frontmatter name must be kebab-case"
    if name != skill_dir.name:
        return False, "Frontmatter name must match directory name"
    if not isinstance(description, str) or not description.strip():
        return False, "Missing description"

    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict):
        return False, "Missing metadata block"
    openclaw = metadata.get("openclaw")
    bioskills = metadata.get("bioskills")
    if not isinstance(openclaw, dict):
        return False, "Missing metadata.openclaw"
    if not isinstance(bioskills, dict):
        return False, "Missing metadata.bioskills"

    os_values = openclaw.get("os")
    if not isinstance(os_values, list) or not os_values:
        return False, "metadata.openclaw.os must be a non-empty list"
    if any(value not in VALID_OS_VALUES for value in os_values):
        return False, "metadata.openclaw.os contains unsupported platform values"

    for field in ("skill_type", "domain", "maturity", "canonical_of", "depends_on"):
        if field not in bioskills:
            return False, f"Missing metadata.bioskills.{field}"

    for section in REQUIRED_SECTIONS:
        if section not in text:
            return False, f"Missing section: {section}"

    tests_path = skill_dir / "tests" / "test-prompts.json"
    if not tests_path.exists():
        return False, "Missing tests/test-prompts.json"

    return True, "Skill is valid"


def validate_manifest(path: Path) -> tuple[bool, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "skills" not in data or not isinstance(data["skills"], list):
        return False, "Manifest missing skills array"
    missing = []
    for skill_dir in data["skills"]:
        resolved = (path.parent / skill_dir).resolve()
        if not resolved.exists():
            missing.append(skill_dir)
    if missing:
        return False, f"Missing skill directories: {missing[:5]}"
    return True, "Manifest is valid"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_skill.py <path/to/skill_dir|openclaw.plugin.json>", file=sys.stderr)
        return 2

    target = Path(sys.argv[1]).resolve()
    if target.name == "openclaw.plugin.json":
        ok, message = validate_manifest(target)
    else:
        ok, message = validate_skill_dir(target)
    stream = sys.stdout if ok else sys.stderr
    print(message, file=stream)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

