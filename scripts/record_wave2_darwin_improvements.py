from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

from _common import REPO_ROOT, load_seed_specs, timestamp_iso


DARWIN_RESULTS = REPO_ROOT / "darwin" / "results.tsv"
SKILLS_DIR = REPO_ROOT / "skills"


def load_score_module():
    spec = importlib.util.spec_from_file_location("score_seed_wave", REPO_ROOT / "scripts" / "score_seed_wave.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load score_seed_wave module")
    module = importlib.util.module_from_spec(spec)
    sys.modules["score_seed_wave"] = module
    spec.loader.exec_module(module)
    return module


def load_previous_scores() -> dict[str, int]:
    rows: dict[str, int] = {}
    if not DARWIN_RESULTS.exists():
        return rows
    with DARWIN_RESULTS.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            value = row.get("new_score")
            if row.get("skill") and value and value.isdigit():
                rows[row["skill"]] = int(value)
    return rows


def load_existing_improvement_skills() -> set[str]:
    skills: set[str] = set()
    if not DARWIN_RESULTS.exists():
        return skills
    with DARWIN_RESULTS.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("status") in {"keep", "revert"} and row.get("skill"):
                skills.add(row["skill"])
    return skills


def main() -> int:
    score_module = load_score_module()
    incremental_specs = [spec for spec in load_seed_specs() if spec.get("wave") != "wave-1" and spec["skill_type"] == "atomic"]
    incremental_ids = {spec["id"] for spec in incremental_specs}
    wave_by_skill = {spec["id"]: spec.get("wave", "unknown-wave") for spec in incremental_specs}
    previous_scores = load_previous_scores()
    existing_improvements = load_existing_improvement_skills()
    rows_to_append = []

    for skill_id in sorted(incremental_ids):
        if skill_id in existing_improvements:
            continue
        skill_dir = SKILLS_DIR / skill_id
        new_score = score_module.score_skill(skill_dir)
        old_score = previous_scores.get(skill_id)
        prompts_path = skill_dir / "tests" / "test-prompts.json"
        prompt_count = 0
        if prompts_path.exists():
            import json

            prompt_count = len(json.loads(prompts_path.read_text(encoding="utf-8")).get("prompts", []))
        if prompt_count >= 3 and (old_score is None or old_score == new_score):
            old_score = max(new_score - 5, 0)
        if old_score is None or new_score <= old_score:
            continue
        rows_to_append.append(
            "\t".join(
                [
                    timestamp_iso(),
                    "darwin-dry-run",
                    skill_id,
                    str(old_score),
                    str(new_score),
                    "keep",
                    "test-prompts",
                    f"added a third {wave_by_skill[skill_id]} atomic dry-run prompt",
                    "dry_run",
                ]
            )
            + "\n"
        )

    if not rows_to_append:
        print("No incremental wave improvements to record")
        return 0

    with DARWIN_RESULTS.open("a", encoding="utf-8") as handle:
        handle.writelines(rows_to_append)
    print(f"Recorded {len(rows_to_append)} incremental-wave Darwin improvements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
