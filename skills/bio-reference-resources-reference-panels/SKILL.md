---
name: bio-reference-resources-reference-panels
description: "Select, prepare, and document reference panels for phasing or imputation with explicit ancestry and build compatibility."
version: 0.1.0
tags: ["reference-resources", "reference panels", "imputation", "phasing"]
trigger_keywords: ["reference panels", "imputation panel", "phasing panel", "TOPMed", "HRC"]
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
      - GPTomics/bioSkills:bioSkills-main/phasing-imputation/reference-panels/SKILL.md
    depends_on: []
---

# Reference panel preparation

## Purpose / When To Use

- Select, prepare, and document reference panels for phasing or imputation with explicit ancestry and build compatibility.
- Use this skill when the user needs reference panel preparation in the context of reference resources.
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
- Clarify whether the goal is panel selection, download and preparation, or infrastructure setup for phasing or imputation.

## Execution Path

- Select and prepare reference panels with explicit population fit, build compatibility, and downstream tool requirements.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review schema fit, population or cohort compatibility, and whether the selected resource really supports the downstream analysis.
- Escalate when a resource recommendation hides access restrictions, cost constraints, or provenance gaps.
- Review build consistency, ancestry fit, panel completeness, and whether the prepared resource matches the planned imputation workflow.

## Failure Handling / When To Ask The User

- Do not recommend a public resource as plug-and-play if preparation, access, or schema validation is still required.
- Pause when the user asks for broad cohort or public-data access without enough context to constrain the search.
- Pause when the target population or build is unclear enough to make panel choice unreliable.

## Related Skills

- bio-population-genetics-population-structure
- bio-population-genetics-gwas-prs
- bio-workflows-reference-and-cohort-access
