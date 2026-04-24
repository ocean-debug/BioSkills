from __future__ import annotations

from collections import defaultdict

from _common import (
    CATALOG_DIR,
    RESTRICTED_LICENSES,
    iter_jsonl,
    load_seed_specs,
    similarity_score,
    timestamp_iso,
    tokenize,
    write_json,
    write_jsonl,
)


INTAKE_DIR = CATALOG_DIR / "intake"


def load_records() -> list[dict]:
    records: list[dict] = []
    for path in sorted(INTAKE_DIR.glob("*.jsonl")):
        records.extend(iter_jsonl(path))
    return records


def normalize(value: str) -> str:
    return value.strip().lower()


def build_seed_index(seed_specs: list[dict]) -> list[dict]:
    indexed = []
    for spec in seed_specs:
        token_source = " ".join(
            [
                spec["id"],
                spec.get("title", ""),
                spec.get("summary", ""),
                " ".join(spec.get("tags", [])),
                " ".join(spec.get("trigger_keywords", [])),
                " ".join(spec.get("match_aliases", [])),
                spec.get("domain", ""),
                spec.get("task", ""),
            ]
        )
        indexed.append(
            {
                **spec,
                "tokens": tokenize(token_source),
                "normalized_aliases": {normalize(alias) for alias in spec.get("match_aliases", [])},
                "normalized_roots": {normalize(root) for root in spec.get("source_roots", [])},
            }
        )
    return indexed


def record_haystack(record: dict) -> str:
    return normalize(
        " ".join(
            [
                record.get("slug", ""),
                record.get("name", ""),
                record.get("description", ""),
                " ".join(record.get("tags", [])),
                " ".join(record.get("trigger_keywords", [])),
                record.get("path", ""),
            ]
        )
    )


def alias_hit(record: dict, spec: dict, haystack: str) -> bool:
    slug = normalize(record.get("slug", ""))
    name = normalize(record.get("name", ""))
    path = normalize(record.get("path", ""))
    for alias in spec["normalized_aliases"]:
        if not alias:
            continue
        if alias == slug or alias == name:
            return True
        if alias in haystack:
            return True
        if alias in path:
            return True
    return False


def root_hit(record: dict, spec: dict) -> bool:
    path = normalize(record.get("path", ""))
    slug = normalize(record.get("slug", ""))
    name = normalize(record.get("name", ""))
    for root in spec["normalized_roots"]:
        if not root:
            continue
        if root in path:
            return True
        if root == slug or root == name:
            return True
    return False


def match_record(record: dict, seed_index: list[dict]) -> tuple[dict | None, float]:
    if not record["in_scope"]:
        return None, 0.0

    record_tokens = set(record["tokens"])
    haystack = record_haystack(record)
    best = None
    best_score = 0.0

    for spec in seed_index:
        if record["skill_type"] != spec["skill_type"]:
            continue

        has_alias = alias_hit(record, spec, haystack)
        has_root = root_hit(record, spec)
        exact_match = has_alias or has_root

        if not exact_match:
            if record["domain"] == "general":
                continue
            if record["domain"] != spec["domain"]:
                continue

        score = similarity_score(record_tokens, spec["tokens"])
        if exact_match:
            score += 1.0
            if has_root:
                score += 0.4
            if has_alias:
                score += 0.35
        elif record["domain"] == spec["domain"]:
            score += 0.25

        if score > best_score:
            best = spec
            best_score = score

    threshold = 0.7 if best and (alias_hit(record, best, haystack) or root_hit(record, best)) else 0.23
    if best is None or best_score < threshold:
        return None, best_score
    return best, best_score


def main() -> int:
    seed_specs = build_seed_index(load_seed_specs())
    records = load_records()
    clusters: dict[str, list[dict]] = defaultdict(list)
    provenance_rows = []

    for record in records:
        matched, score = match_record(record, seed_specs)
        if not record["in_scope"]:
            provenance_rows.append(
                {
                    **record,
                    "canonical_id": None,
                    "status": "out-of-scope",
                    "reason": "not-analysis-or-workflow",
                    "match_score": 0.0,
                }
            )
            continue
        if matched is None:
            provenance_rows.append(
                {
                    **record,
                    "canonical_id": None,
                    "status": "out-of-scope",
                    "reason": "future-wave-or-no-strong-match",
                    "match_score": round(score, 4),
                }
            )
            continue
        clusters[matched["id"]].append({**record, "match_score": round(score, 4)})

    cluster_rows = []
    for spec in seed_specs:
        members = clusters.get(spec["id"], [])
        if not members:
            cluster_rows.append(
                {
                    "canonical_id": spec["id"],
                    "skill_type": spec["skill_type"],
                    "domain": spec["domain"],
                    "wave": spec.get("wave"),
                    "decision": "seed-without-source-cluster",
                    "lead_source": None,
                    "members": [],
                }
            )
            continue

        reusable = [member for member in members if not member["restricted"] and member["license_spdx"] not in RESTRICTED_LICENSES]
        reusable.sort(key=lambda row: row["match_score"], reverse=True)
        lead_source_id = reusable[0]["source_id"] if reusable else None
        decision = "merge-into-canonical"
        if lead_source_id is None:
            decision = "clean-room-rewrite"

        cluster_members = []
        for member in sorted(members, key=lambda row: (row["repo"], row["path"])):
            if member["restricted"]:
                status = "reference-only"
                reason = "restricted-or-unclear-license"
            elif lead_source_id and member["source_id"] == lead_source_id:
                status = "canonical-source"
                reason = "best-reusable-match"
            else:
                status = f"merged-into:{spec['id']}"
                reason = "semantic-duplicate"

            provenance_rows.append(
                {
                    **member,
                    "canonical_id": spec["id"],
                    "status": status,
                    "reason": reason,
                    "match_score": member["match_score"],
                }
            )
            cluster_members.append(
                {
                    "source_id": member["source_id"],
                    "repo": member["repo"],
                    "path": member["path"],
                    "status": status,
                    "match_score": member["match_score"],
                    "restricted": member["restricted"],
                }
            )

        cluster_rows.append(
            {
                "canonical_id": spec["id"],
                "skill_type": spec["skill_type"],
                "domain": spec["domain"],
                "wave": spec.get("wave"),
                "decision": decision,
                "lead_source": lead_source_id,
                "members": cluster_members,
            }
        )

    duplicates = {
        "generated_at": timestamp_iso(),
        "cluster_count": len(cluster_rows),
        "clusters": cluster_rows,
    }
    write_json(CATALOG_DIR / "duplicates.json", duplicates)
    write_jsonl(CATALOG_DIR / "provenance.jsonl", sorted(provenance_rows, key=lambda row: (row["repo"], row["path"])))
    print(f"Wrote {len(cluster_rows)} clusters and {len(provenance_rows)} provenance rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
