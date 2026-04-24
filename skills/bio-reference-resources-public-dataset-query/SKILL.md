---
name: bio-reference-resources-public-dataset-query
description: "Query public datasets with read-only SQL and explicit schema, cost, and provenance safeguards."
version: 0.1.0
tags: ["reference-resources", "public datasets", "SQL", "BigQuery"]
trigger_keywords: ["public dataset query", "BigQuery public data", "read-only SQL", "genomics SQL"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":resources:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: reference-resources
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:phasing-imputation
      - ClawBio/ClawBio:skills/bigquery-public/SKILL.md
      - ClawBio/ClawBio:skills/ukb-navigator/SKILL.md
      - ClawBio/ClawBio:ClawBio-main/skills/bigquery-public/SKILL.md
    depends_on: []
---

# Public dataset SQL access

## Purpose / When To Use

- Query public datasets with read-only SQL and explicit schema, cost, and provenance safeguards.
- Use this skill when the user needs public dataset sql access in the context of reference resources.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- resource-selection question such as reference panel choice, cohort-variable lookup, or public-data query goal
- population, assay, or cohort context that constrains which resource is actually relevant
- optional schema, accession, or query constraints when remote resources must be searched safely

### Outputs

- resource recommendations, query plans, or analysis-ready access instructions with explicit scope limits
- clear provenance for which dataset, cohort field, or reference resource was selected and why

## Decision Rules

- Separate reference-panel preparation, cohort-variable discovery, and public-dataset querying because they serve different downstream tasks.
- Require the target population, cohort question, or query scope before recommending a resource as analysis-ready.
- Constrain the query scope, expected cost, and result shape before recommending or running public-dataset SQL access.

## Execution Path

- Plan read-only public-dataset queries with explicit schema assumptions, cost safeguards, and local capture of returned results.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review schema fit, population or cohort compatibility, and whether the selected resource really supports the downstream analysis.
- Escalate when a resource recommendation hides access restrictions, cost constraints, or provenance gaps.
- Review query scope, schema fit, result reproducibility, and whether the selected public dataset really answers the biological question.

## Failure Handling / When To Ask The User

- Do not recommend a public resource as plug-and-play if preparation, access, or schema validation is still required.
- Pause when the user asks for broad cohort or public-data access without enough context to constrain the search.
- Do not present public-dataset querying as trivial when schema validation or cost control is still unresolved.

## Related Skills

- bio-literature-research-public-data-discovery
- bio-reference-resources-cohort-variable-discovery
- bio-workflows-reference-and-cohort-access
