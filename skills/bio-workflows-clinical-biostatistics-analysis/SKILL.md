---
name: bio-workflows-clinical-biostatistics-analysis
description: "Coordinate CDISC preparation, categorical testing, effect estimation, regression, and subgroup review in one clinical-analysis workflow."
version: 0.1.0
tags: ["workflow", "clinical-biostatistics", "clinical trials", "statistics"]
trigger_keywords: ["clinical statistics workflow", "biostatistics workflow", "clinical analysis pipeline", "trial analysis workflow"]
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
    skill_type: workflow
    domain: clinical-biostatistics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:clinical-biostatistics
    depends_on:
      - bio-clinical-biostatistics-cdisc-data-handling
      - bio-clinical-biostatistics-categorical-tests
      - bio-clinical-biostatistics-effect-measures
      - bio-clinical-biostatistics-logistic-regression
      - bio-clinical-biostatistics-subgroup-analysis
---

# Clinical biostatistics workflow

## Purpose / When To Use

- Coordinate CDISC preparation, categorical testing, effect estimation, regression, and subgroup review in one clinical-analysis workflow.
- Use this skill when the user needs clinical biostatistics workflow in the context of clinical biostatistics.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review missingness, event counts, separability, subgroup size, and consistency of endpoint coding.
- Escalate when claims would depend on rare-event handling, multiplicity, or subgroup interpretation beyond the data support.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not present effect sizes or odds ratios without the population, reference level, and interval estimation context.
- Pause when trial tables or clinical endpoints are not defined well enough for reproducible modeling.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-clinical-biostatistics-cdisc-data-handling
- bio-clinical-biostatistics-categorical-tests
- bio-clinical-biostatistics-effect-measures
- bio-clinical-biostatistics-logistic-regression
- bio-clinical-biostatistics-subgroup-analysis
