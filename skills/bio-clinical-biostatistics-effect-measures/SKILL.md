---
name: bio-clinical-biostatistics-effect-measures
description: "Compute and interpret clinical effect measures with explicit denominator, reference-group, and interval-estimation choices."
version: 0.1.0
tags: ["clinical-biostatistics", "effect size", "odds ratio", "risk ratio"]
trigger_keywords: ["effect measures", "odds ratio", "risk ratio", "NNT"]
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
      - GPTomics/bioSkills:bioSkills-main/clinical-biostatistics/effect-measures/SKILL.md
    depends_on: []
---

# Clinical effect measures

## Purpose / When To Use

- Compute and interpret clinical effect measures with explicit denominator, reference-group, and interval-estimation choices.
- Use this skill when the user needs clinical effect measures in the context of clinical biostatistics.
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
- Select odds ratio, risk ratio, risk difference, or NNT according to endpoint definition and study framing.

## Execution Path

- Compute effect measures with confidence intervals and make the reference group explicit in the final interpretation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review missingness, event counts, separability, subgroup size, and consistency of endpoint coding.
- Escalate when claims would depend on rare-event handling, multiplicity, or subgroup interpretation beyond the data support.
- Review event definitions, zero-cell handling, and whether crude versus adjusted estimates are being conflated.

## Failure Handling / When To Ask The User

- Do not present effect sizes or odds ratios without the population, reference level, and interval estimation context.
- Pause when trial tables or clinical endpoints are not defined well enough for reproducible modeling.
- Pause when the requested effect measure is incompatible with the sampling design or available denominators.

## Related Skills

- bio-clinical-biostatistics-categorical-tests
- bio-clinical-biostatistics-logistic-regression
- bio-workflows-clinical-biostatistics-analysis
