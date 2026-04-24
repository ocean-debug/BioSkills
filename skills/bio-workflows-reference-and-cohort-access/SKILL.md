---
name: bio-workflows-reference-and-cohort-access
description: "Coordinate reference-panel selection, cohort-field discovery, and public-dataset access into a reusable resource-preparation workflow."
version: 0.1.0
tags: ["workflow", "reference-resources", "cohort access", "resource preparation"]
trigger_keywords: ["reference resource workflow", "cohort access workflow", "resource preparation workflow"]
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
    skill_type: workflow
    domain: reference-resources
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:phasing-imputation
      - ClawBio/ClawBio:skills/bigquery-public/SKILL.md
      - ClawBio/ClawBio:skills/ukb-navigator/SKILL.md
    depends_on:
      - bio-reference-resources-reference-panels
      - bio-reference-resources-public-dataset-query
      - bio-reference-resources-cohort-variable-discovery
---

# Reference and cohort access workflow

## Purpose / When To Use

- Coordinate reference-panel selection, cohort-field discovery, and public-dataset access into a reusable resource-preparation workflow.
- Use this skill when the user needs reference and cohort access workflow in the context of reference resources.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review schema fit, population or cohort compatibility, and whether the selected resource really supports the downstream analysis.
- Escalate when a resource recommendation hides access restrictions, cost constraints, or provenance gaps.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not recommend a public resource as plug-and-play if preparation, access, or schema validation is still required.
- Pause when the user asks for broad cohort or public-data access without enough context to constrain the search.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-reference-resources-reference-panels
- bio-reference-resources-public-dataset-query
- bio-reference-resources-cohort-variable-discovery
