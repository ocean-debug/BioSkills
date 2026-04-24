---
name: bio-workflows-popgen-association
description: "Coordinate cohort structure, association, PRS, fine-mapping, and Mendelian-randomisation tasks in one population-genetics workflow."
version: 0.1.0
tags: ["workflow", "population genetics", "association", "GWAS"]
trigger_keywords: ["population-genetics workflow", "GWAS pipeline", "association workflow", "PRS workflow"]
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
    skill_type: workflow
    domain: population-genetics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:population-genetics
      - ClawBio/ClawBio:skills/claw-ancestry-pca/SKILL.md
    depends_on:
      - bio-population-genetics-population-structure
      - bio-population-genetics-association-testing
      - bio-population-genetics-gwas-prs
      - bio-population-genetics-fine-mapping
      - bio-population-genetics-mendelian-randomisation
---

# Population-genetics association workflow

## Purpose / When To Use

- Coordinate cohort structure, association, PRS, fine-mapping, and Mendelian-randomisation tasks in one population-genetics workflow.
- Use this skill when the user needs population-genetics association workflow in the context of population genetics.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sample relatedness, ancestry structure, inflation, imputation or call quality, and LD consistency.
- Escalate if causal or clinical claims exceed the support of the cohort or summary statistics provided.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not merge cohorts or reference panels with incompatible ancestry representation without warning.
- Pause when phenotype definition or covariates are missing for association-scale conclusions.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-population-genetics-population-structure
- bio-population-genetics-association-testing
- bio-population-genetics-gwas-prs
- bio-population-genetics-fine-mapping
- bio-population-genetics-mendelian-randomisation
