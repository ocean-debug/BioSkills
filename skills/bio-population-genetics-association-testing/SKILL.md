---
name: bio-population-genetics-association-testing
description: "Run cohort-aware association testing with explicit phenotype, covariate, and ancestry-adjustment assumptions."
version: 0.1.0
tags: ["population genetics", "association", "GWAS", "covariates"]
trigger_keywords: ["association testing", "GWAS analysis", "population association", "genetic association"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":popgen:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: population-genetics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:population-genetics
      - ClawBio/ClawBio:skills/claw-ancestry-pca/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/population-genetics/association-testing/SKILL.md
    depends_on:
      - bio-population-genetics-population-structure
---

# Population-genetic association testing

## Purpose / When To Use

- Run cohort-aware association testing with explicit phenotype, covariate, and ancestry-adjustment assumptions.
- Use this skill when the user needs population-genetic association testing in the context of population genetics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- genotype matrices, VCF/BCF files, summary statistics, or cohort-level annotations
- sample metadata with ancestry, phenotype, cohort, or covariate structure
- reference panels or LD resources when association, PRS, or fine-mapping is requested

### Outputs

- population structure summaries, association tables, PRS artifacts, or ancestry-aware interpretations
- clear statements of covariate assumptions, LD resources, and cohort compatibility

## Decision Rules

- Separate structure inference, association, PRS, fine-mapping, and causal inference tasks before tool selection.
- Require declared ancestry and covariate handling before reporting cohort-level conclusions.
- Require phenotype definition, covariates, case-control balance, and model family before testing.

## Execution Path

- Run association analysis with explicit cohort filtering, covariates, and output schema.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sample relatedness, ancestry structure, inflation, imputation or call quality, and LD consistency.
- Escalate if causal or clinical claims exceed the support of the cohort or summary statistics provided.
- Review inflation, sample counts, covariate behavior, and residual confounding.

## Failure Handling / When To Ask The User

- Do not merge cohorts or reference panels with incompatible ancestry representation without warning.
- Pause when phenotype definition or covariates are missing for association-scale conclusions.
- Pause when phenotype or covariate definitions are too ambiguous for trustworthy association results.

## Related Skills

- bio-population-genetics-gwas-prs
- bio-workflows-popgen-association
- bio-population-genetics-population-structure
