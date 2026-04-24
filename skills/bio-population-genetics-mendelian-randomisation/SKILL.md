---
name: bio-population-genetics-mendelian-randomisation
description: "Run Mendelian-randomisation analyses with explicit instrument, harmonization, and sensitivity-analysis assumptions."
version: 0.1.0
tags: ["population genetics", "Mendelian randomisation", "causal inference", "instruments"]
trigger_keywords: ["Mendelian randomisation", "MR analysis", "genetic instruments", "causal inference"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/mendelian-randomisation/SKILL.md
    depends_on:
      - bio-population-genetics-association-testing
---

# Mendelian randomisation

## Purpose / When To Use

- Run Mendelian-randomisation analyses with explicit instrument, harmonization, and sensitivity-analysis assumptions.
- Use this skill when the user needs mendelian randomisation in the context of population genetics.
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
- Confirm exposure, outcome, instrument construction, and sensitivity analysis expectations before causal claims are discussed.

## Execution Path

- Run MR with explicit instrument strength, harmonization, and sensitivity outputs.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sample relatedness, ancestry structure, inflation, imputation or call quality, and LD consistency.
- Escalate if causal or clinical claims exceed the support of the cohort or summary statistics provided.
- Review instrument strength, heterogeneity, pleiotropy signals, and directionality assumptions.

## Failure Handling / When To Ask The User

- Do not merge cohorts or reference panels with incompatible ancestry representation without warning.
- Pause when phenotype definition or covariates are missing for association-scale conclusions.
- Do not present causal language when instrument validity is not defensible.

## Related Skills

- bio-population-genetics-association-testing
- bio-workflows-popgen-association
