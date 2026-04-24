---
name: bio-clinical-biostatistics-categorical-tests
description: "Run categorical association tests with sparse-data awareness and clinically interpretable contingency reporting."
version: 0.1.0
tags: ["clinical-biostatistics", "categorical tests", "Fisher", "chi-square"]
trigger_keywords: ["categorical tests", "Fisher exact", "chi-square", "CMH test"]
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
      - GPTomics/bioSkills:bioSkills-main/clinical-biostatistics/categorical-tests/SKILL.md
    depends_on: []
---

# Categorical clinical tests

## Purpose / When To Use

- Run categorical association tests with sparse-data awareness and clinically interpretable contingency reporting.
- Use this skill when the user needs categorical clinical tests in the context of clinical biostatistics.
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
- Choose chi-square, Fisher exact, or stratified categorical testing based on sparsity and study design.

## Execution Path

- Construct the contingency analysis explicitly and pair significance testing with an interpretable effect-size summary.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review missingness, event counts, separability, subgroup size, and consistency of endpoint coding.
- Escalate when claims would depend on rare-event handling, multiplicity, or subgroup interpretation beyond the data support.
- Review expected cell counts, sparse-table behavior, and whether multiple subgroup or post-hoc comparisons are being introduced.

## Failure Handling / When To Ask The User

- Do not present effect sizes or odds ratios without the population, reference level, and interval estimation context.
- Pause when trial tables or clinical endpoints are not defined well enough for reproducible modeling.
- Do not report asymptotic categorical-test results when sparse cells require an exact or alternative approach.

## Related Skills

- bio-clinical-biostatistics-effect-measures
- bio-clinical-biostatistics-subgroup-analysis
- bio-workflows-clinical-biostatistics-analysis
