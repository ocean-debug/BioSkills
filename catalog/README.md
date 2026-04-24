# Catalog Data

Generated and curated metadata lives here.

## Files

- `sources.json`: source repository configuration
- `waves/*.json`: canonical multi-wave skill specifications
- `intake/*.jsonl`: raw source-skill metadata intake
- `duplicates.json`: cluster-level dedupe decisions
- `provenance.jsonl`: per-source skill status after dedupe routing

## Status Semantics

- `canonical-source`
- `merged-into:<canonical-id>`
- `dropped-duplicate`
- `reference-only`
- `out-of-scope`
