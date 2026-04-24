---
name: bio-clinical-biostatistics-logistic-regression
description: "Fit clinical logistic-regression models with explicit endpoint coding, adjustment strategy, and rare-event safeguards."
version: 0.1.0
tags: ["clinical-biostatistics", "logistic regression", "odds ratio", "clinical modeling"]
trigger_keywords: ["logistic regression", "binary endpoint model", "clinical regression", "rare events"]
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
      - GPTomics/bioSkills:bioSkills-main/clinical-biostatistics/logistic-regression/SKILL.md
    depends_on: []
---

# Clinical logistic regression

## Purpose / When To Use

- Fit clinical logistic-regression models with explicit endpoint coding, adjustment strategy, and rare-event safeguards.
- Use this skill when the user needs clinical logistic regression in the context of clinical biostatistics.
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
- Clarify binary versus ordinal modeling, covariate adjustment, and whether rare-event handling is required.

## Execution Path

- Fit the declared logistic model, report coefficients as interpretable effect measures, and surface model assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review missingness, event counts, separability, subgroup size, and consistency of endpoint coding.
- Escalate when claims would depend on rare-event handling, multiplicity, or subgroup interpretation beyond the data support.
- Review separation, class imbalance, influential covariates, and model fit before treating odds ratios as stable.

## Failure Handling / When To Ask The User

- Do not present effect sizes or odds ratios without the population, reference level, and interval estimation context.
- Pause when trial tables or clinical endpoints are not defined well enough for reproducible modeling.
- Do not present logistic-regression outputs without checking whether event counts support the requested model complexity.

## Related Skills

- bio-clinical-biostatistics-effect-measures
- bio-clinical-biostatistics-subgroup-analysis
- bio-workflows-clinical-biostatistics-analysis
