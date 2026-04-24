from __future__ import annotations

from pathlib import Path

from _common import (
    CATALOG_DIR,
    collect_source_records,
    read_json,
    timestamp_iso,
    write_json,
    write_jsonl,
)


def main() -> int:
    sources = read_json(CATALOG_DIR / "sources.json")
    intake_dir = CATALOG_DIR / "intake"
    summary_rows = []

    for source in sources:
        repo = source["repo"]
        branch = source["default_branch"]
        license_spdx = source["license_spdx"]
        records = collect_source_records(repo, branch, license_spdx)
        output_path = intake_dir / f"{repo.replace('/', '__')}.jsonl"
        write_jsonl(output_path, records)

        summary_rows.append(
            {
                "repo": repo,
                "role": source["role"],
                "layout": source["layout"],
                "license_spdx": license_spdx,
                "default_branch": branch,
                "skill_count": len(records),
                "analysis_in_scope": sum(1 for row in records if row["in_scope"]),
                "restricted_count": sum(1 for row in records if row["restricted"]),
                "generated_at": timestamp_iso(),
            }
        )

    write_json(CATALOG_DIR / "intake" / "summary.json", {"generated_at": timestamp_iso(), "sources": summary_rows})
    print(f"Wrote intake for {len(summary_rows)} repositories into {intake_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
