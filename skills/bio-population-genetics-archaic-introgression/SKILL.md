---
name: bio-population-genetics-archaic-introgression
description: "Detect and summarize archaic-introgressed segments with explicit reference-panel and ancestry-context assumptions."
version: 0.1.0
tags: ["population genetics", "introgression", "ancestry", "segments"]
trigger_keywords: ["archaic introgression", "Neanderthal DNA", "Denisovan ancestry", "introgressed segments"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/archaic-introgression/SKILL.md
    depends_on:
      - bio-population-genetics-population-structure
---

# Archaic introgression analysis

## Purpose / When To Use

- Detect and summarize archaic-introgressed segments with explicit reference-panel and ancestry-context assumptions.
- Use this skill when the user needs archaic introgression analysis in the context of population genetics.
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
- Clarify target populations, reference panels, and whether the goal is segment discovery or cohort-level summary.

## Execution Path

- Track introgressed segments, confidence, and population context separately from narrative interpretation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sample relatedness, ancestry structure, inflation, imputation or call quality, and LD consistency.
- Escalate if causal or clinical claims exceed the support of the cohort or summary statistics provided.
- Review segment support, reference fit, and ancestry structure consistency.

## Failure Handling / When To Ask The User

- Do not merge cohorts or reference panels with incompatible ancestry representation without warning.
- Pause when phenotype definition or covariates are missing for association-scale conclusions.
- Pause when introgression inference lacks the reference context needed to separate ancestry from artifact.

## Related Skills

- bio-population-genetics-population-structure
- bio-workflows-phylogenomics
