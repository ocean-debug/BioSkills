---
name: bio-metagenomics-strain-tracking
description: "Track strain-level relatedness or persistence in metagenomic cohorts with explicit sample-comparability assumptions."
version: 0.1.0
tags: ["metagenomics", "strain", "tracking", "microbiome"]
trigger_keywords: ["strain tracking", "strain persistence", "within-host strain", "microbial strain comparison"]
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
      - GPTomics/bioSkills:bioSkills-main/metagenomics/strain-tracking/SKILL.md
    depends_on:
      - bio-metagenomics-taxonomic-profiling
---

# Metagenomic strain tracking

## Purpose / When To Use

- Track strain-level relatedness or persistence in metagenomic cohorts with explicit sample-comparability assumptions.
- Use this skill when the user needs metagenomic strain tracking in the context of metagenomics.
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
- Clarify whether the task is within-host tracking, transmission comparison, or longitudinal persistence.

## Execution Path

- Track strain-level similarity with explicit reference, distance, and sample-comparability assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review host depletion, depth, database fit, contamination risk, and sample compositional stability.
- Escalate if taxonomic and functional conclusions rely on incompatible references or input types.
- Review shared marker support, depth, and ambiguity between closely related strains.

## Failure Handling / When To Ask The User

- Do not compare abundance tables built from incompatible pipelines without stating the limitation.
- Pause when the user requests strain-level claims from low-depth or poorly classified samples.
- Do not overstate transmission or persistence claims from underpowered strain evidence.

## Related Skills

- bio-metagenomics-taxonomic-profiling
- bio-workflows-metagenomics-pipeline
