---
name: bio-population-genetics-gwas-prs
description: "Translate association summary statistics into polygenic-risk-score workflows with explicit ancestry and calibration caveats."
version: 0.1.0
tags: ["population genetics", "PRS", "GWAS", "risk score"]
trigger_keywords: ["GWAS to PRS", "polygenic risk score", "PRS construction", "genetic risk score"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/gwas-prs/SKILL.md
    depends_on:
      - bio-population-genetics-association-testing
---

# GWAS to PRS translation

## Purpose / When To Use

- Translate association summary statistics into polygenic-risk-score workflows with explicit ancestry and calibration caveats.
- Use this skill when the user needs gwas to prs translation in the context of population genetics.
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
- Clarify whether the output is score construction, benchmarking, or cohort-level interpretation and which training summary statistics are used.

## Execution Path

- Construct PRS with explicit ancestry, LD, and tuning assumptions and keep training versus target cohorts separate.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sample relatedness, ancestry structure, inflation, imputation or call quality, and LD consistency.
- Escalate if causal or clinical claims exceed the support of the cohort or summary statistics provided.
- Review score calibration, distribution, ancestry portability, and model stability.

## Failure Handling / When To Ask The User

- Do not merge cohorts or reference panels with incompatible ancestry representation without warning.
- Pause when phenotype definition or covariates are missing for association-scale conclusions.
- Do not present PRS as transportable across cohorts without ancestry and calibration checks.

## Related Skills

- bio-population-genetics-fine-mapping
- bio-workflows-popgen-association
- bio-population-genetics-association-testing
