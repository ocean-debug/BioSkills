---
name: bio-reference-resources-cohort-variable-discovery
description: "Discover cohort variables and field candidates for a research question without losing dataset-specific context and metadata."
version: 0.1.0
tags: ["reference-resources", "cohort access", "UK Biobank", "variable discovery"]
trigger_keywords: ["UK Biobank variables", "cohort variable discovery", "UKB navigator", "find cohort fields"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/ukb-navigator/SKILL.md
    depends_on: []
---

# Cohort variable discovery

## Purpose / When To Use

- Discover cohort variables and field candidates for a research question without losing dataset-specific context and metadata.
- Use this skill when the user needs cohort variable discovery in the context of reference resources.
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
- Clarify whether the task is variable discovery, cohort field interpretation, or literature-backed dataset scouting.

## Execution Path

- Search cohort resources semantically and return the candidate variables or fields with enough metadata for downstream selection.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review schema fit, population or cohort compatibility, and whether the selected resource really supports the downstream analysis.
- Escalate when a resource recommendation hides access restrictions, cost constraints, or provenance gaps.
- Review whether the proposed variables truly map to the research question and whether key field metadata is still missing.

## Failure Handling / When To Ask The User

- Do not recommend a public resource as plug-and-play if preparation, access, or schema validation is still required.
- Pause when the user asks for broad cohort or public-data access without enough context to constrain the search.
- Pause when cohort-field discovery would return a broad unranked dump rather than a defensible shortlist.

## Related Skills

- bio-reference-resources-public-dataset-query
- bio-literature-research-public-data-discovery
- bio-workflows-reference-and-cohort-access
