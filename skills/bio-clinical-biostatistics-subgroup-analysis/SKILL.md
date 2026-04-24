---
name: bio-clinical-biostatistics-subgroup-analysis
description: "Evaluate subgroup effects with explicit interaction logic, multiplicity caveats, and cohort-size awareness."
version: 0.1.0
tags: ["clinical-biostatistics", "subgroup analysis", "interaction", "heterogeneity"]
trigger_keywords: ["subgroup analysis", "interaction test", "heterogeneity", "forest plot"]
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
      - GPTomics/bioSkills:bioSkills-main/clinical-biostatistics/subgroup-analysis/SKILL.md
    depends_on: []
---

# Clinical subgroup analysis

## Purpose / When To Use

- Evaluate subgroup effects with explicit interaction logic, multiplicity caveats, and cohort-size awareness.
- Use this skill when the user needs clinical subgroup analysis in the context of clinical biostatistics.
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
- Separate pre-specified subgroup questions from exploratory slicing before running interaction or homogeneity analyses.

## Execution Path

- Estimate subgroup effects, interaction terms, and heterogeneity signals while preserving the parent estimand.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review missingness, event counts, separability, subgroup size, and consistency of endpoint coding.
- Escalate when claims would depend on rare-event handling, multiplicity, or subgroup interpretation beyond the data support.
- Review subgroup sample size, event support, and multiplicity before emphasizing subgroup differences.

## Failure Handling / When To Ask The User

- Do not present effect sizes or odds ratios without the population, reference level, and interval estimation context.
- Pause when trial tables or clinical endpoints are not defined well enough for reproducible modeling.
- Pause when post-hoc subgroup findings are being framed as confirmatory without interaction evidence.

## Related Skills

- bio-clinical-biostatistics-effect-measures
- bio-experimental-design-multiple-testing
- bio-workflows-clinical-biostatistics-analysis
