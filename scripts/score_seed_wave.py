from __future__ import annotations

import json
from pathlib import Path

from _common import REPO_ROOT, SKILLS_DIR, parse_frontmatter, timestamp_iso


DARWIN_DIR = REPO_ROOT / "darwin"
RESULTS = DARWIN_DIR / "results.tsv"


REQUIRED_SECTIONS = [
    "## Purpose / When To Use",
    "## Inputs / Outputs",
    "## Decision Rules",
    "## Execution Path",
    "## QC / Validation Checkpoints",
    "## Failure Handling / When To Ask The User",
    "## Related Skills",
]


def score_skill(skill_dir: Path) -> int:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    metadata = frontmatter.get("metadata", {}) if isinstance(frontmatter.get("metadata"), dict) else {}
    bioskills = metadata.get("bioskills", {}) if isinstance(metadata.get("bioskills"), dict) else {}
    openclaw = metadata.get("openclaw", {}) if isinstance(metadata.get("openclaw"), dict) else {}
    prompts = json.loads((skill_dir / "tests" / "test-prompts.json").read_text(encoding="utf-8"))

    score = 0
    if frontmatter.get("name") and frontmatter.get("description"):
        score += 15
    if bioskills.get("skill_type") in {"atomic", "workflow"}:
        score += 10
    if bioskills.get("canonical_of"):
        score += 10
    if isinstance(openclaw.get("os"), list) and openclaw.get("homepage"):
        score += 10
    score += min(len(prompts.get("prompts", [])) * 5, 15)
    score += sum(5 for section in REQUIRED_SECTIONS if section in text)
    if bioskills.get("skill_type") == "workflow" and bioskills.get("depends_on"):
        score += 5
    return min(score, 100)


def main() -> int:
    DARWIN_DIR.mkdir(parents=True, exist_ok=True)
    header = "timestamp\tcommit\tskill\told_score\tnew_score\tstatus\tdimension\tnote\teval_mode\n"
    rows = [header]
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").exists():
            continue
        score = score_skill(skill_dir)
        rows.append(
            f"{timestamp_iso()}\tbaseline\t{skill_dir.name}\t-\t{score}\tbaseline\tstructure+dry_run\tcanonical catalog baseline\tdry_run\n"
        )
    RESULTS.write_text("".join(rows), encoding="utf-8")
    print(f"Wrote Darwin baseline scores to {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
