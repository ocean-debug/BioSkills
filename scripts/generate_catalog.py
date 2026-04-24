from __future__ import annotations

from pathlib import Path

from _common import REPO_ROOT, SKILLS_DIR, canonical_homepage, parse_frontmatter, timestamp_iso, write_json


def load_skill(skill_dir: Path) -> dict:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    metadata = frontmatter.get("metadata", {}) if isinstance(frontmatter.get("metadata"), dict) else {}
    openclaw = metadata.get("openclaw", {}) if isinstance(metadata.get("openclaw"), dict) else {}
    bioskills = metadata.get("bioskills", {}) if isinstance(metadata.get("bioskills"), dict) else {}

    test_prompts = skill_dir / "tests" / "test-prompts.json"
    has_script = (skill_dir / "scripts").exists()
    has_tests = test_prompts.exists()
    related = bioskills.get("depends_on", []) or []

    return {
        "name": frontmatter.get("name", skill_dir.name),
        "description": frontmatter.get("description", ""),
        "version": frontmatter.get("version", "0.1.0"),
        "status": bioskills.get("maturity", "seed"),
        "skill_type": bioskills.get("skill_type", "atomic"),
        "domain": bioskills.get("domain", "general"),
        "has_script": has_script,
        "has_tests": has_tests,
        "has_demo": False,
        "demo_command": "",
        "dependencies": related,
        "tags": frontmatter.get("tags", []),
        "trigger_keywords": frontmatter.get("trigger_keywords", []),
        "chaining_partners": related,
        "homepage": openclaw.get("homepage", canonical_homepage()),
    }


def main() -> int:
    skills = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            skills.append(load_skill(skill_dir))

    catalog = {
        "version": "1.0.0",
        "generated_by": "scripts/generate_catalog.py",
        "generated_at": timestamp_iso(),
        "skill_count": len(skills),
        "skills": skills,
    }
    write_json(SKILLS_DIR / "catalog.json", catalog)

    plugin = {
        "id": "bioskills",
        "name": "BioSkills",
        "description": "Canonical bioinformatics and biomedical analysis skills for OpenClaw-style agents",
        "version": "1.0.0",
        "skills": [f"./skills/{skill['name']}" for skill in skills],
        "homepage": canonical_homepage(),
    }
    write_json(REPO_ROOT / "openclaw.plugin.json", plugin)
    print(f"Generated catalog and manifest for {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
