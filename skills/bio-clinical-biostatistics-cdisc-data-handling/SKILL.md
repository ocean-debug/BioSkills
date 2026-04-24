---
name: bio-clinical-biostatistics-cdisc-data-handling
description: "Prepare CDISC-style clinical data so domains, joins, and analysis populations remain explicit and reproducible."
version: 0.1.0
tags: ["clinical-biostatistics", "CDISC", "SDTM", "clinical data"]
trigger_keywords: ["CDISC", "SDTM", "clinical data handling", "USUBJID joins"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":biostats:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: clinical-biostatistics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:clinical-biostatistics
      - GPTomics/bioSkills:bioSkills-main/clinical-biostatistics/cdisc-data-handling/SKILL.md
    depends_on: []
---

# CDISC clinical-data handling

## Purpose / When To Use

- Prepare CDISC-style clinical data so domains, joins, and analysis populations remain explicit and reproducible.
- Use this skill when the user needs cdisc clinical-data handling in the context of clinical biostatistics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- clinical trial or cohort tables with outcomes, covariates, and analysis populations
- data dictionaries, endpoint definitions, and optional CDISC metadata
- statistical-analysis intent such as estimation, testing, subgrouping, or modeling

### Outputs

- clean analysis tables, effect estimates, model summaries, or subgroup-ready comparisons
- explicit statements of estimand, adjustment set, and multiplicity or subgroup caveats

## Decision Rules

- Separate data preparation, endpoint definition, effect estimation, and model fitting before execution.
- Require analysis population, endpoint coding, and covariate strategy to be explicit before reporting results.
- Clarify whether the task is SDTM intake, domain joining, analysis-population preparation, or metadata interpretation.

## Execution Path

- Prepare CDISC tables with explicit USUBJID joins, SUPPQUAL handling, and analysis-ready variable provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review missingness, event counts, separability, subgroup size, and consistency of endpoint coding.
- Escalate when claims would depend on rare-event handling, multiplicity, or subgroup interpretation beyond the data support.
- Review subject-level joins, domain completeness, and whether derived analysis tables still trace back to raw domains.

## Failure Handling / When To Ask The User

- Do not present effect sizes or odds ratios without the population, reference level, and interval estimation context.
- Pause when trial tables or clinical endpoints are not defined well enough for reproducible modeling.
- Pause when SDTM versus ADaM expectations are mixed or key subject identifiers are inconsistent.

## Related Skills

- bio-clinical-biostatistics-categorical-tests
- bio-clinical-biostatistics-logistic-regression
- bio-workflows-clinical-biostatistics-analysis
