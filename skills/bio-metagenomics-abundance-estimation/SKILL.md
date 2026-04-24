---
name: bio-metagenomics-abundance-estimation
description: "Estimate feature or taxon abundance for metagenomic cohorts with explicit normalization and compositional-analysis caveats."
version: 0.1.0
tags: ["metagenomics", "abundance", "microbiome", "normalization"]
trigger_keywords: ["metagenomic abundance", "feature abundance", "relative abundance", "microbiome normalization"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":microbiome:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: metagenomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:metagenomics
      - ClawBio/ClawBio:skills/claw-metagenomics/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/metagenomics/abundance-estimation/SKILL.md
    depends_on:
      - bio-metagenomics-taxonomic-profiling
---

# Metagenomic abundance estimation

## Purpose / When To Use

- Estimate feature or taxon abundance for metagenomic cohorts with explicit normalization and compositional-analysis caveats.
- Use this skill when the user needs metagenomic abundance estimation in the context of metagenomics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- paired or single-end metagenomic reads, contigs, or abundance tables
- sample metadata with body site, cohort, condition, or timepoint context
- database, taxonomic, or AMR reference resources appropriate to the requested task

### Outputs

- taxonomic profiles, abundance tables, assembled contigs, strain tracking summaries, or AMR calls
- clear notes on reference database choice, contamination handling, and compositional caveats

## Decision Rules

- Separate taxonomic profiling, assembly, abundance testing, AMR detection, and strain tracking before execution.
- Require declared database strategy and sample comparability before cross-sample interpretation.
- Confirm whether the output should be taxon-, pathway-, or feature-level abundance and whether compositional methods are expected.

## Execution Path

- Produce abundance tables in a form that is safe for downstream differential or longitudinal analysis.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review host depletion, depth, database fit, contamination risk, and sample compositional stability.
- Escalate if taxonomic and functional conclusions rely on incompatible references or input types.
- Review sparsity, normalization assumptions, and feature prevalence before reporting group differences.

## Failure Handling / When To Ask The User

- Do not compare abundance tables built from incompatible pipelines without stating the limitation.
- Pause when the user requests strain-level claims from low-depth or poorly classified samples.
- Do not treat compositional abundance as absolute biomass without explicit supporting data.

## Related Skills

- bio-metagenomics-taxonomic-profiling
- bio-workflows-metagenomics-pipeline
