---
name: bio-population-genetics-population-structure
description: "Characterize cohort structure and ancestry-related variation before association or comparative interpretation."
version: 0.1.0
tags: ["population genetics", "structure", "ancestry", "PCA"]
trigger_keywords: ["population structure", "ancestry PCA", "cohort structure", "genetic PCs"]
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
      - GPTomics/bioSkills:bioSkills-main/population-genetics/population-structure/SKILL.md
      - ClawBio/ClawBio:ClawBio-main/skills/claw-ancestry-pca/SKILL.md
    depends_on: []
---

# Population structure analysis

## Purpose / When To Use

- Characterize cohort structure and ancestry-related variation before association or comparative interpretation.
- Use this skill when the user needs population structure analysis in the context of population genetics.
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
- Confirm whether the goal is ancestry QC, cohort stratification, or an interpretable population structure summary.

## Execution Path

- Produce PCA or related structure summaries with clear handling of pruning, reference panels, and outliers.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sample relatedness, ancestry structure, inflation, imputation or call quality, and LD consistency.
- Escalate if causal or clinical claims exceed the support of the cohort or summary statistics provided.
- Review sample outliers, reference fit, and whether structure summaries match cohort expectations.

## Failure Handling / When To Ask The User

- Do not merge cohorts or reference panels with incompatible ancestry representation without warning.
- Pause when phenotype definition or covariates are missing for association-scale conclusions.
- Do not assign ancestry labels without reference context and uncertainty handling.

## Related Skills

- bio-population-genetics-association-testing
- bio-workflows-popgen-association
